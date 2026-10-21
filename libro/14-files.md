# Capítulo 14: Archivos

<!-- modulo: m00101 -->

## Introducción

![primer plano de una pantalla de computadora con un menú de archivo abierto](media/Python_14_00_000.jpg)

*crédito: Larissa Chu, CC BY 4.0*

La programación suele implicar leer información de archivos y escribir información en archivos. Este capítulo comienza presentando cómo leer y escribir en archivos en Python.

La lectura y la escritura de archivos pueden provocar excepciones cuando no se encuentra el archivo especificado. Hay muchas otras situaciones en las que pueden producirse excepciones. La segunda mitad del capítulo presenta las excepciones y cómo manejarlas en Python.

<!-- modulo: m00102 -->

## 14.1 Lectura de archivos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Comprender cómo abrir un archivo con la función `open()`.
- Demostrar cómo leer información de un archivo con `read()`, `readline()` y `readlines()`.

### Abrir un archivo

Leer información de archivos y escribir información en ellos es una tarea habitual en la programación.

Python permite abrir un archivo con la función **`open()`**.

**Video:** [Abrir un archivo](https://www.openstax.org/r/opening-a-file)

**Conceptos en práctica: Abrir archivos**

<!-- pregunta: CPL-ch14-m01-p01 -->

1. ¿Cuál es la forma correcta de abrir un archivo llamado *firstfile.txt* para que su contenido se pueda leer en un programa de Python?

   - a) `open("firstfile")`
   - b) `open("firstfile.txt")`
   - c) `fileobj = open("firstfile.txt")`

   <details><summary>Respuesta</summary>

   c) El archivo se abre y se asocia con el objeto fileobj. Será posible leer el archivo mediante fileobj.

   </details>

<!-- pregunta: CPL-ch14-m01-p02 -->

2. Supón que no existe ningún archivo llamado *input.txt*. ¿Cuál es el resultado de intentar ejecutar `open("input.txt")`?

   - a) `Error`
   - b) nada
   - c) Se crea el archivo «input.txt».

   <details><summary>Respuesta</summary>

   a) El archivo debe existir en la misma carpeta que el archivo de Python para poder abrirse.

   </details>

<!-- pregunta: CPL-ch14-m01-p03 -->

3. ¿Cuál es el resultado del siguiente código?
   
   ```python norun
   fileobj = open("newfile.txt")
   print(fileobj)
   ```

   - a) `Error`
   - b) Se imprime información sobre el objeto `fileobj`.
   - c) Se imprime el contenido de *newfile.txt*.

   <details><summary>Respuesta</summary>

   b) Python interpreta este comando como un intento del programador de imprimir los detalles del objeto. Se imprimen los detalles del objeto. Ej.: `<_io.TextIOWrapper name='newfile.txt' mode='r' encoding='cp1252'>`.

   </details>

### Uso de `read()` y lectura de líneas

Python proporciona funciones que se pueden llamar sobre un objeto de archivo para leer su contenido:

- La función **`read()`** lee el contenido de un archivo y devuelve una cadena.
- La función **`readline()`** lee la siguiente línea de un archivo y devuelve una cadena.
- La función **`readlines()`** lee las líneas individuales de un archivo y devuelve una lista de cadenas con todas las líneas del archivo en orden.

**Ejemplo: Uso de read() y readlines()**

Un archivo llamado *input.txt* tiene el siguiente contenido:

```text
12
55
5
91
```

```python norun
"""Demostración de read() y readlines()"""

# Uso de read()
# Abre el archivo y lo asocia con un objeto de archivo
infile = open("input.txt")

# Lee el contenido del archivo en una cadena
str1 = infile.read()

# Imprime str1
print("Resultado de usar read():")
print(str1)

# Cierra siempre el archivo cuando termines de usarlo
infile.close()

# Uso de readlines()
# Abre el archivo y lo asocia con un objeto de archivo
infile2 = open("input.txt")

# Lee el contenido del archivo en una lista de cadenas
str_list = infile2.readlines()

# Imprime el tercer elemento de la lista de cadenas.
print("Resultado de usar readlines() e imprimir el tercer elemento de la lista de cadenas:")
print(str_list[2])

# Cierra siempre el archivo cuando termines de usarlo
infile2.close()
```

La salida del código es:

```text
Resultado de usar read():
12
55
5
91
Resultado de usar readlines() e imprimir el tercer elemento de la lista de cadenas:
5
```

**Video:** [read() y readline()](https://www.openstax.org/r/read-and-readline)

**Conceptos en práctica: Leer archivos**

<!-- pregunta: CPL-ch14-m01-p04 -->

1. ¿Cuál es la forma correcta de usar la función `read()` para leer el contenido de *input.txt* en una cadena `file_str`?

   - a) `file_str = read(fileobj)`
   - b) `file_str = read("input.txt")`
   - c) `file_str = fileobj.read()`

   <details><summary>Respuesta</summary>

   c) La función `read()` se llama sobre `fileobj`. El contenido del archivo se leerá en `file_str`.

   </details>

<!-- pregunta: CPL-ch14-m01-p05 -->

