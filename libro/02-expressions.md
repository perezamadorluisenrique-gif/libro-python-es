# Capítulo 2: Expresiones

<!-- modulo: m00010 -->

## Introducción

![Grace Murray Hopper ante el teclado de la UNIVAC](media/Python_02_00_000.jpg)

*crédito: modificación de la obra «Grace Hopper at Univac I console», cortesía del Computer History Museum*

Un programa de computadora es una secuencia de instrucciones que se ejecutan una tras otra. En Python, muchas instrucciones constan de una o más expresiones. Una **expresión** representa un único valor que se debe calcular. Ej.: la expresión `3*x - 5` se evalúa como `7` cuando `x` vale `4`. Aprender a reconocer expresiones abre la puerta a programar todo tipo de cálculos interesantes.

Las expresiones suelen ser una combinación de literales, variables y operadores. En el ejemplo anterior, `3` y `5` son literales, `x` es una variable, y `*` y `-` son operadores. Las expresiones pueden ser arbitrariamente largas, con muchos cálculos. También pueden ser tan cortas como un solo valor. Ej.: en la instrucción de asignación `x = 5`, el literal `5` es una expresión.

El capítulo Instrucciones presentó expresiones simples como `1 * 2` y `"Hi " + "there"`. Este capítulo explora otros tipos de expresiones para trabajar con números y cadenas. La primera sección muestra una excelente manera de experimentar con expresiones usando un shell de Python. Las secciones siguientes presentan más detalles sobre los enteros y los números de punto flotante, explican cómo importar y usar el módulo `math`, y muestran cómo hacer que las líneas largas de código sean más fáciles de leer.

<!-- modulo: m00011 -->

## 2.1 El shell de Python

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar un shell de Python para ejecutar instrucciones y expresiones de forma interactiva.
- Explicar la función de los atajos de teclado de las flechas arriba y abajo.

### El intérprete

Python es un lenguaje de alto nivel, lo que significa que el código fuente está pensado para que los humanos lo entiendan. Las computadoras, en cambio, solo entienden código máquina de bajo nivel formado por unos y ceros. Los programas escritos en lenguajes de alto nivel deben traducirse a código máquina para ejecutarse. Este proceso de traducción puede ocurrir todo de una vez o poco a poco, según el lenguaje.

Python es un lenguaje interpretado: el código fuente se traduce una línea a la vez mientras el programa se ejecuta. El **intérprete** de Python traduce el código fuente a código máquina y ejecuta el programa resultante. Si ocurre un error, el intérprete deja de traducir el código fuente y muestra un mensaje de error.

La mayoría de los entornos de desarrollo incluyen un shell de Python para experimentar con el código de forma interactiva. Un **shell**, también llamado consola o terminal, es un programa que permite la interacción directa con un intérprete. Normalmente, el intérprete ejecuta un programa completo de una sola vez. Pero dentro de un shell de Python, el intérprete puede ejecutar una línea de código a la vez.

**Video:** [Running a Python shell](https://www.openstax.org/r/python-shell)

**Conceptos en práctica: Uso de un shell de Python**

<!-- pregunta: CPL-ch02-m01-p01 -->

1. Python es un lenguaje _____.

   - a) de alto nivel
   - b) de bajo nivel

   <details><summary>Respuesta</summary>

   a) La mayoría de los lenguajes de programación son de alto nivel y están pensados para que los humanos los entiendan.

   </details>

<!-- pregunta: CPL-ch02-m01-p02 -->

2. ¿Cuál de las siguientes es la línea de código más básica que puede ejecutar el intérprete?

   - a) `print(1 + 1)`
   - b) `1 + 1`
   - c) `1`

   <details><summary>Respuesta</summary>

   c) La línea de código de Python más básica es una sola expresión, como el entero `1`.

   </details>

<!-- pregunta: CPL-ch02-m01-p03 -->

3. ¿Qué resultado muestra el shell después de ejecutar la línea `name = input()`?

   - a) el nombre que se ingresó
   - b) nada (excepto &gt;&gt;&gt;)

   <details><summary>Respuesta</summary>

   b) Después de que la entrada se guarda en la memoria, el shell muestra un indicador (prompt) para la siguiente línea.

   </details>

### Las teclas de flecha

Un shell de Python es útil para explorar y depurar código. El usuario puede probar algo, mirar los resultados y luego probar otra cosa. Cuando ocurre un error, se muestra un mensaje de error, pero el programa sigue ejecutándose. Así, el usuario puede editar la línea anterior y corregir el error de forma interactiva.

La sigla REPL (se pronuncia «rep ul») se usa a menudo para referirse a un shell. **REPL** significa «read-eval-print loop» (bucle de leer, evaluar e imprimir), que describe la naturaleza repetitiva de un shell:

1. **R**ead/leer: ingresar algo de código
2. **E**valuate/evaluar: ejecutar el código
3. **P**rint/imprimir: mostrar los resultados, si los hay
4. **L**oop/repetir: volver al paso 1

La mayoría de los shells guardan un historial de cada línea de código que escribe el usuario. Al presionar la tecla de flecha arriba o abajo del teclado se muestra el historial. La **flecha arriba** muestra la línea anterior; la **flecha abajo** muestra la línea siguiente. Así, el usuario puede repetir una línea sin tener que escribirla de nuevo.

**Video:** [Correcting a typo](https://www.openstax.org/r/correcting-typo)

**Conceptos en práctica: Uso de las teclas de flecha**

<!-- pregunta: CPL-ch02-m01-p04 -->

1. ¿Qué teclas de flecha se necesitaron para corregir el error de tipeo?

   - a) solo la flecha arriba
   - b) las flechas arriba y abajo
   - c) las flechas arriba e izquierda

   <details><summary>Respuesta</summary>

   c) La flecha arriba muestra la línea anterior, y la flecha izquierda mueve el cursor dentro de esa línea.

   </details>

<!-- pregunta: CPL-ch02-m01-p05 -->

2. ¿Qué teclas presionaría el usuario para retroceder dos líneas?

   - a) presionar la flecha arriba dos veces
   - b) presionar la flecha abajo dos veces
   - c) presionar la flecha izquierda dos veces

   <details><summary>Respuesta</summary>

   a) Al presionar la flecha arriba dos veces se llega a la línea anterior a la línea previa.

   </details>

**Pruébalo: Explorar el shell**

Ejecutar código de forma interactiva es una excelente manera de aprender cómo funciona Python. Abre un shell de Python en tu computadora, o usa el que está en [python.org/shell](https://openstax.org/r/100pythonshell). Luego ingresa cualquier código de Python, una línea a la vez, para ver el resultado. Estas son algunas expresiones para probar:

- `x = 5`
- `3*x - 5`
- `3 * (x-5)`
- `x`
- `type(1)`
- `type('1')`
- `str(1)`
- `int('1')`
- `abs(-5)`
- `abs(5)`
- `len("Yo")`
- `len("HoHo")`
- `round(9.49)`
- `round(9.50)`

Nota: estas funciones (`type`, `str`, `int`, `len` y `round`) se explorarán con más detalle más adelante en el capítulo. Puedes leer más sobre las [funciones integradas](https://openstax.org/r/100builtin) en la documentación de Python.

**Pruébalo: Corregir errores**

Abre un shell de Python en tu computadora, o usa el que está en [python.org/shell](https://openstax.org/r/100pythonshell). Ejecuta las siguientes dos instrucciones en el shell:

- `x = 123`
- `y = 456`

Es común cometer errores al escribir en un shell. Las siguientes líneas incluyen errores de tipeo y de otro tipo. Para cada línea: (1) ejecuta la línea en un shell para ver el resultado, (2) presiona la flecha arriba para repetir la línea y (3) edita la línea para obtener el resultado correcto.

- `print("Easy as", X)`
- `print("y divided by 2 is", y / 0)`
- `name = intput("What is your name? ")`
- `print(name, "is", int(name), "letters long.")`
- `print("That's all folks!)`

La salida esperada, después de corregir los errores, debería verse así:

- `Easy as 123`
- `y divided by 2 is 228.0`
- `(no error/output)`
- `Stacie is 6 letters long.`
- `That's all folks!`

<!-- modulo: m00012 -->

## 2.2 Conversión de tipos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar cómo usa el intérprete la conversión implícita de tipos.
- Usar la conversión explícita de tipos con `int()`, `float()` y `str()`.

### Conversión implícita de tipos

Con frecuencia, una operación actualiza una variable y obliga a cambiar su tipo de datos. Ej.: un GPS primero asigna a `distance` el valor `250`, un entero. Después de un giro equivocado, el GPS asigna a `distance` el valor `252.5`, un float. El intérprete de Python usa la **conversión implícita de tipos** para convertir automáticamente un tipo de datos en otro. Una vez que a `distance` se le asigna `252.5`, el intérprete convertirá `distance` de entero a float sin que el programador tenga que especificar la conversión.

**Video:** [Example: Book ratings](https://www.openstax.org/r/book-ratings)

**Conceptos en práctica: Conversión implícita de tipos en la práctica**

<!-- pregunta: CPL-ch02-m02-p01 -->

1. ¿Cuál es el tipo de datos de `book_rating` en la línea 7?

   - a) float
   - b) entero

   <details><summary>Respuesta</summary>

   a) A `book_rating` se le asignó `3.5` en la línea 5 y el intérprete la convirtió de entero a float. `book_rating` no se modifica después de la línea 5.

   </details>

<!-- pregunta: CPL-ch02-m02-p02 -->

2. ¿Cuál sería el tipo de datos de `book_rating` si `update = 1.0` en lugar de `0.5`?

   - a) float
   - b) entero

   <details><summary>Respuesta</summary>

   a) Combinar un float y un entero en un cálculo produce un float. A `book_rating` se le asignaría `4.0`.

   </details>

