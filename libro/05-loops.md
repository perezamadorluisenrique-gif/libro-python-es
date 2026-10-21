# Capítulo 5: Bucles

<!-- modulo: m00036 -->

## Introducción

![una imagen de un fractal](media/Python_05_00_000.jpg)

*crédito: modificación de la obra «Quantum Computing», de Kevin Dooley/Flickr, CC BY 2.0*

Un **bucle** es un bloque de código que ejecuta un conjunto de instrucciones mientras una condición dada sea verdadera. Un bucle se usa con frecuencia para realizar una tarea repetitiva. Ej.: el software de un teléfono comprueba repetidamente si el teléfono está inactivo. Cuando se alcanza el tiempo establecido por el usuario, el teléfono se bloquea. Los bucles también se pueden usar para iterar sobre listas, como los nombres de los estudiantes de una lista de clase, e imprimir los nombres uno por uno.

En este capítulo se presentan dos tipos de bucles: el bucle `for` y el bucle `while`. El capítulo también presenta las instrucciones `break` y `continue` para controlar la ejecución de un bucle.

<!-- modulo: m00037 -->

## 5.1 Bucle while

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar la estructura de bucle en Python.
- Usar un bucle `while` para implementar tareas repetitivas.

### Bucle while

Un **bucle while** es una estructura de código que ejecuta un conjunto de instrucciones, conocido como el cuerpo del bucle, mientras una condición dada, conocida como la expresión del bucle, sea verdadera. En cada iteración, una vez ejecutada la instrucción del bucle, la expresión del bucle se evalúa de nuevo.

- Si es verdadera, el cuerpo del bucle se ejecutará al menos una vez más (lo que también se llama repetir o iterar una vez más).
- Si es falsa, la ejecución del bucle terminará y se ejecutará la siguiente instrucción después del cuerpo del bucle.

**Video:** [While loop](https://www.openstax.org/r/while-loop)

**Conceptos en práctica: Ejemplo de bucle while**

<!-- pregunta: CPL-ch05-m01-p01 -->

1. ¿Cuántas veces se ejecuta el bucle?

   - a) 5
   - b) 6
   - c) 7

   <details><summary>Respuesta</summary>

   b) El bucle se ejecuta seis veces, para los valores `g =` `1`, `2`, `3`, `5`, `8` y `13`.

   </details>

<!-- pregunta: CPL-ch05-m01-p02 -->

2. ¿Cuál es el valor de la variable `g` cuando la condición del bucle while se evalúa como `False`?

   - a) `13`
   - b) `20`
   - c) `21`

   <details><summary>Respuesta</summary>

   c) 21 es el primer número de Fibonacci mayor que 20, y para `g = 21` la condición se evaluará como `False` por primera vez.

   </details>

<!-- pregunta: CPL-ch05-m01-p03 -->

3. ¿Cuáles son los valores impresos en la salida?

   - a) `1 1 2 3 5 8 13 `
   - b) `1 2 3 5 8 13 `
   - c) `1 1 2 3 5 8 13 21 `

   <details><summary>Respuesta</summary>

   a) El código imprime primero el valor inicial de la variable `f`. Luego, en cada iteración, se imprime el valor de `g`, y el valor de `g` a lo largo de la ejecución del código será `1`, `2`, `3`, `5`, `8` y `13`. Por lo tanto, todos los valores impresos son `1`, `1`, `2`, `3`, `5`, `8` y `13`.

   </details>

### Conteo con un bucle while

Un bucle `while` se puede usar para contar hacia arriba o hacia abajo. Se puede usar una variable contador en la expresión del bucle para determinar el número de iteraciones ejecutadas. Ej.: un programador puede querer imprimir todos los números pares entre 1 y 20. La tarea se puede realizar con un contador inicializado en 1. En cada iteración, el valor del contador aumenta en uno, y una condición puede comprobar si el valor del contador es un número par o no. El cambio en el valor del contador en cada iteración se llama **tamaño de paso**. El tamaño de paso puede ser cualquier valor positivo o negativo. Si el tamaño de paso es un número positivo, el contador cuenta en orden ascendente, y si es un número negativo, el contador cuenta en orden descendente.

**Ejemplo: Un programa que imprime todos los números impares entre 1 y 10**

```python
# Inicialización
counter = 1

# Condición del bucle while
while counter <= 10:
  if counter % 2 == 1:
    print(counter)
  # Contar hacia arriba y aumentar el valor del contador en 1 en cada iteración
  counter += 1
```