2. ¿Cuál es la forma correcta de usar la función `readlines()`?

   - a) `file_lines = readlines(fileobj)`
   - b) `file_lines = fileobj.readlines()`

   <details><summary>Respuesta</summary>

   b) La función `readlines()` se llama sobre `fileobj`. `file_lines` es la lista de cadenas `['Hello world!\n', 'How are you?\n']`.

   </details>

<!-- pregunta: CPL-ch14-m01-p06 -->

3. ¿Qué se imprime como resultado de ejecutar `print(fileobj.readline())`?

   - a) Se imprime la primera línea de *input.txt*.
   - b) Se imprime el contenido del archivo *input.txt*.
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) La función `readline()` lee la siguiente línea de un archivo. Como `readline()` se llama justo después de abrir el archivo, se lee la primera línea. Se imprime la cadena resultante `"Hello world!"`. Ten en cuenta que `readline()` incluye el carácter `'\n'`, por lo que la impresión incluirá un salto de línea adicional.

   </details>

**Pruébalo: Leer de un archivo**

Abre el archivo *test.txt* e imprime su contenido.

<!-- coderunner: ch14/CodeRunner_14_02_01_Reading-from-a-file -->

**Pruébalo: Leer un archivo línea por línea**

Se muestra el archivo *input.txt*. El archivo representa un conjunto de números enteros. La línea 1 del archivo indica cuántos enteros siguen. Escribe un programa que lea este archivo y determine el promedio de los números que siguen a la primera línea.

*input.txt*

```text
n: 5
25
13
4
6
19
```

<!-- coderunner: ch14/CodeRunner_14_02_02_Reading-from-a-file-line-by-line -->

<!-- modulo: m00103 -->

## 14.2 Escritura en archivos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Comprender cómo abrir un archivo para escribir.
- Explicar los distintos modos de abrir un archivo en Python.
- Demostrar el uso de la función `write()` para escribir en un archivo.
- Comprender la importancia de cerrar un archivo.

### Abrir un archivo para escribir

Un archivo se puede abrir para lectura, sin permitir cambios, o para escritura, permitiendo que se hagan cambios en él. El **modo** define si un archivo se abre solo para lectura o para escritura. El modo predeterminado de la función `open()` es solo lectura. Un segundo parámetro, el de modo, define el modo.

Ej.: `open("output.txt", 'w')` abre el archivo *output.txt* en modo de escritura. La siguiente tabla enumera los modos más comunes.

**Modos de la función `open()`.**

| Parámetro | Nombre y descripción del modo | Ejemplo |
|---|---|---|
| `'r'` | Modo de lectura:  <br>Abre el archivo especificado para lectura.  <br>Si el archivo no existe, se produce un error.  <br>Cuando no se usa el parámetro de modo, el comportamiento predeterminado es abrir el archivo en modo de lectura. | `fileobj = open("input.txt")`  <br>equivale a:  <br>`fileobj = open("input.txt", 'r')` |
| `'w'` | Modo de escritura:  <br>Abre el archivo especificado para escritura.  <br>Si el archivo no existe, se crea.  <br>Si el archivo ya existe, su contenido se sobrescribe. | `fileobj = open("output.txt", 'w')` |
| `'a'` | Modo de adición:  <br>Abre el archivo especificado para añadir, es decir, agregar información al final del archivo existente.  <br>Si el archivo no existe, se crea. | `fileobj = open("log.txt", 'a')` |

**Conceptos en práctica: Modos de archivo**

<!-- pregunta: CPL-ch14-m02-p01 -->

1. Para leer *logfile.txt*, ¿cuál de las siguientes líneas de código funciona mejor?

   - a) `logfile = open("logfile.txt")`
   - b) `logfile = open("logfile.txt", 'w')`
   - c) `logfile = open("logfile.txt", 'a')`

   <details><summary>Respuesta</summary>

   a) El modo predeterminado de la función `open()` es el de lectura.

   </details>

<!-- pregunta: CPL-ch14-m02-p02 -->

2. Se van a hacer adiciones a *logfile.txt*. ¿Cuál de las siguientes líneas de código funciona mejor?

   - a) `infile = open("logfile.txt")`
   - b) `infile = open("logfile.txt", 'w')`
   - c) `infile = open("logfile.txt", 'a')`

   <details><summary>Respuesta</summary>

   c) `'a'` indica el modo de adición, que permite agregar contenido al archivo.

   </details>

<!-- pregunta: CPL-ch14-m02-p03 -->

3. Se debe crear un archivo nuevo llamado *newlog.txt*. ¿Cuál de las siguientes líneas de código funciona mejor?

   - a) `logfile = open("newlog.txt")`
   - b) `logfile = open("newlog.txt", 'w')`
   - c) `logfile = open("newlog.txt", 'a')`

   <details><summary>Respuesta</summary>

   b) `'w'` indica el modo de escritura, y *newlog.txt* se creará o se sobrescribirá (si *newlog.txt* ya existe) y permitirá escribir.

   </details>

### Uso de `write()` y `close()`