<!-- pregunta: CPL-ch02-m02-p03 -->

3. ¿Cuál es el tipo de datos de `x` después de ejecutar el siguiente código?
   
   ```python
   x = 42.0
   x = x * 1
   ```

   - a) float
   - b) entero

   <details><summary>Respuesta</summary>

   a) Un cálculo con un float y un entero produce un float. Después de ejecutar el código, `x` es un float, `42.0`.

   </details>

### Conversión explícita de tipos

Con frecuencia, un programador necesita cambiar tipos de datos para realizar una operación. Ej.: un programa debe leer dos valores con `input()` y sumarlos. Recuerda que `input()` lee los valores como cadenas. Un programador puede usar la **conversión explícita de tipos** para convertir un tipo de datos en otro.

- **int()** convierte un tipo de datos en un entero. Se elimina cualquier parte fraccionaria. Ej.: `int(5.9)` produce `5`.
- **float()** convierte un tipo de datos en un float. Ej.: `float(2)` produce `2.0`.
- **str()** convierte un tipo de datos en una cadena. Ej.: `str(3.14)` produce `"3.14"`.

**Video:** [Example: Ordering pizza](https://www.openstax.org/r/ordering-pizza)

**Conceptos en práctica: Ejemplo: Pedir pizza**

<!-- pregunta: CPL-ch02-m02-p04 -->

1. ¿Qué función convierte el número de porciones ingresado en un tipo de datos que se pueda usar en el cálculo?

   - a) `float()`
   - b) `input()`
   - c) `int()`

   <details><summary>Respuesta</summary>

   a) `float()` convierte el número de porciones ingresado de cadena a float para el cálculo del pedido de pizza.

   </details>

<!-- pregunta: CPL-ch02-m02-p05 -->

2. ¿Cómo se podría cambiar la línea 3 para mejorar el programa en general?

   - a) Usar `float()` en lugar de `int()`.
   - b) Sumar `1` al resultado de `int()`.
   - c) Agregar `str()` alrededor de `int()`.

   <details><summary>Respuesta</summary>

   b) `int()` elimina cualquier parte fraccionaria. Muchos cálculos producirán una parte fraccionaria. Ej.: 46 personas con 3.0 porciones por persona necesitarán 138 porciones o 17.25 pizzas. `int(17.25)` es `17`, así que al sumar `1` se obtienen `18` pizzas, una mejor estimación para asegurarse de pedir suficiente pizza.

   </details>

**Conceptos en práctica: Uso de int(), float() y str()**

<!-- pregunta: CPL-ch02-m02-p06 -->

1. `y`

   - a) `4`
   - b) `5`

   <details><summary>Respuesta</summary>

   a) `y = int(4.5) = 4`. Se elimina la parte fraccionaria, 0.5.

   </details>

<!-- pregunta: CPL-ch02-m02-p07 -->

2. `str(x)`

   - a) `4.5`
   - b) `"4.5"`

   <details><summary>Respuesta</summary>

   b) `str(4.5)` produce `"4.5"`.

   </details>

<!-- pregunta: CPL-ch02-m02-p08 -->

3. `float(y)`

   - a) `4.0`
   - b) `4.5`

   <details><summary>Respuesta</summary>

   a) `float(y) = float(4) = 4.0`. La parte fraccionaria, 0.5, se eliminó durante la conversión a entero, `int(x)`.

   </details>

**Pruébalo: Promedio de calificaciones**

El siguiente programa calcula el promedio de tres calificaciones de examen predefinidas e imprime el promedio dos veces. Mejora el programa para que lea las tres calificaciones de la entrada e imprima el promedio primero como float y luego como entero, usando conversión explícita de tipos. Ignora cualquier diferencia que ocurra por el redondeo.

<!-- coderunner: ch2/CodeRunner_02_03_01_Grade-average -->

**Pruébalo: Tazas de agua**

El siguiente programa debería leer las onzas de agua que el usuario bebió hoy y calcular el número de tazas bebidas y el número de tazas que faltan por beber según una meta diaria. Supón que una taza contiene 8 onzas. Corrige el código para calcular `cups_drank` y `cups_left` y que coincida con lo siguiente:

- `ounces` es un entero que representa las onzas que bebió el usuario.
- `cups_drank` es un float que representa el número de tazas de agua bebidas.
- `cups_left` es un entero que representa el número de tazas de agua que faltan por beber (redondeado hacia abajo) de la meta diaria de 8 tazas.

<!-- coderunner: ch2/CodeRunner_02_03_02_Cups-of-water -->

**Pruébalo: Producto como float**

El siguiente programa lee dos enteros como cadenas. Calcula el producto de los dos enteros e imprime el resultado como un float.

<!-- coderunner: ch2/CodeRunner_02_03_03_Product-as-float -->

<!-- modulo: m00013 -->

## 2.3 Tipos de datos mixtos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar los tipos de datos que producen las operaciones con enteros, floats y cadenas.
- Usar operadores y conversiones de tipos para combinar enteros, floats y cadenas.

### Combinación de enteros y floats

Con frecuencia, los programadores necesitan combinar números de diferentes tipos de datos. Ej.: un programa calcula el total de un pedido de compras en línea:

```python norun
quantity = int(input())
price = float(input())
total = quantity * price
print(total)
```

`quantity` es un entero y `price` es un float. Entonces, ¿cuál es el tipo de datos de `total`? Para las entradas `3` y `5.0`, `total` es un float, y el programa imprime `15.0`.

Combinar un entero y un float produce un float. Por defecto, un float se imprime con al menos una cifra después del punto decimal y con tantas cifras como se necesiten para representar el valor. Nota: la división con el operador `/` siempre produce un float.

**Video:** [Operations combining integers and floats](https://www.openstax.org/r/combining-int-float)

**Conceptos en práctica: Operaciones que combinan enteros y floats**

<!-- pregunta: CPL-ch02-m03-p01 -->

1. `8 * 0.25`

   - a) `2`
   - b) `2.0`

   <details><summary>Respuesta</summary>

   b) Multiplicar un entero por un float produce un float.

   </details>

<!-- pregunta: CPL-ch02-m03-p02 -->

2. `2 * 9`

   - a) `18`
   - b) `18.0`

   <details><summary>Respuesta</summary>

   a) Multiplicar dos enteros produce un entero.

   </details>

<!-- pregunta: CPL-ch02-m03-p03 -->

3. `20 / 2`

   - a) `10`
   - b) `10.0`

   <details><summary>Respuesta</summary>

   b) Dividir dos enteros produce un float, incluso cuando el resultado es un número entero.

   </details>