**Video:** [Counting with while loop](https://www.openstax.org/r/counting-with-while-loop)

**Conceptos en práctica: Ejemplos de conteo con while**

<!-- pregunta: CPL-ch05-m01-p04 -->

1. ¿Cuántas veces se ejecuta el bucle?

   - a) 3
   - b) 4
   - c) 5

   <details><summary>Respuesta</summary>

   b) El bucle se ejecuta para `n = 4`, `3`, `2`, `1`.

   </details>

<!-- pregunta: CPL-ch05-m01-p05 -->

2. ¿Qué línea se imprime como última línea de la salida?

   - a) `value of n after the loop is -1.`
   - b) `value of n after the loop is 0.`
   - c) `value of n after the loop is 1.`

   <details><summary>Respuesta</summary>

   b) La condición de terminación del bucle es `n = 0`; por lo tanto, el valor de `n` después del bucle es igual a `0`. La última línea impresa será: `value of n after the loop is 0`.

   </details>

<!-- pregunta: CPL-ch05-m01-p06 -->

3. ¿Qué sucede si el código se cambia de la siguiente manera?
   
   ```python norun
   n = 4
   while n > 0:
     print(n)
     # Línea modificada
     n = n + 1
   
   print("value of n after the loop is", n)
   ```

   - a) El código no se ejecutará.
   - b) El código se ejecutará una iteración adicional.
   - c) El código nunca terminará.

   <details><summary>Respuesta</summary>

   c) Como el valor de inicialización de `n` es `4` y el valor de `n` solo aumenta, la condición del bucle siempre seguirá siendo verdadera. El bucle nunca terminará.

   </details>

**Pruébalo: Lectura de entradas en un bucle while**

Escribe un programa que reciba entradas del usuario en un bucle `while` hasta que el usuario ingrese `"begin"`. Prueba el código con los valores de entrada dados para comprobar que el bucle no termina hasta que la entrada sea `"begin"`. Una vez que se reciba la entrada `"begin"`, imprime `"The while loop        condition has been met."`.

Ingresa diferentes palabras de entrada para ver cuándo se cumple la condición del bucle `while`.

<!-- coderunner: ch5/CodeRunner_05_02_01_Reading-inputs-in-a-while-loop -->

**Pruébalo: Suma de números impares**

Escribe un programa que lea dos valores enteros, `n1` y `n2`. Usa un bucle `while` para calcular la suma de los números impares entre `n1` y `n2` (incluyendo `n1` y `n2`). Recuerda que un número es impar si `number % 2 != 0`.

<!-- coderunner: ch5/CodeRunner_05_02_02_Sum-of-odd-numbers -->

<!-- modulo: m00038 -->

## 5.2 Bucle for

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar la estructura del bucle `for`.
- Usar un bucle `for` para implementar tareas repetitivas.

### Bucle for

En Python, un **contenedor** puede ser un rango de números, una cadena de caracteres o una lista de valores. Para acceder a los objetos dentro de un contenedor, se puede diseñar un bucle iterativo que recupere los objetos uno a uno. Un **bucle for** itera sobre todos los elementos de un contenedor. Ej.: iterar sobre una lista de clase e imprimir los nombres de los estudiantes.

**Video:** [For loop example for iterating over a container object](https://www.openstax.org/r/for-loop-iterating)

**Conceptos en práctica: Bucle for sobre un contenedor de tipo cadena**

<!-- pregunta: CPL-ch05-m02-p01 -->

1. ¿Cuál es la salida del programa?

   - a) `7`
   - b) `8`
   - c) `9`

   <details><summary>Respuesta</summary>

   b) Hay ocho caracteres en `str_var`. Iterar sobre todos los caracteres e incrementar el valor de la variable `count` en cada iteración da como resultado un valor de `count` de `8`.

   </details>

<!-- pregunta: CPL-ch05-m02-p02 -->

2. ¿Cuál es la salida del código si la línea `count += 1` se reemplaza por `count *= 2`?

   - a) `0`
   - b) `16`
   - c) `2``8`

   <details><summary>Respuesta</summary>

   a) Como el valor inicial de `count` es `0`, multiplicar `count` por cualquier número da como resultado `0`.

   </details>

<!-- pregunta: CPL-ch05-m02-p03 -->

