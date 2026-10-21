# Introducción a la programación con Python

Libro libre en español para aprender a programar desde cero: el prefacio y 15 capítulos, más de 600 preguntas de repaso con su respuesta y 90 ejercicios autocorregidos que se resuelven en el navegador, también sin conexión.

Es la traducción al español de *Introduction to Python Programming* (OpenStax, 2024), de Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi, con licencia CC BY-NC-SA 4.0. Esta traducción tiene la misma licencia y no está avalada por OpenStax.

## Cómo leerlo

- **En línea:** https://perezamadorluisenrique-gif.github.io/libro-python-es/
- **App sin conexión:** https://perezamadorluisenrique-gif.github.io/libro-python-es/app/. Ejecuta Python en el navegador con Pyodide. Tras la primera visita, que descarga unos 20 MB, funciona sin red.
- **PDF y EPUB:** en la [última versión](https://github.com/perezamadorluisenrique-gif/libro-python-es/releases/latest).

## Qué hay aquí

| Carpeta | Contenido |
|---|---|
| `libro/` | El libro en Markdown, un fichero por capítulo |
| `ejercicios/` | 90 ejercicios (enunciado, código inicial, pruebas, pistas, solución) y el arnés que los corrige |
| `glosario.tsv` | Los 263 términos de la traducción, inglés → español |
| `media/` | Figuras del original |
| `app/` | App sin conexión: lector, ejercicios con Pyodide en un Web Worker y service worker |
| `web/` | Página de inicio |
| `herramientas/` | `construir.py` construye la web en `_site/`; `libro_bookstudio.py` prepara el PDF y el EPUB |
| `pruebas/` | Prueba sin conexión y de accesibilidad (Playwright + axe-core) |

## Construir y probar

Requisitos: Node 22 y Python 3.11 o posterior.

```bash
npm ci
npm run build                          # construye _site/
npx playwright install chromium        # solo la primera vez
npm test                               # app sin conexión + axe-core
python3 herramientas/comprobar.py      # texto: glosario, código que corre, salidas
python3 -m http.server -d _site 8000   # http://localhost:8000
```

`.github/workflows/pages.yml` hace lo mismo en cada push a `main` y publica `_site/` en GitHub Pages.

El PDF y el EPUB se maquetan con [Book Studio](https://github.com/perezamadorluisenrique-gif/book-studio) y se adjuntan a cada *release* (no se guardan en el repositorio):

```bash
git clone --depth 1 https://github.com/perezamadorluisenrique-gif/book-studio trabajo/book-studio
(cd trabajo/book-studio && npm ci)
python3 herramientas/libro_bookstudio.py   # salida/libro.pdf y salida/libro.epub
```

## Erratas y mejoras

Las erratas y sugerencias de traducción son bienvenidas como *issues* o *pull requests*. Si propones un término nuevo, mira antes `glosario.tsv`. `REVISION.md` recoge la segunda revisión completa del texto, y `herramientas/comprobar.py` debe seguir en verde tras cualquier cambio.

## Licencia

El texto, los ejercicios y las figuras son CC BY-NC-SA 4.0: puedes copiarlos, adaptarlos y compartirlos sin fines comerciales, citando la fuente y con la misma licencia. El código es MIT. Detalles en [LICENSE.md](LICENSE.md) y [CREDITOS.md](CREDITOS.md).

---

## In English

*Introducción a la programación con Python* is a free Spanish translation of OpenStax's *Introduction to Python Programming* (2024). It covers the preface and 15 chapters, with 600+ review questions and their answers. It also adds 90 auto-graded exercises that run Python in the browser through Pyodide, offline too. You can read it online, use the offline app, or download the PDF and EPUB from the releases. An English home page is at https://perezamadorluisenrique-gif.github.io/libro-python-es/en/ (the book itself is in Spanish).

The text is CC BY-NC-SA 4.0, like the original. OpenStax has not reviewed or endorsed this translation. The code is MIT. To build it: `npm ci && npm run build && npm test`.