<!-- pregunta: CPL-ch02-m03-p04 -->

4. `7 / 2`

   - a) `3.0`
   - b) `3.5`

   <details><summary>Respuesta</summary>

   b) Dividir dos enteros produce un float y no redondea.

   </details>

<!-- pregunta: CPL-ch02-m03-p05 -->

5. `12.0 / 4`

   - a) `3`
   - b) `3.0`

   <details><summary>Respuesta</summary>

   b) Dividir un float entre un entero produce un float, incluso cuando el resultado es un número entero.

   </details>

<!-- pregunta: CPL-ch02-m03-p06 -->

6. `8 - 1.0`

   - a) `7.0`
   - b) `7`

   <details><summary>Respuesta</summary>

   a) Restar un float a un entero produce un float.

   </details>

<!-- pregunta: CPL-ch02-m03-p07 -->

7. `5 - 0.25`

   - a) `4.5`
   - b) `4.75`

   <details><summary>Respuesta</summary>

   b) Restar un float a un entero produce un float y no redondea.

   </details>

### Combinación de tipos numéricos y cadenas

La facilidad de la conversión de tipos en Python puede llevar a un programador a suponer que cualquier tipo de datos se puede combinar con otro. Ej.: el programa de Noor lee un número de la entrada y lo usa en un cálculo. Esto produce un error en el programa porque la función `input()` guarda el número como una cadena por defecto. Las cadenas y los tipos de datos numéricos son incompatibles para la suma, la resta y la división. Uno de los operandos debe convertirse explícitamente, según el objetivo de la aritmética o de la concatenación de cadenas.

El operador * también sirve como operador de repetición, que acepta un operando de tipo cadena y un operando entero, y repite la cadena. Ej.: `"banjo" * 3` produce `"banjobanjobanjo"`.

**Video:** [Adding a string and an integer](https://www.openstax.org/r/adding-str-int)

**Conceptos en práctica: Operaciones que combinan tipos numéricos y cadenas**

<!-- pregunta: CPL-ch02-m03-p08 -->

1. `int('34') + 56`

   - a) `'3456'`
   - b) `90`
   - c) `'90'`

   <details><summary>Respuesta</summary>

   b) `34 + 56` produce `90`, un entero.

   </details>

<!-- pregunta: CPL-ch02-m03-p09 -->

2. `str(12) + ' red roses'`

   - a) `'12 red roses'`
   - b) `'12'`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) `'12' + ' red roses'` realiza una concatenación de cadenas.

   </details>

<!-- pregunta: CPL-ch02-m03-p10 -->

3. `'50' * 3`

   - a) `'150'`
   - b) `150`
   - c) `'505050'`

   <details><summary>Respuesta</summary>

   c) Multiplicar una cadena por un entero es un atajo útil.

   </details>

<!-- pregunta: CPL-ch02-m03-p11 -->

4. `str(5.2) + 7`

   - a) `12.2`
   - b) `'12.2'`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) Sumar `'5.2'`, una cadena, y `7`, un entero, no es una operación aceptada y provoca un error.

   </details>

<!-- pregunta: CPL-ch02-m03-p12 -->

5. `80.0 + int('100')`

   - a) `180`
   - b) `180.0`
   - c) `'180'`

   <details><summary>Respuesta</summary>

   b) Sumar un float y un entero produce un float.

   </details>

<!-- pregunta: CPL-ch02-m03-p13 -->

6. `str(3.14) + '159'`

   - a) `162.14`
   - b) `'3.14159'`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `'3.14'` y `'159'` se concatenan.

   </details>

<!-- pregunta: CPL-ch02-m03-p14 -->

7. `2.0 * 'this'`

   - a) `'this'`
   - b) `'thisthis'`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) La repetición de cadenas solo funciona con cadenas y enteros.

   </details>

**Pruébalo: Después del punto**

Escribe un programa que lea una cadena de dígitos que representa los dígitos después del punto decimal de un número, num. Concatena la cadena de entrada con `'.'` y `num`, e imprime el resultado. Ej.: si la entrada es `345`, el programa imprimirá `2.345`.

<!-- coderunner: ch2/CodeRunner_02_04_04_After-the-point -->

**Pruébalo: Imprimir n veces**

Escribe un programa que lea dos cadenas, `str1` y `str2`, y un entero, `count`. Concatena las dos cadenas con un espacio en medio y un salto de línea (`"\n"`) al final. Imprime la cadena resultante `count` veces.

<!-- coderunner: ch2/CodeRunner_02_04_05_Print-n-times -->

<!-- modulo: m00014 -->

## 2.4 Errores de punto flotante

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar las imprecisiones numéricas relacionadas con la representación de punto flotante.
- Usar la función `round()` para mitigar los errores de punto flotante en la salida.

### Errores de punto flotante

Las computadoras almacenan la información usando ceros y unos. Toda la información debe convertirse en una cadena de ceros y unos. Ej.: 5 se convierte en 101. Como solo se permiten dos valores, 0 o 1, el formato se llama binario.

Python almacena los valores de punto flotante en binario. La conversión de un número de punto flotante al binario subyacente produce tipos específicos de errores de punto flotante.

Un **error de redondeo** ocurre cuando los valores de punto flotante se almacenan erróneamente como una aproximación. La diferencia entre una aproximación de un valor usada en un cálculo y el valor correcto (verdadero) se llama error de redondeo.

Ej.: almacenar el float (0.1)<sub>10</sub> da como resultado valores binarios que en realidad producen (0.1000000000000000055511151231257827021181583404541015625)<sub>10</sub> al convertirse de nuevo, lo cual no es exactamente igual a (0.1)<sub>10</sub>.

**Error de redondeo.**

|  |  |
|---|---|
| ```python<br># Imprime floats con 30 decimales<br>print(f'{0.1:.30f}') # imprime 0.1<br>print(f'{0.2:.30f}') # imprime 0.2<br>print(f'{0.4:.30f}') # imprime 0.4<br>``` | ```python<br>0.100000000000000005551115123126<br>0.200000000000000011102230246252<br>0.400000000000000022204460492503<br>``` |

*(El ejemplo anterior muestra una cadena con formato o f-string; estas se presentan en el capítulo Objetos.)*

Un **error de desbordamiento** ocurre cuando un valor es demasiado grande para almacenarse. Los valores de punto flotante máximo y mínimo que se pueden representar son 1.8 × 10^308 y -1.8 × 10^308, respectivamente. Intentar almacenar un valor de punto flotante fuera del rango (-1.8 × 10^308,1.8 × 10^308) provoca un error de desbordamiento.

A continuación, 3.0^256 y 3.0^512 se pueden representar, pero 3.0^1024 es demasiado grande y provoca un error de desbordamiento.

**Error de desbordamiento.**

|  |  |
|---|---|
| ```python<br>print('3.0 to the power of 256 =', 3.0**256)<br>print('3.0 to the power of 512 = ', 3.0**512)<br>print('3.0 to the power of 1024 = ', 3.0**1024)<br>``` | ```python<br>3.0 to the power of 256 = 1.3900845237714473e+122<br>3.0 to the power of 512 = 1.9323349832288915e+244<br>3.0 to the power of 1024 =<br>Traceback (most recent call last):<br>  File "<stdin>", line 3, in <module><br>    print('3.0 to the power of 1024 = ', 3.0**1024)<br>OverflowError: (34, 'Numerical result out of range')<br>``` |

**Conceptos en práctica: Errores de punto flotante**

<!-- pregunta: CPL-ch02-m04-p01 -->

1. La instrucción `result = 2.0 * (10.0 ** 500)` asigna a la variable result un valor demasiado grande.

   - a) de redondeo
   - b) de desbordamiento

   <details><summary>Respuesta</summary>

   b) Ocurre un error de desbordamiento porque el valor es mayor que el límite superior del rango de punto flotante.

   </details>

<!-- pregunta: CPL-ch02-m04-p02 -->

2. `0.123456789012345678901234567890 * 0.1` produce `0.012345678901234568430878013601`.

   - a) de redondeo
   - b) de desbordamiento

   <details><summary>Respuesta</summary>

   a) Los dígitos a partir de la posición dieciocho después del punto decimal son inexactos debido a la aproximación, por lo que ocurre un error de redondeo.

   </details>