3. ¿Qué se imprime si el código se cambia de la siguiente manera?
   
   ```python
   str_var = "A string"
   
   count = 0
   for c in str_var:
     count += 1
     # Línea nueva
     print(c, end = '*')
   
   print(count)
   ```

   - a) `A string*`
   - b) `A*s*t*r*i*n*g*`
   - c) `A* *s*t*r*i*n*g*`

   <details><summary>Respuesta</summary>

   c) La línea añadida imprime cada carácter sobre el que se itera (carácter `), e imprime un * adicional después del carácter.`

   </details>

### Función `range()` en un bucle for

Un bucle `for` se puede usar para iterar y contar. La función `range()` es una forma común de implementar el conteo en un bucle `for`. Una función **range()** genera una secuencia de enteros entre los dos números dados, con un tamaño de paso. Esta secuencia de enteros incluye el inicio y excluye el final de la secuencia. La función `range()` puede recibir hasta tres valores de entrada. En la siguiente tabla se muestran ejemplos.

**Uso de la función range().**

| Función range | Descripción | Ejemplo | Salida |
|---|---|---|---|
| `range(end)` | - Genera una secuencia que comienza en `0` hasta `end`.<br>- Tamaño de paso: `1` | `range(4)` | `0, 1, 2, 3` |
| `range(start, end)` | - Genera una secuencia que comienza en `start` hasta `end`.<br>- Tamaño de paso: `1` | `range(0, 3)` | `0, 1, 2` |
| `range(2, 6)` | `2, 3, 4, 5` |  |  |
| `range(-13, -9)` | `-13, -12, -11, -10` |  |  |
| `range(start, end, step)` | - Genera una secuencia que comienza en `start` hasta `end`.<br>- Tamaño de paso: `step` | `range(0, 4, 1)` | `0, 1, 2, 3` |
| `range(1, 7, 2)` | `1, 3, 5` |  |  |
| `range(3, -2, -1)` | `3, 2, 1, 0, -1` |  |  |
| `range(10, 0, -4)` | `10, 6, 2` |  |  |

**Ejemplo: Dos programas que imprimen todos los múltiplos enteros de 5 menores que 50 (observa lo compacta que es la construcción con `for` comparada con la de `while`)**

|  |  |
|---|---|
| ```python<br># Condición del bucle for usando<br># la función range() para imprimir<br># todos los múltiplos de 5 menores que 50<br>for i in range(0, 50, 5):<br>  print(i)<br>``` | ```python<br># Implementación con bucle while para imprimir<br># los múltiplos de 5 menores que 50<br><br># Inicialización<br>i = 0<br># Limitar el rango a valores menores que 50<br>while i < 50:<br>    print(i)<br>    i+=5<br>``` |

**Conceptos en práctica: Bucle for con la función range()**

<!-- pregunta: CPL-ch05-m02-p04 -->

1. ¿Cuáles son los argumentos de la función `range()` para la secuencia creciente de cada tercer entero de 10 a 22 (incluyendo ambos extremos)?

   - a) `range(10, 23, 3)`
   - b) `range(10, 22, 3)`
   - c) `range(22, 10, -3)`

   <details><summary>Respuesta</summary>

   a) La salida será una secuencia creciente entre `10` y `22` (incluyendo ambos): `10`, `13`, `16`, `19` y `22`.

   </details>

<!-- pregunta: CPL-ch05-m02-p05 -->

2. ¿Cuáles son los argumentos de la función `range()` para la secuencia decreciente de cada entero de 5 a 1 (incluyendo ambos extremos)?

   - a) `range(5, 1, 1)`
   - b) `range(5, 1, -1)`
   - c) `range(5, 0, -1)`

   <details><summary>Respuesta</summary>

   c) La expresión comienza una secuencia desde `5`, disminuye en 1 en cada paso y termina en `1`.

   </details>

<!-- pregunta: CPL-ch05-m02-p06 -->

3. ¿Cuál es la secuencia generada por `range(-1, -2, -1)`?

   - a) `1`
   - b) `-1, -2`
   - c) `-2`

   <details><summary>Respuesta</summary>

   a) La función `range()` genera una secuencia descendente, que comienza en `-1` hasta `-2`. Por lo tanto, la salida es `-1`.

   </details>

<!-- pregunta: CPL-ch05-m02-p07 -->

4. ¿Cuál es la salida de `range(1, 2, -1)`?

   - a) `1`
   - b) `1, 2`
   - c) secuencia vacía

   <details><summary>Respuesta</summary>

   c) Cuando el tamaño de paso es negativo, la secuencia generada estará en orden descendente. Por lo tanto, `start` debe ser mayor que `end`; de lo contrario, no se generará ninguna secuencia.

   </details>

<!-- pregunta: CPL-ch05-m02-p08 -->

5. ¿Cuál es la salida de `range(5, 2)`?

   - a) `0, 2, 4`
   - b) `2, 3, 4`
   - c) secuencia vacía

   <details><summary>Respuesta</summary>

   c) Cuando se proporcionan dos argumentos a la función `range()`, los argumentos se consideran el `start` y el `end` de la secuencia, y el tamaño de paso será `1`. Cuando el tamaño de paso es positivo, la secuencia generada estará en orden ascendente y, por lo tanto, `start` debe ser menor que `end`. De lo contrario, no se generará ninguna secuencia.

   </details>

**Pruébalo: Conteo de espacios**

