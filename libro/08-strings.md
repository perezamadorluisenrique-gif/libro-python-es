# Capítulo 8: Cadenas

<!-- modulo: m00058 -->

## Introducción

![Unas fichas sujetas con un hilo, con caracteres escritos en ellas, que forman la palabra «Illuminate»](media/Python_08_00_000.jpg)

*crédito: modificación de la obra «Project 366 #65: 050316 A Night On The Tiles», de Pete/Flickr, CC BY 2.0*

Una **cadena** es una secuencia de caracteres. Python ofrece métodos útiles para procesar valores de cadena. En este capítulo se mostrarán métodos de cadenas que permiten comparar valores de cadena, rebanar cadenas, buscar, probar, formatear y modificar.

<!-- modulo: m00059 -->

## 8.1 Operaciones con cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Comparar cadenas con operadores lógicos y de pertenencia.
- Usar los métodos de cadena `lower()` y `upper()` para convertir valores de cadena a caracteres en minúscula y en mayúscula.

### Comparación de cadenas

Los valores de cadena se pueden comparar con operadores lógicos (`<`, `<=`, `>`, `>=`, `==`, `!=`) y operadores de pertenencia (`in` y `not in`). Al comparar dos valores de cadena, se comparan secuencialmente los caracteres correspondientes de ambos valores hasta llegar a una decisión. Para comparar dos caracteres, se usan sus valores ASCII al aplicar los operadores lógicos.

**Comparación de valores de cadena.**

| Operador | Descripción | Ejemplo | Salida | Explicación |
|---|---|---|---|---|
| `>` o `>=` | Comprueba si el primer valor de cadena es mayor que (o mayor o igual que) el segundo valor de cadena. | `"c" > "d"` | `False` | Al comparar el operando `"c"` con el operando `"d"`, el valor ASCII de `"c"` es menor que el valor ASCII de `"d"`. Por lo tanto, `"c" < "d"`. La expresión `"c" > "d"` se evalúa como False. |
| `<` o `<=` | Comprueba si el primer valor de cadena es menor que (o menor o igual que) el segundo valor de cadena. | `"ab" < "ac"` | `True` | Al comparar el operando `"ab"` con el operando `"ac"`, los primeros caracteres son iguales, pero el segundo carácter de `"ab"` es menor que el segundo carácter de `"ac"`, por lo que `"ab" < "ac"`. |
| `==` | Comprueba si dos valores de cadena son iguales. | `"aa" == "aa"` | `True` | Como todos los caracteres del primer operando y del segundo operando son iguales, los dos valores de cadena son iguales. |
| `!=` | Comprueba si dos valores de cadena no son iguales. | `"a" != "b"` | `True` | Los dos operandos contienen valores de cadena distintos (`"a"` frente a `"b"`), y el resultado de comprobar si no son iguales se evalúa como True. |
| `in` | Comprueba si el segundo operando contiene al primer operando. | `"a" in "bc"` | `False` | Como la cadena `"bc"` no contiene la cadena `"a"`, la salida de `"a" in "bc"` se evalúa como False. |
| `not in` | Comprueba si el segundo operando no contiene al primer operando. | `"a" not in "bc"` | `True` | Como la cadena `"bc"` no contiene la cadena `"a"`, la salida de `"a" not in "bc"` se evalúa como True. |

**Conceptos en práctica: Usar operadores lógicos y de pertenencia para comparar valores de cadena**

<!-- pregunta: CPL-ch08-m01-p01 -->

1. ¿Cuál es la salida de (`"aaa" < "aab"`)?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) Como el valor ASCII de `a` es menor que el valor ASCII de `b`, la salida de `"aaa" < "aab"` es True.

   </details>

<!-- pregunta: CPL-ch08-m01-p02 -->

2. ¿Cuál es la salida de (`"aa" < "a"`)?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) Como `"a"` es más corta que `"aa"`, y el prefijo de longitud 1 de `"aa"`, que es `"a"`, es igual al segundo operando (`"a"`), la cadena más corta se considera menor. Por lo tanto, `"aa" < "a"` se evalúa como False.

   </details>

<!-- pregunta: CPL-ch08-m01-p03 -->

3. ¿Cuál es la salida de (`"aples" in "apples"`)?

   - a) `undefined`
   - b) `True`
   - c) `False`

   <details><summary>Respuesta</summary>

   b) Aunque todos los caracteres de `"aples"` existen en `"apples"`, no aparecen de forma consecutiva, por lo que la cadena `"aples"` no es una subcadena de `"apples"`. Por lo tanto, `"aples"` in `"apples"` devuelve False.

   </details>

### lower() y upper()

Python tiene muchos métodos útiles para modificar cadenas, dos de los cuales son los métodos `lower()` y `upper()`. El método **lower()** devuelve los caracteres alfabéticos convertidos a minúscula, y el método **upper()** devuelve los caracteres alfabéticos convertidos a mayúscula. Ni `lower()` ni `upper()` modifican la cadena.

**Ejemplo: Convertir los caracteres de una cadena**

En el siguiente ejemplo, se llama a los métodos de cadena `lower()` y `upper()` sobre la variable de cadena `x` para convertir todos los caracteres a minúscula y a mayúscula, respectivamente.

```python
x = "Apples"

# El método lower() convierte una cadena a caracteres en minúscula
print(x.lower())

# El método upper() convierte una cadena a caracteres en mayúscula
print(x.upper())
```

La salida del código anterior es:

```salida
apples
APPLES
```

**Conceptos en práctica: Usar lower() y upper()**

<!-- pregunta: CPL-ch08-m01-p04 -->

1. ¿Cuál es la salida de `"aBbA".lower()`?

   - a) `abba`
   - b) `ABBA`
   - c) `abbA`

   <details><summary>Respuesta</summary>

   a) `"aBbA".lower()` convierte todos los caracteres a minúscula, y la salida es `"abba"`.

   </details>

<!-- pregunta: CPL-ch08-m01-p05 -->