### La función round() de punto flotante

La función **round()** de Python se usa para redondear un número de punto flotante a una cantidad dada de decimales. La función requiere dos argumentos. El primer argumento es el número que se va a redondear. El segundo argumento determina el número de decimales al que se redondea el número. Si no se proporciona el segundo argumento, el número se redondeará al entero más cercano. La función `round()` se puede usar para mitigar los errores de punto flotante.

Ej.:

- `round(2.451, 2) = 2.45`
- `round(2.451) = 2`

**Video:** [Examples of round() function](https://www.openstax.org/r/round-function)

**Conceptos en práctica: Ejemplos de la función round()**

<!-- pregunta: CPL-ch02-m04-p03 -->

1. ¿Cuál es la salida de `round(6.6)`?

   - a) `6`
   - b) `6.6`
   - c) `7`

   <details><summary>Respuesta</summary>

   c) `round(6.6) = 7`, ya que 7 es el número entero más cercano a 6.6.

   </details>

<!-- pregunta: CPL-ch02-m04-p04 -->

2. ¿Cuál es la salida de `round(3.5, 2)`?

   - a) `3`
   - b) `3.5`
   - c) `3.50`

   <details><summary>Respuesta</summary>

   b) `round(3.5, 2) = 3.50`, ya que la entrada se redondea a dos decimales.

   *Nota de la traducción: Python muestra `3.5`, no `3.50`; `round()` no añade ceros al final. Para ver dos decimales se usa un formato, como `f"{3.5:.2f}"`.*

   </details>

<!-- pregunta: CPL-ch02-m04-p05 -->

3. ¿Cuál es la salida de `round(12)`?

   - a) `12.0`
   - b) `12`
   - c) `12.00`

   <details><summary>Respuesta</summary>

   b) Cuando `round()` se aplica a un valor entero sin especificar el número de decimales, el valor no cambia.

   </details>

<!-- pregunta: CPL-ch02-m04-p06 -->

4. ¿Cuál es la salida de `round(0.1, 1)`?

   - a) `0.1`
   - b) `0.10`
   - c) `0.1000000000000000055511151231257827021181583404541015625`

   <details><summary>Respuesta</summary>

   a) `round(0.1, 1)` redondea el valor `0.1` a un decimal, que es `0.1`.

   </details>

**Pruébalo: Propinas inexactas**

El siguiente código calcula el monto de la propina, dados el monto de la cuenta y la proporción de propina. Experimenta con los siguientes montos de cuenta y proporciones de propina, y observa si se producen inexactitudes al calcular el monto de la propina.

- monto de la cuenta: 22.70 y 33.33
- proporción de propina: 0.15, 0.18 y 0.20

<!-- coderunner: ch2/CodeRunner_02_05_06_Inaccurate-tips -->

**Pruébalo: Área de un triángulo**

Completa los siguientes pasos para calcular el área de un triángulo e imprime el resultado de cada paso. El área de un triángulo es (bh)/(2), donde *b* es la base y *h* es la altura.

1. Calcula el área de un triángulo con base = 7 y altura = 3.5.
2. Redondea el área del triángulo a un decimal.
3. Redondea el área del triángulo al valor entero más cercano.

<!-- coderunner: ch2/CodeRunner_02_05_07_Area-of-a-triangle -->

<!-- modulo: m00015 -->

## 2.5 División de enteros

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Evaluar expresiones que involucran división entera y módulo.
- Usar el operador de módulo para convertir entre unidades de medida.

### División y módulo

Python ofrece dos maneras de dividir números:

- La **división verdadera** (`/`) convierte los números a floats antes de dividir. Ej.: `7 / 4` se convierte en `7.0 / 4.0`, lo que da `1.75`.
- La **división entera** (`//`) calcula el cociente, o el número de veces que cabe el divisor. Ej.: `7 // 4` es `1` porque el 4 cabe en el 7 una vez, con residuo 3. El **operador de módulo** (`%`) calcula el residuo. Ej.: `7 % 4` es `3`.

Nota: el operador `%` se pronuncia tradicionalmente «mod» (abreviatura de «módulo»). Ej.: al leer `7 % 4` en voz alta, un programador diría «siete mod cuatro».

**Video:** [Quotient and remainder](https://www.openstax.org/r/quotient-remainder)

**Conceptos en práctica: División y módulo**

<!-- pregunta: CPL-ch02-m05-p01 -->

1. `13 / 5`

   - a) `2`
   - b) `2.6`
   - c) `3`

   <details><summary>Respuesta</summary>

   b) 13 dividido entre 5 es 2 y 3/5. El operador / calcula el resultado como un float.

   </details>

<!-- pregunta: CPL-ch02-m05-p02 -->

2. `13 % 5`

   - a) `2`
   - b) `2.6`
   - c) `3`

   <details><summary>Respuesta</summary>

   c) El 5 cabe en el 13 dos veces, con residuo 3. El operador % calcula el residuo.

   </details>

<!-- pregunta: CPL-ch02-m05-p03 -->

3. `1 // 4`

   - a) `0`
   - b) `0.25`
   - c) `1`

   <details><summary>Respuesta</summary>

   a) El 4 cabe en el 1 cero veces, con residuo 1. El operador // calcula el cociente.

   </details>

<!-- pregunta: CPL-ch02-m05-p04 -->

4. `2 % 0`

   - a) `0`
   - b) `2`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) La división entre cero no está definida en matemáticas. Python genera un error al dividir entre cero.

   </details>

### Conversiones de unidades

La división es útil para convertir una unidad de medida en otra. Para convertir centímetros a metros, se divide una variable entre 100. Ej.: 300 centímetros divididos entre 100 son 3 metros.

Con frecuencia, las cantidades no se dividen exactamente como enteros. 193 centímetros son 1.93 metros, o 1 metro y 93 centímetros. Un programa puede usar la división entera y el módulo para separar las unidades:

- El cociente, 1 metro, es `193 // 100`.
- El residuo, 93 centímetros, es `193 % 100`.

Los programas suelen usar la división entera y el módulo juntos. Si una línea de código hace una división entera entre `m`, la siguiente línea probablemente aplicará el módulo con `m`. La unidad `m` entre la que se divide una cantidad se llama **módulo aritmético**. Ej.: al convertir centímetros a metros, el módulo aritmético es 100.

**Video:** [Money and time](https://www.openstax.org/r/money-time)

**Conceptos en práctica: Conversiones de unidades**

<!-- pregunta: CPL-ch02-m05-p05 -->

1. ¿Cuál es el módulo aritmético para convertir minutos a horas?

   - a) 40
   - b) 60
   - c) 280

   <details><summary>Respuesta</summary>

   b) El módulo aritmético es la cantidad entre la que se divide. Para convertir minutos a horas, un programa divide entre 60.

   </details>

<!-- pregunta: CPL-ch02-m05-p06 -->

2. Un programa tiene la línea `pounds = ounces // 16`. ¿Cuál es probablemente la siguiente línea de código?

   - a) `ounces = ounces % 16`
   - b) `pounds = ounces % 16`
   - c) `ounces = ounces - pounds * 16`

   <details><summary>Respuesta</summary>

   a) Los programas que usan la división entera suelen usar el módulo en la línea siguiente.

   </details>

**Pruébalo: Hora de llegada**

Tener un dispositivo móvil puede salvarte la vida en viajes largos por carretera. Programas como Google Maps encuentran la ruta más corta y estiman la hora de llegada. La hora de llegada se basa en la hora actual más lo que durará el viaje.

Escribe un programa que (1) ingrese la hora actual y la duración estimada de un viaje, (2) calcule la hora de llegada y (3) muestre los resultados en horas y minutos. Tu programa debe usar los siguientes indicadores (prompts) (la entrada del usuario aparece en negrita):

```python norun
Current hour (0-23)? 13
Current minute (0-59)? 25
Trip time (in minutes)? 340
```