Escribe un programa que use un bucle `for` y reciba una cadena como entrada y cuente el número de espacios en la cadena proporcionada. El programa debe imprimir el número de espacios contados. Ej.: si la entrada es `"Hi everyone"`, el programa muestra `1`.

<!-- coderunner: ch5/CodeRunner_05_03_03_Counting-spaces -->

**Pruébalo: Secuencias**

Escribe un programa que lea dos valores enteros, `n1` y `n2`, con `n1 < n2`, y realice las siguientes tareas:

1. Imprime todos los números pares entre los dos números proporcionados (incluyendo ambos), en orden ascendente.
2. Imprime todos los números impares entre los dos números proporcionados (excluyendo ambos), en orden descendente.

```text
Input: 2 8
```

```text
Prints:
2 4 6 8
7 5 3
```

Nota: el programa debe devolver un mensaje de error si el segundo número es menor que el primero.

<!-- coderunner: ch5/CodeRunner_05_03_04_Sequences -->

<!-- modulo: m00039 -->

## 5.3 Bucles anidados

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Implementar bucles `while` anidados.
- Implementar bucles `for` anidados.

### Bucles anidados

Un **bucle anidado** tiene uno o más bucles dentro del cuerpo de otro bucle. Los dos bucles se denominan **bucle externo** y **bucle interno**. El bucle externo controla el número de ejecuciones completas del bucle interno. Un bucle anidado puede tener más de un bucle interno.

**Video:** [Nested while loops](https://www.openstax.org/r/nested-while-loops)

**Ejemplo: Citas disponibles**

Considera el horario de un consultorio médico. Cada cita dura 30 minutos. Un programa para imprimir las citas disponibles puede usar un bucle `for` anidado, donde el bucle externo itera sobre las horas y el bucle interno itera sobre los minutos. Este ejemplo imprime la hora en horas y minutos en el rango entre las 8:00 a. m. y las 10:00 a. m. En este ejemplo, el bucle externo itera sobre la parte de las horas entre 8 y 9, y el bucle interno itera sobre la parte de los minutos entre 0 y 59.

```python
hour = 8
minute = 0
while hour <= 9:
  while minute <= 59:
    print(hour, ":", minute)
    minute += 30
  hour += 1
  minute = 0
```

La salida del código anterior es:

```salida
8 : 0
8 : 30
9 : 0
9 : 30
```

**Conceptos en práctica: Conjunto de preguntas sobre bucles while anidados**

<!-- pregunta: CPL-ch05-m03-p01 -->

1. Dado el siguiente código, ¿cuántas veces se ejecuta la instrucción print?
   
   ```python
   i = 1
   while i <= 5:
     j = 1
     while i + j <= 5:
       print(i, j)
       j += 1
     i += 1
   ```

   - a) 5
   - b) 10
   - c) 25

   <details><summary>Respuesta</summary>

   b) Las combinaciones de valores de `i` y `j`, `(i, j)`, que cumplen las condiciones del bucle interno y del externo son las siguientes:
    `(1, 1), (1, 2), (1, 3), (1, 4), `
    `(2, 1), (2, 2), (2, 3), `
    `(3, 1), (3, 2), `
    `(4, 1)`

   </details>

