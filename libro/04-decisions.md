# Capítulo 4: Decisiones

<!-- modulo: m00027 -->

## Introducción

![un grupo de árboles con caminos a ambos lados](media/Python_04_00_000.jpg)

*crédito: modificación de la obra «Fork In The Road», de Ian Sane/Flickr, CC BY 2.0*

El intérprete de Python sigue un único camino de ejecución cuando ejecuta un programa. ¿Qué pasa si un programador quiere definir varios caminos posibles? Ej.: en lugar de tomar siempre el camino de la izquierda, un programa usa el ancho del camino para decidir cuál tomar. Si el camino de la izquierda es más ancho, toma el de la derecha. Si no, toma el de la izquierda.

Una **rama** es un grupo de instrucciones que se ejecutan según una condición. El capítulo sobre expresiones presentó las expresiones. Este capítulo explora cómo se pueden usar las expresiones como condiciones para tomar decisiones en los programas.

<!-- modulo: m00028 -->

## 4.1 Valores booleanos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar qué es un valor booleano.
- Usar variables bool para almacenar valores booleanos.
- Demostrar la conversión de enteros, floats y cadenas a booleanos.
- Demostrar la conversión de booleanos a enteros, floats y cadenas.
- Usar operadores de comparación para comparar enteros, floats y cadenas.

### El tipo de datos bool

Las personas suelen hacer preguntas binarias, como las de sí/no o verdadero/falso. Ej.: ¿Te gusta la piña en la pizza? Ej.: Verdadero o falso: me gusta la piña en la pizza. La respuesta es un valor booleano, es decir, un valor que es verdadero o falso. El tipo de datos **bool**, abreviatura de booleano, representa un valor binario que puede ser verdadero o falso. `true` y `false` son palabras clave, y es obligatorio respetar las mayúsculas y minúsculas.

**Video:** [Example: Crosswalk sign](https://www.openstax.org/r/crosswalk-sign)

**Conceptos en práctica: Uso de variables booleanas**

<!-- pregunta: CPL-ch04-m01-p01 -->

1. ¿Cuál es el tipo de datos de `is_fruit`?

   - a) Booleano
   - b) Entero
   - c) Cadena

   <details><summary>Respuesta</summary>

   c) `"True"` usa comillas, por lo que el valor es una cadena.

   </details>

<!-- pregunta: CPL-ch04-m01-p02 -->

2. ¿Cuál es el tipo de datos de `is_vegetable`?

   - a) Booleano
   - b) Entero
   - c) Cadena

   <details><summary>Respuesta</summary>

   b) `is_vegetable` es un entero y se puede usar en operaciones aritméticas.

   </details>

<!-- pregunta: CPL-ch04-m01-p03 -->

3. ¿Cuál es el tipo de datos de `is_dessert`?

   - a) Booleano
   - b) Entero
   - c) Cadena

   <details><summary>Respuesta</summary>

   a) Una variable a la que se le asigna `True` o `False` es una variable booleana.

   </details>

<!-- pregunta: CPL-ch04-m01-p04 -->

4. ¿Cuántos valores puede representar una variable booleana?

   - a) 2
   - b) 4
   - c) 8

   <details><summary>Respuesta</summary>

   a) Una variable booleana representa el valor `True` o `False`.

   </details>

<!-- pregunta: CPL-ch04-m01-p05 -->

5. ¿Cuál es un valor válido para una variable booleana?

   - a) `true`
   - b) `True`
   - c) `1`

   <details><summary>Respuesta</summary>

   b) `True` y `False` son los únicos dos valores de una variable booleana.

   </details>

<!-- pregunta: CPL-ch04-m01-p06 -->

6. Supón que se agrega lo siguiente al código anterior:
   
   ```python
   is_dessert = 0
   print(type(is_dessert))
   ```
   
    ¿Cuál es la salida?

   - a) `<class 'bool'>`
   - b) `<class 'int'>`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) Asignarle un `int` a un bool produce una conversión implícita de tipos. La conversión de tipos puede causar problemas más adelante en el código si el programador supone que `is_dessert` sigue siendo un booleano.

   </details>

### Conversión de tipos con bool()

Decidir si un valor es verdadero o falso resulta útil al escribir programas e instrucciones basados en decisiones. Convertir tipos de datos a booleanos puede parecer poco intuitivo al principio. Ej.: `Is "ice cream" True?` Pero la conversión es en realidad sencilla.

**bool()** convierte un valor en un valor booleano, `True` o `False`.

- `True`: cualquier número distinto de cero, cualquier cadena no vacía
- `False`: 0, la cadena vacía

**Video:** [Converting integers, floats, and strings using bool()](https://www.openstax.org/r/converting-using-bool)

**Conceptos en práctica: Conversión de tipos numéricos y cadenas a booleanos**

<!-- pregunta: CPL-ch04-m01-p07 -->

1. `bool(0.000)`

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) Cualquier tipo numérico que represente 0 se convierte en `False`. Los números distintos de cero se convierten en `True`.

   </details>

<!-- pregunta: CPL-ch04-m01-p08 -->

2. `bool(-1)`

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) Un número negativo es distinto de cero y se convierte en `True`.

   </details>

<!-- pregunta: CPL-ch04-m01-p09 -->

3. `bool("")`

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) La cadena vacía es la única cadena que se convierte en `False`.

   </details>

<!-- pregunta: CPL-ch04-m01-p10 -->

4. `bool("0")`

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) `"0"` es una cadena no vacía y se convierte en `True`.

   </details>

<!-- pregunta: CPL-ch04-m01-p11 -->

5. Dada la entrada `False`, ¿cuál es el resultado de `bool(input())`?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) La entrada se lee como una cadena, por lo que `bool("False")` es `True`.

   </details>

**Conceptos en práctica: Conversión de booleanos a tipos numéricos y cadenas**

<!-- pregunta: CPL-ch04-m01-p12 -->

1. `float(is_on)`

   - a) `0.0`
   - b) `1.0`

   <details><summary>Respuesta</summary>

   b) `True` convertido a float es `1.0.` `False` convertido a float es `0.0.`

   </details>

<!-- pregunta: CPL-ch04-m01-p13 -->

2. `str(is_on)`

   - a) `"is_on"`
   - b) `"True"`

   <details><summary>Respuesta</summary>

   b) `True` convertido a cadena es `"True"`. False convertido a cadena es `"False"`.

   </details>

<!-- pregunta: CPL-ch04-m01-p14 -->

3. `int(is_on)`

   - a) `0`
   - b) `1`

   <details><summary>Respuesta</summary>

   b) Cuando un booleano se convierte a un tipo numérico, `True` se convierte en `1` y `False` se convierte en `0`.

   </details>

### Operadores de comparación

Los programadores suelen tener que responder preguntas como «¿El usuario actual es el administrador?». Un programador puede querer comparar una variable de cadena, user, con la cadena `"admin"`. Los **operadores de comparación** se usan para comparar valores, y el resultado es verdadero o falso. Ej.: `is_admin = (user == "admin")`. `user` se compara con `"admin"` mediante el operador `==`, que comprueba si hay igualdad. A la variable booleana `is_admin` se le asigna el resultado booleano.

