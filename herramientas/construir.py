#!/usr/bin/env python3
"""Build the whole website into _site/ (what GitHub Pages serves).

    npm ci && python3 herramientas/construir.py

_site/
  index.html, estilo.css   home page: read online, offline app, PDF, EPUB
  leer/NN.html             the book as plain static pages (no JavaScript)
  media/                   figures
  app/                     offline app (reader + exercises with Pyodide + service worker)

The PDF and EPUB are not in git: they are release assets (see PUBLICAR.md). The home page
links to the latest release; set REPO_URL to change the repository it points to.
"""
import glob
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(RAIZ, "_site")
NM = os.path.join(RAIZ, "node_modules")
REPO_URL = os.environ.get("REPO_URL", "https://github.com/perezamadorluisenrique-gif/libro-python-es")
PYODIDE = ["pyodide.js", "pyodide.asm.js", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"]
TITULO = "Introducción a la programación con Python"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from libro_bookstudio import tablas_con_codigo  # noqa: E402

PIE = """<footer>
  <p>Traducción y adaptación al español de <em>Introduction to Python Programming</em> (OpenStax, 2024),
  de Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi, disponible gratis en
  <a href="https://openstax.org/books/introduction-python-programming/pages/1-introduction">openstax.org</a>,
  con licencia <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">CC BY-NC-SA 4.0</a>.
  Esta traducción tiene la misma licencia y no está avalada por OpenStax ni por la Universidad Rice.
  El código de la web es MIT. <a href="REPO">Código fuente y créditos</a>.</p>
</footer>"""


def pagina(titulo, cuerpo, raiz=".", descripcion=""):
    desc = f'\n  <meta name="description" content="{html.escape(descripcion)}">' if descripcion else ""
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(titulo)}</title>{desc}
  <link rel="stylesheet" href="{raiz}/estilo.css">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
{cuerpo}
{PIE.replace("REPO", REPO_URL)}
</body>
</html>
"""


def capitulos():
    out = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "libro", "[0-9][0-9]-*.md"))):
        md = tablas_con_codigo(open(p, encoding="utf-8").read())
        m = re.search(r"^# (.+)$", md, re.M)
        out.append({"id": os.path.basename(p)[:2], "fichero": os.path.basename(p),
                    "titulo": m.group(1).strip() if m else os.path.basename(p), "md": md})
    return out


def ejercicios():
    out = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "ejercicios", "[0-9][0-9]", "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        out.append({"id": os.path.basename(p)[:-5], "capitulo": os.path.basename(os.path.dirname(p)),
                    **{k: d.get(k) for k in ("titulo", "seccion", "enunciado", "inicial", "pruebas",
                                             "solucion", "pistas", "entrada")}})
    return out


def md2html(textos):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(textos, f, ensure_ascii=False)
    try:
        r = subprocess.run(["node", os.path.join(RAIZ, "herramientas", "md2html.mjs"), f.name],
                           cwd=RAIZ, capture_output=True, text=True, check=True)
    finally:
        os.unlink(f.name)
    return json.loads(r.stdout)


def construye_app(caps, ejs):
    dist = os.path.join(SITE, "app")
    shutil.copytree(os.path.join(RAIZ, "app", "src"), dist)
    os.makedirs(os.path.join(dist, "pyodide"))
    for f in PYODIDE:
        shutil.copy(os.path.join(NM, "pyodide", f), os.path.join(dist, "pyodide", f))
    shutil.copy(os.path.join(NM, "marked", "marked.min.js"), os.path.join(dist, "marked.min.js"))
    shutil.copy(os.path.join(RAIZ, "ejercicios", "arnes.py"), os.path.join(dist, "arnes.py"))
    shutil.copytree(os.path.join(RAIZ, "media"), os.path.join(dist, "media"))
    os.makedirs(os.path.join(dist, "datos"))
    json.dump(caps, open(os.path.join(dist, "datos", "libro.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(ejs, open(os.path.join(dist, "datos", "ejercicios.json"), "w", encoding="utf-8"), ensure_ascii=False)
    archivos, h = [], hashlib.sha256()
    for dirpath, _, files in os.walk(dist):
        for f in sorted(files):
            rel = os.path.relpath(os.path.join(dirpath, f), dist).replace(os.sep, "/")
            if rel == "sw.js":
                continue
            archivos.append(rel)
            h.update(rel.encode() + open(os.path.join(dirpath, f), "rb").read())
    archivos.sort()
    plantilla = open(os.path.join(RAIZ, "app", "sw.plantilla.js"), encoding="utf-8").read()
    sw = (plantilla.replace("__VERSION__", h.hexdigest()[:12])
          .replace("__ARCHIVOS__", json.dumps(["./"] + archivos, ensure_ascii=False)))
    open(os.path.join(dist, "sw.js"), "w", encoding="utf-8").write(sw)


def construye_lector(caps, ejs):
    os.makedirs(os.path.join(SITE, "leer"))
    cuerpos = md2html([c["md"] for c in caps])
    indice = "<ol class=\"indice\">" + "".join(
        f'<li><a href="{c["id"]}.html">{html.escape(c["titulo"])}</a></li>' for c in caps) + "</ol>"
    for i, (c, cuerpo) in enumerate(zip(caps, cuerpos)):
        cuerpo = cuerpo.replace('src="media/', 'src="../media/')
        # Wide code blocks and tables scroll sideways: make them keyboard-focusable (axe).
        cuerpo = re.sub(r"<(pre|table)>", r'<\1 tabindex="0">', cuerpo)
        lista = [e for e in ejs if e["capitulo"] == c["id"]]
        extra = ""
        if lista:
            extra = ('<section class="lista-ej" aria-labelledby="ej-titulo"><h2 id="ej-titulo">Ejercicios del capítulo</h2>'
                     '<p>Se resuelven en la app, que ejecuta Python en tu navegador.</p><ul>' + "".join(
                         f'<li><a href="../app/#ej/{e["capitulo"]}/{e["id"]}">{html.escape(e["titulo"] or e["id"])}</a></li>'
                         for e in lista) + "</ul></section>")
        ant = f'<a rel="prev" href="{caps[i - 1]["id"]}.html">← {html.escape(caps[i - 1]["titulo"])}</a>' if i else "<span></span>"
        sig = (f'<a rel="next" href="{caps[i + 1]["id"]}.html">{html.escape(caps[i + 1]["titulo"])} →</a>'
               if i + 1 < len(caps) else "<span></span>")
        nav = f'<nav class="pasos" aria-label="Capítulos vecinos">{ant}{sig}</nav>'
        cab = (f'<header class="barra"><a href="../index.html" class="marca">{TITULO}</a>'
               f'<a href="index.html">Índice</a><a href="../app/#cap/{c["id"]}">Abrir en la app</a></header>')
        doc = pagina(f'{c["titulo"]} · {TITULO}',
                     f'{cab}\n<main id="contenido"><article class="capitulo">{cuerpo}</article>{extra}{nav}</main>', "..")
        open(os.path.join(SITE, "leer", f'{c["id"]}.html'), "w", encoding="utf-8").write(doc)
    cab = f'<header class="barra"><a href="../index.html" class="marca">{TITULO}</a></header>'
    open(os.path.join(SITE, "leer", "index.html"), "w", encoding="utf-8").write(
        pagina(f"Índice · {TITULO}", f'{cab}\n<main id="contenido"><h1>Índice</h1>{indice}</main>', ".."))
    return indice


def construye_inicio(caps, ejs):
    plantilla = open(os.path.join(RAIZ, "web", "index.html"), encoding="utf-8").read()
    indice = "<ol class=\"indice\">" + "".join(
        f'<li><a href="leer/{c["id"]}.html">{html.escape(c["titulo"])}</a></li>' for c in caps) + "</ol>"
    cuerpo = (plantilla.replace("{{INDICE}}", indice)
              .replace("{{EJERCICIOS}}", str(len(ejs)))
              .replace("{{CAPITULOS}}", str(len([c for c in caps if c["id"] != "00"])))
              .replace("{{PDF}}", f"{REPO_URL}/releases/latest/download/libro.pdf")
              .replace("{{EPUB}}", f"{REPO_URL}/releases/latest/download/libro.epub")
              .replace("{{REPO}}", REPO_URL))
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(
        pagina(TITULO, cuerpo, ".", "Libro libre en español para aprender a programar con Python, "
               "con ejercicios autocorregidos que funcionan sin conexión."))
    shutil.copy(os.path.join(RAIZ, "web", "estilo.css"), os.path.join(SITE, "estilo.css"))
    for extra in ("favicon.svg",):
        if os.path.exists(os.path.join(RAIZ, "web", extra)):
            shutil.copy(os.path.join(RAIZ, "web", extra), os.path.join(SITE, extra))


CAPS_EN = ["Preface", "Statements", "Expressions", "Objects", "Decisions", "Loops", "Functions", "Modules", "Strings",
           "Lists", "Dictionaries", "Classes", "Recursion", "Inheritance", "Files", "Data science"]

PIE_EN = """<footer>
  <p>Spanish translation and adaptation of <em>Introduction to Python Programming</em> (OpenStax, 2024),
  by Udayan Das, Aubrey Lawson, Chris Mayfield and Narges Norouzi, available free at
  <a href="https://openstax.org/books/introduction-python-programming/pages/1-introduction">openstax.org</a>,
  under a <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a> license.
  This translation has the same license and is not endorsed by OpenStax or Rice University.
  The website code is MIT. <a href="REPO">Source code and credits</a>.</p>