<!-- pregunta: CPL-ch05-m03-p02 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   i = 1
   
   while i <= 2:
     j = 1
     while j <= 3:
       print('*', end = '')
       j += 1
     print()
     i += 1
   ```

   - a)

     ```python norun
     ******
     ```

   - b)

     ```python norun
     ***
     ***
     ```

   - c)

     ```python norun
     **
     **
     **
     ```

   <details><summary>Respuesta</summary>

   b) Cada ejecución completa del bucle interno imprime tres caracteres «*», y el bucle externo se ejecuta dos veces.

   </details>

<!-- pregunta: CPL-ch05-m03-p03 -->

3. ¿Qué programa imprime la siguiente salida?
   
   ```python norun
   1 2 3 4
   2 4 6 8
   3 6 9 12
   4 8 12 16
   ```

   - a)

     ```python norun
     i = 1
     while i <= 4:
       while j <= 4:
         print(i * j, end = ' ')
         j += 1
       print()
       i += 1
     ```

   - b)

     ```python
     i = 1
     while i <= 4:
       j = 1
       while j <= 4:
         print(i * j, end = ' ')
         j += 1
       print()
       i += 1
     ```

   - c)

     ```python
     i = 1
     while i <= 4:
       j = 1
       while j <= 4:
         print(i * j, end = ' ')
         j += 1
       i += 1
     ```

   <details><summary>Respuesta</summary>

   b) Cada línea `i` de la salida (`i = ``1`, `2`, `3` y `4`) contiene los valores `1` a `4` multiplicados por `i`.
    Por lo tanto, el bucle externo se ejecuta mientras `i <= 4`, y el bucle interno itera sobre `j` mientras el valor de `j` sea menor o igual que `4`.

   </details>

### Bucles for anidados

Un bucle `for` anidado se puede implementar y usar de la misma manera que un bucle `while` anidado. Un bucle `for` es la opción preferible cuando se usa un bucle para contar con la función `range()`, o cuando se itera sobre un objeto contenedor, incluidas las situaciones anidadas. Ej.: iterar sobre las listas de varios cursos. El bucle externo itera sobre los diferentes cursos, y el bucle interno itera sobre los nombres de cada lista de curso.

**Video:** [Nested for loops](https://www.openstax.org/r/nested-for-loops)

**Conceptos en práctica: Prácticas con bucles anidados**

<!-- pregunta: CPL-ch05-m03-p04 -->

1. Dado el siguiente código, ¿cuántas veces se ejecuta el bucle externo?
   
   ```python
   for i in range(3):
     for j in range(4):
       print(i, ' ', j)
   ```

   - a) 3
   - b) 4
   - c) 12

   <details><summary>Respuesta</summary>

   a) El rango de ejecución del bucle externo es `0`, `1` y `2`; por lo tanto, el bucle externo se ejecuta tres veces.

   </details>

<!-- pregunta: CPL-ch05-m03-p05 -->

2. Dado el siguiente código, ¿cuántas veces se ejecuta el bucle interno?
   
   ```python
   for i in range(3):
     for j in range(4):
       print(i, ' ', j)
   ```

   - a) 4
   - b) 12
   - c) 20

   <details><summary>Respuesta</summary>

   b) El bucle interno se evalúa cuatro veces (`j = 0`, `1`, `2` y `3`) por cada valor de `i` establecido por el bucle externo. En el ejemplo dado, `i = 0`, `1` y `2`; por lo tanto, el número total de veces que se ejecuta el bucle interno es `3 * 4 = 12`.

   </details>

<!-- pregunta: CPL-ch05-m03-p06 -->

3. ¿Qué programa imprime la siguiente salida?
   
   ```python norun
   0 1 2 3
   0 2 4 6
   0 3 6 9
   ```

   - a)

     ```python
     for i in range(4):
       for j in range(4):
         print(i * j, end = ' ')
       print()
     ```

   - b)

     ```python
     for i in range(1, 4):
       for j in range(4):
         print(i * j)
     ```

   - c)

     ```python
     for i in range(1, 4):
       for j in range(4):
         print(i * j, end = ' ')
       print()
     ```

   <details><summary>Respuesta</summary>

   c) La salida impresa muestra tres filas, y cada fila `i` muestra los valores en el rango de `0` a `3` multiplicados por `i`. Por lo tanto, el código debe iterar sobre el número de fila en el bucle externo y, en cada fila, iterar sobre el número de elemento en el rango de `0` a `3`.

   </details>

**Bucles mixtos**

Las dos estructuras de bucle `for` y `while` también se pueden combinar en un bucle anidado. Ej.: imprimir los números pares menores que un número dado de una lista. El bucle externo se puede implementar con un bucle `for` que itere sobre la lista proporcionada, y el bucle interno itera con un bucle `while` sobre todos los números pares menores que un número dado de la lista.

```python
numbers = [12, 5, 3]

i = 0
for n in numbers:
  while i < n:
    print (i, end = " ")
    i += 2
  i = 0
  print()
```

**Pruébalo: Impresión de un triángulo de números**

Escribe un programa que imprima la siguiente salida:

```python norun
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

`Finish!`

<!-- coderunner: ch5/CodeRunner_05_04_05_Printing-a-triangle-of-numbers -->

**Pruébalo: Impresión de dos triángulos**

Escribe un programa que imprima la siguiente salida usando bucles `while` y `for` anidados:

```python norun
****
***
**
*
++++
+++
++
+
```

<!-- coderunner: ch5/CodeRunner_05_04_06_Printing-two-triangles -->

<!-- modulo: m00040 -->

## 5.4 Break y continue

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Analizar la ejecución de un bucle con las instrucciones `break` y `continue`.
- Usar las instrucciones de control `break` y `continue` en bucles `while` y `for`.

### Break

Una instrucción **break** se usa dentro de un bucle `for` o `while` para permitir que la ejecución del programa salga del bucle cuando se activa una condición dada. Una instrucción `break` se puede usar para mejorar la eficiencia en tiempo de ejecución cuando ya no es necesario seguir ejecutando el bucle.