Los 6 operadores de comparación:

- igual a: **==**
- distinto de: **!=**
- mayor que: **>**
- menor que: **<**
- mayor o igual que: **>=**
- menor o igual que: **<=**

**Video:** [Example: Rolling a d20 in a tabletop game](https://www.openstax.org/r/rolling-d20)

**Conceptos en práctica: Comparación de valores**

<!-- pregunta: CPL-ch04-m01-p15 -->

1.

   ```python
   x = 14
   compare_result = (x <= 13)
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) 14 es mayor que 13, por lo que 14 no es menor o igual que 13.

   </details>

<!-- pregunta: CPL-ch04-m01-p16 -->

2.

   ```python
   w = 0
   compare_result = (w != 0.4)
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) 0 es menor que 0.4, por lo que 0 no es igual a 0.4.

   </details>

<!-- pregunta: CPL-ch04-m01-p17 -->

3.

   ```python
   v = 4
   compare_result = (v < 4.0)
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) 4 es igual a 4.0, por lo que 4 no es menor que 4.0.

   </details>

<!-- pregunta: CPL-ch04-m01-p18 -->

4.

   ```python norun
   y = 2
   compare_result = (y > "ab")
   ```

   - a) `True`
   - b) `False`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) Los tipos numéricos no se pueden comparar con cadenas mediante los operadores de comparación &gt;, &lt;, &gt;=, &lt;=. Usar == o != producirá un booleano.

   </details>

<!-- pregunta: CPL-ch04-m01-p19 -->

5.

   ```python
   z = "cilantro"
   compare_result = (z == "coriander")
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) Las cadenas se comparan comparando los valores Unicode de cada carácter. Las letras tienen valores Unicode ascendentes en orden alfabético (y se distingue entre mayúsculas y minúsculas). `"c"` y `"c"` son iguales, así que se compara `"i"` con `"o"`. `"i"` no es igual a `"o"`, por lo que se produce `False`, aunque el cilantro y el coriandro provienen de la misma planta.

   </details>

<!-- pregunta: CPL-ch04-m01-p20 -->

6.

   ```python
   a = "dog"
   compare_result = (a < "cat")
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) Las letras tienen valores Unicode ascendentes en orden alfabético (y se distingue entre mayúsculas y minúsculas). `"d"` es mayor que `"c"`, no menor, por lo que se produce `False`.

   </details>

**= vs ==**

Un error común es usar = para comparar en lugar de ==. Ej.: `is_zero = num=0` siempre le asignará `0` a `is_zero` y a `num`, sin importar el valor original de num. El operador = realiza una asignación y modificará la variable. El operador == realiza una comparación, no modifica la variable y produce `True` o `False`.

**Para saber más**

- [Unicode Basic Latin Chart](https://openstax.org/r/100unicodelatin)

**Pruébalo: Viernes booleano**

«It's Friday, I'm in love» (Es viernes, estoy enamorado), de la canción «Friday I'm in Love», lanzada por The Cure en 1992.

Escribe un programa que lea el día de la semana. Asigna a la variable booleana `in_love` el resultado de si el día es viernes o no.

<!-- coderunner: ch4/CodeRunner_04_02_01_Programming-practice_-Friday-boolean -->

**Pruébalo: Números pares**

Escribe un programa que lea un entero e imprima si el entero es par o no. Recuerda que un número es par si es divisible entre 2. Para comprobarlo usa `number % 2 == 0`. Ej.: si la entrada es `6`, la salida es `"6 is even: True"`.

<!-- coderunner: ch4/CodeRunner_04_02_02_Programming-practice_-Even-numbers -->

<!-- modulo: m00029 -->

## 4.2 Instrucciones if-else

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar qué operaciones se realizan cuando se ejecuta un programa con instrucciones `if` e `if-else`.
- Identificar los componentes de una instrucción `if` e `if-else` y el formato necesario.
- Crear una instrucción `if-else` para realizar una operación cuando una condición es verdadera y otra operación en caso contrario.

### Instrucción if

Si el clima está lluvioso, ¡toma un paraguas! Las personas toman decisiones según condiciones, como si el clima está lluvioso, y los programas realizan operaciones según condiciones, como el valor de una variable. Ej.: un programa suma dos números. Si el resultado es negativo, el programa imprime un error.

Una **condición** es una expresión que se evalúa como verdadera o falsa. Una **instrucción if** es una estructura de toma de decisiones que contiene una condición y un cuerpo de instrucciones. Si la condición es verdadera, se ejecuta el cuerpo. Si la condición es falsa, no se ejecuta el cuerpo.

El cuerpo de la instrucción `if` debe estar agrupado y tener un nivel de sangría. La guía de estilo PEP 8 recomienda cuatro espacios por nivel de sangría. El intérprete de Python producirá un error si el cuerpo está vacío.

**Video:** [Example: Quantity check](https://www.openstax.org/r/quantity-check)

**Uso de variables booleanas**

Una variable booleana ya tiene un valor de `True` o `False` y se puede usar directamente en una condición en lugar de usar el operador de igualdad. Ej.: `if is_raining == True:` se puede simplificar como `if is_raining:`.

**Conceptos en práctica: Uso de instrucciones if**

<!-- pregunta: CPL-ch04-m02-p01 -->

1. Dado el siguiente código, ¿qué parte es la condición?
   
   ```python norun
   if age < 12:
     print("Discount for children available")
   ```

   - a) `age`
   - b) `age < 12`
   - c) `print("Discount for children available")`

   <details><summary>Respuesta</summary>

   b) `age < 12` está entre `"if"` y `":"` y es una expresión que se evalúa como `True` o `False`.

   </details>

<!-- pregunta: CPL-ch04-m02-p02 -->

2. Dado el siguiente código, ¿qué líneas se ejecutan si la condición es verdadera?
   
   ```python norun
   print("Have a great day.")
   if is_raining:
     print("Don't forget an umbrella!")
   print("See you soon.")
   ```

   - a) 1, 2, 3
   - b) 1, 2, 4
   - c) 1, 2, 3, 4

   <details><summary>Respuesta</summary>

   c) El programa ejecuta el cuerpo cuando la condición es verdadera.

   </details>

<!-- pregunta: CPL-ch04-m02-p03 -->

3. Dado el siguiente código (igual que el anterior), ¿qué líneas se ejecutan si la condición es False?
   
   ```python norun
   print("Have a great day.")
   if is_raining:
     print("Don't forget an umbrella!")
   print("See you soon.")
   ```

   - a) 1, 2, 3
   - b) 1, 2, 4
   - c) 1, 2, 3, 4

   <details><summary>Respuesta</summary>

   b) El cuerpo, la línea 3, no se ejecuta porque la condición es falsa.

   </details>

<!-- pregunta: CPL-ch04-m02-p04 -->

4. Dado `num = -10`, ¿cuál es el valor final de `num`?
   
   ```python norun
   if num < 0:
     num = 25
   if num < 100:
     num = num + 50
   ```

   - a) `-10`
   - b) `40`
   - c) `75`

   <details><summary>Respuesta</summary>

   c) `-10 < 0` es verdadero, por lo que a `num` se le asigna `25`. Luego `25 < 100`, así que a `num` se le asigna `25 + 50`, que es `75`.

   </details>

<!-- pregunta: CPL-ch04-m02-p05 -->

5. Dada la entrada `10`, ¿cuál es el valor final de `positive_num`?
   
   ```python norun
   positive_num = int(input("Enter a positive number:"))
   if positive_num < 0:
     print("Negative input set to 0")
   positive_num = 0
   ```

   - a) `10`
   - b) `0`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) La línea 4 no tiene sangría, por lo que a `positive_num` siempre se le asigna `0`. El valor positivo de la entrada se pierde.

   </details>

### Instrucción if-else

Una instrucción `if` define las acciones que se realizan cuando una condición es verdadera. ¿Y si una acción debe realizarse solo cuando la condición es falsa? Ej.: si el restaurante está a menos de una milla, iremos caminando. Si no, iremos en auto.

Una **instrucción else** se usa junto con una instrucción `if` y contiene un cuerpo de instrucciones que se ejecuta cuando la condición de la instrucción `if` es falsa. Cuando se ejecuta una instrucción `if-else`, se toma una y solo una de las ramas. Es decir, se ejecuta el cuerpo del `if` o el cuerpo del `else`. Nota: la instrucción `else` está en el mismo nivel de sangría que la instrucción `if`, y el cuerpo tiene sangría.

Plantilla de la instrucción `if-else`:

```python norun
# Instrucciones previas