La función **`write()`** se usa para escribir en un archivo que ya está abierto. La función `write()` solo acepta un parámetro de tipo cadena. Los demás tipos de variables deben convertirse a cadena antes de escribirlos con `write()`.

La función `write()` no agrega automáticamente un carácter de salto de línea como hace la función `print()`. Hay que agregar un salto de línea de forma explícita con el carácter `('\n')`.

La función `write()` escribe automáticamente en un almacén temporal llamado búfer del archivo. Para asegurarse de que la información se escriba en un archivo, hay que usar la función `close()`. La función `close()` confirma los cambios y cierra el archivo.

**Ejemplo: Escribir y añadir en un archivo**

```python
"""Operaciones para escribir y añadir en archivos."""

# Crea un archivo nuevo
opfile = open("output.txt", 'w')

# Escribe en el archivo
opfile.write("Escribiendo en un archivo nuevo.")

# Para agregar otra línea hay que usar el carácter de salto de línea
opfile.write("\nSegunda línea.")

# Asegura que los cambios se guarden cerrando el archivo
opfile.close()

# Lee y muestra el contenido del archivo
infile = open("output.txt")
print("\nLectura del archivo original:\n")
print(infile.read())
infile.close()

# Vuelve a abrir el archivo en modo de adición para agregarle contenido
opfile = open("output.txt", 'a')

# Observa el uso de los caracteres de salto de línea
opfile.write("\nAgregando al archivo.")
opfile.write("\nAgregando otra línea.")

# Asegura que los cambios se guarden cerrando el archivo
opfile.close()

# Lee y muestra el contenido del archivo modificado
infile = open("output.txt")
print("\nLectura del archivo modificado:\n")
print(infile.read())
infile.close()
```

La salida del código es:

```salida
Lectura del archivo original:

Escribiendo en un archivo nuevo.
Segunda línea.

Lectura del archivo modificado:

Escribiendo en un archivo nuevo.
Segunda línea.
Agregando al archivo.
Agregando otra línea.
```

**Video:** [write() y close()](https://www.openstax.org/r/write-and-close)

**Conceptos en práctica: Escribir en archivos**

<!-- pregunta: CPL-ch14-m02-p04 -->

1.

   ```python
   outfile = open("resources.txt", 'w')
   outfile.write("new content")
   ```

   - a) nada
   - b) El contenido del archivo *resources.txt* se sobrescribe con la línea `"new content"`.
   - c) El archivo *resources.txt* se sobrescribe, pero el contenido de *resources.txt* es incierto.

   <details><summary>Respuesta</summary>

   c) Es probable que *resources.txt* esté vacío, pero el estado de *resources.txt* es incierto. Para asegurarse de que el contenido se guarde correctamente, hay que usar la función `close()`.

   </details>

<!-- pregunta: CPL-ch14-m02-p05 -->

2.

   ```python
   outfile = open("resources.txt", 'w')
   outfile.write("new content")
   outfile.close()
   ```

   - a) El contenido del archivo *resources.txt* se sobrescribe con la línea `"new content"`.
   - b) La línea `"new content"` se agrega al final de *resources.txt*.

   <details><summary>Respuesta</summary>

   a) El modo de escritura sobrescribirá el archivo existente. La instrucción `close()` confirma los cambios en el archivo.

   </details>

<!-- pregunta: CPL-ch14-m02-p06 -->

3.

   ```python
   outfile = open("resources.txt", 'a')
   outfile.write("new content")
   outfile.close()
   ```

   - a) El contenido del archivo *resources.txt* se sobrescribe con la línea `"new content"`.
   - b) La línea `"new content"` se agrega al final de *resources.txt*.

   <details><summary>Respuesta</summary>

   b) El modo de adición agrega contenido al archivo existente. *resources.txt* se abre de modo que se puedan hacer adiciones al archivo.

   </details>

**Pruébalo: Escribir en un archivo nuevo**

Escribe una línea de texto en un archivo llamado *out.txt*. No olvides usar `close()`. *out.txt* solo debe contener la línea de texto que has escrito.

<!-- coderunner: ch14/CodeRunner_14_03_03_Writing-to-a-new-file -->

**Pruébalo: Escribir en un archivo existente**

Agrega dos líneas de texto al archivo llamado *out.log*, de modo que *out.log* tenga tres líneas después de ejecutar el código.

Pista: no olvides que necesitas un carácter de salto de línea.

<!-- coderunner: ch14/CodeRunner_14_03_04_Writing-to-an-existing-file -->

<!-- modulo: m00104 -->

## 14.3 Archivos en distintas ubicaciones y trabajo con archivos CSV

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Demostrar cómo acceder a archivos dentro de un sistema de archivos.
- Demostrar cómo procesar un archivo CSV.

### Abrir un archivo en cualquier ubicación

Cuando solo se usa el nombre del archivo como argumento de la función `open()`, el archivo debe estar en la misma carpeta que el archivo de Python que se está ejecutando. Ej.: para que `fileobj = open("file1.txt")` en *files.py* se ejecute correctamente, el archivo *file1.txt* debe estar en la misma carpeta que *files.py*.

