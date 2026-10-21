# Capítulo 7: Módulos

<!-- modulo: m00051 -->

## Introducción

![Fotografía de paisaje de montañas con colores que van del naranja al rosa y al morado](media/Python_07_00_000.jpg)

*crédito: modificación de la obra «Lone Pine Sunset», de Romain Guy/Flickr, dominio público*

A medida que los programas se vuelven más largos y complejos, resulta útil organizar el código en módulos. Este capítulo muestra cómo definir, importar y encontrar módulos nuevos. La [biblioteca estándar](https://openstax.org/r/100pythlibrary) de Python ofrece más de 200 [módulos integrados](https://openstax.org/r/100200modules). Cientos de miles de [otros módulos](https://openstax.org/r/100pypi) están disponibles en línea.

Un **módulo** es un archivo *.py* que contiene definiciones de funciones y otras instrucciones. El nombre del módulo es el nombre del archivo sin la extensión *.py* del final. Ej.: El siguiente código, escrito en un archivo llamado *greetings.py*, define un módulo llamado `greetings`.

```python
"""Funciones que imprimen saludos estándar."""

def hello():
  print("Hello!")

def bye():
  print("Goodbye!")
```

Técnicamente, todos los programas de este libro son módulos. Pero no todos los módulos están diseñados para ejecutarse como un programa. Ejecutar *greetings.py* como programa lograría muy poco. Se definirían dos funciones, pero nunca se llamarían. Estas funciones están pensadas para ser llamadas en otros módulos.

<!-- modulo: m00052 -->

## 7.1 Conceptos básicos de los módulos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Escribir un módulo que conste solo de definiciones de funciones.
- Importar el módulo y usar sus funciones en un programa.

### Definir un módulo

Los módulos se definen colocando código en un archivo *.py*. El módulo `area` que aparece a continuación está en un archivo llamado area.py. Este módulo ofrece funciones para calcular áreas.

**Ejemplo: El módulo area**

```python
"""Funciones para calcular el área de figuras geométricas."""

import math

# Figuras 2D

def square(side):
    """Obtiene el área de un cuadrado."""
    return side**2

def rectangle(length, width):
    """Obtiene el área de un rectángulo."""
    return length * width

def triangle(base, height):
    """Obtiene el área de un triángulo."""
    return 0.5 * base * height

def trapezoid(base1, base2, height):
    """Obtiene el área de un trapecio."""
    return 0.5 * (base1 + base2) * height

def circle(radius):
    """Obtiene el área de un círculo."""
    return math.pi * radius**2

def ellipse(major, minor):
    """Obtiene el área de una elipse."""
    return math.pi * major * minor

# Figuras 3D

def cube(side):
    """Obtiene el área superficial de un cubo."""
    return 6 * side**2

def cylinder(radius, height):
    """Obtiene el área superficial de un cilindro."""
    return 2 * math.pi * radius * (radius + height)

def cone(radius, height):
    """Obtiene el área superficial de un cono."""
    return math.pi * radius * (radius + math.hypot(height, radius))

def sphere(radius):
    """Obtiene el área superficial de una esfera."""
    return 4 * math.pi * radius**2
```

**Conceptos en práctica: Definir un módulo**

<!-- pregunta: CPL-ch07-m01-p01 -->

1. ¿Cuántas funciones se definen en el módulo `area`?

   - a) 6
   - b) 10
   - c) 49

   <details><summary>Respuesta</summary>

   b) El código tiene diez instrucciones `def`, cada una de las cuales define una función.

   </details>

<!-- pregunta: CPL-ch07-m01-p02 -->

2. ¿Cuál sería el resultado de ejecutar *area.py* como programa?

   - a) Las funciones quedarían definidas y listas para ser llamadas.
   - b) Nada; el módulo no tiene instrucciones que ejecutar.
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   a) Muchos módulos constan solo de definiciones de funciones. Las funciones están pensadas para ser llamadas en otros módulos.

   </details>

<!-- pregunta: CPL-ch07-m01-p03 -->

3. ¿Cuál es el valor de retorno de `cube(5)`?

   - a) `60`
   - b) `125`
   - c) `150`

   <details><summary>Respuesta</summary>

   c) `area.cube(5)` es `6 * 5**2`, que es `6 * 25`, que es `150`.

   </details>

### Importar un módulo

El módulo definido en *area.py* se puede usar en otros programas. Al importar el módulo `area`, se quita el sufijo .py:

```python norun
import area

print("Área de una cancha de baloncesto:", area.rectangle(94, 50))
print("Área de una pista de circo:", area.circle(21))
```

La salida es:

```text
Área de una cancha de baloncesto: 4700
Área de una pista de circo: 1385.4423602330987
```

**Video:** [Importing area in a Python shell](https://www.openstax.org/r/importing-area)

**Conceptos en práctica: Importar un módulo**

<!-- pregunta: CPL-ch07-m01-p04 -->

1. ¿Qué instrucción importaría un módulo desde un archivo llamado *secret.py*?

   - a) `import secret`
   - b) `import secret.py`
   - c) `import "secret.py"`

   <details><summary>Respuesta</summary>

   a) Al importar un módulo desde otro archivo, se quita el sufijo *.py*.

   </details>