if condition:
  # Cuerpo
else:
  # Cuerpo

# Instrucciones posteriores
```

**Video:** [Example: Trivia question](https://www.openstax.org/r/trivia-question)

**Conceptos en práctica: Exploración de las instrucciones if-else**

<!-- pregunta: CPL-ch04-m02-p06 -->

1. Dado el siguiente código, ¿para qué rango de `x` se toma la rama `else`?
   
   ```python norun
   if x >= 15:
     # Hacer algo
   else:
     # Hacer algo distinto
   ```

   - a) `x >= 15`
   - b) `x <= 15`
   - c) `x < 15`

   <details><summary>Respuesta</summary>

   c) La rama `if` se toma cuando `x >= 15`, por lo que la rama `else` se toma cuando `x` no es mayor o igual que `15`.

   </details>

<!-- pregunta: CPL-ch04-m02-p07 -->

2. Dado `x = 40`, ¿cuál es el valor final de `y`?
   
   ```python norun
   if x > 30:
     y = x - 10
   else:
     y = x + 10
   ```

   - a) `30`
   - b) `40`
   - c) `50`

   <details><summary>Respuesta</summary>

   a) `40 > 30`, por lo que se ejecuta el cuerpo de la instrucción `if`. `y = 40 - 10 = 30`.

   </details>

<!-- pregunta: CPL-ch04-m02-p08 -->

3. Dado `y = 50`, ¿cuál *no* es un valor final posible de `y`?
   
   ```python norun
   if x < 50:
     y = y / 2
   else:
     y = y * 2
   y = y + 5
   ```

   - a) `30`
   - b) `55`
   - c) `105`

   <details><summary>Respuesta</summary>

   b) En una instrucción `if-else` siempre se toma una de las ramas. Según el valor de `x`, `y` tendrá un valor final de `30` o de `105`.

   </details>

**Pruébalo: División mejorada**

El siguiente programa divide dos enteros. La división entre 0 produce un error. Modifica el programa para que lea un nuevo denominador (sin indicador) si el denominador es 0.

<!-- coderunner: ch4/CodeRunner_04_03_03_Improved-division -->

**Pruébalo: Conversión de unidades de temperatura**

El siguiente programa lee una temperatura como un float y la unidad como una cadena: `"f"` para Fahrenheit o `"c"` para Celsius.

Calcula `new_temp`, el resultado de convertir `temp` de Fahrenheit a Celsius o de Celsius a Fahrenheit según `unit`. Calcula `new_unit`: `"c"` si `unit` es `"f"` y `"f"` si `unit` es `"c"`.

Fórmulas de conversión:

- Grados Celsius = (grados Fahrenheit - 32) * 5/9
- Grados Fahrenheit = (grados Celsius * 5/9) + 32

<!-- coderunner: ch4/CodeRunner_04_03_04_Converting-temperature-units -->

<!-- modulo: m00030 -->

## 4.3 Operaciones booleanas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar el propósito de los operadores lógicos.
- Describir las tablas de verdad de `and`, `or` y `not`.
- Crear expresiones con operadores lógicos.
- Interpretar instrucciones `if-else` con condiciones que usan operadores lógicos.

### Operador lógico: and

Las decisiones suelen basarse en varias condiciones. Ej.: un programa que imprime si un negocio está abierto puede comprobar que `hour >= 9` y `hour < 17`. Un **operador lógico** toma uno o más operandos de tipo condición y produce `True` o `False`.

Python tiene tres operadores lógicos: *and*, *or* y *not*. El operador **and** toma dos operandos de tipo condición y devuelve `True` si ambas condiciones son verdaderas.

**Tabla de verdad: p and q.**

| p | q | p and q |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

**Video:** [Example: Museum entry](https://www.openstax.org/r/museum-entry)

**Conceptos en práctica: Uso del operador and**

<!-- pregunta: CPL-ch04-m03-p01 -->

1. Considera el ejemplo anterior. Jaden intenta entrar cuando la capacidad es 2500 y faltan 2 horas para el cierre. ¿Puede entrar Jaden?

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   a) `2500 < 3000` es `True`, y `2.5 > 1.0` es `True`, por lo que Jaden puede entrar.

   </details>

<!-- pregunta: CPL-ch04-m03-p02 -->

2. Considera el ejemplo anterior. Darcy intenta entrar cuando la capacidad es 3000. ¿Para qué valores de `hrs_to_close` podrá entrar Darcy?

   - a) `hrs_to_close > 1.0`
   - b) ningún valor

   <details><summary>Respuesta</summary>

   b) `3000 > 3000` es `False`. `False and True` es `False`. `False and False` es `False`. Por lo tanto, ningún valor de `hrs_to_close` permitirá que Darcy entre.

   </details>

<!-- pregunta: CPL-ch04-m03-p03 -->

3. Dados `is_admin = False` y `is_online = True`, ¿cuál es el valor de `is_admin` y `is_online`?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) `False and True` es `False`.

   </details>

<!-- pregunta: CPL-ch04-m03-p04 -->

4. Dados `x = 8` y `y = 21`, ¿cuál es el valor final de `z`?
   
   ```python norun
   if (x < 10) and (y > 20):
     z = 5
   else:
     z = 0
   ```

   - a) `0`
   - b) `5`

   <details><summary>Respuesta</summary>

   b) `(8 < 10) and (21 > 20)` se evalúa como `True and True`, que es `True`. Por lo tanto, se ejecuta el cuerpo del `if` y a `z` se le asigna `5`.

   </details>

### Operador lógico: or

A veces una decisión solo requiere que una condición sea verdadera. Ej.: si un estudiante está en la banda o en el coro, se presentará en el concierto de primavera. El operador **or** toma dos operandos de tipo condición y devuelve `True` si alguna de las condiciones es `True`.

**Tabla de verdad: p or q.**

| p | q | p or q |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

**Video:** [Example: Streaming prompt](https://www.openstax.org/r/streaming-prompt)

**Conceptos en práctica: Uso del operador or**

<!-- pregunta: CPL-ch04-m03-p05 -->

1. Dados `days = 21` e `is_damaged` igual a `False`, ¿se procesa el reembolso?
   
   ```python norun
   if (days < 30) or is_damaged:
     # Procesar reembolso
   ```

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   a) `(21 < 30) or False` se evalúa como `True or False`, que es `True`.

   </details>

<!-- pregunta: CPL-ch04-m03-p06 -->

2. ¿Para qué valores de `age` no hay descuento?
   
   ```python norun
   if (age < 12) or (age > 65):
     # Aplicar descuento de estudiante/adulto mayor
   ```

   - a) `age >= 12`
   - b) `age <= 65`
   - c) `(age >= 12)` and `(age <= 65)`

   <details><summary>Respuesta</summary>

   c) El descuento no se aplica a las edades entre 12 y 65, ambas incluidas.

   </details>

<!-- pregunta: CPL-ch04-m03-p07 -->

3. Dados `a = 9` y `b = 10`, ¿pasa la prueba?
   
   ```python norun
   if (a%2 == 0 and b%2 == 1) or (a%2 == 1 and b%2 == 0):
     # Prueba superada
   else:
     # Prueba fallida
   ```

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   a) `(9%2==0 and 10%2 ==1)` se evalúa como `(False and False)`, que es `False`. `(9%2 == 1 and 10%2 == 0)` se evalúa como `(True and True)`, que es `True`. `False or True` es `True`. La instrucción `if` comprueba si los números forman un par par-impar o impar-par.

   </details>

### Operador lógico: not

Si la computadora no está encendida, presiona el botón de encendido. El operador **not** toma un operando de tipo condición y devuelve `True` cuando el operando es falso y `False` cuando el operando es verdadero.

*not* es un operador útil que hace más legible una condición y sirve para alternar el valor de un booleano. Ej.: `is_on = not is_on`.

**Tabla de verdad: not p.**

| p | not p |
|---|---|
| `True` | `False` |
| `False` | `True` |

**Video:** [Example: Diving warning](https://www.openstax.org/r/diving-warning)

**Conceptos en práctica: Uso del operador not**

<!-- pregunta: CPL-ch04-m03-p08 -->

1. Dado `x = 13`, ¿cuál es el valor de `not(x < 10)`?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) `not(13 < 10)` se evalúa como `not(False)`, que es `True`.

   </details>

<!-- pregunta: CPL-ch04-m03-p09 -->

2. Dado `x = 18`, ¿está `x` en el rango correcto?
   
   ```python norun
   if not(x > 15 and x < 20):
     # x está en el rango correcto
   ```

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   b) `not(18 > 15 and 18 < 20)` se evalúa como `not(True and True)`, luego `not(True)` y, finalmente, `False`.

   </details>

<!-- pregunta: CPL-ch04-m03-p10 -->

3. Dados `is_turn = False` y `timer = 65`, ¿cuál es el valor final de `is_turn`?
   
   ```python norun
   if timer > 60:
     is_turn = not is_turn
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) `65 > 60` es `True`, por lo que a `is_turn` se le asigna `not(False)`, que es `True`.

   </details>