Con frecuencia, un programador necesita abrir archivos de carpetas distintas de aquella en la que se encuentra el archivo de Python. Una **ruta** identifica de forma única la ubicación de una carpeta en una computadora. La ruta se puede usar junto con el nombre del archivo para abrir un archivo en cualquier carpeta. Ej.: para abrir un archivo llamado *logfile.log* ubicado en `/users/turtle/desktop` se puede usar lo siguiente:

`fileobj = open("/users/turtle/desktop/logfile.log")`

**Apertura de archivos en distintas rutas.**

| Sistema operativo | Ubicación del archivo | Ejemplo de la función `open()` |
|---|---|---|
| Mac | `/users/student/` | `fileobj = open("/users/student/output.txt")` |
| Linux | `/usr/code/` | `fileobj = open("/usr/code/output.txt")` |
| Windows | `c:\projects\code\` | `fileobj = open("c:/projects/code/output.txt")`  <br>o  <br>`fileobj = open("c:\\projects\\code\\output.txt")` |

*En cada uno de los casos siguientes, un archivo llamado output.txt se encuentra en una carpeta distinta de la carpeta de Python. Windows usa barras invertidas \ en lugar de barras diagonales / en la ruta. Si la barra invertida se incluye directamente en `open()`, se necesita una barra invertida adicional para que Python entienda correctamente la ubicación.*

**Conceptos en práctica: Abrir archivos en distintas ubicaciones**

<!-- pregunta: CPL-ch14-m03-p01 -->

1. `/users/turtle/files` en una Mac para lectura

   - a) `fileobj = open("out.txt")`
   - b) `fileobj = open("/users/turtle/files/out.txt")`
   - c) `fileobj = open("/users/turtle/files/out.txt", 'w')`

   <details><summary>Respuesta</summary>

   b) La ruta seguida del nombre del archivo permite abrirlo correctamente y, de forma predeterminada, en modo de lectura.

   </details>

<!-- pregunta: CPL-ch14-m03-p02 -->

2. `c:\documents\` en una computadora con Windows para lectura

   - a) `fileobj = open("out.txt")`
   - b) `fileobj = open("c:/documents/out.txt", 'a')`
   - c) `fileobj = open("c:/documents/out.txt")`

   <details><summary>Respuesta</summary>

   c) El uso de barras diagonales / en lugar de las barras invertidas \ habituales de Windows permite que la ruta se lea correctamente. La ruta seguida del nombre del archivo permite abrirlo y, al leer un archivo, es preferible el modo de lectura.

   </details>

<!-- pregunta: CPL-ch14-m03-p03 -->

3. `/users/turtle/logs` en una computadora con Linux para escritura

   - a) `fileobj = open("out.txt")`
   - b) `fileobj = open("/users/turtle/logs/out.txt")`
   - c) `fileobj = open("/users/turtle/logs/out.txt", 'w')`

   <details><summary>Respuesta</summary>

   c) El archivo se crea o se sobrescribe y se pueden escribir cambios en él.

   </details>

<!-- pregunta: CPL-ch14-m03-p04 -->

4. `c:\proj\assets` en una computadora con Windows en modo de adición

   - a) `fileobj = open("c:\\proj\\assets\\out.txt", 'a')`
   - b) `fileobj = open("c:\proj\assets\out.txt", 'a')`

   <details><summary>Respuesta</summary>

   a) Como las barras invertidas de la ruta de Windows aparecen en el argumento de cadena, donde normalmente indican a Python que forman parte de una secuencia de escape, hay que neutralizarlas con un carácter de barra invertida \ adicional.

   </details>

### Trabajo con archivos CSV

En Python, los archivos se leen y se escriben como Unicode de forma predeterminada. Muchos formatos de archivo comunes usan Unicode, como los archivos de texto (*.txt*), los archivos de código de Python (*.py*) y otros archivos de código (*.c*, *.java*).

Los archivos de valores separados por comas (CSV, *.csv*) se usan con frecuencia para almacenar datos tabulares. Estos archivos almacenan celdas de información como Unicode separadas por comas. Los archivos CSV se pueden leer con los métodos aprendidos hasta ahora, como se ve en el siguiente ejemplo.

****

![Un archivo CSV mostrado en un programa de hojas de cálculo, con los datos en filas y celdas, y en un editor de texto, que ilustra su formato sin procesar de valores separados por comas.](media/Python_14_3_image1.png)

***Archivos CSV.** Un archivo CSV es simplemente un archivo de texto con las filas separadas por caracteres de salto de línea `\n` y las celdas separadas por comas.*

Texto sin procesar del archivo:

`Title, Author, Pages\n1984, George Orwell, 268\nJane Eyre, Charlotte Bronte, 532\nWalden, Henry David Thoreau, 156\nMoby Dick, Herman Melville, 538`

**Ejemplo: Procesar un archivo CSV**

```python norun
"""Procesamiento de un archivo CSV."""
# Abre el archivo CSV para lectura
file_obj = open("books.csv")