En este ejemplo, la hora actual es 13:25 (1:25 p. m.). La duración del viaje es de 340 minutos (5 horas y 40 minutos). 340 minutos después de las 13:25 son las 19:05 (7:05 p. m.). Tu programa debe mostrar el resultado con este formato:

```python norun
Arrival hour is 19
Arrival minute is 5
```

La hora de llegada debe estar entre 0 y 23. Ej.: sumar 120 minutos a las 23:00 debe dar la 1:00, no las 25:00. El minuto de llegada debe estar entre 0 y 59. Ej.: sumar 20 minutos a las 8:55 debe dar las 9:15, no las 8:75.

Pista: multiplica la hora actual por 60 para convertir las horas a minutos. Luego, calcula la hora de llegada, en minutos totales, como un entero.

Tu código no debe usar palabras clave de Python de capítulos posteriores, como `if` o `while`. La solución solo requiere suma, multiplicación, división y módulo.

<!-- coderunner: ch2/CodeRunner_02_06_09_Arrival-time -->

**Pruébalo: Máquina de cambio**

Las cajas de autopago son cada vez más populares en los supermercados. Los clientes escanean sus propios artículos y una computadora determina el monto total de la compra. Los clientes que pagan en efectivo insertan billetes de dólar, y una máquina entrega automáticamente el cambio en monedas.

Ahí es donde entra este programa. Tu tarea es calcular cuántas monedas de cada tipo se deben entregar. Tu programa debe usar los siguientes indicadores (prompts) (la entrada del usuario aparece en negrita):

```text
Total amount? 18.76
Cash payment? 20
```

Puedes suponer que el pago en efectivo siempre será un número entero (que representa billetes de dólar) mayor o igual que el monto total. El programa debe calcular y mostrar el cambio que se debe devolver y cuántos dólares, monedas de 25 centavos (quarters), de 10 centavos (dimes), de 5 centavos (nickels) y de 1 centavo (pennies) se deben entregar:

```text
Change Due $1.24

 Dollars: 1
Quarters: 0
   Dimes: 2
 Nickels: 0
 Pennies: 4
```

Pista: calcula el cambio total, en centavos, como un entero. Usa la función `round()` para evitar errores de punto flotante.

Tu código no debe usar palabras clave de Python de capítulos posteriores, como `if` o `while`. La solución solo requiere resta, multiplicación, división y módulo.

<!-- coderunner: ch2/CodeRunner_02_06_08_Change-machine -->

<!-- modulo: m00016 -->

## 2.6 El módulo math

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Distinguir entre las funciones integradas y las funciones de math.
- Usar las funciones y constantes definidas en el módulo math.

### Importar módulos

Python incluye una extensa [biblioteca estándar](https://openstax.org/r/100pythlibrary) de módulos. Un **módulo** es código escrito previamente que se puede importar en un programa. La **instrucción import** define una variable para acceder al código de un módulo. Las instrucciones import suelen aparecer al comienzo de un programa.

La biblioteca estándar también define funciones integradas como `print()`, `input()` y `float()`. Una **función integrada** siempre está disponible y no necesita importarse. La [lista completa de funciones integradas](https://openstax.org/r/100builtin) está disponible en la documentación oficial de Python.

Un módulo de uso común en la biblioteca estándar es el [módulo math](https://openstax.org/r/100mathmodule). Este módulo define funciones como `sqrt()` (raíz cuadrada). Para llamar a `sqrt()`, un programa debe usar `import math` y la variable `math` resultante seguida de un punto. Ej.: `math.sqrt(25)` se evalúa como `5.0`.

El siguiente programa importa y usa el módulo math, y usa funciones integradas para la entrada y la salida.

**Ejemplo: Cálculo de la distancia entre dos puntos**

```python norun
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance is", distance)
```

**Video:** [Importing math in a Python shell](https://www.openstax.org/r/importing-math)

**Conceptos en práctica: Funciones integradas y el módulo math**

<!-- pregunta: CPL-ch02-m06-p01 -->

1. En el ejemplo anterior, al evaluar math, ¿por qué el intérprete generó un `NameError`?

   - a) El módulo math no estaba disponible.
   - b) La variable pie estaba mal escrita.
   - c) El módulo math no se importó.

   <details><summary>Respuesta</summary>

   c) La instrucción import define la variable math necesaria para acceder al módulo.

   </details>

<!-- pregunta: CPL-ch02-m06-p02 -->

2. ¿Cuál de estas funciones es integrada y no necesita importarse?

   - a) `log()`
   - b) `round()`
   - c) `sqrt()`

   <details><summary>Respuesta</summary>

   b) La función `round()`, para redondear números de punto flotante, es integrada.

   </details>

<!-- pregunta: CPL-ch02-m06-p03 -->

3. ¿Qué expresión produce un error?

   - a) `math.abs(1)`
   - b) `math.log(1)`
   - c) `math.sqrt(1)`

   <details><summary>Respuesta</summary>

   a) `abs()` es una función integrada. El módulo math no tiene una función `abs()`.

   </details>

### Funciones matemáticas

A continuación se muestran las funciones y constantes matemáticas de uso común. La [lista completa del módulo math](https://openstax.org/r/100mathmodule) está disponible en la documentación oficial de Python.

**Constantes de ejemplo del módulo math.**

| Constante | Valor | Descripción |
|---|---|---|
| `math.e` | e = 2.71828… | Número de Euler: la base del logaritmo natural. |
| `math.pi` | π = 3.14159… | La razón entre la circunferencia y el diámetro de un círculo. |
| `math.tau` | τ = 6.28318… | La razón entre la circunferencia y el radio de un círculo. Tau es igual a 2π. |

**Funciones de ejemplo del módulo math.**

| Función | Descripción | Ejemplos |
|---|---|---|
| **Teoría de números** |  |  |
| `math.ceil(x)` | El techo de `x`: el menor entero mayor o igual que `x`. | `math.ceil(7.4)` → `8`  <br>`math.ceil(-7.4)` → `-7` |
| `math.floor(x)` | El piso de `x`: el mayor entero menor o igual que `x`. | `math.floor(7.4)` → `7`  <br>`math.floor(-7.4)` → `-8` |
| **Potencias y logaritmos** |  |  |
| `math.log(x)` | El logaritmo natural de `x` (en base e). | `math.log(math.e)` → `1.0`  <br>`math.log(0)` → `ValueError: math domain error` |
| `math.log(x, base)` | El logaritmo de `x` en la base dada. | `math.log(8, 2)` → `3.0`  <br>`math.log(10000, 10)` → `4.0` |
| `math.pow(x, y)` | `x` elevado a la potencia `y`. A diferencia del operador `**`, `math.pow()` convierte `x` e `y` al tipo float. | `math.pow(3, 0)` → `1.0`  <br>`math.pow(3, 3)` → `27.0` |
| `math.sqrt(x)` | La raíz cuadrada de `x`. | `math.sqrt(9)` → `3.0`  <br>`math.sqrt(-9)` → `ValueError: math domain error` |
| **Trigonométricas** |  |  |
| `math.cos(x)` | El coseno de `x` radianes. | `math.cos(0)` → `1.0`  <br>`math.cos(math.pi)` → `-1.0` |
| `math.sin(x)` | El seno de `x` radianes. | `math.sin(0)` → `0.0`  <br>`math.sin(math.pi/2)` → `1.0` |
| `math.tan(x)` | La tangente de `x` radianes. | `math.tan(0)` → `0.0`  <br>`math.tan(math.pi/4)` → `0.999`  <br>(Error de redondeo; el resultado debería ser 1.0.) |

**Conceptos en práctica: Uso de funciones y constantes de math**

<!-- pregunta: CPL-ch02-m06-p04 -->

1. ¿Cuál es el valor de `math.tau/2`?

   - a) aproximadamente `2.718`
   - b) aproximadamente `3.142`
   - c) aproximadamente `6.283`

   <details><summary>Respuesta</summary>

   b) Tau es igual a 2&#x03C0;, así que tau dividido entre 2 es &#x03C0;.

   </details>

<!-- pregunta: CPL-ch02-m06-p05 -->

2. ¿Cuál es el valor de `math.sqrt(100)`?

   - a) el float `10.0`
   - b) el entero `10`
   - c) `ValueError: math domain error`

   <details><summary>Respuesta</summary>

   a) La función `math.sqrt()` devuelve un float, incluso cuando recibe un entero.

   </details>