2. ¿Cuál es la salida de `"aBbA".upper()`?

   - a) `abba`
   - b) `ABBA`
   - c) `ABbA`
   - d) `aBBA`

   <details><summary>Respuesta</summary>

   b) `"aBbA".upper()` convierte todos los caracteres a mayúscula, y la salida es `"ABBA"`.

   </details>

<!-- pregunta: CPL-ch08-m01-p06 -->

3. ¿Cuál es la salida de (`"a".upper() == "A"`)?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) `upper()` convierte `"a"` a mayúscula (`"A"`). Al comprobar `"a".upper() == "A"`, la salida es True.

   </details>

**Pruébalo: Número de caracteres de la cadena**

Se define una variable de cadena, `s_input`. Usa `lower()` y `upper()` para convertir la cadena a minúscula y a mayúscula, e imprime los resultados en la salida. Imprime también el número de caracteres de la cadena, incluidos los espacios.

<!-- coderunner: ch8/CodeRunner_08_02_01_Number-of-characters-in-the-string -->

**Pruébalo: ¿Cuál es mi carácter?**

Dada la cadena `s_input`, que es un objeto de cadena de un solo carácter, si el carácter está entre `"a"` y `"t"` o entre `"A"` y `"T"`, imprime `True`. De lo contrario, imprime `False`.  
Pista: Puedes convertir `s_input` a minúscula y comprobar si `s_input` está entre `"a"` y `"t"`.

<!-- coderunner: ch8/CodeRunner_08_02_02_What-is-my-character_ -->

<!-- modulo: m00060 -->

## 8.2 Rebanado de cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar la indexación de cadenas para acceder a los caracteres de la cadena.
- Usar el rebanado de cadenas para obtener una subcadena de una cadena.
- Identificar las características de inmutabilidad de las cadenas.

### Indexación de cadenas

Una cadena es un tipo de secuencia. Una cadena está formada por una secuencia de caracteres indexados de izquierda a derecha, comenzando en 0. Para una variable de cadena `s`, el carácter más a la izquierda tiene el índice 0 y el carácter más a la derecha tiene el índice `len(s) - 1`. Ej.: La longitud de la cadena `"Cloud"` es 5, por lo que el último índice es 4.

También se puede usar la indexación negativa para referirse a los caracteres de derecha a izquierda, comenzando en -1. Para una variable de cadena `s`, el carácter más a la izquierda tiene el índice `-len(s)` y el carácter más a la derecha tiene el índice -1. Ej.: La longitud de la cadena `"flower"` es 6, por lo que el índice del primer carácter con indexación negativa es -6.

**Video:** [String indexing](https://www.openstax.org/r/string-indexing)

**Conceptos en práctica: Acceder a los caracteres de una cadena mediante indexación**

<!-- pregunta: CPL-ch08-m02-p01 -->

1. ¿Qué carácter está en el índice 1 de la cadena `"hello"`?

   - a) `"h"`
   - b) `"e"`
   - c) `"o"`

   <details><summary>Respuesta</summary>

   b) Como la indexación comienza en 0, el carácter en el índice 1 es el segundo carácter de la cadena, que es `"e"`.

   </details>

<!-- pregunta: CPL-ch08-m02-p02 -->

2. ¿Cuál es el carácter en el índice -2 de la cadena `"Blue"`?

   - a) `"e"`
   - b) `"u"`
   - c) `"l"`

   <details><summary>Respuesta</summary>

   b) Como la indexación negativa comienza en -1 desde el extremo derecho de la cadena hacia la izquierda, `"u"` está en el índice -2.

   </details>

<!-- pregunta: CPL-ch08-m02-p03 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   word = "chance"
   print(word[-1] == word[5])
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) El carácter `"e"` de la cadena `"chance"` tiene el índice -1 (indexación negativa) y 5 (indexación positiva).

   </details>

### Rebanado de cadenas

El **rebanado de cadenas** se usa cuando un programador necesita acceder a una secuencia de caracteres. Para ello se puede usar un operador de rebanado. Cuando se usa `[a:b]` con el nombre de una variable de cadena, se devuelve la secuencia de caracteres que comienza en el índice `a` (inclusive) y llega hasta el índice `b` (exclusive). Tanto `a` como `b` son opcionales. Si no se proporciona `a` o `b`, los valores predeterminados son 0 y `len(string)`, respectivamente.

**Ejemplo: Obtener los minutos**

Considera un valor de hora dado como `"hh:mm"`, donde `"hh"` representa la hora y `"mm"` representa los minutos. Para obtener solo la parte de los minutos de la cadena, se puede usar el siguiente código:

```python
time_string = "13:46"
minutes = time_string[3:5]
print(minutes)
```

La salida del código anterior es:

```salida
46
```

**Ejemplo: Obtener la hora**

Considera un valor de hora dado como `"hh:mm"`, donde `"hh"` representa la hora y `"mm"` representa los minutos. Para obtener solo la parte de la hora de la cadena, se puede usar el siguiente código:

```python
time_string = "14:50"
hour = time_string[:2]
print(hour)
```

La salida del código anterior es:

```salida
14
```

**Conceptos en práctica: Obtener una subcadena mediante el rebanado de cadenas**

<!-- pregunta: CPL-ch08-m02-p04 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   a_string = "Hello world"
   print(a_string[2:4])
   ```

   - a) `"el"`
   - b) `"ll"`
   - c) `"llo"`

   <details><summary>Respuesta</summary>

   b) `a_string[2:4]` es un rebanado que incluye el tercer y el cuarto carácter, que es `"ll"`.

   </details>

<!-- pregunta: CPL-ch08-m02-p05 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   location = "classroom"
   print(location[-3:-1])
   ```

   - a) `"ro"`
   - b) `"oo"`
   - c) `"oom"`

   <details><summary>Respuesta</summary>

   b) El rebanado `[-3:-1]` incluye los caracteres de los índices -3 y -2, que son `"oo"`.

   </details>