# Las filas están separadas por caracteres de salto de línea \n, así que se puede usar readlines() para leer todas las filas en una lista de cadenas
csv_rows = file_obj.readlines()

list_csv = []

# Quita los caracteres \n de cada fila, sepárala por comas y guárdala en una estructura 2D
for row in csv_rows:
  # Quita el carácter \n
  row = row.strip("\n")
  # Separa usando comas
  cells = row.split(",")
  list_csv.append(cells)

# Imprime el resultado
print(list_csv)
```

La salida del código es:

```text
[['Title', ' Author', ' Pages'], ['1984', ' George Orwell', ' 268'], ['Jane Eyre', ' Charlotte Bronte', ' 532'], ['Walden', ' Henry David Thoreau', ' 156'], ['Moby Dick', ' Herman Melville', ' 538']]
```

**Conceptos en práctica: Tipos de archivo y archivos CSV**

<!-- pregunta: CPL-ch14-m03-p05 -->

1. ¿Por qué funciona `readlines()` para leer las filas de un archivo CSV?

   - a) `readlines()` lee línea por línea usando el carácter de salto de línea `\n`.
   - b) `readlines()` no es adecuado para leer un archivo CSV.
   - c) `readlines()` reconoce automáticamente un archivo CSV y funciona en consecuencia.

   <details><summary>Respuesta</summary>

   a) El carácter de salto de línea `\n` indica dónde están los saltos de línea de un archivo y la función `readlines()` lo usa para distinguir las líneas.

   </details>

<!-- pregunta: CPL-ch14-m03-p06 -->

2. Para el código del ejemplo, ¿cuál sería la salida de la instrucción `print(list_csv[1][2])`?

   - a) `532`
   - b) `268`
   - c) `Jane Eyre`

   <details><summary>Respuesta</summary>

   b) La celda de la 2.ª fila y la 3.ª columna contiene `'268'`.

   </details>

<!-- pregunta: CPL-ch14-m03-p07 -->

3. ¿Cuál es la salida del siguiente código para el archivo *books.csv* que se vio arriba?
   
   ```python norun
   file_obj = open("books.csv")
   
   csv_read = file_obj.readline()
   
   print(csv_read)
   ```

   - a) `['Title, Author, Pages\n', '1984, George Orwell, 268\n', 'Jane Eyre, Charlotte Bronte, 532\n', 'Walden, Henry David Thoreau, 156\n', 'Moby Dick, Herman Melville, 538']`
   - b) `[['Title', ' Author', ' Pages'], ['1984', ' George Orwell', ' 268'], ['Jane Eyre', ' Charlotte Bronte', ' 532'], ['Walden', ' Henry David Thoreau', ' 156'], ['Moby Dick', ' Herman Melville', ' 538']]`
   - c) `Title, Author, Pages`

   <details><summary>Respuesta</summary>

   c) La primera línea de *books.csv* se lee en `csv_read`. La primera línea es `'Title, Author, Pages'`, que es igual que la primera fila.

   </details>

**Para saber más**

Archivos como los documentos de Word (*.docx*) y los documentos PDF (*.pdf*), formatos de imagen como Portable Network Graphics (PNG, *.png*) y Joint Photographic Experts Group (JPEG, *.jpeg* o *.jpg*), así como muchos otros tipos de archivo, se codifican de forma diferente.

Algunos tipos de archivos que no son Unicode se pueden leer con bibliotecas especializadas que permiten leer y escribir distintos tipos de archivo.

[PyPDF](https://openstax.org/r/100readthedocs) es una biblioteca popular que se puede usar para extraer información de archivos PDF.

[BeautifulSoup](https://openstax.org/r/100software) se puede usar para extraer información de archivos XML y HTML. Los archivos XML y HTML suelen contener Unicode con una estructura dada por etiquetas entre corchetes angulares <>.

[python-docx](https://openstax.org/r/100readwrtedocx) se puede usar para leer y escribir archivos DOCX.

Además, [csv](https://openstax.org/r/100csvlibrary) es una biblioteca integrada que se puede usar para extraer información de archivos CSV.

**Pruébalo: Procesar un archivo CSV**

El archivo *fe.csv* contiene las calificaciones de un grupo de estudiantes en un examen final. Escribe un programa que muestre la calificación promedio.

<!-- coderunner: ch14/CodeRunner_14_04_05_Processing-a-CSV-file -->

<!-- modulo: m00105 -->

## 14.4 Manejo de excepciones

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir dos excepciones que pueden producirse al leer archivos.
- Escribir instrucciones `try`/`except` que manejen excepciones integradas.

### Errores en tiempo de ejecución

Al leer un archivo pueden producirse varios errores:

- `FileNotFoundError`: el nombre del archivo o la ruta no son válidos.
- `IndexError`/`ValueError`: el formato del archivo no es válido.
- Otros errores causados por un contenido no válido del archivo.

Cuando se produce un error, el programa termina con un mensaje de error.

**Ejemplo: Una errata en un archivo**

Un archivo llamado food_order.txt tiene el siguiente contenido:

```text
5 sandwiches
4 chips
1 pickle
soft drinks
```

El siguiente programa espera que cada línea del archivo comience con un entero:

```python norun
for line in open("food_order.txt"):
    space = line.index(" ")
    qty = int(line[:space])
    item = line[space+1:-1]
    print(qty, item)