</footer>"""


def construye_inicio_en(caps, ejs):
    """English home page (en/index.html); the book itself stays in Spanish."""
    if len(caps) != len(CAPS_EN):
        sys.exit("CAPS_EN no cubre los capítulos")
    def nombre(n):
        return "Preface" if n == 0 else f"Chapter {n}: {CAPS_EN[n]}"
    indice = "<ol class=\"indice\">" + "".join(
        f'<li><a href="../leer/{c["id"]}.html" hreflang="es">{nombre(int(c["id"]))}</a></li>' for c in caps) + "</ol>"
    cuerpo = (open(os.path.join(RAIZ, "web", "index.en.html"), encoding="utf-8").read()
              .replace("{{INDICE}}", indice)
              .replace("{{EJERCICIOS}}", str(len(ejs)))
              .replace("{{CAPITULOS}}", str(len([c for c in caps if c["id"] != "00"])))
              .replace("{{PDF}}", f"{REPO_URL}/releases/latest/download/libro.pdf")
              .replace("{{EPUB}}", f"{REPO_URL}/releases/latest/download/libro.epub")
              .replace("{{REPO}}", REPO_URL))
    os.makedirs(os.path.join(SITE, "en"), exist_ok=True)
    open(os.path.join(SITE, "en", "index.html"), "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(TITULO)} (a free Python textbook in Spanish)</title>
  <meta name="description" content="A free Spanish-language textbook to learn programming with Python, with self-checking exercises that work offline.">
  <link rel="stylesheet" href="../estilo.css">
</head>
<body>
<a class="saltar" href="#contenido">Skip to content</a>
{cuerpo}
{PIE_EN.replace("REPO", REPO_URL)}
</body>
</html>
""")


def main():
    if not os.path.isdir(os.path.join(NM, "pyodide")):
        sys.exit("falta node_modules: ejecuta npm ci")
    shutil.rmtree(SITE, ignore_errors=True)
    os.makedirs(SITE)
    caps, ejs = capitulos(), ejercicios()
    shutil.copytree(os.path.join(RAIZ, "media"), os.path.join(SITE, "media"))
    construye_app(caps, ejs)
    construye_lector(caps, ejs)
    construye_inicio(caps, ejs)
    construye_inicio_en(caps, ejs)
    open(os.path.join(SITE, ".nojekyll"), "w").close()
    total = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(SITE) for f in fs)
    print(f"_site: {total / 1e6:.1f} MB; {len(caps)} capítulos, {len(ejs)} ejercicios")


if __name__ == "__main__":
    main()