**Pruébalo: Límites de velocidad**

Escribe un programa que lea la velocidad de un auto como un entero y compruebe si la velocidad del auto está dentro de los límites de la autopista. La velocidad de un auto debe ser de al menos 45 mph, pero no mayor que 70 mph en la autopista.

Si la velocidad está dentro de los límites, imprime `"Good driving"`. Si no, imprime `"Follow the speed limits"`.

<!-- coderunner: ch4/CodeRunner_04_04_05_Speed-limits -->

<!-- modulo: m00031 -->

## 4.4 Precedencia de operadores

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir cómo influye la precedencia en el orden de las operaciones.
- Describir cómo influye la asociatividad en el orden de las operaciones.
- Explicar el propósito de usar paréntesis en expresiones con varios operadores.

### Precedencia

Cuando una expresión tiene varios operadores, ¿cuál se evalúa primero? Las reglas de precedencia indican el nivel de prioridad de los operadores. Los operadores con mayor precedencia se ejecutan primero. Ej.: `1 + 2 * 3` es `7` porque la multiplicación tiene precedencia sobre la suma. Sin embargo, `(1 + 2) * 3` es `9` porque los paréntesis tienen precedencia sobre la multiplicación.

**Precedencia de operadores, de mayor a menor.**

| Operador | Significado |
|---|---|
| () | Paréntesis |
| ** | Exponenciación (asociativo por la derecha) |
| *, /, //, % | Multiplicación, división, división entera, módulo |
| +, - | Suma, resta |
| <, <=, >, >=, ==, != | Operadores de comparación |
| not | Operador lógico `not` |
| and | Operador lógico `and` |
| or | Operador lógico `or` |

**Video:** [Operator precedence](https://www.openstax.org/r/operator-precedence)

**Conceptos en práctica: Reglas de precedencia**

<!-- pregunta: CPL-ch04-m04-p01 -->

1. `x ** 2 + 6 / 3`

   - a) `6 / 3`
   - b) `x ** 2`
   - c) `2 + 6`

   <details><summary>Respuesta</summary>

   b) La exponenciación tiene la mayor precedencia, luego la división y después la suma.

   </details>

<!-- pregunta: CPL-ch04-m04-p02 -->

2. `not 3 * 5 > 10`

   - a) `3 * 5`
   - b) `not 3`
   - c) `5 > 10`

   <details><summary>Respuesta</summary>

   a) La multiplicación tiene la mayor precedencia, luego el operador mayor que y después not.

   </details>

<!-- pregunta: CPL-ch04-m04-p03 -->

3. `z == 5 and x / 8 < 100`

   - a) `5 and x`
   - b) `x / 8`
   - c) `8 < 100`

   <details><summary>Respuesta</summary>

   b) La división tiene la mayor precedencia, luego la igualdad y el menor que, y después `and`.

   </details>

### Asociatividad