<!-- pregunta: CPL-ch07-m01-p05 -->

2. ¿Qué código devolvería el área de un círculo con un radio de 3 metros?

   - a) `circle(3)`
   - b) `area.circle(3)`
   - c) `circle.area(3)`

   <details><summary>Respuesta</summary>

   b) La función circle debe llamarse usando la variable area que hace referencia al módulo.

   </details>

<!-- pregunta: CPL-ch07-m01-p06 -->

3. Un programador quiere escribir una función que calcule el área de un hexágono. ¿Dónde debería escribirse la función?

   - a) el programa principal
   - b) el módulo area
   - c) el módulo secret

   <details><summary>Respuesta</summary>

   b) Agregar la función al módulo area facilita reutilizarla en otros programas.

   </details>

**Pruébalo: Módulo de conversión**

Escribe un módulo que defina las siguientes funciones:

1. `cel2fah(c)` –  
Convierte una temperatura de grados Celsius a Fahrenheit.  
La fórmula es `9/5 * c + 32`.
2. `fah2cel(f)` –  
Convierte una temperatura de grados Fahrenheit a Celsius.  
La fórmula es `5/9 * (f - 32)`.
3. `km2mi(km)` –  
Convierte una distancia de kilómetros a millas.  
La fórmula es `km / 1.60934`.
4. `mi2km(mi)` –  
Convierte una distancia de millas a kilómetros.  
La fórmula es `mi * 1.60934`.

Cada función debe incluir una cadena de documentación (docstring) como primera línea. Se te ha proporcionado un docstring para el módulo.

El módulo no debe hacer nada excepto definir funciones. Cuando hagas clic en el botón «Run», el módulo debe ejecutarse sin errores. No debe mostrarse ninguna salida.

<!-- coderunner: ch7/CodeRunner_07_02_01_Conversion-module -->

**Pruébalo: Vacaciones en Europa**

Escribe un programa que use el módulo `conversion` del ejercicio anterior para completar una historia corta. La salida del programa debe coincidir con el siguiente ejemplo (entrada en negrita):

```text
How fast were you driving? 180
Woah, that's like 112 mph!
What was the temperature? 35
That's 95 degrees Fahrenheit!
```

Ten en cuenta que este ejercicio requiere dos archivos:

1. *european.py*, el programa principal. Se proporcionan instrucciones de entrada y salida como punto de partida. Edita las líneas con comentarios TODO para usar el módulo conversion.
2. *conversion.py*, el otro módulo. Copia y pega tu código del ejercicio anterior. Importa este módulo en *european.py* después del docstring.

<!-- coderunner: ch7/CodeRunner_07_02_02_European-vacation -->

<!-- modulo: m00053 -->

## 7.2 Importar nombres

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Importar funciones de un módulo usando la palabra clave `from`.
- Explicar cómo evitar una colisión de nombres al importar un módulo.

### La palabra clave from

Se pueden importar funciones específicas de un módulo usando la palabra clave `from`:

```python norun
from area import triangle, cylinder
```

Estas funciones se pueden llamar directamente, sin hacer referencia al módulo:

```python norun
print(triangle(1, 2))
print(cylinder(3, 4))
```

**Para saber más**

Como se muestra a continuación, la palabra clave `from` puede dar lugar a nombres confusos.

**Video:** [Importing functions](https://www.openstax.org/r/importing-functions)

**Conceptos en práctica: La palabra clave from**

<!-- pregunta: CPL-ch07-m02-p01 -->

1. ¿Qué instrucción import se necesitaría antes de ejecutar `print(sqrt(25))`?

   - a) `from math import sqrt`
   - b) `import sqrt from math`
   - c) `import math`

   <details><summary>Respuesta</summary>

   a) Esta instrucción importa la función `sqrt` definida en el módulo math.

   </details>

<!-- pregunta: CPL-ch07-m02-p02 -->

2. ¿Cuántas variables define la instrucción `from math import sin, cos, tan`?

   - a) 0
   - b) 3
   - c) 4

   <details><summary>Respuesta</summary>

   b) Se define una variable por cada función importada: `sin`, `cos` y `tan`.

   </details>

<!-- pregunta: CPL-ch07-m02-p03 -->

3. ¿Qué error ocurriría al intentar llamar a una función que no se importó?

   - a) `ImportError`
   - b) `NameError`
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   b) Un error de nombre ocurre cuando no se encuentra el nombre de una variable, lo cual puede deberse a que falta una instrucción import.

   </details>

### Colisiones de nombres

Los módulos escritos por distintos programadores podrían usar el mismo nombre para una función. Una **colisión de nombres** ocurre cuando una función se define varias veces. Si una función se define más de una vez, se usa la definición más reciente:

```python norun
from area import cube

def cube(x):    # Colisión de nombres (reemplaza la función importada)
  return x ** 3

print(cube(2)) # Llama a la función local cube(), no a area.cube()
```

Un programador podría no darse cuenta de que la función `cube` está definida dos veces, porque no ocurre ningún error al ejecutar el programa. Las colisiones de nombres no se consideran errores y a menudo producen un comportamiento inesperado.