<!-- pregunta: CPL-ch02-m06-p06 -->

3. ¿Cómo se escribe π*r*² en la sintaxis de Python?

   - a) `pi * r**2`
   - b) `math.pi * r**2`
   - c) `math.pi * r*2`

   <details><summary>Respuesta</summary>

   b) Esta expresión es una forma concisa de escribir π*r*².

   </details>

<!-- pregunta: CPL-ch02-m06-p07 -->

4. ¿Qué expresión devuelve el entero 27?

   - a) `3 ** 3`
   - b) `3.0 ** 3`
   - c) `math.pow(3, 3)`

   <details><summary>Respuesta</summary>

   a) Cuando recibe enteros, el operador ** devuelve un resultado entero.

   </details>

**Pruébalo: Fórmula cuadrática**

En álgebra, una ecuación cuadrática se escribe como ax^2 + bx + c = 0. Los coeficientes *a*, *b* y *c* son valores conocidos. La variable *x* representa un valor desconocido. Ej.: 2x^2 + 3x-5 = 0 tiene los coeficientes a = 2, b = 3 y c = -5. La fórmula cuadrática ofrece una manera rápida y sencilla de resolver una ecuación cuadrática para *x*:

x = (-b±√(b^2-4ac))/(2a)

El símbolo más-menos indica que la ecuación tiene dos soluciones. Sin embargo, Python no tiene un operador más-menos. Para usar esta fórmula en Python, hay que separarla:

x_1 = (-b + √(b^2-4ac))/(2a)

x_2 = (-b-√(b^2-4ac))/(2a)

Escribe el código de la fórmula cuadrática en el siguiente programa. Prueba tu programa con los siguientes valores de *a*, *b* y *c*:

| Entrada proporcionada | Salida esperada |  |  |  |
|---|---|---|---|---|
| `a` | `b` | `c` | `x1` | `x2` |
| `1` | `0` | `-4` | `2.0` | `-2.0` |
| `1` | `2` | `-3` | `1.0` | `-3.0` |
| `2` | `1` | `-1` | `0.5` | `-1.0` |
| `0` | `1` | `1` | `division by zero` |  |
| `1` | `0` | `1` | `math domain error` |  |

<!-- coderunner: ch2/CodeRunner_02_07_10_Quadratic-formula -->

**Pruébalo: Fórmulas del cilindro**

En geometría, el área de la superficie y el volumen de un cilindro circular recto se pueden calcular de la siguiente manera:

A = 2πrh + 2πr^2

V = πr^2h

Escribe el código de estas dos fórmulas en el siguiente programa. Pista: tu solución debe usar tanto `math.pi` como `math.tau`. Prueba tu programa con los siguientes valores de r y h:

| Entrada proporcionada | Salida esperada |  |  |
|---|---|---|---|
| `r` | `h` | `area` | `volume` |
| `0` | `0` | `0.0` | `0.0` |
| `1` | `1` | `12.57` | `3.14` |
| `1` | `2` | `18.85` | `6.28` |
| `2.5` | `4.8` | `114.67` | `94.25` |
| `3.1` | `7.0` | `196.73` | `211.33` |

Si obtienes un error, intenta buscar qué significa ese error.

<!-- coderunner: ch2/CodeRunner_02_07_11_Cylinder-formulas -->

<!-- modulo: m00017 -->

## 2.7 Formato del código

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar un buen espaciado para expresiones e instrucciones.
- Escribir instrucciones de varias líneas usando la unión implícita de líneas.

### Espaciado recomendado

La mayoría de los espacios en el código de Python se ignoran al ejecutar los programas; sin embargo, los espacios al comienzo de una línea son muy importantes. Los siguientes dos programas son equivalentes:

- Buen espaciado:

  ```python norun
  name = input("Enter someone's name: ")
place = input("Enter a famous place: ")
print(name, "should visit", place + "!")
  ```
- Mal espaciado:

  ```python norun
  name=input ("Enter someone's name: " )
place =input("Enter a famous place: ")
print( name,"should visit" , place+ "!")
  ```

Alguien podría argumentar que los espacios que faltan o sobran no importan. Después de todo, los dos programas anteriores se ejecutan exactamente igual. Sin embargo, la versión con «mal espaciado» es más difícil de leer. Código como `name=input` y `place+` puede generar confusión.

Los buenos programadores escriben código lo más fácil de leer posible. Así, es más probable que otros programadores entiendan el código. Para fomentar la coherencia, la comunidad de Python tiene un conjunto de pautas sobre dónde poner espacios y líneas en blanco, cómo nombrar las variables, cómo dividir las líneas largas y otros temas importantes.

**Guía de estilo de Python**

[PEP 8](https://openstax.org/r/100PEP8) es la guía de estilo oficial de Python. **PEP** significa Python Enhancement Proposal (propuesta de mejora de Python). Los miembros de la comunidad de Python escriben PEP para documentar buenas prácticas y proponer nuevas características. La siguiente tabla se basa en las pautas de PEP 8 bajo el título [Whitespace in Expressions and Statements](https://openstax.org/r/100whitespace).

**Pautas para los espacios.**

| Pauta | Ejemplo | Errores comunes |
|---|---|---|
| Paréntesis: sin espacio antes ni después. | `print("Go team!")` | `print ("Go team!")`  <br>`print( "Go team!" )` |
| Comas: sin espacio antes, un espacio después. | `print("Hello", name)` | `print("Hello" , name)`  <br>`print("Hello",name)` |
| Asignación: un espacio antes y después del `=`. | `name = input("Your name? ")` | `name=input("Your name? ")`  <br>`name= input("Your name? ")`  <br>`name =input("Your name? ")` |
| Concatenación: un espacio antes y después del `+`. | `print("Hi", name + "!")` | `print("Hi", name+"!")`  <br>`print("Hi", name+ "!")`  <br>`print("Hi", name +"!")` |
| Aritmética: usa espacios para mostrar la menor precedencia. | `x**2 + 5*x - 8` | `x ** 2 + 5 * x - 8`  <br>`x ** 2+5 * x-8`  <br>`x**2+5*x-8` |

**Conceptos en práctica: Espaciado recomendado**

<!-- pregunta: CPL-ch02-m07-p01 -->

1. ¿Qué instrucción tiene el formato correcto?

   - a) `name = input("What is your name? ")`
   - b) `name = input ("What is your name? ")`
   - c) `name = input( "What is your name? " )`

   <details><summary>Respuesta</summary>

   a) El código tiene un espacio antes y después del operador de asignación (=).

   </details>

<!-- pregunta: CPL-ch02-m07-p02 -->

2. ¿Qué instrucción tiene el formato correcto?

   - a) `name=name+"!"`
   - b) `name = name+"!"`
   - c) `name = name + "!"`

   <details><summary>Respuesta</summary>

   c) Cada operador (=, +) tiene un espacio tanto antes como después.

   </details>

<!-- pregunta: CPL-ch02-m07-p03 -->

3. ¿Qué instrucción tiene el formato correcto?

   - a) `print("Hello",name)`
   - b) `print("Hello", name)`
   - c) `print("Hello " , name)`

   <details><summary>Respuesta</summary>

   b) Después de la coma hay un espacio.

   </details>

<!-- pregunta: CPL-ch02-m07-p04 -->

4. ¿Qué expresión tiene el formato correcto?

   - a) `b**2 - 4*a*c`
   - b) `b ** 2 - 4 * a * c`
   - c) `b**2 - 4*a * c`

   <details><summary>Respuesta</summary>

   a) Las expresiones `b**2` y `4*a*c` se evalúan primero. Agregar espacios alrededor del operador `-` hace que el orden de las operaciones sea más legible.

   </details>

### Concatenación automática