<!-- pregunta: CPL-ch08-m02-p06 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   greeting = "hi Leila"
   name = greeting[3:]
   ```

   - a) `" Leila"`
   - b) `"Leila"`
   - c) `"ila"`

   <details><summary>Respuesta</summary>

   b) El rebanado de cadena `greeting[3:]` es la subcadena que comienza en el índice 3 y llega hasta el final de la cadena, que es `"Leila"`.

   </details>

### Inmutabilidad de las cadenas

Los objetos de cadena son **inmutables**, es decir, no se pueden modificar ni cambiar una vez creados. Una vez creado un objeto de cadena, su contenido no se puede alterar modificando directamente caracteres o elementos individuales de la cadena. En su lugar, para hacer cambios en una cadena, se crea un nuevo objeto de cadena con los cambios deseados, y la cadena original queda sin modificar.

**Video:** [Strings are immutable](https://www.openstax.org/r/strings-are-immutable)

**Conceptos en práctica: Modificar el contenido de una cadena**

<!-- pregunta: CPL-ch08-m02-p07 -->

1. ¿Cuál es la forma correcta de reemplazar el primer carácter de una cadena por el carácter «*» en una nueva cadena?

   - a)

     ```python norun
     x = "string"
     x[0] = "*"
     ```

   - b)

     ```python
     x = "string"
     x = "*" + x[1:]
     ```

   - c)

     ```python
     x = "string"
     x = "*" + x
     ```

   <details><summary>Respuesta</summary>

   b) Para modificar el contenido de una cadena, se debe crear una nueva variable con las modificaciones deseadas.

   </details>

<!-- pregunta: CPL-ch08-m02-p08 -->

2. ¿Qué tipo de error resultará del siguiente código?
   
   ```python norun
   string_variable = "example"
   string_variable[-1] = ""
   ```

   - a) `TypeError`
   - b) `IndexError`
   - c) `NameError`

   <details><summary>Respuesta</summary>

   a) Intentar asignar un valor a un índice o a un rango de índices de una cadena produce `TypeError: 'str' object does not support item assignment`.

   </details>

<!-- pregunta: CPL-ch08-m02-p09 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   str = "morning"
   str = str[1]
   print(str)
   ```

   - a) `TypeError`
   - b) `m`
   - c) `o`

   <details><summary>Respuesta</summary>

   c) El carácter en el índice 1, `"o"`, reemplaza el contenido de la variable `str`. Por lo tanto, la instrucción print imprime `"o"`.

   </details>

**Pruébalo: Cambiar el mensaje de saludo**

Dada la cadena `"Hello my fellow        classmates"`, que contiene un mensaje de saludo, imprime la primera palabra obteniendo el comienzo de la cadena hasta el quinto carácter (inclusive). Cambia la primera palabra de la cadena por `"Hi"` en lugar de `"hello"` e imprime de nuevo el mensaje de saludo.

<!-- coderunner: ch8/CodeRunner_08_03_03_Changing-the-greeting-message -->

**Pruébalo: Editar la cadena en posiciones específicas**

Dada una variable de cadena, `string_variable`, y una lista de índices, elimina los caracteres de los índices especificados e imprime la cadena resultante.

```python norun
Input:
string_variable = "great"
indices = [0, 1]
```

```text
Prints:
eat
```

<!-- coderunner: ch8/CodeRunner_08_03_04_Editing-the-string-at-specified-locations -->

<!-- modulo: m00061 -->

## 8.3 Búsqueda y prueba de cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar el operador `in` para identificar si una cadena dada contiene una subcadena.
- Llamar al método `count()` para contar el número de subcadenas en una cadena dada.
- Buscar una subcadena en una cadena mediante el método `find()`.
- Usar el método `index()` para encontrar el índice de la primera aparición de una subcadena en una cadena dada.
- Escribir un bucle for sobre cadenas usando el operador in.

### Operador in

El operador booleano **in** se puede usar para comprobar si una cadena contiene otra cadena. `in` devuelve `True` si la primera cadena existe en la segunda cadena y `False` en caso contrario.

**Video:** [What is in the phrase?](https://www.openstax.org/r/what-in-phrase)

**Conceptos en práctica: Usar el operador in para encontrar subcadenas**

<!-- pregunta: CPL-ch08-m03-p01 -->

1. ¿Cuál es la salida de (`"a" in "an umbrella"`)?

   - a) `2`
   - b) `False`
   - c) `True`
   - d) `1`

   <details><summary>Respuesta</summary>

   c) Como `"a"` es una subcadena de `"an umbrella"`, la salida de `"a"` in `"an umbrella"` es `True`.

   </details>

<!-- pregunta: CPL-ch08-m03-p02 -->

2. ¿Cuál es la salida de (`"ab" in "arbitrary"`)?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) `"ab"` no es una subcadena de `"arbitrary"`; por lo tanto, la salida es `False`.

   </details>

<!-- pregunta: CPL-ch08-m03-p03 -->

3. ¿Cuál es la salida de (`"" in "string"`)?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) Como `""` es una subcadena de longitud 0 de `"string"`, la salida es `True`.

   </details>

### Bucle for con el operador in

El operador `in` se puede usar para iterar sobre los caracteres de una cadena mediante un bucle `for`. En cada iteración del bucle `for` se lee un carácter, que será la variable del bucle en esa iteración.

**Video:** [for loop using in operator](https://www.openstax.org/r/for-loop-in-operator)

**Conceptos en práctica: Usar el operador in dentro de un bucle for**

<!-- pregunta: CPL-ch08-m03-p04 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   for c in "string":
     print(c, end = "")
   ```

   - a)

     ```python norun
     string
     ```

   - b)

     ```python norun
     s
     t
     r
     i
     n
     g
     ```

   - c)

     ```python norun
     s t r i n g
     ```

   <details><summary>Respuesta</summary>

   a) El bucle `for` recorre los caracteres de `"string"` e imprime todos los caracteres sin ningún carácter separador.

   </details>

<!-- pregunta: CPL-ch08-m03-p05 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   count = 0
   for c in "abca":
     if c == "a":
       count += 1
   print(count)
   ```

   - a) `0`
   - b) `1`
   - c) `2`

   <details><summary>Respuesta</summary>

   c) El código dado itera sobre los caracteres de la cadena `"abca"`, y cada vez que se encuentra el carácter `"a"`, una variable contador aumenta en 1. Como `"a"` aparece dos veces en `"abca"`, la salida será `2`.

   </details>

