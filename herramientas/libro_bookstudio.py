#!/usr/bin/env python3
"""Prepara libro/ como «libro» de Book Studio y genera salida/libro.pdf y salida/libro.epub.

Uso: python3 herramientas/libro_bookstudio.py [--solo-preparar]

- Book Studio (https://github.com/perezamadorluisenrique-gif/book-studio, MIT) va en
  trabajo/book-studio, instalado con `npm ci`:
    git clone --depth 1 https://github.com/perezamadorluisenrique-gif/book-studio trabajo/book-studio
    (cd trabajo/book-studio && npm ci)
  Otra ruta: variable BOOK_STUDIO.
- trabajo/libro-bs/ es la carpeta que lee Book Studio: una nota manifiesto con
  `book: true`, los capítulos adaptados y media/.
Adaptaciones (solo para la maqueta; libro/ no cambia):
  * se quitan los comentarios HTML (anclas <!-- modulo|pregunta|coderunner -->);
  * «# Capítulo N: Título» → «# Título» (Book Studio numera los capítulos);
  * <details><summary>Respuesta</summary> … </details> → «**Respuesta:** …»;
  * π, τ y √ → «pi», «tau», «raíz» (las fuentes incluidas no tienen esos glifos);
  * ```salida → bloque de texto precedido de «*Salida:*»; ```python norun → ```python.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BS = Path(os.environ.get("BOOK_STUDIO", RAIZ / "trabajo" / "book-studio"))
VAULT = RAIZ / "trabajo" / "libro-bs"
SALIDA = RAIZ / "salida"

ATRIBUCION = (
    "Traducido y adaptado al español de *Introduction to Python Programming* (OpenStax, 2024), "
    "de Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi, disponible gratis en "
    "openstax.org, con licencia CC BY-NC-SA 4.0. Esta traducción tiene la misma licencia y no "
    "está avalada por OpenStax."
)


def adapta(texto: str) -> str:
    texto = re.sub(r"<!--.*?-->\n?", "", texto, flags=re.S)
    texto = re.sub(r"^# Capítulo \d+: *", "# ", texto, count=1, flags=re.M)
    texto = re.sub(r"<details><summary>Respuesta</summary>\n\n?", "**Respuesta:** ", texto)
    texto = re.sub(r"^[ \t]*</details>[ \t]*\n?", "", texto, flags=re.M)
    texto = re.sub(r"\*\*Respuesta:\*\*\s+", "**Respuesta:** ", texto)
    # Las fuentes de Book Studio no traen π, τ ni √: se escriben con letras.
    texto = re.sub(r"&#x0*3c0;|&#0*960;", "π", texto, flags=re.I)
    for g, r in (("π", "pi"), ("τ", "tau"), ("√", "raíz")):
        texto = texto.replace(g, r)
    texto = re.sub(r"^( *)```salida *$", r"\1*Salida:*\n\n\1```text", texto, flags=re.M)
    texto = re.sub(r"^( *)```python norun *$", r"\1```python", texto, flags=re.M)
    texto = tablas_con_codigo(texto)
    return re.sub(r"\n{3,}", "\n\n", texto)


def _celdas(linea: str) -> list[str]:
    cuerpo = linea.strip()[1:-1] if linea.strip().endswith("|") else linea.strip()[1:]
    return [c.strip() for c in re.split(r"(?<!\\)\|", cuerpo)]


def _bloque_celda(c: str) -> str:
    c = c.replace("\\|", "|")
    if c.startswith("```"):
        lineas = c.split("<br>")
        if lineas[-1].strip() != "```":
            lineas.append("```")
        return "\n".join(lineas)
    if "<br>|" in c or c.startswith("|"):
        return "```text\n" + c.replace("<br>", "\n").strip() + "\n```"
    return c.replace("<br>", "  \n")


def tablas_con_codigo(texto: str) -> str:
    """Las tablas con código o tablas anidadas en las celdas no caben en una página
    impresa: se convierten en una ficha por fila (cabecera en negrita + contenido)."""
    lineas, out, i = texto.split("\n"), [], 0
    while i < len(lineas):
        if lineas[i].startswith("|") and i + 1 < len(lineas) and re.match(r"^\|(-+\|)+$", lineas[i + 1].strip()):
            j = i + 2
            while j < len(lineas) and lineas[j].startswith("|"):
                j += 1
            filas = lineas[i:j]
            if any("```" in f or "<br>" in f for f in filas[2:]):
                cab = _celdas(filas[0])
                cuerpo = [_celdas(f) for f in filas[2:]]
                es_rotulo = lambda c: bool(re.fullmatch(r"\*\*[^*]+\*\*", c))
                k = 0
                while k < len(cuerpo):
                    cs = cuerpo[k]
                    if all(es_rotulo(c) for c in cs if c) and k + 1 < len(cuerpo):
                        # Fila de rótulos («Ejemplo | Salida»): cada rótulo va con su celda de abajo.
                        for r, c in zip(cs, cuerpo[k + 1]):
                            out += [r, "", _bloque_celda(c), ""] if c else []
                        k += 2
                        continue
                    for n, c in enumerate(cs):
                        if not c:
                            continue
                        bloque = _bloque_celda(c)
                        if n == 0 and not bloque.startswith("```") and not es_rotulo(c):
                            out += [f"**{c}**", ""]
                        elif n > 0 and len(cab) > 2 and cab[n]:
                            out += [f"*{cab[n]}:*", "", bloque, ""]
                        else:
                            out += [bloque, ""]
                    k += 1
                i = j
                continue
        out.append(lineas[i])
        i += 1
    return "\n".join(out)


def titulo(texto: str) -> str:
    m = re.search(r"^# (.+)$", texto, flags=re.M)
    return m.group(1).strip() if m else ""


def prepara() -> None:
    if VAULT.exists():
        shutil.rmtree(VAULT)
    VAULT.mkdir(parents=True)
    shutil.copytree(next(m for m in (RAIZ / "media", RAIZ / "fuente" / "media") if m.is_dir()), VAULT / "media")
    capitulos = sorted((RAIZ / "libro").glob("[0-9][0-9]-*.md"))
    enlaces_cuerpo = []
    for f in capitulos:
        (VAULT / f.name).write_text(adapta(f.read_text(encoding="utf-8")), encoding="utf-8")
        if not f.name.startswith("00-"):
            enlaces_cuerpo.append(f.stem)
    (VAULT / "Licencia.md").write_text(
        "# Licencia y créditos\n\n" + ATRIBUCION + "\n\n"
        "Obra original: *Introduction to Python Programming*, OpenStax, Rice University, 2024. "
        "Acceso gratuito en https://openstax.org/books/introduction-python-programming/pages/1-introduction\n\n"
        "Licencia: Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional "
        "(CC BY-NC-SA 4.0), https://creativecommons.org/licenses/by-nc-sa/4.0/ . "
        "Puede copiarse, adaptarse y compartirse sin fines comerciales, citando la fuente y con la misma licencia. "
        "No se vende. OpenStax y Rice University no han revisado ni avalan esta traducción.\n\n"
        "Las figuras proceden del original; cada una conserva su línea de crédito. "
        "Maquetado con Book Studio.\n",
        encoding="utf-8",
    )
    lista = "\n".join(f"{i}. [[{s}]]" for i, s in enumerate(enlaces_cuerpo, 1))
    (VAULT / "Introducción a la programación con Python.md").write_text(
        "---\n"
        "book: true\n"
        "title: Introducción a la programación con Python\n"
        "subtitle: Traducción al español de Introduction to Python Programming (OpenStax)\n"
        "author: Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi\n"
        "language: es\n"
        "year: 2026\n"
        'description: "Libro de introducción a Python, traducido y adaptado al español."\n'
        f'copyright: "{ATRIBUCION.replace(chr(42), "")}"\n'
        "subjects: [Programación, Python, Educación]\n"
        "theme: modern\n"
        "trim: 6x9\n"
        "---\n\n"
        "## Front matter\n\n- [[Licencia]]\n- [[00-prefacio]]\n\n"
        f"## Chapters\n\n{lista}\n",
        encoding="utf-8",
    )


def renderiza() -> int:
    SALIDA.mkdir(exist_ok=True)
    tmp = RAIZ / "trabajo" / "bs-out"
    if tmp.exists():
        shutil.rmtree(tmp)
    r = subprocess.run(["npm", "run", "-s", "sample", "--", str(VAULT), "--plan", "free", "--out", str(tmp)],
                       cwd=BS, capture_output=True, text=True)
    (RAIZ / "trabajo" / "bookstudio.log").write_text(r.stdout + r.stderr, encoding="utf-8")
    print("\n".join((r.stdout + r.stderr).splitlines()[:3]))
    for ext in ("pdf", "epub"):
        hechos = list(tmp.glob(f"*.{ext}"))
        if hechos:
            shutil.copy(hechos[0], SALIDA / f"libro.{ext}")
            print(f"salida/libro.{ext}: {hechos[0].stat().st_size / 1e6:.1f} MB")
        else:
            print(f"falta {ext}")
    return r.returncode


if __name__ == "__main__":
    prepara()
    if "--solo-preparar" not in sys.argv:
        sys.exit(renderiza())