Se debe tener cuidado para evitar las colisiones de nombres. Seleccionar funciones específicas de un módulo para importarlas reduce el uso de memoria; sin embargo, importar un módulo completo puede ayudar a evitar colisiones, porque se usaría el formato *módulo.nombre*. Es un compromiso que el programador debe considerar.

**Video:** [Module and function names](https://www.openstax.org/r/module-function-names)

**Conceptos en práctica: Colisiones de nombres**

<!-- pregunta: CPL-ch07-m02-p04 -->

1. Un programa comienza con `from area import square, circle`. ¿Qué código causa una colisión de nombres?

   - a)

     ```python
     def area(phone):
       """Obtiene el código de área de un número de teléfono."""
     ```

   - b)

     ```python
     def circle(x, y, size):
       """Dibuja un círculo con centro en (x, y)."""
     ```

   - c)

     ```python
     def is_square(length, width):
       """Devuelve True si length y width son iguales."""
     ```

   <details><summary>Respuesta</summary>

   b) Esta instrucción reemplaza la función circle importada anteriormente, aunque `circle()` y `area.circle()` tengan parámetros distintos.

   </details>

<!-- pregunta: CPL-ch07-m02-p05 -->

2. Un programa comienza con `import area`. ¿Qué código causa una colisión de nombres?

   - a)

     ```python
     area = 51
     ```

   - b)

     ```python norun
     import cylinder from volume
     ```

   - c)

     ```python
     def cube(size):
       """Genera un cubo de Rubik de "size X size"."""
     ```

   <details><summary>Respuesta</summary>

   a) Asignar la variable area reemplaza el módulo importado anteriormente por el entero `51`. La variable ya no se puede usar para llamar a las funciones del módulo area.

   </details>

<!-- pregunta: CPL-ch07-m02-p06 -->

3. ¿Qué línea causará un error?
   
   ```python norun
   def hello():
     print("Hello!")
   
   def hello(name):
     print("Hello,", name)
   
   hello()
   hello("Chris")
   ```

   - a) línea 4
   - b) línea 7
   - c) línea 8

   <details><summary>Respuesta</summary>

   b) La definición más reciente de `hello()` requiere un argumento, por lo que esta línea produciría un error.

   </details>

**Para saber más**

Si un nombre se define, importa o asigna varias veces, Python usa la definición más reciente. Otros lenguajes permiten que varias funciones tengan el mismo nombre si los parámetros son distintos. Esta característica, conocida como **sobrecarga de funciones**, no forma parte del lenguaje Python.

**Pruébalo: Importaciones faltantes**

Agrega las instrucciones import que faltan al principio del archivo. No hagas ningún cambio en el resto del código. Al final, el programa debe ejecutarse sin errores.

<!-- coderunner: ch7/CodeRunner_07_03_03_Missing-imports -->

**Pruébalo: Recuerdos de fiesta**

El siguiente programa no se ejecuta correctamente debido a colisiones de nombres. Corrige el programa modificando las instrucciones import, las llamadas a funciones y las asignaciones de variables. La salida debe ser:

```text
Bouncy ball area: 13
Bouncy ball volume: 4
Cone hat area: 227
Cone hat volume: 209
```

<!-- coderunner: ch7/CodeRunner_07_03_04_Party-favors -->

<!-- modulo: m00054 -->

## 7.3 Código de nivel superior

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar el código que se ejecutará como efecto secundario de una importación.
- Explicar el propósito de `if __name__ == "__main__"`.

### Efectos secundarios

Los módulos definen funciones y constantes para usarlas en otros programas. Al importar un módulo, se ejecuta *todo* el código del módulo de arriba abajo. Si un módulo no se diseña con cuidado, podría ejecutarse código no deseado como efecto secundario. El código no deseado suele estar en el nivel superior, fuera de las definiciones de funciones.

**Video:** [Sphere test code](https://www.openstax.org/r/sphere-test)

**Conceptos en práctica: Efectos secundarios**

<!-- pregunta: CPL-ch07-m03-p01 -->

1. ¿Qué línea causaría un efecto secundario al importarse?
   
   ```python
   import math
   
   print("Defining sphere function")
   
   def sphere(radius):
     """Obtiene el volumen de una esfera."""
     return 4/3 * math.pi * radius**3
   ```

   - a) línea 1
   - b) línea 3
   - c) línea 5

   <details><summary>Respuesta</summary>

   b) Cada vez que se importe este módulo, Python imprimirá `"Defining sphere function"` como efecto secundario.

   </details>

<!-- pregunta: CPL-ch07-m03-p02 -->

2. El siguiente módulo *volume.py* causa un efecto secundario.
   
   ```python
   import math
   
   def sphere(radius):
     """Obtiene el volumen de una esfera."""
     return 4/3 * math.pi * radius**3
   
   for r in range(10000000):
     volume = sphere(r)
   ```

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   a) Aunque no se imprime nada, llamar a la función sphere diez millones de veces causa un retraso en el programa principal.

   </details>

<!-- pregunta: CPL-ch07-m03-p03 -->

