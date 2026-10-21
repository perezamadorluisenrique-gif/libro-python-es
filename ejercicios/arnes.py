"""Exercise harness. Reads {"codigo": str, "pruebas": str} as JSON from stdin.
Runs `codigo`, then `pruebas` (plain asserts) in the same namespace. Prints the
student's output, then `OK` as the last line and exits 0 if every test passes;
otherwise prints `FALLO: <reason>` and exits 1. Pure stdlib, no subprocess, so the
same `corre()` works inside Pyodide (the app calls it directly)."""
import contextlib, io, json, sys, traceback


def corre(codigo, pruebas, entrada=""):
    """Return (ok, salida_del_alumno, mensaje)."""
    ns = {"__name__": "__main__"}
    buf = io.StringIO()
    old_in = sys.stdin
    sys.stdin = io.StringIO(entrada)
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(codigo, "<tu código>", "exec"), ns)
        ns["__salida__"] = buf.getvalue()  # tests may inspect what the program printed
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(pruebas, "<pruebas>", "exec"), ns)
    except AssertionError as e:
        return False, buf.getvalue(), "prueba fallida" + (f": {e}" if str(e) else "")
    except Exception:
        tb = traceback.format_exc().strip().splitlines()[-1]
        return False, buf.getvalue(), "error: " + tb
    finally:
        sys.stdin = old_in
    return True, buf.getvalue(), "OK"


if __name__ == "__main__":
    d = json.load(sys.stdin)
    ok, salida, msg = corre(d["codigo"], d["pruebas"], d.get("entrada", ""))
    sys.stdout.write(salida)
    if salida and not salida.endswith("\n"):
        sys.stdout.write("\n")
    print("OK" if ok else "FALLO: " + msg)
    sys.exit(0 if ok else 1)