```

Lamentablemente, la línea `"soft drinks"` no comienza con un entero. Como resultado, el programa termina y muestra un mensaje de error:

```python norun
Traceback (most recent call last):
  File "food_order.py", line 3
    qty = int(line[:space])
ValueError: invalid literal for int() with base 10: 'soft'
```

**Conceptos en práctica: Excepciones comunes**

<!-- pregunta: CPL-ch14-m04-p01 -->

1. La línea `"soft drinks"` se cambia por `"3-4 soft drinks"`.

   - a) `FileNotFoundError`
   - b) `IndexError`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   c) La cadena `"3-4"` no es un entero, por lo que la función `int()` genera un `ValueError` igual que antes.

   </details>

<!-- pregunta: CPL-ch14-m04-p02 -->

2. `for line in open("food_order.text"):`

   - a) `FileNotFoundError`
   - b) `IndexError`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   a) El nombre del archivo debería terminar en `.txt`, no en `.text`.

   </details>

<!-- pregunta: CPL-ch14-m04-p03 -->

3.

   ```python norun
   parts = line.split()
   qty = parts[0]
   item = parts[1]
   ```

   - a) `FileNotFoundError`
   - b) `IndexError`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   b) Si la línea no tiene espacios, `len(parts)` será solo `1`, y `parts[1]` estará fuera de rango.

   </details>

**Para saber más**

La página [Excepciones integradas](https://openstax.org/r/100exceptions) de la biblioteca estándar de Python explica el significado de cada excepción.

### Try y except

Los programas se pueden diseñar para manejar excepciones en lugar de terminar. Una instrucción **try** ejecuta código que podría generar una excepción. Una cláusula `except` ejecuta código en respuesta a la excepción.

**Ejemplo: Intentar abrir un archivo**

El siguiente programa, llamado *try_open.py*, pide al usuario un nombre de archivo y cuenta el número de líneas del archivo.

```python norun
name = input("Introduce un nombre de archivo: ")
try:
    file = open(name)
    lines = file.readlines()
    count = len(lines)
    print(name, "tiene", count, "líneas")
except FileNotFoundError:
    print("Archivo no encontrado:", name)
print("¡Que tengas un buen día!")
```

Al ejecutar este programa con la entrada *try_open.py*, el nombre del propio archivo del programa, la salida es:

```text
Introduce un nombre de archivo: try_open.py
try_open.py tiene 9 líneas
¡Que tengas un buen día!
```

Si el nombre del archivo no existe, se genera un `FileNotFoundError` en la línea 3. Entonces el programa salta a la cláusula `except` de la línea 7 y continúa ejecutándose. La salida resultante es:

```text
Introduce un nombre de archivo: try_open.txt
Archivo no encontrado: try_open.txt
¡Que tengas un buen día!
```

**Conceptos en práctica: Predecir la salida con excepciones**

<!-- pregunta: CPL-ch14-m04-p04 -->

1.

   ```python
   word = "one"
   try:
     number = int(word)
     print(word, "equals", number)
   except ValueError:
     print(word, "is not a number")
   ```

   - a) `one equals 1`
   - b) `one is not a number`
   - c) `ValueError: invalid literal for int() with base 10: 'one'`

   <details><summary>Respuesta</summary>

   b) La función `int()` genera un `ValueError` al intentar convertir `"one"` en un entero, por lo que el programa salta a la cláusula except.

   </details>

<!-- pregunta: CPL-ch14-m04-p05 -->

2.

   ```python norun
   word = "one"
   try:
     number = int(word)
     print(word, "equals", number)
   except IndexError:
     print(word, "is not a number")
   ```

   - a) `one equals 1`
   - b) `one is not a number`
   - c) `ValueError: invalid literal for int() with base 10: 'one'`

   <details><summary>Respuesta</summary>

   c) El programa falla y muestra este error porque la cláusula except no maneja `ValueError`.

   </details>

<!-- pregunta: CPL-ch14-m04-p06 -->

3.

   ```python
   word = "one"
   try:
     char = word[3]
     print("The char is", char)
   except:
     print("That didn't work")
   ```

   - a) `The char is e`
   - b) `That didn't work`
   - c) `IndexError: string index out of range`

   <details><summary>Respuesta</summary>

   b) Si una cláusula except no especifica un tipo de error concreto, se maneja cualquier tipo de error.

   </details>

**Pruébalo: Analizador de tipos**

Los programas de análisis a menudo necesitan encontrar números en grandes cuerpos de texto. ¿Cómo puede un programa saber si una cadena como `"123.45"` representa un número? Un enfoque es usar excepciones:

1. Intenta convertir la cadena en un entero. Si no se genera un `ValueError`, la cadena representa un entero.
2. De lo contrario, intenta convertir la cadena en un float. Si no se genera un `ValueError`, la cadena representa un float.
3. De lo contrario, la cadena no representa un número.