3. El siguiente módulo *greeting.py* causa un efecto secundario.
   
   ```python norun
   name = input("¿Cómo te llamas? ")
   print(f"¡Mucho gusto, {name}!")
   live = input("¿Dónde vives? ")
   print(f"{live} es un gran lugar.")
   ```

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   a) Todo el código está en el nivel superior y no se define ninguna función. Importar este módulo ejecutaría todo el código como efecto secundario.

   </details>

### Usar __name__

Los módulos de Python suelen incluir la instrucción `if __name__ == "__main__"` para evitar efectos secundarios. Esta instrucción es verdadera cuando el módulo se ejecuta como programa y falsa cuando el módulo se importa.

**Video:** [The main module](https://www.openstax.org/r/main-module)

**Conceptos en práctica: Usar __name__**

<!-- pregunta: CPL-ch07-m03-p04 -->

1. ¿Cuál es la salida al **ejecutar** el siguiente módulo *test.py*?
   
   ```python
   import math
   
   print(math.__name__)
   print(__name__)
   ```

   - a)

     ```python norun
     >math
     test
     ```

   - b)

     ```python norun
     __main__
     test
     ```

   - c)

     ```python norun
     math
     __main__
     ```

   <details><summary>Respuesta</summary>

   c) La variable `__name__` es el nombre del módulo, a menos que el módulo se haya ejecutado como programa principal. En ese caso, `__name__` es `"__main__"`.

   </details>

<!-- pregunta: CPL-ch07-m03-p05 -->

2. ¿Cuál es la salida al **importar** el siguiente módulo *test.py*?
   
   ```python
   import math
   
   print(math.__name__)
   print(__name__)
   ```

   - a)

     ```python norun
     math
     test
     ```

   - b)

     ```python norun
     __main__
     test
     ```

   - c)

     ```python norun
     math
     __main__
     ```

   <details><summary>Respuesta</summary>

   a) Como *test.py* se importó, el valor de `__name__` es `"test"`.

   </details>

<!-- pregunta: CPL-ch07-m03-p06 -->

3. ¿Qué línea es útil para evitar efectos secundarios al importar?

   - a) `if __name__ == "main":`
   - b) `if __name__ == __main__:`
   - c) `if __name__ == "__main__":`

   <details><summary>Respuesta</summary>

   c) Esta línea se encuentra en muchos módulos de Python para comprobar si el módulo se ejecutó como programa principal.

   </details>

**Para saber más**

Las variables que empiezan y terminan con doble guion bajo tienen un significado especial en Python. Los guiones bajos dobles se llaman informalmente variables «dunder» o «mágicas». Otros ejemplos son `__doc__` (el docstring del módulo) y `__file__` (el nombre de archivo del módulo).

**Pruébalo: Efectos secundarios**

Este ejercicio es una continuación del ejercicio «Importaciones faltantes». Antes, agregaste las instrucciones import que faltaban al principio del programa. Ahora, modifica el programa para evitar efectos secundarios al importarlo como módulo:

1. Agrega `if __name__ == "__main__"` al final.
2. Mueve todo el código de prueba bajo esa instrucción `if`.

El programa debe ejecutarse sin errores y producir la misma salida que antes.

<!-- coderunner: ch7/CodeRunner_07_04_05_Side-effects -->

**Pruébalo: Prueba de conversión**

Este ejercicio es una continuación del ejercicio «Módulo de conversión». Antes, escribiste las funciones `cel2fah`, `fah2cel`, `km2mi` y `mi2km`. Escribe código de prueba al final de *conversion.py* (el archivo original) para cada una de estas funciones. El código de prueba no debe ejecutarse como efecto secundario cuando otros programas importen `conversion`. Al ejecutar *conversion.py* como programa principal, la salida de la prueba debe ser:

```python norun
0 C is 32 F
5 C is 41 F
10 C is 50 F
15 C is 59 F
20 C is 68 F

20 F is -7 C
25 F is -4 C
30 F is -1 C
35 F is 2 C
40 F is 4 C

1 km is 0.6 mi
2 km is 1.2 mi
3 km is 1.9 mi
4 km is 2.5 mi
5 km is 3.1 mi

5 mi is 8.0 km
6 mi is 9.7 km
7 mi is 11.3 km
8 mi is 12.9 km
9 mi is 14.5 km
```

<!-- coderunner: ch7/CodeRunner_07_04_06_Conversion-test -->

<!-- modulo: m00055 -->

## 7.4 La función help

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar la función `help()` para explorar el contenido de un módulo.
- Identificar las partes del código que se incluyen en la documentación.

### Colores en sitios web