<!-- pregunta: CPL-ch08-m03-p06 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   word = "cab"
   for i in word:
     if i == "a":
       print("A", end = "")
     if i == "b":
       print("B", end = "")
     if i == "c":
       print("C", end = "")
   ```

   - a) `cab`
   - b) `abc`
   - c) `CAB`
   - d) `ABC`

   <details><summary>Respuesta</summary>

   c) El código itera sobre los caracteres de `"cab"` e imprime el equivalente en mayúscula de cada carácter. Por lo tanto, la salida es `"CAB"`.

   </details>

### count()

El método **count()** cuenta el número de apariciones de una subcadena en una cadena dada. Si la subcadena dada no existe en la cadena dada, se devuelve el valor `0`.

**Video:** [Counting the number of occurrences of a substring](https://www.openstax.org/r/counting-substrings)

**Conceptos en práctica: Usar count() para contar el número de subcadenas**

<!-- pregunta: CPL-ch08-m03-p07 -->

1. ¿Cuál es la salida de (`"aaa".count("a")`)?

   - a) `True`
   - b) `1`
   - c) `3`

   <details><summary>Respuesta</summary>

   c) `"aaa".count("a")` devuelve `3`, que es el número de apariciones de `"a"` en la cadena `"aaa"`.

   </details>

<!-- pregunta: CPL-ch08-m03-p08 -->

2. ¿Cuál es la salida de (`"weather".count("b")`)?

   - a) `0`
   - b) `-1`
   - c) `False`

   <details><summary>Respuesta</summary>

   a) No existe ninguna aparición de `"b"` en `"weather"`; por lo tanto, la salida de `"weather".count("b")` es `0`.

   </details>

<!-- pregunta: CPL-ch08-m03-p09 -->

3. ¿Cuál es la salida de (`"aaa".count("aa")`)?

   - a) `1`
   - b) `2`
   - c) `3`

   <details><summary>Respuesta</summary>

   a) Existen dos subcadenas `"aa"` en `"aaa"`, una que comienza en el índice 0 y otra que comienza en el índice 1.

   *Nota de la traducción: la explicación del original es incorrecta. `count()` no cuenta apariciones que se solapan: después de encontrar `"aa"` en el índice 0 sigue buscando desde el índice 2, así que el resultado es `1`.*

   </details>

### find()

El método **find()** devuelve el índice de la primera aparición de una subcadena en una cadena dada. Si la subcadena no existe en la cadena dada, se devuelve el valor `-1`.

**Video:** [Finding the first index of a substring](https://www.openstax.org/r/finding-substring-index)

**Conceptos en práctica: Usar find() para localizar una subcadena**

<!-- pregunta: CPL-ch08-m03-p10 -->

1. ¿Cuál es la salida de `"banana".find("a")`?

   - a) `1`
   - b) `3`
   - c) `5`

   <details><summary>Respuesta</summary>

   a) El método `find()` devuelve el índice de la primera aparición de la subcadena en la cadena dada. El índice de la primera aparición de `"a"` es 1.

   </details>

<!-- pregunta: CPL-ch08-m03-p11 -->

2. ¿Cuál es la salida de `"banana".find("c")`?

   - a) `0`
   - b) `-1`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   b) Como `"c"` no es una subcadena de `"banana"`, el método `find()` devuelve `-1`.

   </details>

<!-- pregunta: CPL-ch08-m03-p12 -->

3. ¿Cuál es la salida de `"b".find("banana")`?

   - a) `-1`
   - b) `0`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   a) Como `"banana"` no es una subcadena de `"b"`, se devuelve `-1`.

   </details>

### index()

El método **index()** funciona de manera similar al método `find()`, ya que devuelve el índice de la primera aparición de una subcadena en una cadena dada. El método `index()` supone que la subcadena existe en la cadena dada; de lo contrario, lanza un `ValueError`.

**Ejemplo: Obtener los minutos de una hora**

Considera un valor de hora dado como parte de una cadena con el formato `"hh:mm"`, donde `"hh"` representa la hora y `"mm"` representa los minutos. Para obtener solo la parte de los minutos de la cadena, se puede usar el siguiente código:

```python
time_string = "The time is 12:50"
index = time_string.index(":")
print(time_string[index+1:index+3])
```

La salida del código anterior es:

```salida
50
```

**Conceptos en práctica: Usar index() para localizar una subcadena**

<!-- pregunta: CPL-ch08-m03-p13 -->

1. ¿Cuál es la salida de `"school".index("o")`?

   - a) `3`
   - b) `4`
   - c) `-3`

   <details><summary>Respuesta</summary>

   a) El método `index()` devuelve el índice del inicio de la primera aparición de una subcadena en la cadena dada. El índice de la primera aparición de `"o"` en `"school"` es 3.

   </details>

<!-- pregunta: CPL-ch08-m03-p14 -->

2. ¿Cuál es la salida de `"school".index("ooo")`?

   - a) `3`
   - b) `4`
   - c) `ValueError`

   <details><summary>Respuesta</summary>

   c) La subcadena `"ooo"` no existe en la cadena `"school"`, por lo que el método `index()` devuelve un `ValueError`.

   </details>

<!-- pregunta: CPL-ch08-m03-p15 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   sentence = "This is a sentence"
   index = sentence.index(" ")
   print(sentence[:index])
   ```

   - a) `"This"`
   - b) `"This "`
   - c) `"sentence"`

   <details><summary>Respuesta</summary>

   a) `sentence.index(" ")` devuelve el índice del primer carácter de espacio. La instrucción print imprime el prefijo de la oración que termina justo antes del primer carácter de espacio, por lo que la salida es `"This"`.

   </details>

**Pruébalo: Encontrar todos los espacios**