Las cadenas largas dificultan la lectura de los programas de Python. Ej.: este programa imprime la primera oración de la [Declaración de Independencia de EE. UU.](https://openstax.org/r/100declaration):

`print("The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.")`

PEP 8 recomienda que cada línea de código tenga menos de 80 caracteres. Así, los programadores no tendrán que desplazarse horizontalmente para leer el código. El programa anterior se puede reescribir dividiendo la cadena original:

```python
print("The unanimous Declaration of the thirteen united States of "
      "America, When in the Course of human events, it becomes "
      "necessary for one people to dissolve the political bands "
      "which have connected them with another, and to assume among "
      "the powers of the earth, the separate and equal station to "
      "which the Laws of Nature and of Nature's God entitle them, a "
      "decent respect to the opinions of mankind requires that they "
      "should declare the causes which impel them to the separation.")
```

Por comodidad, Python concatena automáticamente varias cadenas. En esta situación no se necesita el operador `+`.

**Video:** [String concatenation](https://www.openstax.org/r/string-concat)

**Conceptos en práctica: Concatenación de literales de cadena**

<!-- pregunta: CPL-ch02-m07-p05 -->

1. ¿Qué línea imprime la palabra `"grandmother"`?

   - a) `print(grandmother)`
   - b) `print("grand" "mother")`
   - c) `print("grand", "mother")`

   <details><summary>Respuesta</summary>

   b) Las dos cadenas consecutivas se combinan automáticamente en una sola cadena antes de imprimirse.

   </details>

<!-- pregunta: CPL-ch02-m07-p06 -->

2. ¿Qué cadena es equivalente a `"Today is" "a holiday"`?

   - a) `'Today isa holiday'`
   - b) `'Today is a holiday'`
   - c) `'Today is" "a holiday'`

   <details><summary>Respuesta</summary>

   a) Las cadenas originales no tienen un espacio entre las palabras `"is"` y `"a"`.

   </details>

<!-- pregunta: CPL-ch02-m07-p07 -->

3. Si name es `"Ada"`, ¿qué muestra `print("Hello," name)`?

   - a) `Hello,Ada`
   - b) `Hello, Ada`
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   c) El literal `"Hello,"` y la variable `name` no se pueden concatenar sin usar el operador `+`. Como alternativa, los dos valores se podrían separar con una coma en la función print.

   </details>

### Instrucciones de varias líneas

La mayoría de las instrucciones de un programa de Python necesitan solo una línea de código. Pero de vez en cuando las instrucciones más largas necesitan abarcar varias líneas. Python ofrece dos maneras de escribir instrucciones de varias líneas:

- Unión explícita de líneas, usando caracteres `\`:

  ```python
  decl = "The unanimous Declaration of the thirteen united States of " \
        "America, When in the Course of human events, it becomes " \
        "necessary for one people to dissolve the political bands..."
  ```
- Unión implícita de líneas, usando paréntesis:

  ```python
  decl = ("The unanimous Declaration of the thirteen united States of "
        "America, When in the Course of human events, it becomes "
        "necessary for one people to dissolve the political bands...")
  ```

La unión implícita de líneas es más común, ya que muchas instrucciones y expresiones usan paréntesis de todos modos. PEP 8 recomienda evitar la unión explícita de líneas siempre que sea posible.

**Conceptos en práctica: Instrucciones de varias líneas**

<!-- pregunta: CPL-ch02-m07-p08 -->

1. ¿Qué carácter se usa para la unión explícita de líneas?

   - a) `/`
   - b) `\`
   - c) `|`

   <details><summary>Respuesta</summary>

   b) La barra invertida, cuando se usa al final de una línea, indica una instrucción de varias líneas.

   </details>

<!-- pregunta: CPL-ch02-m07-p09 -->

2. ¿Cuál es la mejor manera de imprimir una cadena muy larga?

   - a) Dividir la cadena en varias cadenas más pequeñas.
     
     ```python
     print("..." # primera parte de la cadena
     "..." # siguiente parte de la cadena
     "...")
     ```
   - b) Imprimir la cadena con varias instrucciones print.
     
     ```python
     print("...") # primera parte de la cadena
     print("...") # siguiente parte de la cadena
     print("...")
     ```
   - c) Asignar la cadena a una variable e imprimir la variable.
     
     ```python
     text = "..." # la cadena completa
     print(text)
     ```

   <details><summary>Respuesta</summary>

   a) Usar una sola instrucción print con paréntesis une las líneas de forma implícita y no aumenta el número de instrucciones.

   </details>

<!-- pregunta: CPL-ch02-m07-p10 -->

3. ¿Qué ejemplo consta de dos instrucciones?

   - a)

     ```python
     print("Happy "
     "New Year")
     ```
   - b)

     ```python
     saying = ("Happy "
     "New Year")
     ```
   - c)

     ```python
     saying= "Happy "
     "New Year"
     ```

   <details><summary>Respuesta</summary>

   c) La primera línea asigna `"Happy "` a la variable saying. La segunda línea no tiene ningún efecto en el programa.

   </details>

**Pruébalo: Espaciado desordenado**

El siguiente código funciona correctamente pero tiene un mal formato. En particular, el código no incluye los espacios recomendados por PEP 8. Además, dos de las líneas tienen unos 90 caracteres. Reformatea el código para seguir las pautas de esta sección. Ten cuidado de no cambiar el comportamiento del código en sí.

<!-- coderunner: ch2/CodeRunner_02_08_13_Spaced-out -->

**Pruébalo: Cinco citas**

Escribe un programa que imprima las siguientes cinco citas (fuente: [BrainyQuote](https://openstax.org/r/100brainyquote)) de Guido van Rossum, el creador de Python. Tu programa debe tener exactamente cinco instrucciones print, una para cada cita:

```text
1. "Si hablas de Java en particular, Python es más o menos el mejor ajuste que puedes encontrar entre todos los demás lenguajes. Pero lo curioso es que, desde el punto de vista del lenguaje, JavaScript tiene mucho en común con Python, aunque es una especie de subconjunto restringido."
2. "La segunda línea de material que saldrá de este proyecto es un entorno de programación y un conjunto de herramientas de programación en los que realmente queremos centrarnos de nuevo en las necesidades del principiante. Este entorno tendrá que ser extremadamente fácil de usar."
3. "Tengo la esperanza de que hay una mejor manera. Las herramientas de más alto nivel que realmente permitan ver con más claridad la estructura del software serán de un valor enorme."
4. "Ahora bien, creo que es mucho más fácil enseñar Python a los estudiantes de programación que enseñarles C, C++ o Java al mismo tiempo, porque todos los detalles de esos lenguajes son mucho más difíciles. Otros lenguajes de scripting tampoco funcionan muy bien en ese caso."
5. "Supongo que la decisión de crear un lenguaje pequeño de propósito especial o de usar un lenguaje de propósito general existente es una de las decisiones más difíciles que debe tomar quien se enfrente a la necesidad de un nuevo lenguaje."
```

Observa que todas estas líneas tienen más de 80 caracteres, y algunas contienen comillas simples. Da formato al código usando instrucciones de varias líneas y secuencias de escape según sea necesario.

<!-- coderunner: ch2/CodeRunner_02_08_12_Five-quotes -->

<!-- modulo: m00018 -->

## 2.8 Carreras con Python

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Resumir cómo se usa Python en campos distintos de las ciencias de la computación (CS) y las tecnologías de la información (TI).
- Describir dos tipos diferentes de aplicaciones hechas con Python.

### Campos y aplicaciones

Aprender Python abre la puerta a muchas carreras relacionadas con la programación. Algunos ejemplos de puestos de trabajo son ingeniero de software, científico de datos, desarrollador web y analista de sistemas. Estos trabajos suelen requerir un título en ciencias de la computación (CS), tecnologías de la información (TI) o un campo afín. Sin embargo, la programación no se limita a estos campos y carreras.

Muchos profesionales usan Python para apoyar su trabajo. Los programas de Python pueden automatizar tareas y resolver problemas rápidamente. La primera tabla muestra algunos ejemplos de Python fuera de los campos de la computación. Saber programar es una habilidad útil que puede mejorar cualquier carrera.

Python es un lenguaje versátil que admite muchos tipos de aplicaciones. La segunda tabla muestra algunos ejemplos de programas que se pueden escribir en Python. Dada la utilidad y la popularidad de Python, es un excelente lenguaje para aprender. Una comunidad de profesionales y entusiastas dispuesta a ayudar te respalda.

**Python fuera de CS y TI.**

| Campo | Ejemplo de uso de Python |
|---|---|
| **Negocios** | Un contador escribe un programa de Python para generar informes de ventas personalizados. |
| **Educación** | Un profesor escribe un programa de Python para organizar las entregas de tareas. |
| **Bellas artes** | Un artista escribe un programa de Python para operar una exhibición de arte interactiva. |
| **Humanidades** | Un lingüista escribe un programa de Python para analizar los cambios en el uso de palabras de jerga. |
| **Ciencias** | Un biólogo escribe un programa de Python para analizar secuencias de ADN en busca de cáncer. |

**Aplicaciones creadas con Python.**

| Aplicación | Ejemplo de uso de Python |
|---|---|
| **Inteligencia artificial** | Un ingeniero desarrolla modelos para apoyar el reconocimiento de imágenes y de voz. Ej.: [biblioteca TensorFlow](https://openstax.org/r/100tensorflow). |
| **Visualización de datos** | Un estadístico crea gráficos para dar sentido a grandes cantidades de datos. Ej.: [biblioteca Matplotlib](https://openstax.org/r/100matplotlib). |
| **Propósito general** | La mayoría de los programas de este libro son de propósito general. Ej.: leer entradas, realizar cálculos, imprimir resultados. |
| **Computación científica** | Python es muy útil para realizar experimentos y analizar datos. Ej.: [el proyecto SciPy](https://openstax.org/r/100scipyproject). |
| **Desarrollo web** | Python puede hacer funcionar sitios web interactivos. Ej.: Instagram está creado con [Django](https://openstax.org/r/100django), un framework de Python. |

**Conceptos en práctica: Campos y aplicaciones**

<!-- pregunta: CPL-ch02-m08-p01 -->

1. ¿Cuáles de los siguientes campos usan Python para apoyar su trabajo?

   - a) geografía
   - b) atención médica
   - c) ciencias políticas
   - d) todas las anteriores

   <details><summary>Respuesta</summary>

   d) Python es uno de los lenguajes de programación más usados del mundo, especialmente en campos ajenos a CS y TI.

   </details>

<!-- pregunta: CPL-ch02-m08-p02 -->

2. ¿Cuál de las siguientes bibliotecas de Python crea gráficos y diagramas?

   - a) Matplotlib
   - b) SciPy
   - c) TensorFlow

   <details><summary>Respuesta</summary>

   a) Matplotlib es una biblioteca popular para crear gráficos, diagramas y otras visualizaciones.

   </details>

<!-- pregunta: CPL-ch02-m08-p03 -->

3. ¿Cuáles de las siguientes aplicaciones se crearon con Python?

   - a) Facebook
   - b) Instagram
   - c) WhatsApp

   <details><summary>Respuesta</summary>

   b) Hasta 2023, Instagram es la mayor implementación del framework web Django de Python.

   </details>

**Para saber más**

Para ver más ejemplos de aplicaciones que se pueden crear con Python, consulta [«Top 12 Fascinating Python Applications in Real-World»](https://openstax.org/r/100top12apps) de Rohit Sharma. Para obtener más información sobre las carreras relacionadas con Python, consulta [«What Does a Python Developer Do?»](https://openstax.org/r/100careers) en la guía de carreras de BrainStation.

<!-- modulo: m00019 -->

## Resumen del capítulo

Los puntos principales de este capítulo son:

- Las expresiones y las instrucciones se pueden ejecutar de forma interactiva usando un shell.
- Las cadenas de entrada se pueden convertir a otros tipos. Ej.: `int(input())`.
- Las cadenas se pueden concatenar con otros tipos. Ej.: `"$" + str(cost)`.
- Los floats están sujetos a errores de redondeo y de desbordamiento.
- Los enteros se pueden dividir exactamente usando `//` y `%`.
- Módulos como `math` proporcionan muchas funciones útiles.
- Dar formato a las líneas largas ayuda a mejorar la legibilidad.