Esta sección presenta un módulo de ejemplo para trabajar con [colores HTML](https://openstax.org/r/100htmlcolors). HyperText Markup Language (HTML) se usa para diseñar sitios web y aplicaciones gráficas. Los navegadores web como Chrome y Safari leen HTML y muestran el contenido correspondiente. Ej.: El código HTML `<p style="color: Red">Look out!</p>` representa un párrafo con texto rojo.

HTML define 140 [nombres de colores](https://openstax.org/r/100colornames) estándar. Se pueden especificar colores adicionales usando un formato hexadecimal: `#RRGGBB`. Los dígitos RR, GG y BB representan los componentes rojo, verde y azul del color. Ej.: `#DC143C` es 220 de rojo + 20 de verde + 60 de azul, que es el color `Crimson`.

Los valores de rojo, verde y azul van de 0 a 255 (o de 00 a FF en hexadecimal). Los valores más bajos especifican colores más oscuros, y los valores más altos especifican colores más claros. Ej.: `#008000` es el color `Green`, y `#00FF00` es el color `Lime`.

**Video:** [HTML color codes](https://www.openstax.org/r/HTML-color-codes)

**Conceptos en práctica: Códigos de color HTML**

<!-- pregunta: CPL-ch07-m04-p01 -->

1. ¿Qué color es `#000080`?

   - a) rojo granate
   - b) azul marino
   - c) verde oliva

   <details><summary>Respuesta</summary>

   b) Los dígitos tienen 0 de rojo y 0 de verde, por lo que el color debe ser un tono de azul. El azul marino es una versión más oscura del azul estándar, `#0000FF`.

   </details>

<!-- pregunta: CPL-ch07-m04-p02 -->

2. ¿Cuánto es 255 en hexadecimal?

   - a) 00
   - b) 80
   - c) FF

   <details><summary>Respuesta</summary>

   c) FF en hexadecimal es 255, la cantidad máxima de rojo, verde o azul en un color.

   </details>

<!-- pregunta: CPL-ch07-m04-p03 -->

3. ¿Qué color es más claro?

   - a) `#FFA500 (orange)`
   - b) `#008000 (green)`

   <details><summary>Respuesta</summary>

   a) Los valores de rojo, verde y azul del naranja son más altos que los valores de rojo, verde y azul del verde.

   </details>

### Módulo de ejemplo colors

Un módulo para trabajar con códigos de color HTML sería útil para diseñadores gráficos y desarrolladores web. El siguiente código de Python está en un archivo llamado *colors.py*.

- La línea 1 es el docstring del módulo.
- Las líneas 3–16 asignan variables para los colores de uso frecuente.
- Las líneas 18–24 definen una función que se usará *dentro* del módulo.
- Las líneas 26–45 definen funciones que se usarán en otros módulos.

Nota: Las funciones `tohex()` y `torgb()` usan características de Python (formato de cadenas y rebanado) que se describen más adelante en el libro. Por ahora, la documentación y los comentarios son más importantes que los detalles de implementación.

```python
"""Funciones para trabajar con nombres de colores y valores hex/rgb."""

# Colores primarios
RED = "#FF0000"
YELLOW = "#FFFF00"
BLUE = "#0000FF"

# Colores secundarios
ORANGE = "#FFA500"
GREEN = "#008000"
VIOLET = "#EE82EE"

# Colores neutros
BLACK = "#000000"
GRAY = "#808080"
WHITE = "#FFFFFF"

def _tohex(value):
  """Convierte un entero en una cadena hexadecimal de 8 bits (2 dígitos)."""
  if value <= 0:
    return "00"
  if value >= 255:
    return "FF"
  return format(value, "02X")

def tohex(r, g, b):
  """Da formato a enteros de rojo, verde y azul como un color en hexadecimal."""
  return "#" + _tohex(r) + _tohex(g) + _tohex(b)

def torgb(color):
  """Convierte un color en hexadecimal a enteros de rojo, verde y azul."""
  r = int(color[1:3], 16) # Primeros 2 dígitos
  g = int(color[3:5], 16) # 2 dígitos del medio
  b = int(color[5:7], 16) # Últimos 2 dígitos
  return r, g, b

def lighten(color):
  """Aumenta en 32 cada uno de los valores de rojo, verde y azul de un color."""
  r, g, b = torgb(color)
  return tohex(r+32, g+32, b+32)

def darken(color):
  """Disminuye en 32 cada uno de los valores de rojo, verde y azul de un color."""
  r, g, b = torgb(color)
  return tohex(r-32, g-32, b-32)
```

**Conceptos en práctica: El módulo colors**

<!-- pregunta: CPL-ch07-m04-p04 -->

1. ¿Cuáles son los componentes del color YELLOW?

   - a) rojo=0, verde=255, azul=255
   - b) rojo=255, verde=255, azul=0
   - c) rojo=255, verde=0, azul=255

   <details><summary>Respuesta</summary>

   b) El valor hexadecimal de YELLOW es `#FFFF00`, es decir, 255 de rojo + 255 de verde + 0 de azul.

   </details>

<!-- pregunta: CPL-ch07-m04-p05 -->

2. ¿Qué código devolvería un tono más oscuro de azul?

   - a) `darken(BLUE)`
   - b) `colors.darken(BLUE)`
   - c) `colors.darken(colors.BLUE)`

   <details><summary>Respuesta</summary>

   c) A la función `darken` y a la variable `BLUE` se accede mediante la variable `colors`.

   </details>

<!-- pregunta: CPL-ch07-m04-p06 -->