Escribe un programa que, dada una cadena, cuente el número de espacios que contiene. Imprime también la cadena dada sin ningún espacio.

```text
Input: "This is great"
```

```text
Prints:
2
Thisisgreat
```

<!-- coderunner: ch8/CodeRunner_08_04_05_Finding-all-spaces -->

<!-- modulo: m00062 -->

## 8.4 Formato de cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Dar formato a una plantilla de cadena usando argumentos de entrada.
- Usar `format()` para generar formatos numéricos a partir de una plantilla dada.

### Especificación de formato de cadenas

Python ofrece una sintaxis de sustitución de cadenas para dar formato a las cadenas con argumentos de entrada. La **cadena de formato** incluye la especificación de reglas de patrón para la cadena y su modificación según la especificación de formato. Algunos ejemplos son el uso de patrones para construir diferentes valores de cadena y la especificación de reglas para modificar la longitud y la alineación de la cadena.

### Formato de cadenas con campos de reemplazo

Los **campos de reemplazo** se usan para definir un patrón que permite crear múltiples valores de cadena que cumplen un formato dado. El siguiente ejemplo muestra dos valores de cadena que usan la misma plantilla para solicitar a distintas personas que tomen diferentes cursos.

**Ejemplo: Valores de cadena a partir de la misma plantilla**

```text
Hola John, me gustaría tomar un curso de programación con el prof. Potter.

Hola Kishwar, me gustaría tomar un curso de matemáticas con el prof. Robinson.
```

En el ejemplo anterior, los campos de reemplazo son 1) el nombre de la persona a quien se hace la solicitud, 2) el título del curso y 3) el nombre del instructor. Para crear una plantilla, se pueden agregar campos de reemplazo con `{}` para indicar un marcador de posición para la entrada del usuario. El método **format()** se usa para pasar las entradas de los campos de reemplazo en una plantilla de cadena.

**Ejemplo: Formato de una plantilla de cadena para solicitudes de inscripción a cursos**

A continuación se define una plantilla de cadena con campos de reemplazo para crear valores de cadena con diferentes argumentos de entrada. El método `format()` se usa para pasar las entradas a la plantilla en el mismo orden.

```python
s = "Hola {}, me gustaría tomar un curso de {} con el prof. {}."

print(s)
print(s.format("John", "programación", "Potter"))
print(s.format("Kishwar", "matemáticas", "Robinson"))
```

La salida del código anterior es:

```salida
Hola {}, me gustaría tomar un curso de {} con el prof. {}.
Hola John, me gustaría tomar un curso de programación con el prof. Potter.
Hola Kishwar, me gustaría tomar un curso de matemáticas con el prof. Robinson.
```

**Conceptos en práctica: Plantillas de cadena y formato**

<!-- pregunta: CPL-ch08-m04-p01 -->

1. ¿Cuál es la salida de `print("Hello {}!".format("Ana"))`?

   - a) `Ana`
   - b) `Hello Ana`
   - c) `Hello Ana!`

   <details><summary>Respuesta</summary>

   c) `"Ana"` se sustituye por el campo de reemplazo {} de la plantilla y, por lo tanto, la salida es `"Hello Ana!"`.

   </details>

<!-- pregunta: CPL-ch08-m04-p02 -->

2. ¿Cuál es la salida de `print("{}:{}".format("One", "1"))`?

   - a) `One1`
   - b) `One:1`
   - c) `1:One`

   <details><summary>Respuesta</summary>

   b) Los dos argumentos se pasan a la plantilla `"{}:{}"`, que produce `"One:1"`.

   </details>

<!-- pregunta: CPL-ch08-m04-p03 -->

3. ¿Cuál es la salida de `print("{}".format("one", "two", "three"))`?

   - a) `one`
   - b) `two`
   - c) `onetwothree`

   <details><summary>Respuesta</summary>

   a) Los argumentos de la función `format()` se pasan en orden y se sustituyen en los campos de reemplazo. La plantilla puede ignorar los argumentos adicionales, que quedan sin usar.

   </details>

### Campos de reemplazo con nombre

Los campos de reemplazo se pueden etiquetar con un nombre, y entonces se llaman **campos de reemplazo con nombre**, para facilitar el acceso y la legibilidad del código. El siguiente ejemplo ilustra cómo se pueden usar los campos de reemplazo con nombre en plantillas de cadena.

**Ejemplo: Plantilla del clima de las estaciones con campos de reemplazo con nombre**

Un argumento de reemplazo con nombre es una forma cómoda de asignar etiquetas de nombre a los campos de reemplazo y de pasar los valores asociados a esos campos usando los nombres correspondientes (en lugar de pasar los valores en orden).

```python
s = "En {season} el clima es {temperature}."

print(s)
print(s.format(season = "verano", temperature = "caluroso"))
print(s.format(season = "invierno", temperature = "frío"))
```

La salida del código anterior es:

```salida
En {season} el clima es {temperature}.
En verano el clima es caluroso.
En invierno el clima es frío.
```

**Uso múltiple de un argumento con nombre**

Como los campos de reemplazo con nombre se refieren mediante una clave de nombre, un campo de reemplazo con nombre puede aparecer y usarse más de una vez en la plantilla. Además, no es necesario el orden posicional cuando se usan campos de reemplazo con nombre.

```python
s = "En {season} el clima es {temperature}; muy muy {temperature}."

print(s)
print(s.format(season = "verano", temperature = "caluroso"))
print(s.format(temperature = "frío", season = "invierno"))
```

La salida del código anterior es:

```salida
En {season} el clima es {temperature}; muy muy {temperature}.
En verano el clima es caluroso; muy muy caluroso.
En invierno el clima es frío; muy muy frío.
```

**Conceptos en práctica: Ejemplos de campos de reemplazo con nombre**

<!-- pregunta: CPL-ch08-m04-p04 -->