¿Qué pasa si operadores contiguos tienen el mismo nivel de precedencia? La asociatividad determina el orden de las operaciones cuando la precedencia es la misma. Ej.: `8 / 4 * 3` se evalúa como `(8/4) * 3` y no como `8 / (4*3)`, porque la multiplicación y la división son asociativas por la izquierda. La mayoría de los operadores son asociativos por la izquierda y se evalúan de izquierda a derecha. La exponenciación es la excepción principal (indicada arriba) y es asociativa por la derecha; es decir, se evalúa de derecha a izquierda. Ej.: `2 ** 3 ** 4` se evalúa como `2 ** (3**4)`.

Cuando se encadenan operadores de comparación, la expresión se convierte en la combinación equivalente de comparaciones y se evalúa de izquierda a derecha. Ej.: `10 < x <= 20` se evalúa como `10 < x` y `x <= 20`.

**Video:** [Operation precedence](https://www.openstax.org/r/operation-precedence)

**Conceptos en práctica: Asociatividad**

<!-- pregunta: CPL-ch04-m04-p04 -->

1. `10 + 3 * 2 / 4`

   - a) `10 + (3 * (2 / 4))`
   - b) `10 + ((3 * 2) / 4)`
   - c) `(10 + 3) * (2 / 4)`

   <details><summary>Respuesta</summary>

   b) La multiplicación y la división tienen la mayor precedencia, son asociativas por la izquierda y tienen mayor precedencia que la suma.

   </details>

<!-- pregunta: CPL-ch04-m04-p05 -->

2. `2 * 2 ** 2 ** 3`

   - a) `2 * ((2 ** 2) ** 3)`
   - b) `2 * (2 ** (2 ** 3))`
   - c) `((2*2) ** 2) ** 3`

   <details><summary>Respuesta</summary>

   b) La exponenciación es asociativa por la derecha y tiene mayor precedencia que la multiplicación.

   </details>

<!-- pregunta: CPL-ch04-m04-p06 -->

3. `100 < x > 150`

   - a) `100 < x and x < 150`
   - b) `100 < x or x > 150`
   - c) `100 < x and x > 150`

   <details><summary>Respuesta</summary>

   c) La expresión es válida y se separa en comparaciones conectadas con `and`.

   </details>

### Cómo imponer el orden y la claridad con paréntesis

Las reglas de precedencia de operadores pueden ser difíciles de recordar. Los paréntesis no solo imponen un orden de operaciones distinto, sino que también reducen la confusión.

**Video:** [Using parentheses](https://www.openstax.org/r/using-parentheses)

**Conceptos en práctica: Uso de paréntesis**

<!-- pregunta: CPL-ch04-m04-p07 -->

1. Considera el ejemplo anterior. ¿Por qué el orden de evaluación fue distinto del que quería el programador?

   - a) La igualdad tiene precedencia sobre `and`.
   - b) Todos los operadores se evalúan de derecha a izquierda.
   - c) El orden es aleatorio cuando no se usan paréntesis.

   <details><summary>Respuesta</summary>

   a) El operador de igualdad, ==, tiene mayor precedencia que el `and` lógico.

   </details>

<!-- pregunta: CPL-ch04-m04-p08 -->

2. Dados `x = 8` y `y = 9`, ¿cuál es el resultado de lo siguiente?
    `x + 3 * y - 5`

   - a) `30`
   - b) `44`
   - c) `94`

   <details><summary>Respuesta</summary>

   a) La expresión se evalúa como `x + (3*y) - 5. 8 + (3*9) - 5 = 30`.

   </details>

<!-- pregunta: CPL-ch04-m04-p09 -->

3. Dados `x = 8` y `y = 9`, ¿cuál es el resultado de lo siguiente?
    `(x+3) * (y-5)`

   - a) `30`
   - b) `44`
   - c) `94`

   <details><summary>Respuesta</summary>

   b) Primero se evalúan las expresiones entre paréntesis. `(8+3) * (9-5) = 11 * 4 = 44`.

   </details>

**Recomendaciones de PEP 8: espaciado alrededor de los operadores**

La guía de estilo PEP 8 recomienda un espaciado uniforme alrededor de los operadores para evitar espacios en blanco superfluos y confusos.

- Evita los espacios múltiples y una cantidad desigual de espacios en blanco alrededor de operadores con dos operandos.  
Evita: `x= y * 44`  
Mejor: `x = y * 44`
- Evita los espacios inmediatamente dentro de los paréntesis.  
Evita: `x = ( 4 * y )`  
Mejor: `x = (4 * y)`
- Rodea con un espacio los siguientes operadores: asignación, asignación aumentada, comparación, booleanos.  
Evita: `x= y<44`  
Mejor: `x = y < 44`
- Considera agregar espacios alrededor de los operadores de menor precedencia.  
Evita: `x = 5 * z+20`  
Mejor: `x = 5*z + 20`

<!-- modulo: m00032 -->

## 4.5 Decisiones encadenadas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar las ramas que se toman en una instrucción `if-elif` e `if-elif-else`.
- Crear una instrucción de decisión encadenada para evaluar varias condiciones.

### elif

A veces una decisión complicada se basa en más de una condición. Ej.: un sitio de planificación de viajes revisa las escalas de un itinerario. Si una escala dura más de 24 horas, el sitio debería sugerir alojamiento. *Si no, si* la escala dura menos de una hora, el sitio debería alertar sobre una posible conexión perdida.

Dos instrucciones `if` separadas no garantizan que se tome solo una rama y podrían hacer que se tomen ambas. Ej.: el programa siguiente intenta agregar una bonificación según la calificación de un examen ingresada. Si la entrada es `60`, ambas instrucciones `if` se ejecutan de forma incorrecta y la calificación resultante es 75.

```python norun
score = int(input())
if score < 70:
  score += 10
# Incorrecto:
if 70 <= score < 85:
  score += 5
```

Encadenar instrucciones de decisión con `elif` permite al programador comprobar varias condiciones. Una instrucción **elif** (abreviatura de else if, «si no, si») comprueba una condición cuando la condición de la instrucción de decisión anterior es falsa. Una instrucción `elif` forma parte de una cadena y debe ir después de una instrucción `if` (o `elif`).

Plantilla de la instrucción `if-elif`:

```python norun
# Instrucciones previas

if condition:
  # Cuerpo
elif condition:
  # Cuerpo

# Instrucciones posteriores
```

**Video:** [Example: Livestream features](https://www.openstax.org/r/livestream)

**Conceptos en práctica: Uso de elif**

<!-- pregunta: CPL-ch04-m05-p01 -->

1. Completa el espacio en blanco para ejecutar `Cuerpo 2` cuando `condition_1` es falsa y `condition_2` es verdadera.
   
   ```python norun
   if condition_1:
     # Cuerpo 1
   __ condition_2:
     # Cuerpo 2
   ```

   - a) `if`
   - b) `elif`
   - c) `else`

   <details><summary>Respuesta</summary>

   b) `elif` evaluará `condition_2` si `condition_1` es `False` y ejecutará `Cuerpo 2` si `condition_2` es `True`.

   </details>

<!-- pregunta: CPL-ch04-m05-p02 -->