En este punto, deberías poder escribir programas que pidan entradas de tipos mixtos, realicen cálculos matemáticos y muestren los resultados con mejor formato. La práctica de programación que sigue reúne la mayoría de los temas presentados en el capítulo.

**Referencia del capítulo 2.**

| Función | Descripción |
|---|---|
| `abs(x)` | Devuelve el valor absoluto de `x`. |
| `int(x)` | Convierte `x` (una cadena o un float) en un entero. |
| `float(x)` | Convierte `x` (una cadena o un entero) en un float. |
| `str(x)` | Convierte `x` (un float o un entero) en una cadena. |
| `round(x, ndigits)` | Redondea `x` a `ndigits` posiciones después del punto decimal. Si se omite `ndigits`, devuelve el entero más cercano a `x`. |
| **Operador** | **Descripción** |
| `s * n`  <br>(Repetición) | Crea una cadena con `n` copias de `s`. Ej.: `"Ha" * 3` es `"HaHaHa"`. |
| `x / y`  <br>(División real) | Divide `x` entre `y` y devuelve el resultado completo como un float. Ej.: `7 / 4` es `1.75`. |
| `x // y`  <br>(División entera) | Divide `x` entre `y` y devuelve el cociente como un entero. Ej.: `7 // 4` es `1`. |
| `x % y`  <br>(Módulo) | Divide `x` entre `y` y devuelve el residuo como un entero. Ej.: `7 % 4` es `3`. |

**Pruébalo: Hornear pan**

Se acercan las fiestas y necesitas comprar ingredientes para hornear muchas hogazas de pan. Según una [receta de King Arthur Flour](https://openstax.org/r/100kingarthurflr), necesitarás los siguientes ingredientes para cada hogaza:

- 1 1/2 cucharaditas de levadura instantánea
- 1 1/2 cucharaditas de sal
- 1 1/2 cucharaditas de azúcar
- 2 1/2 tazas de harina para todo uso
- 2 tazas de masa madre
- 1/2 taza de agua tibia

Escribe un programa que reciba como entrada las siguientes variables: `bread_weight` (float), `serving_size` (float) y `num_guests` (int). La salida se verá como la siguiente:

Nota: las medidas que calcula el programa son exactas, pero para hornear, el panadero tendría que usar alguna aproximación. Ej.: 9.765625 tazas de harina para todo uso en realidad significa 9 y 3/4 tazas.

```python norun
For 25 people, you will need 3.90625 loaves of bread:

  5.859375 teaspoons instant yeast
  5.859375 teaspoons salt
  5.859375 teaspoons sugar
  9.765625 cups all-purpose flour
  7.8125 cups sourdough starter
  1.953125 cups lukewarm water
```

En la salida anterior, `bread_weight` es 16.0 onzas, `serving_size` es 2.5 onzas y `num_guests` es 25 personas. Usa estas tres variables para calcular el número de hogazas necesarias.

Asegúrate de que tu salida coincida exactamente con el ejemplo anterior. Observa que cada línea de ingredientes comienza con dos espacios.

<!-- coderunner: ch2/CodeRunner_02_10_14_Baking-bread -->

**Pruébalo: Calculadora de propinas**

Google tiene una variedad de [trucos de búsqueda](https://openstax.org/r/100googletricks) que presentan a los usuarios resultados instantáneos. Si buscas en Google [tip calculator](https://openstax.org/r/100tipcalculatr), se incluye una herramienta interactiva en la parte superior de los resultados. El objetivo de este ejercicio es implementar una calculadora de propinas similar.

Comienza pidiendo al usuario que ingrese los siguientes valores (la entrada del usuario aparece en negrita):

```python norun
Enter bill amount: 43.21
Percentage to tip: 18
Number of people: 2
```

Luego calcula el monto de la propina y el monto total de la cuenta, según la entrada del usuario. Muestra los resultados con este formato:

```python norun
Tip amount: $7.78
Total amount: $50.99

Tip per person: $3.89
Total per person: $25.49
```

Tu programa debe mostrar todos los montos en dólares redondeados a dos decimales. La salida debe tener exactamente seis líneas, como se muestra arriba. Observa la línea en blanco antes de cada sección de la salida. Observa también el espacio antes del signo de dólar, pero no después.

<!-- coderunner: ch2/CodeRunner_02_10_15_Tip-calculator -->