1. ¿Cuál es la salida de `print("Hey {name}!".format(name = "Bengio"))`?

   - a) `Hey name!`
   - b) `Hey Bengio`
   - c) `Hey Bengio!`

   <details><summary>Respuesta</summary>

   c) `"Bengio"` se sustituye en el campo de reemplazo con nombre asociado a la etiqueta `name`; por lo tanto, la salida es `"Hey Bengio!"`.

   </details>

<!-- pregunta: CPL-ch08-m04-p05 -->

2. ¿Cuál es la salida de `print("Hey {name}!".format("Bengio"))`?

   - a) `Hey name!`
   - b) `KeyError`
   - c) `Hey Bengio!`

   <details><summary>Respuesta</summary>

   b) Como la plantilla de cadena usa un argumento con nombre, las entradas solo se aceptan mediante las claves correspondientes. Por lo tanto, el código genera `KeyError: 'name'`.

   </details>

<!-- pregunta: CPL-ch08-m04-p06 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   greeting = "Hi"
   name = "Jess"
   print("{greeting} {name}".format(greeting = greeting, name = name))
   ```

   - a) `greeting name`
   - b) `Hi Jess`
   - c) `Jess Hi`

   <details><summary>Respuesta</summary>

   b) La variable greeting, con el valor `"Hi"`, se sustituye en el campo de reemplazo greeting. Lo mismo se hace con el campo de reemplazo name y la variable name. La salida es `"Hi Jess"`.

   </details>

### Campos de reemplazo numerados

El método `format()` de las cadenas de Python puede usar el orden posicional para emparejar los argumentos numerados. Los campos de reemplazo que usan el orden posicional de los argumentos se llaman **campos de reemplazo numerados**. La indexación de los argumentos comienza en 0. Ej.: `print("{1}{0}".format("Home", "Welcome"))` imprime el valor de cadena `"Welcome Home"`: el primer argumento, `"Home"`, está en el índice 0, y el segundo argumento, `"Welcome"`, está en el índice 1. Al sustituir estos argumentos en el orden de `"{1}{0}"` se crea la cadena `"Welcome Home"`.

Los campos de reemplazo numerados pueden usar el valor de un argumento en varios campos de reemplazo utilizando el mismo índice de argumento. El siguiente ejemplo ilustra cómo se usa un argumento en más de un campo de reemplazo numerado.

**Ejemplo: Campos de reemplazo numerados para construir una frase**

En este ejemplo se usan campos de reemplazo numerados para construir frases como `"very very cold"` o `"very hot"`.

```python
template1 = "{0} {0} {1}"
template2 = "{0} {1}"

print(template1.format("very", "cold"))
print(template2.format("very", "hot"))
```

La salida del código anterior es:

```salida
very very cold
very hot
```

### Formato de la longitud y la alineación de cadenas

Puede ser necesario dar formato a la longitud de las cadenas para uniformar el estilo de la salida cuando se crean e imprimen varios valores de cadena del mismo contexto. El siguiente ejemplo muestra un caso de uso del formato de cadenas al imprimir una tabla con columnas de longitud mínima y una alineación específica.

**Ejemplo: Una tabla con formato de una lista de clase**

Una tabla con formato de una lista de clase

```text
Student Name              Major          Grade
----------------------------------------------
Manoj Sara          Computer Science        A-
Gabriel Wang     Electrical Engineering      A
Alex Narayanan       Social Sciences        A+
```

En el ejemplo anterior, la tabla tiene tres columnas con formato. La primera columna ocupa 15 caracteres y está alineada a la izquierda. La segunda columna usa 25 caracteres y está centrada, y la última columna usa dos caracteres y está alineada a la derecha. Para crear la tabla con formato se usan controles de especificación de alineación y de longitud.

El ancho de campo en la especificación de formato de cadenas se usa para especificar la longitud mínima de la cadena dada. Si la cadena es más corta que la longitud mínima dada, se rellena con espacios. Un **ancho de campo** se incluye en el campo de especificación de formato mediante un entero después de dos puntos. Ej.: `{name:15}` especifica que la longitud mínima de los valores de cadena que se pasan al campo `name` es 15.

Como el ancho de campo se puede usar para especificar la longitud mínima de una cadena, la cadena se puede rellenar con espacios por la derecha, por la izquierda o por ambos lados para quedar alineada a la izquierda, alineada a la derecha y centrada, respectivamente. El **tipo de alineación de cadena** se especifica con los caracteres `<`, `>` o `^` después de los dos puntos cuando se especifica la longitud del campo. Ej.: `{name:^20}` especifica un campo de reemplazo con nombre con una longitud mínima de 20 caracteres y alineado al centro.

**Formato de alineación de cadenas.**

| Tipo de alineación | Símbolo | Ejemplo | Salida |
|---|---|---|---|
| Alineada a la izquierda | `<` | `     template = "{hex:<7}{name:<10}"     print(template.format(hex = "#FF0000", name = "Red"))     print(template.format(hex = "#00FF00", name = "green"))` | `     #FF0000Red     #00FF00green` |
| Alineada a la derecha | `>` | `     template = "{hex:>7}{name:>10}"     print(template.format(hex = "#FF0000", name = "Red"))     print(template.format(hex = "#00FF00", name = "green"))` | `     #FF0000          Red     #00FF00        green` |
| Centrada | ^ | `     template = "{hex:^7}{name:^10}"     print(template.format(hex = "#FF0000", name = "Red"))     print(template.format(hex = "#00FF00", name = "green"))` | `     #FF0000   Red     #00FF00  green` |

**Conceptos en práctica: Especificar el ancho de campo y la alineación**

<!-- pregunta: CPL-ch08-m04-p07 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   template = "{name:12}"
   formatted_name = template.format(name = "Alice")
   print(len(formatted_name))
   ```

   - a) `5`
   - b) `12`
   - c) `"Alice"`

   <details><summary>Respuesta</summary>

   b) La plantilla especifica que la longitud mínima del campo `name` es 12, por lo que `len(formatted_name)` es `12`.

   </details>

<!-- pregunta: CPL-ch08-m04-p08 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   template = "{greeting:>6}"
   formatted_greeting = template.format(greeting = "Hello")
   print(formatted_greeting[0])
   ```

   - a) `H`
   - b) `" Hello"`
   - c) Carácter de espacio

   <details><summary>Respuesta</summary>

   c) La alineación y la especificación de la longitud del campo dan formato al campo `greeting` para que tenga seis caracteres de longitud y esté alineado a la derecha. Por lo tanto, la variable `formatted_greeting` tomará el valor `" Hello"`, y el carácter 0 de la cadena es un carácter de espacio.

   </details>