Ej.: un bucle que busca el carácter `"a"` en una cadena dada llamada `user_string`. El siguiente bucle es un bucle `for` normal que recorre todos los caracteres de `user_string`. Si se encuentra el carácter, la instrucción break saca la ejecución del bucle `for`. Como la tarea ya se cumplió, se omite el resto de la ejecución del bucle `for`.

```python
user_string = "This is a string."
for i in range(len(user_string)):
  if user_string[i] == 'a':
    print("Found at index:", i)
    break
```

**Video:** [Break statement in a while loop](https://www.openstax.org/r/while-break)

**Bucle infinito**

Una instrucción `break` es una parte esencial de un bucle que no tiene una condición de terminación. Un bucle sin condición de terminación se conoce como **bucle infinito**. Ej.: un bucle infinito que cuenta hacia arriba a partir de 1 e imprime el valor del contador mientras este sea menor que 10. Se activa una condición `break` cuando el valor del contador es igual a 10 y, por lo tanto, la ejecución del programa sale del bucle.

```python
counter = 1
while True:
  if counter >= 10:
    break
  print(counter)
  counter += 1
```

**Conceptos en práctica: Uso de una instrucción break**

<!-- pregunta: CPL-ch05-m04-p01 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   string_val = "Hello World"
   for c in string_val:
     if c == " ":
       break
     print(c)
   ```

   - a) `Hello`
   - b)

     ```python norun
     Hello World
     ```

   - c)

     ```python norun
     H
     e
     l
     l
     o
     ```

   <details><summary>Respuesta</summary>

   c) El código imprime, en líneas separadas, todos los caracteres anteriores a la primera aparición de un carácter de espacio. Por lo tanto, la salida es:
   
   ```python norun
   H
   e
   l
   l
   o
   ```

   </details>

<!-- pregunta: CPL-ch05-m04-p02 -->

2. Dado el siguiente código, ¿cuántas veces se ejecuta la instrucción print?
   
   ```python
   i = 1
   while True:
     if i%3 == 0 and i%5 == 0:
       print(i)
       break
     i += 1
   ```

   - a) 0
   - b) 1
   - c) 15

   <details><summary>Respuesta</summary>

   b) En cuanto se ejecuta la instrucción `print`, la instrucción `break` termina el bucle. Además, para `i = 15` se cumple la condición `(i%3 == 0 and i%5 == 0)` y, por lo tanto, la instrucción print se ejecutará exactamente una vez.

   </details>

<!-- pregunta: CPL-ch05-m04-p03 -->

3. ¿Cuál es el valor final de i?
   
   ```python
   i = 1
   count = 0
   while True:
     if i%2 == 0 or i%3 == 0:
       count += 1
     if count >= 5:
       print(i)
       break
     i += 1
   ```

   - a) `5`
   - b) `8`
   - c) `30`

   <details><summary>Respuesta</summary>

   b) El bucle encuentra los primeros cinco números divisibles entre `2` o entre `3`. Estos números son `2`, `3`, `4`, `6` y `8` y, por lo tanto, `8` es el valor final de `i`.

   </details>

### Continue

Una instrucción **continue** permite omitir la ejecución del resto del bucle sin salir del bucle por completo. Una instrucción `continue` se puede usar en un bucle `for` o `while`. Después de ejecutar la instrucción `continue`, la expresión del bucle se evaluará de nuevo y el bucle continuará desde la expresión del bucle. Una instrucción `continue` facilita el control y la legibilidad del bucle.

**Video:** [Continue statement in a while loop](https://www.openstax.org/r/while-control)

**Conceptos en práctica: Uso de una instrucción continue**

<!-- pregunta: CPL-ch05-m04-p04 -->

1. Dado el siguiente código, ¿cuántas veces se ejecuta la instrucción print?
   
   ```python
   i = 10
   while i >= 0:
     i -= 1
     if i%3 != 0:
       continue
     print(i)
   ```

   - a) 3
   - b) 4
   - c) 11

   <details><summary>Respuesta</summary>

   b) La instrucción print se ejecuta para los números del rango de 0 a 10 (incluyendo ambos) que son divisibles entre 3. La salida impresa es:
   
   ```python
   9
   6
   3
   0
   ```

   </details>

<!-- pregunta: CPL-ch05-m04-p05 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   for c in "hi Ali":
     if c == " ":
       continue
     print(c)
   ```

   - a)

     ```python norun
     h
     i
     
     A
     l
     i
     ```

   - b)

     ```python norun
     h
     i
     A
     l
     i
     ```

   - c)

     ```python norun
     hi
     Ali
     ```

   <details><summary>Respuesta</summary>

   b) El bucle comprueba si el carácter que se está evaluando es un espacio o no. Si lo es, se omitirá el resto del bucle y el carácter de espacio no se imprimirá.

   </details>

**Pruébalo: Uso de la instrucción de control break en un bucle**

