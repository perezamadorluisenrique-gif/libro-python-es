// Reader + exercises. Routes: #cap/NN, #ej/NN/<id>. Everything is local (see sw.js).
"use strict";
const $ = (s) => document.querySelector(s);
let LIBRO = [], EJERCICIOS = [];
let worker = null, siguiente = 0, pyListo = false;
const LIMITE_MS = 10000; // max run time once Python is loaded (infinite loops)
const pendientes = new Map();

function estado(t) { $("#estado").textContent = t; }

function pyWorker() {
  if (!worker) {
    estado("Preparando Python…");
    worker = new Worker("worker.js");
    worker.onmessage = (e) => {
      if (e.data.listo) { pyListo = true; estado(""); return; }
      const r = pendientes.get(e.data.id);
      pendientes.delete(e.data.id);
      estado("");
      if (r) r(e.data);
    };
  }
  return worker;
}

function ejecuta(codigo, pruebas, entrada) {
  return new Promise((res) => {
    const id = ++siguiente;
    const w = pyWorker();
    let reloj = null;
    const vigila = () => {
      reloj = setTimeout(() => {
        if (!pendientes.has(id)) return;
        if (!pyListo) return vigila(); // still loading Python: keep waiting
        pendientes.delete(id);
        w.terminate();
        worker = null; pyListo = false;
        res({ ok: false, salida: "", mensaje: `tu programa tardó más de ${LIMITE_MS / 1000} s (¿un bucle infinito?)` });
      }, LIMITE_MS);
    };
    pendientes.set(id, (r) => { clearTimeout(reloj); res(r); });
    vigila();
    w.postMessage({ id, codigo, pruebas, entrada });
  });
}

// tabindex: wide code blocks and tables scroll sideways and must be reachable by keyboard (axe).
const md = (t) => marked.parse(t, { gfm: true }).replace(/<(pre|table)>/g, '<$1 tabindex="0">');
const esc = (t) => t.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

function indice() {
  $("#indice").innerHTML = "<ol>" + LIBRO.map((c) =>
    `<li><a href="#cap/${c.id}">${esc(c.titulo)}</a></li>`).join("") + "</ol>";
}

function capitulo(id) {
  const c = LIBRO.find((x) => x.id === id);
  if (!c) return inicio();
  const ejs = EJERCICIOS.filter((e) => e.capitulo === id);
  const i = LIBRO.indexOf(c);
  $("#contenido").innerHTML = `<article class="capitulo">${md(c.md)}</article>` +
    (ejs.length ? `<section class="lista-ej"><h2>Ejercicios del capítulo</h2><ul>` +
      ejs.map((e) => `<li><a href="#ej/${id}/${e.id}">${esc(e.titulo)}</a> <small>${esc(e.seccion || "")}</small></li>`).join("") +
      `</ul></section>` : "") +
    `<p class="pasos">${i > 0 ? `<a href="#cap/${LIBRO[i - 1].id}">← Anterior</a>` : ""}
     ${i < LIBRO.length - 1 ? `<a href="#cap/${LIBRO[i + 1].id}">Siguiente →</a>` : ""}</p>`;
  window.scrollTo(0, 0);
}

function ejercicio(cap, id) {
  const e = EJERCICIOS.find((x) => x.capitulo === cap && x.id === id);
  if (!e) return capitulo(cap);
  const guardado = (() => { try { return localStorage.getItem("ej:" + cap + "/" + id); } catch { return null; } })();
  $("#contenido").innerHTML = `
    <p><a href="#cap/${cap}">← Volver al capítulo</a></p>
    <h1>${esc(e.titulo)}</h1>
    <div class="enunciado">${md(e.enunciado)}</div>
    <label for="codigo">Tu código</label>
    <textarea id="codigo" spellcheck="false" rows="14">${esc(guardado ?? e.inicial)}</textarea>
    <p class="botones">
      <button id="probar">Comprobar</button>
      <button id="pista" class="sec">Pista</button>
      <button id="reiniciar" class="sec">Reiniciar</button>
      <button id="versol" class="sec">Ver solución</button>
    </p>
    <div id="pistas"></div>
    <pre id="resultado" aria-live="polite"></pre>`;
  const ta = $("#codigo");
  ta.addEventListener("keydown", (ev) => {
    if (ev.key === "Tab") {
      ev.preventDefault();
      ta.setRangeText("    ", ta.selectionStart, ta.selectionEnd, "end");
    }
  });
  ta.addEventListener("input", () => { try { localStorage.setItem("ej:" + cap + "/" + id, ta.value); } catch {} });
  let np = 0;
  $("#pista").onclick = () => {
    const p = e.pistas || [];
    if (np < p.length) $("#pistas").insertAdjacentHTML("beforeend", `<div class="pista">${md(p[np++])}</div>`);
    if (np >= p.length) $("#pista").disabled = true;
  };
  $("#reiniciar").onclick = () => { ta.value = e.inicial; ta.dispatchEvent(new Event("input")); };
  $("#versol").onclick = () => {
    if (confirm("¿Ver la solución? Intentarlo antes ayuda a aprender.")) { ta.value = e.solucion; ta.dispatchEvent(new Event("input")); }
  };
  $("#probar").onclick = async () => {
    const out = $("#resultado");
    out.className = "";
    out.textContent = "Ejecutando…";
    $("#probar").disabled = true;
    const r = await ejecuta(ta.value, e.pruebas, e.entrada || "");
    $("#probar").disabled = false;
    out.className = r.ok ? "ok" : "fallo";
    out.textContent = (r.salida ? r.salida.replace(/\n?$/, "\n") : "") + (r.ok ? "OK" : "FALLO: " + r.mensaje);
  };
  window.scrollTo(0, 0);
}

function inicio() {
  $("#contenido").innerHTML = `<h1>Introducción a la programación con Python</h1>
    <p>Libro libre en español con ${EJERCICIOS.length} ejercicios autocorregidos. Todo funciona sin conexión:
    Python se ejecuta en tu navegador.</p>` + $("#indice").innerHTML;
}

function ruta() {
  document.body.classList.remove("menu-abierto");
  const [tipo, a, b] = location.hash.slice(1).split("/");
  if (tipo === "cap") capitulo(a);
  else if (tipo === "ej") ejercicio(a, b);
  else inicio();
}

async function arranca() {
  [LIBRO, EJERCICIOS] = await Promise.all([
    fetch("datos/libro.json").then((r) => r.json()),
    fetch("datos/ejercicios.json").then((r) => r.json()),
  ]);
  indice();
  $("#menu").onclick = () => document.body.classList.toggle("menu-abierto");
  window.addEventListener("hashchange", ruta);
  ruta();
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").then(() => navigator.serviceWorker.ready)
      .then(() => { document.documentElement.dataset.offline = "listo"; })
      .catch((e) => console.warn("service worker:", e));
  }
}

arranca();