Implementa la función `get_type()` con este enfoque. El bloque principal proporcionado llama a `get_type()` para cada palabra de un archivo. `get_type()` debe devolver `"int"`, `"float"` o `"str"`, según la palabra. La salida para el archivo data.txt proporcionado es:

```text
str: Hello
int: 100
str: times!
float: 3.14159
str: is
str: pi.
```

<!-- coderunner: ch14/CodeRunner_14_05_06_Type-analyzer -->

**Pruébalo: Países unidos**

Escribe un programa que pida al usuario que introduzca una palabra y un nombre de archivo. El programa debe imprimir cada línea del archivo que contenga la palabra. Este es un ejemplo de ejecución del programa (la entrada del usuario aparece en negrita):

```text
Enter a word: United
Enter a filename: countries.csv
United Arab Emirates,9890402,83600,118
United Kingdom,67886011,241930,281
United States of America,331002651,9147420,36
```

Este ejemplo usa un archivo llamado countries.csv basado en la [lista alfabética de países](https://openstax.org/r/100countries) de Worldometer. Cada línea del archivo incluye el nombre de un país, su población, su superficie terrestre y su densidad de población, separados por comas.

El usuario podría escribir mal el nombre del archivo (Ej.: *countries.txt* en lugar de *countries.csv*). Tu programa debe mostrar un mensaje de error si no se encuentra el archivo, y seguir pidiendo al usuario que introduzca un nombre de archivo hasta que se encuentre:

```text
...
Enter a filename: countries
File not found: countries
Enter a filename: countries.txt
File not found: countries.txt
Enter a filename: countries.csv
...
```

Pista: intenta abrir el archivo especificado por el usuario. Se genera un `FileNotFoundError` si el nombre del archivo no es válido.

<!-- coderunner: ch14/CodeRunner_14_05_07_United-countries -->

<!-- modulo: m00106 -->

## 14.5 Generar excepciones

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar una instrucción `raise` para indicar que la entrada del usuario no es válida.
- Explicar el flujo de ejecución cuando se genera una excepción.

### La instrucción raise

Un programa puede generar una excepción cuando detecta un error. Generar una excepción obliga al programa a tratar el error. Si la excepción no se maneja con `try` y `except`, el programa muestra un mensaje de error y termina.

**Ejemplo: Tamaño de pizza no válido**

La siguiente clase representa una pizza a la venta. El diccionario `SIZES` asocia una abreviatura con el nombre y el precio de un tamaño. La línea 11 comprueba si el tamaño recibido por el constructor está en el diccionario. La línea 12 genera un `ValueError` con un mensaje de error específico.

```python norun
class Pizza:

    SIZES = {
        "S": ("Small", 5.99),
        "M": ("Medium", 7.99),
        "L": ("Large", 9.99),
        "XL": ("X-Large", 11.99),
    }

    def __init__(self, size):
        if size not in Pizza.SIZES:
          raise ValueError(f"Unknown size '{size}'")
        self.size = size

    def __str__(self):
        name, price = Pizza.SIZES[self.size]
        return f"{name} pizza for ${price}"

if __name__ == "__main__":
    p1 = Pizza("L")
    print(p1)
    p2 = Pizza("Z")
    print(p2)
```

```python norun
Large pizza for $9.99
Traceback (most recent call last):
  File "pizza.py", line 23, in <module>
    p2 = Pizza("Z")
  File "pizza.py", line 12, in __init__
    raise ValueError(f"Unknown size '{size}'")
ValueError: Unknown size 'Z'
```

Generar una excepción en un constructor evita que se construya un objeto no válido. En el ejemplo, `p1` se construye pero `p2` no.

**Conceptos en práctica: Predecir la salida con raise**

<!-- pregunta: CPL-ch14-m05-p01 -->

1.

   ```python norun
   p3 = Pizza("M")
   print(p3)
   ```

   - a) `Medium pizza for $7.99`
   - b) `ValueError: Unknown size 'M'`
   - c) `TypeError: missing argument`

   <details><summary>Respuesta</summary>

   a) `"M"` es un tamaño válido, por lo que el objeto `Pizza` se construye.

   </details>

<!-- pregunta: CPL-ch14-m05-p02 -->

2. `raise PizzaError("Invalid size")`

   - a) `Invalid size`
   - b) `PizzaError: Invalid size`
   - c) `NameError: name 'PizzaError' is not defined`

   <details><summary>Respuesta</summary>

   c) `PizzaError` no es un tipo de excepción integrado.

   </details>

<!-- pregunta: CPL-ch14-m05-p03 -->

3. `raise ValueError`

   - a) `ValueError`
   - b) `NameError: name 'ValueError' is not defined`
   - c) `SyntaxError: Missing parenthesis in call to 'ValueError'`

   <details><summary>Respuesta</summary>

   a) Se puede generar una excepción sin proporcionar un mensaje de error. En ese caso, el mensaje de error está vacío, pero el nombre de la excepción se imprime igualmente.

   </details>

**Pruébalo: Objetos de idioma**