3. ¿Qué símbolo indica que una función no está pensada para ser llamada por otros módulos?

   - a) guion bajo (`_`)
   - b) signo de número (`#`)
   - c) dos puntos (`:`)

   <details><summary>Respuesta</summary>

   a) Los nombres de función que empiezan con un guion bajo están pensados para usarse solo dentro del módulo actual.

   </details>

### Documentación de módulos

La función integrada `help()` ofrece un resumen de las funciones y los datos de un módulo. Llamar a `help(module_name)` en un shell es una forma práctica de conocer un módulo.

**Ejemplo: Salida de help(colors) en un shell**

La documentación que aparece a continuación se genera automáticamente a partir de los docstrings de *colors.py*.

```python norun
>>> help(colors)

Help on module colors:

NAME
  colors - Funciones para trabajar con nombres de colores y valores hex/rgb.

FUNCTIONS
  darken(color)
    Disminuye en 32 cada uno de los valores de rojo, verde y azul de un color.

  lighten(color)
    Aumenta en 32 cada uno de los valores de rojo, verde y azul de un color.

  tohex(r, g, b)
    Da formato a enteros de rojo, verde y azul como un color en hexadecimal.

  torgb(color)
    Convierte un color en hexadecimal a enteros de rojo, verde y azul.

DATA
  BLACK = '#000000'
  BLUE = '#0000FF'
  GRAY = '#808080'
  GREEN = '#008000'
  ORANGE = '#FFA500'
  RED = '#FF0000'
  VIOLET = '#EE82EE'
  WHITE = '#FFFFFF'
  YELLOW = '#FFFF00'

FILE
  /home/student/Desktop/colors.py
```

**Conceptos en práctica: La función help()**

<!-- pregunta: CPL-ch07-m04-p07 -->

1. La documentación incluye comentarios del código fuente.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   b) Solo los docstrings se incluyen en la documentación. La función help ignora todos los comentarios.

   </details>

<!-- pregunta: CPL-ch07-m04-p08 -->

2. ¿En qué orden aparecen las funciones en la documentación?

   - a) orden alfabético
   - b) orden de definición
   - c) orden aleatorio

   <details><summary>Respuesta</summary>

   a) Las funciones se ordenan alfabéticamente por nombre para facilitar la búsqueda de una función.

   </details>

<!-- pregunta: CPL-ch07-m04-p09 -->

3. ¿Qué función definida en *colors.py* no se incluye en la documentación?

   - a) `_tohex`
   - b) `tohex`
   - c) `torgb`

   <details><summary>Respuesta</summary>

   a) Las funciones que empiezan con un guion bajo están pensadas para usarse solo dentro de un módulo, no en otros módulos.

   </details>

**Pruébalo: Ayuda sobre módulos**

Los módulos `random` y `statistics` son útiles para realizar experimentos científicos. Puedes familiarizarte con estos dos módulos revisando rápidamente su documentación.

Abre un shell de Python en tu computadora, o usa el que está en [python.org/shell](https://openstax.org/r/100pythonshell). Escribe las siguientes líneas, una a la vez, en el shell.

- `import random`
- `help(random)`
- `import statistics`
- `help(statistics)`

Muchos entornos de shell, incluido el de python.org, muestran la salida de `help()` una página a la vez. Usa las teclas de navegación del teclado (flechas arriba/abajo, retroceso/avance de página, inicio/fin) para leer la documentación. Cuando termines de leer, presiona la tecla Q («quit», salir) para volver al shell de Python.

**Pruébalo: Ayuda sobre funciones**

La función `help()` se puede llamar sobre funciones específicas de un módulo. Abre un shell de Python en tu computadora, o usa el que está en [python.org/shell](https://openstax.org/r/100pythonshell). Escribe las siguientes líneas, una a la vez, en el shell.

- `import random`
- `help(random.randint)`
- `help(random.choice)`
- `import statistics`
- `help(statistics.median)`
- `help(statistics.mode)`

Recuerda usar las teclas de navegación del teclado y presionar la tecla Q («quit», salir) para volver al shell de Python.

<!-- modulo: m00056 -->

## 7.5 Cómo encontrar módulos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar las diferencias entre la biblioteca estándar y PyPI.
- Buscar en python.org y pypi.org módulos de interés.

### Módulos integrados

La **biblioteca estándar de Python** es una colección de funciones y módulos integrados que respaldan tareas de programación comunes. Ej.: El módulo `math` ofrece funciones como `sqrt()` y constantes como `pi`. La documentación oficial de Python incluye una [referencia de la biblioteca](https://openstax.org/r/100pythlibrary) y un [índice de módulos](https://openstax.org/r/100200modules) para familiarizarse con la biblioteca estándar.

Durante décadas, Python ha mantenido una filosofía de «[baterías incluidas](https://openstax.org/r/100batteries)». Esta filosofía significa que la biblioteca estándar debe venir con todo lo que la mayoría de los programadores necesitan. De hecho, ¡la biblioteca estándar incluye más de 200 módulos integrados!

**Ejemplos de módulos integrados en la biblioteca estándar.**

| Módulo | Descripción |
|---|---|
| `calendar` | Funciones generales relacionadas con calendarios. |
| `datetime` | Tipos y funciones básicos de fecha y hora. |
| `email` | Genera y procesa mensajes de correo electrónico. |
| `math` | Funciones y constantes matemáticas. |
| `os` | Interactúa con el sistema operativo. |
| `random` | Genera números pseudoaleatorios. |
| `statistics` | Funciones de estadística matemática. |
| `sys` | Parámetros y funciones específicos del sistema. |
| `turtle` | Marco educativo para gráficos sencillos. |
| `zipfile` | Lee y escribe archivos comprimidos en formato ZIP. |

**Conceptos en práctica: Módulos integrados**

<!-- pregunta: CPL-ch07-m05-p01 -->

1. ¿Qué página ofrece una lista de módulos integrados ordenados por categoría?

   - a) referencia de la biblioteca
   - b) índice de módulos
   - c) PEP 2

   <details><summary>Respuesta</summary>

   a) Esta referencia describe la biblioteca estándar, incluidas las funciones, los tipos y los módulos integrados.

   </details>

