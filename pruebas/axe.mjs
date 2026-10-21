// Accessibility check (npm test, after npm run build): runs axe-core on the home page, the
// online reader (every chapter) and the app (every chapter and an exercise), in light and dark mode.
// Fails on any `serious` or `critical` violation. Writes the full report to pruebas/axe-informe.json.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const SITE = path.join(AQUI, "..", "_site");
const AXE = fs.readFileSync(createRequire(import.meta.url).resolve("axe-core/axe.min.js"), "utf8");
const TIPOS = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".json": "application/json",
  ".wasm": "application/wasm", ".zip": "application/zip", ".py": "text/plain", ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml", ".gif": "image/gif" };

const servidor = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, "http://x").pathname);
  if (p.endsWith("/")) p += "index.html";
  const f = path.join(SITE, p);
  if (!f.startsWith(SITE) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TIPOS[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => servidor.listen(0, "127.0.0.1", r));
const BASE = `http://127.0.0.1:${servidor.address().port}/`;

const ej = JSON.parse(fs.readFileSync(path.join(SITE, "app", "datos", "ejercicios.json"), "utf8"))[0];
const CAPS = fs.readdirSync(path.join(SITE, "leer")).filter((f) => /^\d\d\.html$/.test(f)).map((f) => f.slice(0, 2));
const PAGINAS = [
  ["inicio", "index.html", "main"],
  ["inicio en", "en/index.html", "main"],
  ["índice del lector", "leer/index.html", "main"],
  ...CAPS.map((c) => [`lector: ${c}`, `leer/${c}.html`, "main"]),
  ["app: inicio", "app/", "#contenido h1"],
  ...CAPS.map((c) => [`app: cap. ${c}`, `app/#cap/${c}`, "article.capitulo h1"]),
  ["app: ejercicio", `app/#ej/${ej.capitulo}/${ej.id}`, "#codigo"],
];

const navegador = await chromium.launch();
const informe = [];
let graves = 0;
try {
  for (const esquema of ["light", "dark"]) {
    const ctx = await navegador.newContext({ colorScheme: esquema });
    for (const [nombre, ruta, espera] of PAGINAS) {
      const page = await ctx.newPage();
      await page.goto(BASE + ruta);
      await page.waitForSelector(espera, { timeout: 30000 });
      await page.addScriptTag({ content: AXE });
      const r = await page.evaluate(async () => await window.axe.run(document, { resultTypes: ["violations"] }));
      const malas = r.violations.filter((v) => v.impact === "serious" || v.impact === "critical");
      graves += malas.length;
      informe.push({ pagina: nombre, esquema, violaciones: r.violations.map((v) => ({
        id: v.id, impact: v.impact, nodos: v.nodes.length, ejemplo: v.nodes[0]?.target })) });
      console.log(`${malas.length ? "FALLO" : "ok   "} ${esquema.padEnd(5)} ${nombre}: ` +
        (r.violations.length ? r.violations.map((v) => `${v.id}(${v.impact}×${v.nodes.length})`).join(" ") : "sin infracciones"));
      await page.close();
    }
    await ctx.close();
  }
} finally {
  await navegador.close();
  servidor.close();
}
fs.writeFileSync(path.join(AQUI, "axe-informe.json"), JSON.stringify(informe, null, 1));
console.log(graves ? `axe: ${graves} infracciones serious/critical` : "axe: OK (0 serious/critical)");
process.exit(graves ? 1 : 0);
