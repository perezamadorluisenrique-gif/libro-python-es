// Markdown -> HTML with the same `marked` the app uses. Reads a JSON array of strings
// from the file given as argv[2] and prints a JSON array of HTML strings.
import fs from "node:fs";
import { marked } from "marked";

const textos = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
process.stdout.write(JSON.stringify(textos.map((t) => marked.parse(t, { gfm: true }))));