2. Dados `x = 42` e `y = 0`, ¿cuál es el valor final de `y`?
   
   ```python norun
   if x > 44:
     y += 2
   elif x < 50:
     y += 5
   ```

   - a) `2`
   - b) `5`
   - c) `7`

   <details><summary>Respuesta</summary>

   b) `x > 44`, `42 > 44`, es `False`, por lo que se evalúa `x < 50`. `42 < 50` es `True`, por lo que `y = 0 + 5`. Solo se toma una de las ramas `if` y `elif`.

   </details>

<!-- pregunta: CPL-ch04-m05-p03 -->

3. ¿Qué condiciones completan el código de modo que, si `x` es menor que 0, se ejecute `Cuerpo 1` y, si no, si `x` es igual a 0, se ejecute `Cuerpo 2`?
   
   ```python norun
   if _________:
     # Cuerpo 1
   elif _________:
     # Cuerpo 2
   ```

   - a) `x < 0`
      `x == 0`
   - b) `x == 0`
      `x < 0`
   - c) `x <= 0`
      [sin condición]

   <details><summary>Respuesta</summary>

   a) Si `x < 0`, se ejecuta `Cuerpo 1`. Si no, si `x == 0`, se ejecuta `Cuerpo 2`.

   </details>

<!-- pregunta: CPL-ch04-m05-p04 -->

4. ¿Cuál de las siguientes es una instrucción de decisión encadenada válida?

   - a)

     ```python norun
     if condition_1:
       # Cuerpo 1
     elif condition_2:
       # Cuerpo 2
     ```

   - b)

     ```python norun
     if condition_1:
       # Cuerpo 1
       elif condition_2:
         # Cuerpo 2
     ```

   - c)

     ```python norun
     elif condition_1:
       # Cuerpo 1
     if condition_2:
       # Cuerpo 2
     ```

   <details><summary>Respuesta</summary>

   a) El `elif` debe estar encadenado a una instrucción anterior y al mismo nivel de sangría.

   </details>

<!-- pregunta: CPL-ch04-m05-p05 -->

5. Dado `attendees = 350`, ¿cuál es el valor final de `rooms`?
   
   ```python norun
   rooms = 1
   if attendees >= 100:
     rooms += 3
   if attendees <= 200:
     rooms += 7
   elif attendees <= 400:
     rooms += 14
   ```

   - a) `4`
   - b) `15`
   - c) `18`

   <details><summary>Respuesta</summary>

   c) Las instrucciones `if` e `if-elif` no están encadenadas. El primer `if` se evalúa como `True` y se ejecuta. Luego se evalúa el `if-elif` y se ejecuta la rama `elif`.

   </details>

### Instrucciones if-elif-else

Los `elif` se pueden encadenar con una instrucción `if-else` para crear una instrucción de decisión más compleja. Ej.: un programa muestra los posibles movimientos de ajedrez según el tipo de pieza. Si la pieza es un peón, muestra el avance de una (o dos) casillas. Si no, si la pieza es un alfil, muestra los movimientos en diagonal. Si no, si . . . (termina con el resto de las piezas).

**Video:** [Example: Possible chess moves](https://www.openstax.org/r/chess-moves)

**Conceptos en práctica: Uso de elif dentro de instrucciones if-elif-else**

<!-- pregunta: CPL-ch04-m05-p06 -->

1. Dado `hour = 12`, ¿qué se imprime?
   
   ```python norun
   if hour < 8:
     print("Too early")
   elif hour < 12:
     print("Good morning")
   elif hour < 13:
     print("Lunchtime")
   elif hour < 17:
     print("Good afternoon")
   else:
     print("Too late")
   ```

   - a) `Good morning`
   - b) `Lunchtime`
   - c) `Good afternoon`
   - d) `Too late`

   <details><summary>Respuesta</summary>

   b) La tercera rama se ejecuta si `hour < 8 and hour < 12` es `False` y `hour < 13` es `True`.

   </details>

<!-- pregunta: CPL-ch04-m05-p07 -->

2. ¿Dónde se puede agregar una instrucción `elif`?
   
   ```python norun
   _1_
   if condition:
     # Cuerpo
     _2_
   elif condition:
     # Cuerpo
   _3_
   else:
     # Cuerpo
   _4_
   ```

   - a) 1
   - b) 2
   - c) 3
   - d) 4

   <details><summary>Respuesta</summary>

   c) Un `elif` se puede encadenar a otro `elif` para formar una decisión encadenada más larga.

   </details>

<!-- pregunta: CPL-ch04-m05-p08 -->

3. Dados `x = -1` e `y = -2`, ¿cuál es el valor final de `y`?
   
   ```python norun
   if x < 0 and y < 0:
     y = 10
   elif x < 0 and y > 0:
     y = 20
   else:
     y = 30
   ```

   - a) `10`
   - b) `20`
   - c) `30`

   <details><summary>Respuesta</summary>

   a) En una instrucción de decisión encadenada solo se ejecuta una rama. `-1 < 0 and -2 < 0` es `True`, por lo que `y = 10`.

   </details>

<!-- pregunta: CPL-ch04-m05-p09 -->

4. ¿Cómo se podrían reescribir las siguientes instrucciones como una instrucción encadenada?
   
   ```python norun
   if price < 9.99:
     order = 50
   if 9.99 <= price < 19.99:
     order = 30
   if price >= 19.99:
     order = 10
   ```

   - a)

     ```python norun
     if price < 9.99:
       order = 50
     else:
       order = 30
     order = 10
     ```

   - b)

     ```python norun
     if price < 9.99:
       order = 50
     elif price < 19.99:
       order = 30
     elif price == 19.99:
       order = 10
     ```

   - c)

     ```python norun
     if price < 9.99:
       order = 50
     elif price < 19.99:
       order = 30
     else:
       order = 10
     ```

   <details><summary>Respuesta</summary>

   c) La primera rama se ejecuta si `price < 9.99`. La segunda rama se ejecuta si `price < 19.99` y la primera condición falla; es decir, `price >= 9.99`. La tercera rama se ejecuta si fallan la primera y la segunda condición; es decir, `price >= 19.99`. Encadenar puede simplificar las instrucciones de decisión.

   </details>

**Pruébalo: Conversión de tamaños de ganchillo**

Escribe un programa que lea el tamaño estadounidense de un ganchillo y calcule el diámetro métrico en milímetros. (Se usa un subconjunto de tamaños). Si la entrada no coincide con B-G, se debe asignar -1.0 al diámetro. Ej.: si la entrada es `D`, la salida es `"3.25 mm"`.

Conversiones de tamaño estadounidense: mm

- B : 2.25
- C : 2.75
- D : 3.25
- E : 3.5
- F : 3.75
- G : 4.0

<!-- coderunner: ch4/CodeRunner_04_06_06_Crochet-hook-size-conversion -->

**Pruébalo: Longitudes de onda de los colores**

Escribe un programa que lea un entero que represente una longitud de onda de luz visible en nanómetros. Imprime el color correspondiente usando los siguientes rangos inclusivos:

- Violet: 380–449
- Blue: 450–484
- Cyan: 485–499
- Green: 500–564
- Yellow: 565–589
- Orange: 590–624
- Red: 625–750

Supón que la entrada está dentro del espectro de luz visible, de 380 a 750 inclusive.

Dada la entrada:

```text
550
```

La salida es:

```text
Green
```

<!-- coderunner: ch4/CodeRunner_04_06_07_Color-wavelengths -->

<!-- modulo: m00033 -->

## 4.6 Decisiones anidadas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir las rutas de ejecución de programas con instrucciones `if-else` anidadas.
- Implementar un programa con instrucciones `if-else` anidadas.

### Instrucciones de decisión anidadas

Supón que un programador está escribiendo un programa que lee el ID de un juego y la cantidad de jugadores, e imprime si el usuario tiene la cantidad correcta de jugadores para el juego.

El programador puede comenzar con lo siguiente:

```python norun
if game == 1 and players < 2:
  print("Not enough players")
if game == 1 and players > 4:
  print("Too many players")
if game == 1 and (2 <= players <= 4):
  print("Ready to start")
if game == 2 and players < 3:
  print("Not enough players")
if game == 2 and players > 6:
  print("Too many players")
if game == 2 and (3 <= players <= 6):
  print("Ready to start")
```

El programador se da cuenta de que el código es redundante. ¿Y si pudiera decidir primero el ID del juego y luego tomar una decisión sobre los jugadores? El anidamiento permite que una instrucción de decisión esté dentro de otra instrucción de decisión, y se indica con un nivel de sangría.

Un programa mejorado:

```python norun
if game == 1:
  if players < 2:
    print("Not enough players")
  elif players > 4:
    print("Too many players")
  else:
    print("Ready to start")
if game == 2:
  if players < 3:
    print("Not enough players")
  elif players > 6:
    print("Too many players")
  else:
    print("Ready to start")
# Probar los ID de juego del 3 en adelante
```

**Video:** [Example: Poisonous plant identification](https://www.openstax.org/r/plant-identification)

**Conceptos en práctica: Uso de instrucciones if-else anidadas**

<!-- pregunta: CPL-ch04-m06-p01 -->

1. Considera el ejemplo anterior. Dados `leaf_count = 9` y `leaf_shape = "teardrop"`, ¿cuál es la salida?

   - a) `Might be poison ivy`
   - b) `Might be poison oak`
   - c) `Might be poison sumac`

   <details><summary>Respuesta</summary>

   c) `leaf_count == 3` es `False`, por lo que se ejecuta el cuerpo del `else` externo.

   </details>

<!-- pregunta: CPL-ch04-m06-p02 -->

2. Dado `num_dancers = 49`, ¿qué se imprime?
   
   ```python norun
   if num_dancers < 0:
     print("Error: num_dancers is negative")
   else:
     if num_dancers % 2 == 1:
       print("Error: num_dancers is odd")
     print(num_dancers, "dancers")
   ```

   - a) `Error: num_dancers is odd`
   - b) `49 dancers`
   - c) `Error: num_dancers is odd`
     `49 dancers`

   <details><summary>Respuesta</summary>

   c) `num_dancers` es positivo, por lo que se toma la rama `else`. `num_dancers` es impar, por lo que se imprime el error antes de que el programa continúe después del `if` anidado e imprima `num_dancers`.

   </details>

<!-- pregunta: CPL-ch04-m06-p03 -->

3. Dados `x = 256`, `y = 513` y `max = 512`, ¿cuál de las siguientes opciones se ejecutará?
   
   ```python norun
   if x == y:
     # Cuerpo 1
   elif x < y:
     # Cuerpo 2
     if y >= max:
       # Cuerpo 3
     else:
       # Cuerpo 4
   else:
     # Cuerpo 5
   ```

   - a) `Cuerpo 2`
   - b) `Cuerpo 2`, `Cuerpo 3`
   - c) `Cuerpo 2`, `Cuerpo 5`

   <details><summary>Respuesta</summary>

   b) `256 == 513` es `False` y `256 < 513` es `True`, por lo que se toma la rama `elif` y se ejecuta `Cuerpo 2`. `513 >= 512` es `True`, por lo que se ejecuta `Cuerpo 3`.

   </details>

<!-- pregunta: CPL-ch04-m06-p04 -->

4. Dados `x = 118`, `y = 300` y `max = 512`, ¿cuál de las siguientes opciones se ejecutará?
   
   ```python norun
   if x == y:
     # Cuerpo 1
   elif x < y:
     # Cuerpo 2
     if y >= max:
       # Cuerpo 3
   else:
     # Cuerpo 4
   else:
     # Cuerpo 5
   ```

   - a) `Cuerpo 2`
   - b) `Cuerpo 3`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) El primer `else` no tiene sangría y se trata como el `else` del `if` original. Por lo tanto, el segundo `else` no está conectado a ninguna instrucción `if` y produce un error.

   </details>

**Pruébalo: Pedidos de comida**

Escribe un programa que lea una cadena, `"lunch"` o `"dinner"`, que represente la elección del menú, y un entero, `1`, `2` o `3`, que represente la elección de comida del usuario. Luego, el programa imprime la elección de comida del usuario.

Opciones de comida para el almuerzo

- 1: Ensalada César
- 2: Wrap de pollo picante
- 3: Sopa de calabaza

Opciones de comida para la cena

- 1: Salmón al horno
- 2: Hamburguesa de pavo
- 3: Risotto de champiñones

Ej.: si la entrada es:

```text
lunch

    3
```

La salida es:  
`Your order: Butternut squash soup`

<!-- coderunner: ch4/CodeRunner_04_07_07_Programming-practice_-Meal-orders -->

<!-- modulo: m00034 -->

## 4.7 Expresiones condicionales

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar los componentes de una expresión condicional.
- Crear una expresión condicional.

### Expresiones condicionales

Una **expresión condicional** (también conocida como «operador ternario») es una versión simplificada, en una sola línea, de una instrucción `if-else`.

Plantilla de la expresión condicional:

```python norun
expression_if_true if condition else expression_if_false
```

Una expresión condicional se evalúa comprobando primero la condición. Si `condition` es verdadera, se evalúa `expression_if_true`, y el resultado es el valor de la expresión condicional. Si no, se evalúa `expression_if_false`, y el resultado es el valor de la expresión condicional.

A una variable se le puede asignar una expresión condicional. Ej.: el máximo de dos números se puede calcular con `max_num = y if x < y else x`

Nota: las expresiones condicionales tienen la precedencia más baja de todas las operaciones de Python.

**Video:** [Example: Version check](https://www.openstax.org/r/version-check)

**Conceptos en práctica: Uso de expresiones condicionales**

<!-- pregunta: CPL-ch04-m07-p01 -->

1. ¿Cuál es la versión con expresión condicional de la siguiente instrucción `if-else`?
   
   ```python norun
   if x%2 == 0:
     response = 'even'
   else:
     response = 'odd'
   ```

   - a) `response = if x%2 == 0 "even" else "odd"`
   - b) `response = "odd" if x%2 == 0 else "even"`
   - c) `response = "even" if x%2 == 0 else "odd"`

   <details><summary>Respuesta</summary>

   c) La expresión condicional le asignará `"even"` a `response` si `x` es par. A `response` se le asigna `"odd"` si `x` es impar.

   </details>