Escribe un programa que lea una cadena e imprima `"Found"` si la cadena contiene un carácter de espacio. De lo contrario, imprime `"Not found"`.

<!-- coderunner: ch5/CodeRunner_05_05_07_Using-break-control-statement-in-a-loop -->

**Pruébalo: Uso de una instrucción continue en un bucle**

Completa el siguiente código para que el programa calcule la suma de todos los números de la lista `my_list` que sean mayores o iguales que 5.

<!-- coderunner: ch5/CodeRunner_05_05_08_Using-a-continue-statement-in-a-loop -->

<!-- modulo: m00041 -->

## 5.5 else de bucle

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar la instrucción `else` de un bucle para identificar cuándo la ejecución del bucle se interrumpe con una instrucción `break`.
- Implementar una instrucción `else` de bucle con un bucle `for` o `while`.

### else de bucle

Una instrucción **else de bucle** se ejecuta después de que el bucle termina su ejecución sin ser interrumpido por una instrucción break. Un `else` de bucle se usa para identificar si el bucle terminó normalmente o si su ejecución fue interrumpida por una instrucción `break`.

Ej.: un bucle `for` que itera sobre una lista de números para averiguar si el valor `10` está en la lista. En cada iteración, si se encuentra `10`, se imprime el mensaje `"Found 10!"` y la ejecución puede terminar con una instrucción break. Si `10` no está en la lista, el bucle termina cuando se han evaluado todos los enteros de la lista y, por lo tanto, se ejecutará la instrucción `else` e imprimirá `"10 is not in the list."`. Como alternativa, se puede usar una variable booleana para registrar si el número `10` se encontró una vez que termina la ejecución del bucle.

**Ejemplo: Buscar el número 10 en una lista**

En los siguientes ejemplos de código, el código de la izquierda imprime `"Found 10!"` si el valor de la variable `i` es `10`. Si el valor `10` no está en la lista, el código imprime `"10 is not in the list."`. El código de la derecha usa la variable booleana `seen` para registrar si el valor `10` está en la lista. Después de la ejecución del bucle, si el valor de `seen` sigue siendo falso, el código imprime `"10 is not in the list."`.

|  |  |
|---|---|
| ```python<br>numbers = [2, 5, 7, 11, 12]<br>for i in numbers:<br>  if i == 10:<br>    print("Found 10!")<br>    break<br>else:<br>  print("10 is not in the list.")<br>``` | ```python<br>numbers = [2, 5, 7, 11, 12]<br>seen = False<br>for i in numbers:<br>  if i == 10:<br>    print("Found 10!")<br>    seen = True<br>if seen == False:<br>  print("10 is not in the list.")<br>``` |

**Video:** [Loop else template](https://www.openstax.org/r/loop-else)

**Conceptos en práctica: Prácticas con else de bucle**

<!-- pregunta: CPL-ch05-m05-p01 -->

1. ¿Cuál es la salida?
   
   ```python
   n = 16
   exp = 0
   i = n
   while i > 1:
     if n%2 == 0:
       i = i/2
       exp += 1
     else:
       break
   else:
     print(n,"is 2 to the", exp)
   ```

   - a) `16 is 2 to the 3`
   - b) `16 is 2 to the 4`
   - c) sin salida

   <details><summary>Respuesta</summary>

   b) La variable `i` se inicializa en `16` y el bucle `while` se ejecuta con `i = 16`, `8`, `4` y `2`. En cada iteración del bucle, el valor de la variable `exp` aumenta en 1. Por lo tanto, al final del bucle, `exp = 4`. Como el bucle termina sin interrupción, se ejecuta la instrucción `else` posterior al bucle e imprime `16 is 2 to the 4`.

   </details>

<!-- pregunta: CPL-ch05-m05-p02 -->

2. ¿Cuál es la salida?
   
   ```python
   n = 7
   exp = 0
   i = n
   while i > 1:
     if n%2 == 0:
       i = i//2
       exp += 1
     else:
       break
   else:
     print(n,"is 2 to the", exp)
   ```

   - a) sin salida
   - b) `7 is 2 to the 3`
   - c) `7 is 2 to the 2`

   <details><summary>Respuesta</summary>

   a) El valor inicial de `i` es `7`. Por lo tanto, en la primera iteración del bucle se ejecuta la instrucción `else` dentro del bucle, y la instrucción `break` termina el bucle. Como la ejecución del bucle se interrumpe, el `else` posterior al bucle no se ejecutará y no habrá salida.

   </details>

<!-- pregunta: CPL-ch05-m05-p03 -->