<!-- pregunta: CPL-ch07-m05-p02 -->

2. ¿Cuál es el valor de `calendar.SUNDAY`?

   - a) `1`
   - b) `6`
   - c) `7`

   <details><summary>Respuesta</summary>

   b) Como se explica en la documentación del módulo `calendar`, `MONDAY` es `0` y `SUNDAY` es `6`.

   </details>

<!-- pregunta: CPL-ch07-m05-p03 -->

3. ¿Qué módulo integrado permite desarrollar interfaces gráficas de usuario?

   - a) `tkinter`
   - b) `turtle`
   - c) `webbrowser`

   <details><summary>Respuesta</summary>

   a) El módulo `tkinter` significa interfaz de Tk (Tk interface). Tk es un conjunto de herramientas estándar para crear ventanas, cuadros de texto, botones y otros widgets gráficos.

   </details>

### Módulos de terceros

El **Python Package Index** (PyPI), disponible en [pypi.org](https://openstax.org/r/100pypi), es la biblioteca oficial de software de terceros para Python. La abreviatura «PyPI» se pronuncia como *pie pea eye* (en contraste con [PyPy](https://openstax.org/r/100pypy), un proyecto distinto).

PyPI permite que cualquier persona desarrolle y comparta módulos con la comunidad de Python. Entre los autores de módulos hay personas individuales, grandes empresas y organizaciones sin fines de lucro. PyPI ayuda a los programadores a instalar módulos y recibir actualizaciones.

La mayor parte del software disponible en PyPI es gratuito y de código abierto. PyPI cuenta con el respaldo de la [Python Software Foundation](https://openstax.org/r/100foundation) y lo mantiene un grupo independiente de desarrolladores.

**Ejemplos de módulos de terceros disponibles en PyPI.**

| Módulo | Descripción |
|---|---|
| `arrow` | Convierte y da formato a fechas, horas y marcas de tiempo. |
| `BeautifulSoup` | Extrae datos de documentos HTML y XML. |
| `bokeh` | Gráficos interactivos y aplicaciones en el navegador. |
| `matplotlib` | Visualizaciones estáticas, animadas e interactivas. |
| `moviepy` | Edición, composición y procesamiento de video. |
| `nltk` | Kit de herramientas de lenguaje natural para lenguas humanas. |
| `numpy` | Paquete fundamental para la computación numérica. |
| `pandas` | Biblioteca de análisis de datos, series temporales y estadística. |
| `pillow` | Procesamiento de imágenes en jpg, png y otros formatos. |
| `pytest` | Herramienta de pruebas completa y marco de pruebas unitarias. |
| `requests` | Elegante biblioteca HTTP para conectarse a servidores web. |
| `scikit-learn` | Herramientas simples y eficientes para el análisis predictivo de datos. |
| `scipy` | Algoritmos fundamentales para la computación científica. |
| `scrapy` | Rastrea sitios web y extrae datos de páginas web. |
| `tensorflow` | Plataforma de aprendizaje automático de extremo a extremo para todos. |

**Conceptos en práctica: Módulos de terceros**

<!-- pregunta: CPL-ch07-m05-p04 -->

1. ¿Qué módulos se pueden usar para editar imágenes y videos?

   - a) `BeautifulSoup` y `Scrapy`
   - b) `Bokeh` y `Matplotlib`
   - c) `MoviePy` y `Pillow`

   <details><summary>Respuesta</summary>

   c) `MoviePy` es un módulo para la edición de video, y `Pillow` es un módulo para el procesamiento de imágenes.

   </details>

<!-- pregunta: CPL-ch07-m05-p05 -->

2. ¿Qué módulo de terceros reemplaza al módulo integrado `datetime`?

   - a) `arrow`
   - b) `calendar`
   - c) `time`

   <details><summary>Respuesta</summary>

   a) Según la sección «Features» de la documentación, `Arrow` es un «reemplazo directo y totalmente implementado de `datetime`».

   </details>

<!-- pregunta: CPL-ch07-m05-p06 -->

3. Busca el módulo webcolors en PyPI. ¿Qué función que ofrece webcolors busca el nombre de color correspondiente a un código hexadecimal?

   - a) `hex_to_name`
   - b) `name_to_hex`
   - c) `normalize_hex`

   <details><summary>Respuesta</summary>

   a) Esta función convierte un código de color en un nombre de color. Ej.: `hex_to_name("#daa520")` devuelve `"goldenrod"`.

   </details>