<!-- pregunta: CPL-ch08-m04-p09 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   template = "{:5}"
   print(template.format("123456789"))
   ```

   - a) `56789`
   - b) `123456`
   - c) `123456789`

   <details><summary>Respuesta</summary>

   c) La especificación de la longitud del campo impone la longitud mínima de la cadena. Las entradas más largas que la longitud mínima especificada no se modifican.

   </details>

### Formato de números

El método `format()` se puede usar para dar formato a valores numéricos. Los valores numéricos se pueden rellenar para que tengan una longitud mínima, una precisión y un carácter de signo dados. La sintaxis para modificar valores numéricos sigue la estructura `{[index]:[width][.precision][type]}`. En la sintaxis dada,

- El campo `index` se refiere al índice del argumento.
- El campo `width` se refiere a la longitud mínima de la cadena.
- El campo `precision` se refiere a la precisión de punto flotante del número dado.
- El campo `type` indica el tipo de la entrada que se pasa al método `format()`. Las entradas de punto flotante y decimales se identifican con `"f"` y `"d"`, respectivamente. Los valores de cadena se identifican con `"s"`.

La siguiente tabla resume las opciones de formato para modificar valores numéricos.

**Opciones de formato numérico.**

| Ejemplo | Salida | Explicación |
|---|---|---|
| `print("{:.7f}".format(0.9795))` | `0.9795000` | La especificación de formato `.7` indica que la salida debe tener siete decimales. La especificación `f` es un identificador del formato de punto flotante. |
| `print("{:.3f}".format(12))` | `12.000` | La especificación de formato `.3` indica que la salida debe tener tres decimales. La especificación `f` es un identificador del formato de punto flotante. |
| `print("{:+.2f}".format(4))` | `+4.00` | La especificación de formato `.2` indica que la salida debe tener dos decimales. La especificación `f` es un identificador del formato de punto flotante. El signo `+` antes de la especificación de precisión agrega un carácter de signo a la salida. |
| `print("{:0>5d}".format(5))` | `00005` | La especificación de formato `0>5` define el campo de ancho como 5 y, por lo tanto, la salida debe tener una longitud mínima de 5. Además, si el número tiene menos de cinco dígitos, debe rellenarse con ceros por la izquierda. La especificación `d` es un identificador del formato de números decimales. |
| `print("{:.3s}".format("12.50"))` | `12.` | La especificación de formato `.3` indica que la salida tendrá tres caracteres. La especificación `s` es un identificador del formato de cadenas. |

**Conceptos en práctica: Ejemplos de formato de valores numéricos**

<!-- pregunta: CPL-ch08-m04-p10 -->

1. ¿Cuál es la salida de `print('{0:.3f}'.format(3.141592))`?

   - a) `3.141592`
   - b) `3.1`
   - c) `3.142`

   <details><summary>Respuesta</summary>

   c) La especificación de formato `.3` indica que la precisión de la salida debe ser de tres decimales.

   </details>

<!-- pregunta: CPL-ch08-m04-p11 -->

2. ¿Cuál es la salida de `print('{:1>3d}'.format(3))`?

   - a) `113`
   - b) `311`
   - c) `3.000`

   <details><summary>Respuesta</summary>

   a) La especificación `{:1>3d}` produce en la salida un número de 3 dígitos y, si el argumento dado no tiene tres dígitos, el número se rellena con unos por la izquierda.

   </details>

<!-- pregunta: CPL-ch08-m04-p12 -->

3. ¿Cuál es la salida de `print('{:+d}'.format(123))`?

   - a) `123`
   - b) `+123`
   - c) `:+123`

   <details><summary>Respuesta</summary>

   b) `{:+d}` da formato al número decimal agregándole el signo positivo.

   </details>

**Pruébalo: Dar formato a una lista de números**

Dada una lista de números (de punto flotante o enteros), imprime los números con una precisión de dos decimales y al menos seis caracteres.

```text
Input: [12.5, 2]
```

```text
Prints: 012.50

002.00
```

<!-- coderunner: ch8/CodeRunner_08_05_06_Formatting-a-list-of-numbers -->

<!-- modulo: m00063 -->

## 8.5 División y unión de cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar el método `split()` para dividir una cadena en subcadenas.
- Combinar los objetos de una lista en una cadena mediante el método `join()`.

### split()

Una cadena de Python se puede dividir en subcadenas a partir de un **delimitador**. Un delimitador también se denomina separador. El método **split()**, cuando se aplica a una cadena, la divide en subcadenas usando el argumento dado como delimitador. Ej.: `"1-2".split('-')` devuelve una lista de subcadenas `["1", "2"]`. Cuando no se da ningún argumento al método `split()`, se usan como delimitadores los caracteres de espacio en blanco. Ej.: `"1\t2\n3 4".split()` devuelve `["1", "2", "3", "4"]`.

**Video:** [split() for breaking down the string into tokens](https://www.openstax.org/r/split-function)

**Conceptos en práctica: Ejemplos de delimitadores de cadena y del método split()**

<!-- pregunta: CPL-ch08-m05-p01 -->

1. ¿Cuál es la salida de `print("1*2*3*".split('*'))`?

   - a) `["1", "*", "2", "*", "3", "*"]`
   - b) `["1", "2", "3"]`
   - c) `[1, 2, 3]`

   <details><summary>Respuesta</summary>

   b) Cuando `"1*2*3*"` se divide en subcadenas usando el delimitador `'*'`, la salida es `["1", "2", "3"]`.

   </details>

<!-- pregunta: CPL-ch08-m05-p02 -->

2. ¿Cuál es la salida de `print("a year includes 12 months".split())`?

   - a) `["a year includes 12 months"]`
   - b) `["a", "year", "includes", 12, "months"]`
   - c) `["a", "year", "includes", "12", "months"]`

   <details><summary>Respuesta</summary>

   c) Cuando `"a year includes 12 months"` se divide en subcadenas usando los caracteres de espacio en blanco, se crea la lista `["a", "year", "includes", "12", "months"]`.

   </details>

<!-- pregunta: CPL-ch08-m05-p03 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   s = """This
   is a
   test"""
   
   out = s.split()
   print(out)
   ```

   - a) `Error`
   - b) `['This', 'is', 'a', 'test']`
   - c) `['This', 'is a', 'test']`

   <details><summary>Respuesta</summary>

   b) Al dividir la cadena de varias líneas, la salida es `['This', 'is', 'a', 'test']`.

   </details>