3. ¿Cuál es la salida?
   
   ```python
   numbers = [1, 2, 2, 6]
   for i in numbers:
     if i >= 5:
       print("Not all numbers are less than 5.")
       break
     else:
       print(i)
       continue
   else:
     print("all numbers are less than 5.")
   ```

   - a)

     ```python norun
     1
     2
     2
     6
     Not all numbers are less than 5.
     ```

   - b)

     ```python norun
     1
     2
     2
     Not all numbers are less than 5.
     ```

   - c)

     ```python norun
     1
     2
     2
     6
     all numbers are less than 5.
     ```

   <details><summary>Respuesta</summary>

   b) El bucle itera sobre todos los valores enteros de la lista. Si un valor es menor que `5`, el valor se imprimirá, y si el valor es mayor que `5`, el código imprime «`Not all numbers are less than 5.`» y la ejecución del código termina.

   </details>

**Pruébalo: Suma de valores menores que 10**

Escribe un programa que, dada una lista, calcule la suma de todos los valores enteros menores que 10. Si hay en la lista un valor mayor o igual que 10, no se debe imprimir ninguna salida. Prueba el código con diferentes valores en la lista.

<!-- coderunner: ch5/CodeRunner_05_06_09_Sum-of-values-less-than-10 -->

<!-- modulo: m00042 -->

## Resumen del capítulo

Estos son los puntos destacados de este capítulo:

- Un bucle `while` ejecuta un conjunto de instrucciones, conocido como el cuerpo del bucle, mientras una condición dada, conocida como la expresión del bucle, sea verdadera.
- Un bucle `for` se puede usar para iterar sobre los elementos de un objeto contenedor.
- Una función `range()` genera una secuencia de enteros entre los dos números dados, con un tamaño de paso.
- Un bucle anidado tiene uno o más bucles dentro del cuerpo de otro bucle.
- Una instrucción `break` se usa dentro de un bucle `for` o `while` para permitir que la ejecución del programa salga del bucle cuando se activa una condición dada.
- Una instrucción `continue` permite omitir la ejecución del resto del bucle sin salir del bucle por completo.
- Una instrucción `else` de bucle se ejecuta después de que el bucle termina su ejecución sin ser interrumpido por una instrucción `break`.

En este punto, deberías poder escribir programas con estructuras de bucle. La práctica de programación que sigue reúne la mayoría de los temas presentados en el capítulo.

**Referencia del capítulo 5.**

| Función | Descripción |
|---|---|
| `range(end)` | Genera una secuencia que comienza en 0 hasta `end` con un tamaño de paso de 1. |
| `range(start, end)` | Genera una secuencia que comienza en `start` hasta `end` con un tamaño de paso de 1. |
| `range(start, end, s)` | Genera una secuencia que comienza en `start` hasta `end` con un tamaño de paso de `s`. |
| **Estructuras de bucle** | **Descripción** |
| Bucle `while` | ```python<br># inicialización<br>while expression:<br>  # cuerpo del bucle<br><br># instrucciones después del bucle<br>``` |
| Bucle `for` | ```python<br># inicialización<br>for loop_variable in container:<br>  # cuerpo del bucle<br><br># instrucciones después del bucle<br>``` |
| Bucle `while` anidado | ```python<br>while outer_loop_expression:<br>  # cuerpo del bucle externo (1)<br>  while inner_loop_expression:<br>    # cuerpo del bucle interno<br>  # cuerpo del bucle externo (2)<br><br># instrucciones después del bucle<br>``` |
| Instrucción `break` | ```python<br># inicialización<br>while loop_expression:<br>  # cuerpo del bucle<br>  if break_condition:<br>    break<br>  # resto del cuerpo del bucle<br><br># instrucciones después del bucle<br>``` |
| Instrucción `continue` | ```python<br># inicialización<br>while loop_expression:<br>  # cuerpo del bucle<br>  if continue_condition:<br>    continue<br>  # resto del cuerpo del bucle<br><br># instrucciones después del bucle<br>``` |
| Instrucción `else` de bucle | ```python<br># inicialización<br>for loop_expression:<br>  # cuerpo del bucle<br>  if break_condition:<br>    break<br>  # resto del cuerpo del bucle<br>else:<br>  # instrucción else del bucle<br><br># instrucciones después del bucle<br>``` |

**Pruébalo: Números primos**

Escribe un programa que reciba un número entero positivo (`N`) e imprima los primeros `N` números primos en líneas separadas.

Nota: un número primo es un número que no es divisible entre ningún número positivo mayor que 1. Para comprobar si un `number` es primo, se puede comprobar la condición `number % i != 0` para `i` mayor que `1` y menor que `number`.

Ej.: si `N = 6`, la salida es:

```text
2
3
5
7
11
13
```

<!-- coderunner: ch5/CodeRunner_05_07_10_Prime-numbers -->