El archivo top27.csv se basa en la [lista de idiomas por número de hablantes nativos](https://openstax.org/r/100languages) de Wikipedia. Un lingüista quiere trabajar con estos datos de forma orientada a objetos y ya ha definido una clase `Language`. Sin embargo, el código no funciona correctamente por errores en el archivo CSV. (El programa de CSV no se puede cambiar porque su propósito es detectar este tipo de errores.)

Tu tarea es modificar el constructor para que genere un `ValueError` en las siguientes situaciones:

- Si la línea no tiene exactamente cuatro valores (separados por comas).
- Si el número de hablantes no es un número de punto flotante positivo.

Nota: el archivo top27.csv proporcionado incluye errores en inglés, coreano y francés. Tu programa debe generar un `ValueError` solo para esos idiomas. No se debe generar ningún otro error (incluido `IndexError`).

<!-- coderunner: ch14/CodeRunner_14_06_08_Language-objects -->

**Pruébalo: Búsqueda de claves**

Al buscar un valor en un diccionario, una clave debe coincidir exactamente. Ej.: dado `fruit = {"apple": 1, "banana": 2}`, la expresión `fruit["Apple"]` genera un `KeyError` porque `"Apple"` no es igual que `"apple"`. Del mismo modo, `fruit["NANA"]` genera un `KeyError` porque `"nana"` no coincide exactamente con `"banana"`.

Implementa la función `lookup()`. Esta función intenta encontrar en el diccionario una clave que coincida con el término de búsqueda. Una clave coincide si el término de búsqueda es una subcadena de la clave, sin distinguir entre mayúsculas y minúsculas. Ej.: la clave `"banana"` coincide con el término de búsqueda `"NANA"`.

Si no se encuentra ninguna clave que coincida, `lookup()` debe generar un `KeyError` con el mensaje `"search term not found"`. Si se encuentran varias coincidencias, `lookup()` debe generar un `KeyError` con el mensaje `"multiple keys found"`. En caso contrario, `lookup()` debe devolver tanto la clave como el valor del elemento coincidente del diccionario.

Dado el archivo books.csv, la salida debe ser:

```text
Found: ('Pride and Prejudice', 9780141439518)
Found: ('The Hobbit', 9780547928227)
Error: search term not found
Error: multiple keys found
```

<!-- coderunner: ch14/CodeRunner_14_06_09_Looking-up-keys -->

<!-- modulo: m00107 -->

## Resumen del capítulo

Los puntos principales de este capítulo son:

- Python puede leer y escribir datos en archivos con la función integrada `open()`.
- Debido al uso de búfer, es posible que los cambios en un archivo no sean visibles hasta que se cierre el archivo.
- Hay que quitar o agregar los caracteres de salto de línea al leer o escribir archivos.
- Los archivos de valores separados por comas (CSV) se usan habitualmente para representar datos.
- Las excepciones que provocan la terminación de un programa se pueden manejar con `try` y `except`.
- Generar una excepción es una forma alternativa de salir de una función cuando se produce un error.

**Referencia del capítulo 14.**

| Instrucción | Descripción |
|---|---|
| `file = open("myfile.txt")` | Abre un archivo para lectura. |
| `file = open("myfile.txt", 'w')` | Abre un archivo para escritura. |
| `file = open("myfile.txt", 'a')` | Abre un archivo para añadir contenido. |
| `file.close()` | Cierra un archivo después de hacer cambios. |
| `data = file.read()` | Lee todo el contenido de un archivo. La variable `data` es una cadena. |
| `data = file.readline()` | Lee la siguiente línea de un archivo. La variable `data` es una cadena. |
| `data = file.readlines()` | Lee todas las líneas de un archivo. La variable `data` es una lista de cadenas. |
| `file.write("Have a nice day!\n")` | Escribe una línea en un archivo. A diferencia de `print()`, la función `write()` no agrega automáticamente un salto de línea. |
| `file.write(["Line 1\n", "Line 2\n"])` | Escribe varias líneas en un archivo. Igual que con `write()`, no se agrega automáticamente un salto de línea al final de cada línea. |
| ```python<br>try:<br>    # Instrucciones<br>except:<br>    # Instrucciones<br>``` | Intenta ejecutar instrucciones que podrían generar un error. Si se genera cualquier error, ejecuta otras instrucciones. |
| ```python<br>try:<br>    # Instrucciones<br>except ValueError:<br>    # Instrucciones<br>``` | Intenta ejecutar instrucciones que podrían generar un `ValueError`. Si se genera un `ValueError`, ejecuta otras instrucciones. |
| ```python<br>try:<br>    # Instrucciones<br>except ValueError as err:<br>    # Instrucciones<br>``` | Intenta ejecutar instrucciones que podrían generar un `ValueError`. Si se genera un `ValueError`, ejecuta otras instrucciones. La variable `err` contiene más detalles sobre el `ValueError`. |
| ` raise ValueError ` | Genera un `ValueError` sin un mensaje de error específico. |
| ` raise ValueError("number is prime") ` | Genera un `ValueError` con el mensaje `"number is prime"`. |
