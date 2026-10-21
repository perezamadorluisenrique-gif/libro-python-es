// Offline test (npm test, after npm run build): serves _site/, loads the app once online,
// then stops the server AND cuts the network, reloads, opens a chapter and solves an
// exercise with Pyodide from the service-worker cache. Exit 0 = pass.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const SITE = path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "_site");
const DIST = path.join(SITE, "app");
const TIPOS = { ".html": "text/html", ".js": "text/javascript", ".mjs": "text/javascript", ".css": "text/css",
  ".json": "application/json", ".wasm": "application/wasm", ".zip": "application/zip", ".py": "text/plain",
  ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml", ".gif": "image/gif" };

const servidor = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, "http://x").pathname);
  if (p.endsWith("/")) p += "index.html";
  const f = path.join(SITE, p);
  if (!f.startsWith(SITE) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TIPOS[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => servidor.listen(0, "127.0.0.1", r));
const URL0 = `http://127.0.0.1:${servidor.address().port}/app/`;

const ejercicios = JSON.parse(fs.readFileSync(path.join(DIST, "datos", "ejercicios.json"), "utf8"));
const ej = ejercicios.find((e) => e.capitulo === "05") || ejercicios[0];

// watchdog: never hang the scorer
setTimeout(() => { console.error("prueba colgada más de 8 min"); process.exit(1); }, 8 * 60 * 1000).unref();
const navegador = await chromium.launch();
let fallo = null;
try {
  const ctx = await navegador.newContext();
  const page = await ctx.newPage();
  page.on("pageerror", (e) => console.error("pageerror:", e.message));
  await page.goto(URL0);
  await page.waitForFunction(() => navigator.serviceWorker.controller && document.documentElement.dataset.offline === "listo",
    null, { timeout: 120000 });
  console.log("1/5 cargada en línea; service worker activo");

  await new Promise((r) => servidor.close(r));
  servidor.closeAllConnections?.();
  await ctx.setOffline(true);
  await page.goto(URL0 + "#cap/05");
  await page.reload();
  await page.waitForSelector("article.capitulo h1", { timeout: 30000 });
  const h1 = await page.textContent("article.capitulo h1");
  if (!/Bucles/.test(h1)) throw new Error("capítulo 5 sin título esperado: " + h1);
  console.log("2/5 sin red: capítulo abierto:", h1.trim());

  await page.click(`a[href="#ej/${ej.capitulo}/${ej.id}"]`);
  await page.waitForSelector("#codigo");
  await page.fill("#codigo", ej.solucion);
  await page.click("#probar");
  await page.waitForFunction(() => /(^|\n)(OK|FALLO: .*)$/.test(document.querySelector("#resultado").textContent.trim()),
    null, { timeout: 180000 });
  const r = (await page.textContent("#resultado")).trim();
  if (!r.endsWith("OK")) throw new Error(`ejercicio ${ej.capitulo}/${ej.id}: se esperaba OK y salió: ${r}`);
  console.log(`3/5 sin red: ejercicio «${ej.titulo}» resuelto (OK)`);

  await page.fill("#codigo", "print('no')");
  await page.click("#probar");
  await page.waitForFunction(() => /FALLO|OK$/.test(document.querySelector("#resultado").textContent.trim()), null, { timeout: 60000 });
  const r2 = (await page.textContent("#resultado")).trim();
  if (!/FALLO/.test(r2)) throw new Error("una respuesta errónea no falló: " + r2);
  console.log("4/5 sin red: una respuesta errónea falla");

  await page.fill("#codigo", "while True:\n    pass");
  await page.click("#probar");
  await page.waitForFunction(() => /FALLO|OK$/.test(document.querySelector("#resultado").textContent.trim()), null, { timeout: 60000 });
  const r3 = (await page.textContent("#resultado")).trim();
  if (!/bucle infinito/.test(r3)) throw new Error("un bucle infinito no se cortó: " + r3);
  await page.fill("#codigo", ej.solucion);
  await page.click("#probar");
  await page.waitForFunction(() => /FALLO|OK$/.test(document.querySelector("#resultado").textContent.trim()) &&
    !/bucle infinito/.test(document.querySelector("#resultado").textContent), null, { timeout: 180000 });
  const r4 = (await page.textContent("#resultado")).trim();
  if (!r4.endsWith("OK")) throw new Error("tras cortar un bucle infinito, Python no se recuperó: " + r4);
  console.log("5/5 sin red: un bucle infinito se corta y Python se recarga desde la caché");
} catch (e) {
  fallo = e;
} finally {
  await navegador.close();
  servidor.close();
}
if (fallo) { console.error(String(fallo.stack || fallo)); process.exit(1); }
console.log("prueba sin conexión: OK");
process.exit(0);