**Para saber más**

Los blogs de programación suelen destacar módulos de PyPI para demostrar la utilidad de Python. Los siguientes ejemplos ofrecen más información de contexto sobre los módulos mencionados arriba.

- [Top 20 Python Libraries for Data Science for 2023](https://openstax.org/r/100simplelearn)
- [24 Best Python Libraries You Should Check in 2022](https://openstax.org/r/100library2022)
- [Most Popular Python Packages in 2021](https://openstax.org/r/100packages2021)

**Pruébalo: Feliz cumpleaños**

Las páginas de documentación de los módulos suelen incluir ejemplos para ayudar a los programadores a familiarizarse con el módulo. Para este ejercicio, consulta los siguientes ejemplos de la documentación del módulo `datetime`:

- [Examples of Usage: date](https://openstax.org/r/100dateexamples)
- [Examples of Usage: timedelta](https://openstax.org/r/100timedeltaex)

Escribe un programa que cree un objeto `date` que represente tu fecha de cumpleaños. Luego obtén un objeto `date` que represente la fecha de hoy (la fecha en que se ejecuta el programa). Calcula la diferencia entre las dos fechas y muestra los resultados con el siguiente formato:

```text
Your birth date: 2005-03-14
Today's date is: 2023-06-01

You were born 6653 days ago
(that is 574819200 seconds)

You are about 18 years old
```

<!-- coderunner: ch7/CodeRunner_07_06_07_Happy-birthday -->

**Pruébalo: Una edad más exacta**

El módulo `datetime` no ofrece una forma integrada de mostrar la edad exacta de una persona. Ej.: El siguiente programa calcula una edad exacta (en años y días) usando división entera y módulo. La salida es: `You are 15 years and 4 days old`.

```text
from datetime import date

birth = date(2005, 3, 14)
today = date(2020, 3, 14) # 15 years later
delta = today - birth

years = delta.days // 365
days = delta.days % 365
print("You are", years, "years and", days, "days old")
```

Observa cómo se incluyen los años bisiestos en el cálculo. El 29 de febrero ocurre cuatro veces entre `birth` y `today`. Por lo tanto, el usuario no tiene solo 15 años, sino 15 años y 4 días.

Muchos módulos de uso común de PyPI, incluido `arrow`, están instalados en el shell de Python de [python.org/shell](https://openstax.org/r/100pythonshell). Abre el shell de Python y escribe las siguientes líneas:

```python norun
import arrow
birth = arrow.get(2005, 3, 14)
birth.humanize()
```

Consulta los ejemplos de [humanize()](https://openstax.org/r/100humanize) en la documentación del módulo `arrow`. En el shell de Python, averigua cómo mostrar la cantidad de años y días transcurridos desde `birth` usando *una sola línea de código*. Luego muestra la cantidad de años, meses y días transcurridos desde `birth`. Por último, usa la función `print()` para mostrar los resultados con este formato: `You are 18 years 4 months and 7 days old`.

Si el tiempo lo permite, experimenta con otras funciones que ofrece el módulo `arrow`.

<!-- modulo: m00057 -->

## Resumen del capítulo

Los puntos destacados de este capítulo incluyen:

- Los programas se pueden organizar en varios archivos *.py* (módulos). La palabra clave `import` permite que un programa use funciones definidas en otro archivo *.py*.
- La palabra clave `from` se puede usar para importar funciones específicas de un módulo. Sin embargo, los programas deben evitar importar (o definir) varias funciones con el mismo nombre.
- Los módulos suelen incluir la línea `if __name__ == "__main__"` para evitar que se ejecute código como efecto secundario cuando otros programas importan el módulo.
- Al trabajar en un shell, la función `help()` se puede usar para consultar la documentación de un módulo. La documentación se genera a partir de los docstrings.
- Python incluye más de 200 módulos integrados y cientos de miles de módulos de terceros. Los programadores pueden buscar módulos en [docs.python.org](https://openstax.org/r/100docstrings) y [pypi.org](https://openstax.org/r/100pypi).

**Referencia del capítulo 7.**

| Instrucción | Descripción |
|---|---|
| `import module` | Importa un módulo para usarlo en otro programa. |
| `from module import function` | Importa una función específica de un módulo. |
| `if __name__ == "__main__":` | Una línea de código que se encuentra al final de muchos módulos. Esta instrucción indica qué código se debe ejecutar si el módulo se ejecuta como programa (en otras palabras, qué código *no* se debe ejecutar si otro programa importa este módulo). |
| `help(module_name)` | Muestra la documentación del módulo indicado. La documentación incluye el docstring del módulo, seguido de una lista de las funciones definidas en el módulo, seguida de una lista de las variables globales asignadas en el módulo, seguida del nombre de archivo del módulo. |
| `help(function_name)` | Muestra el docstring de la función indicada. |
| `date(2023, 2, 14)` | Crea un objeto `date` que representa el 14 de febrero de 2023.  <br>Requiere: `from datetime import date`. |
