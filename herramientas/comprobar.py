#!/usr/bin/env python3
"""Check the Spanish book text in libro/.

Usage:
    python3 herramientas/comprobar.py                 # every chapter in libro/
    python3 herramientas/comprobar.py 05-loops.md     # one chapter
    python3 herramientas/comprobar.py --fuente DIR    # also compare structure with the English source (DIR/NN-*.md)

Checks (adapted from the `score` script of the original project):
  * glosario.tsv is valid and the prose uses none of its forbidden variants (column `evitar`);
  * every ```python block runs without error and every ```salida block matches the output of
    the python block just before it;
  * the answer letter of each question matches herramientas/claves.tsv (if present);
  * with --fuente: same anchors (<!-- modulo/pregunta/coderunner -->), same number of headings
    and same sequence of code blocks as the source chapter.

Exit code 0 when everything passes. Prints one line per chapter: `OK NN-x.md` or `MAL NN-x.md: ...`.
"""
import csv
import keyword
import os
import re
import subprocess
import sys
import tempfile
import textwrap

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = os.path.join(RAIZ, "libro")
GLOSARIO = os.path.join(RAIZ, "glosario.tsv")
CLAVES = os.path.join(RAIZ, "herramientas", "claves.tsv")

FENCE = re.compile(r"^( *)```(.*)$")
ANCLA = re.compile(r"<!-- (modulo|pregunta|coderunner): ([^ ]+) -->")
PREGUNTA = re.compile(r"<!-- pregunta: (\S+) -->(?:(?!<!-- pregunta:).)*?</summary>\s*?\n\s*\n\s*([a-e])\)", re.S)


def bloques(md):
    L = md.split("\n")
    out, i = [], 0
    while i < len(L):
        m = FENCE.match(L[i])
        if m and L[i].strip() != "```":
            j = i + 1
            while j < len(L) and L[j].strip() != "```":
                j += 1
            out.append((m.group(2).strip(), textwrap.dedent("\n".join(L[i + 1:j])), i + 1))
            i = j + 1
        else:
            i += 1
    return out


def prosa(md):
    s = re.sub(r"^ *```.*?^ *```", " ", md, flags=re.S | re.M)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"``.+?``|`[^`\n]+`", " ", s)
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"https?://\S+", " ", s)
    return s


def titulos(md):
    sin = re.sub(r"^ *```.*?^ *```", "", md, flags=re.S | re.M)
    return len(re.findall(r"^#{1,6} ", sin, flags=re.M))


def ejecutar(code, timeout=10):
    with tempfile.TemporaryDirectory() as tmp:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", code], input="", capture_output=True,
                               text=True, timeout=timeout, cwd=tmp)
            return p.returncode, p.stdout, p.stderr
        except subprocess.TimeoutExpired:
            return -9, "", "timeout"


def normaliza(s):
    return [l.rstrip() for l in s.strip().split("\n")]


def carga_glosario():
    errs, evitar = [], []
    rows = list(csv.reader(open(GLOSARIO, encoding="utf-8"), delimiter="\t"))
    if not rows or rows[0] != ["en", "es", "evitar", "nota"]:
        errs.append("glosario: cabecera distinta de: en, es, evitar, nota")
    vistos, preferidos = set(), {}
    for k, r in enumerate(rows[1:], 2):
        if len(r) != 4:
            errs.append(f"glosario línea {k}: {len(r)} columnas")
            continue
        en, es, ev, _ = r
        if en in vistos:
            errs.append(f"glosario línea {k}: '{en}' repetido")
        vistos.add(en)
        base = en.rstrip("()")
        if base in keyword.kwlist and base != "class" and es.rstrip("()") != base:
            errs.append(f"glosario línea {k}: palabra clave de Python traducida ('{en}' → '{es}')")
        if es:
            preferidos.setdefault(es.lower(), en)
        for v in filter(None, (x.strip() for x in ev.split(","))):
            evitar.append((v, en, es))
    # A variant forbidden for one term must not be the preferred translation of another term.
    for v, en, es in evitar:
        otro = preferidos.get(v.lower())
        if otro and otro != en:
            errs.append(f"glosario: '{v}' se evita para '{en}' pero es la traducción de '{otro}'")
    return evitar, errs


def incoherencias(texto, evitar):
    t = texto.lower()
    hall = []
    for v, en, es in evitar:
        pat = r"(?<![\wáéíóúñü])" + re.escape(v.lower()) + r"(?![\wáéíóúñü])"
        c = len(re.findall(pat, t))
        if c:
            hall.append((v, es, c))
    return hall


def claves_distintas(md):
    if not os.path.exists(CLAVES):
        return []
    claves = {r["id"]: r["letra"] for r in csv.DictReader(open(CLAVES, encoding="utf-8"), delimiter="\t")}
    ids = re.findall(r"<!-- pregunta: (\S+) -->", md)
    letra = dict(PREGUNTA.findall(md))
    return [i for i in ids if i in letra and claves.get(i) != letra[i]]


def comprueba(nombre, evitar, fuente=None):
    md = open(os.path.join(LIBRO, nombre), encoding="utf-8").read()
    prob = []
    bl = bloques(md)
    if fuente:
        src = open(os.path.join(fuente, nombre), encoding="utf-8").read()
        if ANCLA.findall(md) != ANCLA.findall(src):
            prob.append("anclas distintas de la fuente")
        if titulos(md) != titulos(src):
            prob.append(f"títulos: fuente {titulos(src)}, libro {titulos(md)}")
        if [b[0] for b in bloques(src)] != [b[0] for b in bl]:
            prob.append("secuencia de bloques distinta de la fuente")
    ultimo = None
    for info, cuerpo, ln in bl:
        if info == "python":
            rc, out, err = ejecutar(cuerpo)
            if rc != 0:
                prob.append(f"línea {ln}: el bloque python falla: {err.strip().splitlines()[-1][:120] if err.strip() else rc}")
                ultimo = None
            else:
                ultimo = out
        elif info == "salida":
            if ultimo is None or normaliza(ultimo) != normaliza(cuerpo):
                prob.append(f"línea {ln}: la salida mostrada no coincide con la ejecución")
            ultimo = None
        else:
            ultimo = None
    malas = claves_distintas(md)
    if malas:
        prob.append(f"claves de respuesta distintas de herramientas/claves.tsv: {malas[:3]}")
    inc = incoherencias(prosa(md), evitar)
    if inc:
        prob.append("glosario: " + ", ".join(f"'{v}'×{c} (usar '{es}')" for v, es, c in inc))
    n_py = sum(1 for b in bl if b[0] == "python")
    return prob, n_py


def main(argv):
    fuente = None
    if "--fuente" in argv:
        i = argv.index("--fuente")
        fuente = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    nombres = argv or sorted(f for f in os.listdir(LIBRO) if f.endswith(".md"))
    evitar, errs = carga_glosario()
    for e in errs:
        print("MAL", e)
    total_py, mal = 0, bool(errs)
    for n in nombres:
        prob, n_py = comprueba(n, evitar, fuente)
        total_py += n_py
        if prob:
            mal = True
            print(f"MAL {n}: " + "; ".join(prob))
        else:
            print(f"OK {n} ({n_py} bloques python)")
    print(f"{'MAL' if mal else 'OK'}: {len(nombres)} capítulos, {total_py} bloques python, {len(evitar)} variantes vigiladas")
    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
