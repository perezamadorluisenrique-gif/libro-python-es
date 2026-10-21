// Web Worker: loads the locally bundled Pyodide and runs exercises with arnes.corre().
importScripts("pyodide/pyodide.js");

const listo = (async () => {
  const py = await loadPyodide({ indexURL: new URL("pyodide/", self.location.href).href });
  const arnes = await (await fetch("arnes.py")).text();
  py.FS.writeFile("/home/pyodide/arnes.py", arnes);
  py.runPython("import sys; sys.path.insert(0, '/home/pyodide'); import arnes");
  return py;
})();
listo.then(() => self.postMessage({ listo: true }));

self.onmessage = async (e) => {
  const { id, codigo, pruebas, entrada } = e.data;
  try {
    const py = await listo;
    const corre = py.globals.get("arnes").corre;
    const r = corre(codigo, pruebas, entrada || "");
    const [ok, salida, mensaje] = r.toJs();
    r.destroy();
    self.postMessage({ id, ok, salida, mensaje });
  } catch (err) {
    self.postMessage({ id, ok: false, salida: "", mensaje: "error interno: " + err });
  }
};