<!-- pregunta: CPL-ch04-m07-p02 -->

2. Dados `x = 100` y `offset = 10`, ¿cuál es el valor de `result`?
   
   ```python norun
   result = x + offset if x < 100 else x - offset
   ```

   - a) `90`
   - b) `100`
   - c) `110`

   <details><summary>Respuesta</summary>

   a) `100 < 100` es `False`, por lo que a `result` se le asigna `x - offset = 100 - 10 = 90`.

   </details>

<!-- pregunta: CPL-ch04-m07-p03 -->

3. ¿Qué parte de la expresión condicional es incorrecta?
   
   ```python norun
   min_num = x if x < y else min_num = y
   ```

   - a) `min_num = x`
   - b) `x < y`
   - c) `min_num = y`

   <details><summary>Respuesta</summary>

   c) No se puede asignar `min_num = y` allí. La expresión correcta es `min_num = x if x < y else y`

   </details>

<!-- pregunta: CPL-ch04-m07-p04 -->

4. ¿Cuál de las siguientes es una versión mejorada de la siguiente instrucción `if-else`?
   
   ```python norun
   if x < 50:
     result = True
   else:
     result = False
   ```

   - a) `result = True if x < 50 else False`
   - b) `result = x < 50`

   <details><summary>Respuesta</summary>

   b) Las expresiones condicionales que se evalúan como un booleano son redundantes. En su lugar se debe usar la expresión booleana.

   </details>

<!-- pregunta: CPL-ch04-m07-p05 -->

5. ¿Cuáles son los valores posibles de `total`?
   
   ```python norun
   total = fee + 10 if hours > 12 else 2
   ```

   - a) `10`, `2`
   - b) `fee + 10`, `2`
   - c) `fee + 10`, `fee + 2`

   <details><summary>Respuesta</summary>

   b) La expresión se evalúa como `(fee + 10) if hours > 12 else 2`. Por lo tanto, si `hours > 12`, el resultado será `fee + 10`; de lo contrario, el resultado será `2`.

   </details>

**Pruébalo: Valores de ping**

Escribe un programa que lea un entero, `ping`, e imprima `ping_report`, una cadena que indique si el ping es de bajo a promedio o demasiado alto. Los valores de `ping` menores que 150 tienen un `ping_report` de `"low to average"`. Los valores de `ping` de 150 o más tienen un `ping_report` de `"too high"`. Usa una expresión condicional para asignar `ping_report`.

Ej.: si la entrada es `30`, la salida es `"Ping is low to average"`.

<!-- coderunner: ch4/CodeRunner_04_08_08_Ping-values -->

<!-- modulo: m00035 -->

## Resumen del capítulo

Los puntos principales de este capítulo son:

- Los booleanos representan un valor de `True` o `False`.
- Los operadores de comparación comparan valores y producen `True` o `False`.
- Los operadores lógicos toman uno o más operandos de tipo condición y producen `True` o `False`.
- Los operadores se evalúan en orden según su precedencia y asociatividad.
- Las condiciones son expresiones que se evalúan como `True` o `False`.
- Las instrucciones de decisión permiten distintos caminos de ejecución (ramas) en el código según las condiciones.
- Las instrucciones de decisión se pueden anidar dentro de otras instrucciones de decisión.
- Las expresiones condicionales son versiones en una sola línea de las instrucciones `if-else`.

En este punto, deberías poder escribir programas que evalúen condiciones y ejecuten instrucciones de código en consecuencia, con el orden correcto de las operaciones. La práctica de programación siguiente reúne la mayoría de los temas presentados en el capítulo.

**Referencia del capítulo 4.**

| Función | Descripción |
|---|---|
| `bool(x)` | Convierte `x` en un valor booleano, `True` o `False`. |
| **Operador** | **Descripción** |
| `x == y`  <br>(Igualdad) | Compara los valores de `x` e `y` y devuelve `True` si los valores son iguales y `False` en caso contrario. Ej.: `10 == 10` es `True`. |
| `x != y`  <br>(Desigualdad) | Compara los valores de `x` e `y` y devuelve `True` si los valores son distintos y `False` en caso contrario. Ej.: `7 != 4` es `True`. |
| `x > y`  <br>(Mayor que) | Compara los valores de `x` e `y` y devuelve `True` si `x` es mayor que `y` y `False` en caso contrario. Ej.: `9 > 3` es `True`. |
| `x < y`  <br>(Menor que) | Compara los valores de `x` e `y` y devuelve `True` si `x` es menor que `y` y `False` en caso contrario. Ej.: `9 < 8` es `False`. |
| `x >= y`  <br>(Mayor o igual que) | Compara los valores de `x` e `y` y devuelve `True` si `x` es mayor o igual que `y` y `False` en caso contrario. Ej.: `2 >= 2` es `True`. |
| `x <= y`  <br>(Menor o igual que) | Compara los valores de `x` e `y` y devuelve `True` si `x` es menor o igual que `y` y `False` en caso contrario. Ej.: `8 <= 7` es `False`. |
| `x and y`  <br>(Lógico) | Evalúa los valores booleanos de `x` e `y` y devuelve `True` si ambos son verdaderos. Ej.: `True and False` es `False`. |
| `x or y`  <br>(Lógico) | Evalúa los valores booleanos de `x` e `y` y devuelve `True` si alguno es verdadero. Ej.: `True or False` es `True`. |
| `not x`  <br>(Lógico) | Evalúa el valor booleano de `x` y devuelve `True` si el valor es falso y `False` si el valor es verdadero. Ej.: `not True` es `False`. |
| **Instrucción de decisión** | **Descripción** |
| Instrucción `if` | ```python<br># Instrucciones previas<br><br>if condition:<br>  # Cuerpo<br><br># Instrucciones posteriores<br>``` |
| Instrucción `else` | ```python<br># Instrucciones previas<br><br>if condition:<br>  # Cuerpo<br>else:<br>  # Cuerpo<br><br># Instrucciones posteriores<br>``` |
| Instrucción `elif` | ```python<br># Instrucciones previas<br><br>if condition:<br>  # Cuerpo<br>elif condition:<br>  # Cuerpo<br>else:<br>  # Cuerpo<br><br># Instrucciones posteriores<br>``` |
| Instrucción `if` anidada | ```python<br># Instrucciones previas<br><br>if condition:<br>  if condition:<br>    # Cuerpo<br>  else:<br>    # Cuerpo<br>else:<br>  if condition:<br>    # Cuerpo<br>  else:<br>    # Cuerpo<br><br># Instrucciones posteriores<br>``` |
| **Expresión condicional** | `expression_if_true if condition else expression_if_false` |
