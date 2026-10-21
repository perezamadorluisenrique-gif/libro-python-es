# Créditos y licencias

## Obra original

*Introduction to Python Programming*, OpenStax, Rice University, 2024.
Autores principales: Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi.
Acceso gratuito en https://openstax.org/books/introduction-python-programming/pages/1-introduction
Fuente CNXML: https://github.com/openstax/osbooks-introduction-python-programming (rama `main`; preguntas «Concepts in Practice» de la rama `exercises_migration_main`).
Licencia: Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0), https://creativecommons.org/licenses/by-nc-sa/4.0/

## Esta obra derivada

«Introducción a la programación con Python» es una traducción y adaptación al español de la obra anterior.
Se distribuye con la misma licencia, **CC BY-NC-SA 4.0**: puede copiarse, adaptarse y compartirse sin fines comerciales, citando la fuente y con la misma licencia. No se vende.
OpenStax y Rice University no han revisado ni avalan esta traducción. No se usan su logotipo ni su marca.

Nota de atribución que acompaña a cada copia:

> Traducido y adaptado al español de *Introduction to Python Programming* (OpenStax, 2024), de Udayan Das, Aubrey Lawson, Chris Mayfield y Narges Norouzi, disponible gratis en openstax.org, con licencia CC BY-NC-SA 4.0. Esta traducción tiene la misma licencia y no está avalada por OpenStax.

## Imágenes

Las figuras de `fuente/media/` proceden del repositorio original; cada una conserva su línea de crédito («credit: …») en el texto. Algunas tienen licencias propias indicadas en esa línea.

## Lo que NO se reutiliza

- El «code runner» interactivo del original (`media/interactive/coderunner/`, Monaco + Skulpt) lo desarrolló Wiley y queda fuera de la licencia CC: no se copia. Los ejercicios y la app de este proyecto son propios y usan Pyodide (licencia MPL 2.0).

## PDF y EPUB (assets de cada release)

- Maquetados con **Book Studio** (Siulved54, licencia MIT; repositorio `perezamadorluisenrique-gif/book-studio`), plan gratuito, tema «Modern», 6" × 9".
- Las fuentes que Book Studio incrusta (Crimson Pro, Montserrat, Inconsolata, etc.) tienen la licencia SIL Open Font License 1.1, que permite incrustarlas en documentos.
- Bibliotecas que usa Book Studio: pdf-lib, fontkit, JSZip, marked, yaml y hyphen (licencias MIT/BSD).

## Web

- La web (`_site/`) se construye con `herramientas/construir.py`. Usa Pyodide 0.27.7 (MPL 2.0) y marked 15.0.12 (MIT), empaquetados localmente: no carga nada de otros servidores.
- Pruebas: Playwright 1.56.0 (Apache-2.0) y axe-core 4.10.3 (MPL 2.0), solo en desarrollo.