### join()

El método **join()** es el inverso del método `split()`: una lista de valores de cadena se concatena para formar una única cadena de salida. Al unir los elementos de cadena de la lista, se agrega el delimitador entre los elementos. Ej.: `','.join(["this", "is", "great"])` devuelve `"this,is,great"`.

**Video:** [join() for combining tokens into one string](https://www.openstax.org/r/join-function)

**Conceptos en práctica: Aplicar el método join() a una lista de valores de cadena**

<!-- pregunta: CPL-ch08-m05-p04 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   elements = ['A', 'beautiful', 'day', 'for', 'learning']
   
   print(",".join(elements))
   ```

   - a) `'A beautiful day for learning'`
   - b) `['A, beautiful, day, for, learning']`
   - c) `'A,beautiful,day,for,learning'`

   <details><summary>Respuesta</summary>

   c) Los elementos de la lista `elements` se concatenan usando una coma, por lo que la salida es `'A,beautiful,day,for,learning'`.

   </details>

<!-- pregunta: CPL-ch08-m05-p05 -->

2. ¿Cuál es la longitud de la cadena `"sss".join(["1","2"])`?

   - a) 2
   - b) 5
   - c) 8

   <details><summary>Respuesta</summary>

   b) La salida de `"sss".join(["1","2"])` es `"1sss2"`, que tiene una longitud de 5.

   </details>

<!-- pregunta: CPL-ch08-m05-p06 -->

3. ¿Cuál es el valor almacenado en la variable `out`?
   
   ```python
   s = ["1", "2"]
   out = "".join(s)
   ```

   - a) `12`
   - b) `"12"`
   - c) `"1 2"`

   <details><summary>Respuesta</summary>

   b) Como el separador es una cadena vacía, los elementos de la lista se concatenarán sin separador y la salida será `"12"`.

   </details>

**Pruébalo: Palabras únicas separadas por comas**

Escribe un programa que acepte como entrada una secuencia de palabras separadas por comas e imprima las palabras en líneas separadas. Ej.: Dada la cadena `"happy,smiling,face"`, la salida sería:

```text
happy
smiling
face
```

<!-- coderunner: ch8/CodeRunner_08_06_07_Unique-and-comma-separated-words -->

**Pruébalo: Pedido de almuerzo**

Usa el método `join()` para repetir, separado por comas, el pedido de un usuario en un restaurante. El usuario introducirá cada alimento en una línea distinta. Al terminar de pedir, el usuario introducirá una línea en blanco. La salida depende de cuántos elementos pida el usuario:

- Si el usuario no introduce nada, el programa muestra:  
`You ordered nothing`.
- Si el usuario introduce un elemento (Ej.: eggs), el programa muestra:  
`You ordered eggs`.
- Si el usuario introduce dos elementos (Ej.: eggs, ham), el programa muestra:  
`You ordered eggs and ham`.
- Si el usuario introduce tres o más elementos (Ej.: eggs, ham, toast), el programa muestra:  
`You ordered eggs, ham, and toast`.

En el caso general de tres o más elementos, cada elemento debe separarse por una coma y un espacio. La palabra «and» debe agregarse antes del último elemento.

<!-- coderunner: ch8/CodeRunner_08_06_08_Lunch-order -->

<!-- modulo: m00064 -->

## Resumen del capítulo

Los puntos principales de este capítulo son:

- Una cadena es una secuencia de caracteres.
- Los operadores lógicos se pueden usar para comparar dos valores de cadena. La comparación de cadenas se realiza comparando los valores ASCII correspondientes de los caracteres en el orden en que aparecen en la cadena.
- La indexación de cadenas se usa para acceder a un carácter o a una secuencia de caracteres de la cadena.
- Los objetos de cadena son inmutables.
- Rebanado de cadenas.

Llegados a este punto, deberías poder escribir programas que trabajen con valores de cadena.

**Referencia del capítulo 8.**

| Método | Descripción |
|---|---|
| `len()` | Devuelve la longitud de la cadena. |
| `upper()` | Devuelve los caracteres en mayúscula. |
| `lower()` | Devuelve los caracteres en minúscula. |
| `count()` | Devuelve el número de apariciones de una subcadena dada en una cadena. |
| `find()` | Devuelve el índice de la primera aparición de una subcadena dada en una cadena. Si la subcadena no existe en la cadena, se devuelve -1. |
| `index()` | Devuelve el índice de la primera aparición de una subcadena dada en una cadena. Si la subcadena no existe en la cadena, se devuelve un `ValueError`. |
| `format()` | Se usa para crear cadenas con patrones especificados mediante argumentos. |
| `join()` | Toma una lista de valores de cadena y los combina en una sola cadena colocando un separador dado entre los valores. |
| `split()` | Separa una cadena en tokens según una cadena separadora dada. Si no se proporciona ninguna cadena separadora, se usan como separadores los caracteres de espacio en blanco. |
| **Operador** | **Descripción** |
| `in` | Comprueba si una subcadena existe en una cadena. |
| Operador `in` en un bucle `for` | ```python<br>for character in string:<br>  # loop body<br>``` |
