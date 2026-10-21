# Capítulo 10: Diccionarios

<!-- modulo: m00073 -->

## Introducción

![Una imagen de un diccionario.](media/Python_10_00_000.jpg)

*crédito: modificación de la obra «Dictionary», de Caleb Roenigk/Flickr, CC BY 2.0*

Un **diccionario** de Python es un tipo de datos para almacenar datos en formato de pares clave-valor. En este capítulo se presenta el tipo de datos diccionario. También se presentan formas de usar los diccionarios, como recorrer sus elementos con un bucle y aplicar instrucciones condicionales sobre un diccionario.

<!-- modulo: m00074 -->

## 10.1 Conceptos básicos de los diccionarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir la estructura de un objeto diccionario.
- Usar `type()` para identificar el tipo de un objeto diccionario.
- Explicar por qué un objeto diccionario no tiene valores de clave duplicados.

### Diccionarios

Un **diccionario** en Python es un objeto contenedor que incluye pares clave-valor. Un ejemplo de un elemento **clave-valor** es una palabra de un diccionario de inglés con su definición correspondiente.

**Video:** [Dictionaries](https://www.openstax.org/r/dictionaries)

**Conceptos en práctica: Conceptos básicos de los diccionarios**

<!-- pregunta: CPL-ch10-m01-p01 -->

1. ¿Cuáles son las claves del objeto diccionario `days`?

   - a) `"Sunday", "Monday", "Tuesday"`
   - b) `1, 2, 3`
   - c) `0, 1, 2`

   <details><summary>Respuesta</summary>

   a) El primer elemento de cada par clave-valor es la clave. Por lo tanto, `"Sunday", "Monday", "Tuesday"` son los elementos clave.

   </details>

<!-- pregunta: CPL-ch10-m01-p02 -->

2. ¿Cuáles son los valores del objeto diccionario `days`?

   - a) `0, 1, 2`
   - b) `1, 2, 3`
   - c) `"Sunday", "Monday", "Tuesday"`

   <details><summary>Respuesta</summary>

   b) El segundo elemento de cada par clave-valor es el valor. Por lo tanto, `1, 2, 3` son los elementos de valor.

   </details>

<!-- pregunta: CPL-ch10-m01-p03 -->

3. ¿Cuál es el valor asociado con la clave `"Sunday"`?

   - a) `"Sunday"`
   - b) `1`
   - c) `0`

   <details><summary>Respuesta</summary>

   b) Según el objeto diccionario `days`, el valor asignado a `"Sunday"` es `1`.

   </details>

### Tipo y propiedades de los diccionarios

El tipo **dict** implementa un diccionario en Python. Como un objeto diccionario se usa para buscar valores mediante claves, no puede contener valores de clave duplicados.

**Video:** [Dictionary properties](https://www.openstax.org/r/dictionary-properties)

**Conceptos en práctica: Tipo y propiedades de los diccionarios**

<!-- pregunta: CPL-ch10-m01-p04 -->

1. ¿Qué devuelve `type(encoding)`?

   - a) `dictionary`
   - b) `dict`
   - c) `str`

   <details><summary>Respuesta</summary>

   b) El tipo de un objeto diccionario es `dict`.

   </details>

<!-- pregunta: CPL-ch10-m01-p05 -->

2. El diccionario `encoding` contiene claves duplicadas, ya que tiene tanto `"a"` como `"A"` como claves.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   b) Un diccionario no puede tener claves duplicadas, y `"a"` y `"A"` son dos claves distintas porque `"a"` y `"A"` son caracteres diferentes.

   </details>

<!-- pregunta: CPL-ch10-m01-p06 -->

3. Un diccionario puede tener valores duplicados.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   a) Un diccionario puede tener valores duplicados, pero no claves duplicadas.

   </details>

**Pruébalo: Investigar los tipos de variables**

Dadas las variables del código siguiente, examina los tipos de las variables.

<!-- coderunner: ch10/CodeRunner_10_02_01_Investigate-variable-types -->

<!-- modulo: m00075 -->

## 10.2 Creación de diccionarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Crear un objeto diccionario con pares clave-valor dados.

### Creación de diccionarios

Existen dos métodos para crear un diccionario vacío:

- Usar llaves `{}`. Ej.: `dict_1 = {}`.
- Usar la función `dict()`. Ej.: `dict_2 = dict()`.

También se puede crear un objeto diccionario con pares clave-valor iniciales encerrados entre llaves. Ej.: `my_dict = {"pizza": 2, "pasta": 3, "drink": 4}` crea un objeto diccionario `my_dict`. Una clave y su valor asociado se separan con dos puntos, y los pares clave-valor se separan con comas.

**Video:** [Creating a dictionary object](https://www.openstax.org/r/creating-dictionary-object)

**Conceptos en práctica: Ejercicios de creación de diccionarios**

<!-- pregunta: CPL-ch10-m02-p01 -->

1. ¿Cuál es la sintaxis correcta para crear un diccionario vacío en Python?

   - a) `my_dict = ()`
   - b) `my_dict = {}`
   - c) `my_dict = []`

   <details><summary>Respuesta</summary>

   b) Se pueden usar llaves para crear un diccionario vacío.

   </details>

<!-- pregunta: CPL-ch10-m02-p02 -->

2. ¿Cuál es la sintaxis correcta para crear un diccionario con un elemento `"one": 1`?

   - a) `my_dict = ("one": 1)`
   - b) `my_dict = ("one", 1)`
   - c) `my_dict = {"one": 1}`

   <details><summary>Respuesta</summary>

   c) `{"one": 1}` crea un objeto diccionario con un elemento `"one": 1`.

   </details>

<!-- pregunta: CPL-ch10-m02-p03 -->

3. ¿Cuántos elementos contiene el objeto `my_dict`?
   
    `my_dict = {"a": 1, "b": 2} `

   - a) 1
   - b) 2
   - c) 4

   <details><summary>Respuesta</summary>

   b) El diccionario `my_dict` contiene dos pares de elementos. Los dos pares son `"a": 1` y `"b": 2`.

   </details>

### dict() para crear diccionarios

Se puede crear un objeto diccionario con pares clave-valor iniciales usando la función `dict()`.

- Crear un diccionario a partir de una lista de tuplas.

  ```python norun
  my_list = [("apple", 2), ("banana", 3), ("orange", 4)]
my_dict = dict(my_list)
  ```
- Crear un diccionario usando argumentos con nombre.

  ```python
  my_dict = dict(apple=2, banana=3, orange=4)
  ```
- Crear un diccionario a partir de otro diccionario.

  ```python norun
  old_dict = {"apple": 2, "banana": 3, "orange": 4}
new_dict = dict(old_dict)
  ```

**Video:** [dict() for dictionary initialization](https://www.openstax.org/r/dict-initialization)

**Conceptos en práctica: La función dict() para crear diccionarios**

<!-- pregunta: CPL-ch10-m02-p04 -->

1. ¿Cuál es la sintaxis correcta para crear un diccionario con valores iniciales en Python?

   - a) `my_dict = [key1:value1, key2:value2]`
   - b) `my_dict = dict(key1=value1, key2=value2)`
   - c) `my_dict = {key1=value1, key2=value2}`

   <details><summary>Respuesta</summary>

   b) La función `dict()`, junto con argumentos con nombre, se puede usar para crear un objeto diccionario.

   </details>

<!-- pregunta: CPL-ch10-m02-p05 -->

2. ¿Cuál es la salida del código siguiente?
   
   ```python
   my_dict = dict({"a": 1})
   print(my_dict)
   ```

   - a)

     ```python
     {"a": 1}
     ```

   - b)

     ```python norun
     <class, 'dict'>
     ```

   - c)

     ```python
     "a"
     1
     ```

   <details><summary>Respuesta</summary>

   a) `my_dict` es un diccionario con un par clave-valor, `"a": 1`.

   </details>

<!-- pregunta: CPL-ch10-m02-p06 -->

3. ¿Qué opción crea un diccionario con dos pares clave-valor, `"a": "A"` y `"b": "B"`?

   - a) `dict(a: A, b: B)`
   - b) `dict([("a", "A"), ("b", "B")])`
   - c) `dict({"a" = "A", "b" = "B"})`

   <details><summary>Respuesta</summary>

   b) La función `dict()` puede crear un objeto diccionario a partir de una lista de tuplas. El primer elemento de cada tupla actúa como la clave, y el segundo elemento es el valor.

   </details>

**Pruébalo: Diccionario de información personal**

Crea un diccionario, `my_info`, con tres pares clave-valor. Las claves deben ser `"first name"`, `"last name"` y `"age"`, y los valores deben ser la información correspondiente sobre ti. Luego, imprime `my_info`.

<!-- coderunner: ch10/CodeRunner_10_03_02_Personal-information-dictionary -->

<!-- modulo: m00076 -->

## 10.3 Operaciones con diccionarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Reconocer que un objeto diccionario es mutable.
- Evaluar los elementos, las claves y los valores de un diccionario.
- Demostrar la capacidad de acceder a los elementos de un diccionario, evaluarlos y modificarlos.
- Modificar un diccionario agregando elementos.
- Modificar un diccionario eliminando elementos.

### Acceso a los elementos de un diccionario

En Python, se puede acceder a los valores asociados con las claves de un diccionario usando las claves como índices. Estas son dos formas de acceder a los elementos de un diccionario en Python:

- Notación con corchetes: los corchetes `[]` con la clave dentro acceden al valor asociado con esa clave. Si la clave no se encuentra, se lanzará una excepción.
- Método `get()`: el método `get()` se llama con la clave como argumento para acceder al valor asociado con esa clave. Si la clave no se encuentra, el método devuelve `None` de forma predeterminada, o un valor predeterminado especificado como segundo argumento.

Ej.: en el código siguiente, se inicializa un objeto diccionario `my_dict` con los elementos `{"apple": 2, "banana": 3, "orange": 4}`. La notación con corchetes y el método `get()` se usan para acceder a los valores asociados con las claves `"banana"` y `"apple"`, respectivamente. Al acceder al diccionario para obtener la clave `"pineapple"`, se devuelve `-1` porque la clave no existe en el diccionario.

```python
my_dict = {"apple": 2, "banana": 3, "orange": 4}
print(my_dict["banana"]) # Imprime: 3
print(my_dict.get("apple")) # Imprime: 2
print(my_dict.get("pineapple", -1)) # Imprime: -1
```

**Video:** [Accessing dictionary items](https://www.openstax.org/r/accessing-dictionary)

**Conceptos en práctica: Elementos de un diccionario**

<!-- pregunta: CPL-ch10-m03-p01 -->

1. ¿Cuál es la salida de `members["Jaya"]`?

   - a) `0`
   - b) `None`
   - c) `"Student"`

   <details><summary>Respuesta</summary>

   c) El valor asociado con la clave `"Jaya"` es `"Student"`.

   </details>

<!-- pregunta: CPL-ch10-m03-p02 -->

2. ¿Cuál es la salida de `members.get("jaya")`?

   - a) `0`
   - b) `None`
   - c) `"Student"`

   <details><summary>Respuesta</summary>

   b) Cuando una clave no existe en un diccionario, se devuelve `None` de forma predeterminada.

   </details>

<!-- pregunta: CPL-ch10-m03-p03 -->

3. ¿Cuál es la salida de `members.get("jaya", "does not exist")`?

   - a) `"Student"`
   - b) `"does not exist"`
   - c) `None`

   <details><summary>Respuesta</summary>

   b) El segundo argumento de la función `get()` se devolverá si la clave no se encuentra en el diccionario.

   </details>

### Obtención de las claves y los valores de un diccionario

Las claves, los valores, y tanto las claves como los valores de un diccionario se pueden obtener mediante las llamadas a las funciones `keys()`, `values()` e `items()`, respectivamente. Los tipos de retorno de `keys()`, `values()` e `items()` son `dict_keys`, `dict_values` y `dict_items`, que se pueden convertir en un objeto `list` mediante el constructor de listas `list()`.

**Ejemplo: Formato con plantillas de cadena para solicitudes de inscripción a cursos**

Se crea un objeto diccionario con los elementos `{"a": 97, "b": 98, "c": 99}`. Se llama a las funciones `keys()`, `values()` e `items()` para obtener las claves, los valores y los elementos del diccionario, respectivamente. También se usa `list()` para convertir la salida en un objeto `list`.

```python
dictionary_object = {"a": 97, "b": 98, "c": 99}

print(dictionary_object.keys())
print(list(dictionary_object.keys()))
print(dictionary_object.values())
print(dictionary_object.items())
```

La salida del código anterior es:

```python norun
dict_keys(["a", "b", "c"])
["a", "b", "c"]
dict_values([97, 98, 99])
dict_items([("a", 97), ("b", 98), ("c", 99)])
```

**Conceptos en práctica: Claves y valores de un diccionario**

<!-- pregunta: CPL-ch10-m03-p04 -->

1. ¿Cuál es el tipo de salida de `numbers.keys()`?

   - a) `dict_keys`
   - b) `dict_values`
   - c) `list`

   <details><summary>Respuesta</summary>

   a) El tipo de retorno de la función `keys()` es `dict_keys`.

   </details>

<!-- pregunta: CPL-ch10-m03-p05 -->

2. ¿Cuál es la salida de `print(numbers.values())`?

   - a) `[1, 2, 3]`
   - b) `dict_keys([1, 2, 3])`
   - c) `dict_values([1, 2, 3])`

   <details><summary>Respuesta</summary>

   c) Los valores del diccionario numbers son `1`, `2` y `3`. Al imprimir `numbers.values()`, se imprime `dict_values([1, 2, 3])`.

   </details>

<!-- pregunta: CPL-ch10-m03-p06 -->

3. ¿Cuál es la salida de `print(list(numbers.keys()))`?

   - a) `["three", "two", "one"]`
   - b) `["one", "two", "three"]`
   - c) `dict_keys(["one", "two", "three"])`

   <details><summary>Respuesta</summary>

   b) Las claves del diccionario son `"one", "two", "three"`. Al usar el constructor `list()`, se devuelve un objeto lista que contiene todas las claves.

   </details>

### Mutabilidad de los diccionarios

En Python, un diccionario es un tipo de datos mutable, lo que significa que su contenido se puede modificar después de crearlo. Los elementos de un diccionario se pueden agregar, actualizar o eliminar después de crear el objeto diccionario.

Para agregar un elemento a un diccionario, se puede usar la notación con corchetes o la función `update()`.

- Notación con corchetes: al usar corchetes para crear un nuevo objeto clave y asignarle un valor, el nuevo par clave-valor se agregará al diccionario.

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
my_dict["pineapple"] = 1
print(my_dict) # Imprime: {"apple": 2, "banana": 3, "orange": 4, "pineapple": 1}
  ```
- Método `update()`: el método `update()` se puede llamar con pares clave-valor adicionales para actualizar el contenido del diccionario.

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
my_dict.update({"pineapple": 1, "cherry": 0})
print(my_dict) # Imprime: {"apple": 2, "banana": 3, "orange": 4, "pineapple": 1, "cherry": 0}
  ```

Para modificar un elemento de un diccionario, se pueden usar los dos enfoques anteriores sobre una clave existente del diccionario junto con el valor actualizado. Ej.:

- Notación con corchetes:

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
my_dict["apple"] = 1
print(my_dict) # Imprime: {"apple": 1, "banana": 3, "orange": 4}
  ```
- Método `update()`:

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
my_dict.update({"apple": 1})
print(my_dict) # Imprime: {"apple": 1, "banana": 3, "orange": 4}
  ```

Los elementos se pueden eliminar de un diccionario mediante la palabra clave `del` o el método `pop()`.

- Palabra clave `del`:

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
del my_dict["orange"]
print(my_dict) # Imprime: {"apple": 2, "banana": 3}
  ```
- Método `pop()`:

  ```python norun
  my_dict = {"apple": 2, "banana": 3, "orange": 4}
deleted_value = my_dict.pop("banana")
print(deleted_value) # Imprime: 3
print(my_dict) # Imprime: {"apple": 2, "orange": 4}
  ```

**Video:** [Modifying dictionary items](https://www.openstax.org/r/modifying-dictionary)

**Conceptos en práctica: Modificar un diccionario**

<!-- pregunta: CPL-ch10-m03-p07 -->

1. ¿Qué opción modifica el valor de la clave `"Coconut soup"` a `"$11"` manteniendo iguales los demás elementos?

   - a) `food = {""Coconut soup": "$15""}`
   - b) `food["Coconut soup"] = 11`
   - c) `food["Coconut soup"] = "$11"`

   <details><summary>Respuesta</summary>

   c) Al acceder a una clave de un diccionario y asignarle un nuevo valor, el valor asociado con la clave se actualizará.

   </details>

<!-- pregunta: CPL-ch10-m03-p08 -->

2. ¿Qué opción elimina el elemento `"Butter Chicken": "$18"` del diccionario `food`?

   - a) `food.remove("Butter Chicken")`
   - b) `del food["Butter Chicken"]`
   - c) `del food.del("Butter Chicken")`

   <details><summary>Respuesta</summary>

   b) Con la palabra clave `del`, se pueden eliminar elementos de un diccionario usando la clave.

   </details>

<!-- pregunta: CPL-ch10-m03-p09 -->

3. ¿Cuál es el contenido del diccionario `food` después de llamar a `food.update({"Kabob": "$22", "Sushi": "$16"})`?

   - a) `{"Coconut soup": "$15", "Butter Chicken": "$18", "Kabob": "$22", "Sushi": "$16"}`
   - b) `{"Coconut soup": "$15", "Butter Chicken": "$18", "Kabob": "$20", "Sushi": "$16"}`
   - c) `{ "Sushi": "$16", "Coconut soup": "$15", "Butter Chicken": "$18", "Kabob": "$20"}`

   <details><summary>Respuesta</summary>

   a) La función `update()` modifica el valor asociado con la clave `"Kabob"` y agrega un nuevo elemento, `"Sushi": "$16"`.

   </details>

**Pruébalo: Crear paso a paso un diccionario de autos**

Sigue los pasos siguientes para crear un diccionario de `cars` y modificarlo paso a paso.

1. Crea un diccionario vacío.
2. Agrega un par clave-valor de `"Mustang": 10`.
3. Agrega otro par clave-valor de `"Volt": 3`.
4. Imprime el diccionario.
5. Modifica el valor asociado con la clave `"Mustang"` para que sea igual a `2`.
6. Elimina la clave `"Volt"` y el valor asociado.
7. Imprime el contenido del diccionario.

```text
Prints {"Mustang": 2}
```

<!-- coderunner: ch10/CodeRunner_10_04_03_Create-a-dictionary-of-cars-step-by-step -->

**Pruébalo: La cantidad de caracteres únicos**

Dado un valor de cadena, calcula e imprime la cantidad de caracteres únicos usando un diccionario.

```python norun
Input:
string_value = "This is a string"
```

```text
Prints 10
```

<!-- coderunner: ch10/CodeRunner_10_04_04_The-number-of-unique-characters -->

<!-- modulo: m00077 -->

## 10.4 Condicionales y bucles en diccionarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Escribir una instrucción condicional para comprobar una clave o un valor.
- Escribir un bucle `for` para iterar sobre los elementos de un diccionario.

### Condicionales para diccionarios

Las instrucciones condicionales se pueden usar con diccionarios para comprobar si ciertas claves, valores o elementos existen en el diccionario, o si un valor cumple una condición particular.

**Ejemplo: Plantillas y ejemplos de una instrucción condicional sobre un diccionario**

| dict.items() |
|---|
| ```python<br># (key, value) in dictionary.items()<br><br>movies = {"The godfather": 1974, "Interstellar": 2014}<br><br>print(("Interstellar", 2014) in movies.items())<br>``` |
| `True` |

| Condicionales sobre valores o claves |
|---|
| ```python<br># dictionary[key] operand test_value<br><br>movies = {"The godfather": 1974, "Interstellar": 2014}<br><br>print(movies["The godfather"] < 2000)<br>``` |
| `True` |

| dict.keys() |
|---|
| ```python<br># key in dictionary.keys()<br><br>movies = {"The godfather": 1974, "Interstellar": 2014}<br><br>print("Interstellar" in movies.keys())<br>``` |
| `True` |

| dict.values() |
|---|
| ```python<br># value in dictionary.values()<br><br>movies = {"The godfather": 1974, "Interstellar": 2014}<br><br>print(2014 in movies.values())<br>``` |
| `True` |

**Conceptos en práctica: Condicionales sobre diccionarios**

<!-- pregunta: CPL-ch10-m04-p01 -->

1. ¿Cuál es la salida de `"apple"` in `fruit_count.keys()`?

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) `"apple"` es una clave del diccionario y existe en las claves devueltas por `fruit_count.keys()`.

   </details>

<!-- pregunta: CPL-ch10-m04-p02 -->

2. ¿Cuál es la salida de `("orange", 5)` in `fruit_count.items()`?

   - a) `SyntaxError`
   - b) `True`
   - c) `False`

   <details><summary>Respuesta</summary>

   b) La clave `"orange"`, con el valor asociado `5`, existe en el diccionario y el valor devuelto es `True`.

   </details>

<!-- pregunta: CPL-ch10-m04-p03 -->

3. ¿Qué instrucción condicional comprueba si el valor asociado con la clave `"pomegranate"` es mayor que `0`?

   - a) `fruit_count("pomegranate") > 0`
   - b) `fruit_count["pomegranate"] > 0`
   - c) `fruit_count.get("pomegranate" > 0)`

   <details><summary>Respuesta</summary>

   b) Se pueden escribir instrucciones condicionales para examinar claves y valores.

   </details>

### Bucles sobre un diccionario

Recorrer un diccionario de Python con un bucle es una forma de iterar sobre los pares clave-valor del diccionario. El bucle sobre un diccionario se puede hacer iterando sobre las claves o sobre los elementos. Cuando se recorre con las claves, estas se obtienen con la función `keys()` y se pasan a la variable del bucle una por una. Cuando se recorren los elementos con la función `items()`, tanto la clave como el valor de cada elemento se pasan a la variable del bucle.

**Un bucle for sobre un diccionario obtiene cada clave del diccionario**

```python norun
for key in dictionary: # Expresión del bucle
  # Instrucciones que se ejecutan en el bucle

# Instrucciones que se ejecutan después del bucle
```

**Ejemplo: Iterar sobre un diccionario**

| dict.items() |
|---|
| ```python<br>zip_codes = {"Berkeley": 94709, "Santa Cruz": 95064, "Mountain View": 94030}<br><br>for key, value in zip_codes.items():<br>  print(key, value)<br>``` |
| ```python<br>Berkeley 94709<br>Santa Cruz 95064<br>Mountain View 94030<br>``` |

| dict.keys() |
|---|
| ```python<br>zip_codes = {"Berkeley": 94709, "Santa Cruz": 95064, "Mountain View": 94030}<br><br>for key in zip_codes.keys():<br>  print(key)<br>``` |
| ```python<br>Berkeley<br>Santa Cruz<br>Mountain View<br>``` |

| dict.values() |
|---|
| ```python<br>zip_codes = {"Berkeley": 94709, "Santa Cruz": 95064, "Mountain View": 94030}<br><br>for value in zip_codes.values():<br>  print(value)<br>``` |
| ```python<br>94709<br>95064<br>94030<br>``` |

**Conceptos en práctica: Bucles sobre diccionarios**

<!-- pregunta: CPL-ch10-m04-p04 -->

1. ¿Qué método se usa para recorrer con un bucle los valores de un diccionario de Python?

   - a) `keys()`
   - b) `values()`
   - c) `items()`

   <details><summary>Respuesta</summary>

   b) El método `values()` itera sobre los valores de un diccionario.

   </details>

<!-- pregunta: CPL-ch10-m04-p05 -->

2. ¿Cuál es la salida del código siguiente?
   
   ```python
   fruit_count = {"apple": 2, "orange": 5, "banana": 1}
   for key in fruit_count.keys():
     print(key, end = " ")
   ```

   - a) `apple orange banana `
   - b) `2 5 1`
   - c) `("apple", 2) ("orange", 5) ("banana", 1)`

   <details><summary>Respuesta</summary>

   a) El bucle itera sobre las claves `"apple"`, `"orange"` y `"banana"`, e imprime las claves separadas por espacios.

   </details>

<!-- pregunta: CPL-ch10-m04-p06 -->

3. ¿Cuál es la salida del código siguiente?
   
   ```python
   fruit_count = {"apple": 2, "orange": 5, "banana": 1}
   for value in fruit_count.values():
     print(value * 2, end = " ")
   ```

   - a) `apple orange banana`
   - b) `2 5 1`
   - c) `4 10 2`

   <details><summary>Respuesta</summary>

   c) El bucle multiplica todos los valores por 2 e imprime el resultado. Por lo tanto, se imprimen `4`, `10` y `2`.

   </details>

**Pruébalo: Conteo de caracteres en una cadena**

Dado un valor de cadena, calcula e imprime la cantidad de apariciones de todos los caracteres usando un diccionario.

```python norun
Input:
string_value = "This is a string"
```

```python norun
Prints {"T": 1, "h": 1, "i": 3, "s": 3, " ": 3, "a": 1, "t": 1, "r": 1, "n": 1,
"g": 1}
```

<!-- coderunner: ch10/CodeRunner_10_05_05_Character-count-in-a-string -->

**Pruébalo: Calcular la cantidad total de frutas**

Dado un diccionario `fruit_count` que contiene información sobre frutas y la cantidad de cada fruta, calcula la cantidad total de frutas de todos los tipos de fruta.

```python norun
Input:
fruit_count = {"banana": 2, "orange": 5, "peach": 5}
```

```text
Prints 12
```

<!-- coderunner: ch10/CodeRunner_10_05_06_Calculate-the-total-number-of-fruits -->

<!-- modulo: m00078 -->

## 10.5 Diccionarios anidados y comprensión de diccionarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar la estructura de los diccionarios anidados.
- Usar la comprensión de diccionario para crear un objeto diccionario.

### Diccionarios anidados

Como se describió antes, los diccionarios de Python son un tipo de estructura de datos que permite almacenar datos en pares clave-valor. Los **diccionarios anidados** son diccionarios que se almacenan como valores dentro de otro diccionario. Ej.: un organigrama en el que las claves son los distintos departamentos y los valores son diccionarios de los empleados de un departamento dado. Para almacenar la información de los empleados de un departamento, se puede usar un diccionario cuyas claves son los ID de los empleados y cuyos valores son los nombres de los empleados. Las tablas siguientes describen la estructura de estos diccionarios anidados y cómo se puede acceder a los valores anidados.

**Ejemplo: Definir diccionarios anidados y acceder a sus elementos**

| Definición de diccionarios anidados |
|---|
| ```python<br>company_org_chart = {<br>  "Marketing": {<br>    "ID234": "Jane Smith"<br>  },<br>  "Sales": {<br>    "ID123": "Bob Johnson",<br>    "ID122": "David Lee"<br>  },<br>  "Engineering": {<br>    "ID303": "Radhika Potlapally",<br>    "ID321": "Maryam Samimi"<br>  }<br>}<br>``` |

| Acceso a los elementos de un diccionario anidado |
|---|
| ```python<br>print(company_org_chart["Sales"]["ID122"])<br>print(company_org_chart["Engineering"]["ID321"])<br>```<br>```python<br>David Lee<br>Maryam Samimi<br>``` |

**Conceptos en práctica: Estructura de los diccionarios anidados**

<!-- pregunta: CPL-ch10-m05-p01 -->

1. ¿Qué es un diccionario anidado en Python?

   - a) Un diccionario que contiene solo enteros como claves y valores.
   - b) Un diccionario que contiene otro diccionario como valor.
   - c) Un diccionario que contiene solo cadenas como claves y valores.
   - d) Un diccionario que contiene solo listas como claves y valores.

   <details><summary>Respuesta</summary>

   b) Un diccionario anidado contiene otro diccionario.

   </details>

<!-- pregunta: CPL-ch10-m05-p02 -->

2. ¿Cómo se puede acceder a un valor en un diccionario anidado en Python?

   - a) usando la clave del diccionario externo
   - b) usando la clave del diccionario interno
   - c) usando las claves de los diccionarios externo e interno

   <details><summary>Respuesta</summary>

   c) Se deben usar tanto la clave externa como la interna para indexar los diccionarios externo e interno, respectivamente, y obtener un valor interno.

   </details>

<!-- pregunta: CPL-ch10-m05-p03 -->

3. ¿Cuál es la sintaxis para crear un diccionario anidado en Python?

   - a) `{key: value}`
   - b) `{key1: {key2: value}}`
   - c) `{key: {value: key2}}`

   <details><summary>Respuesta</summary>

   b) Un diccionario anidado es un valor de otro diccionario, y representa los datos en una estructura de dos niveles.

   </details>

### Comprensión de diccionario

La **comprensión de diccionario** es una forma concisa y eficiente de crear un diccionario en Python. Con la comprensión de diccionario, los elementos de un objeto iterable se transforman en pares clave-valor. La sintaxis de la comprensión de diccionario es similar a la de la comprensión de listas, pero en lugar de corchetes se usan llaves para definir un diccionario.

Esta es la sintaxis general de la comprensión de diccionario:

**Sintaxis de la comprensión de diccionario**

```python norun
{key_expression: value_expression for element in iterable}
```

**Video:** [Squares of numbers](https://www.openstax.org/r/squares-of-numbers)

**Conceptos en práctica: Comprensión de diccionario**

<!-- pregunta: CPL-ch10-m05-p04 -->

1. ¿Cuál es la salida del código siguiente?
   
   ```python
   numbers = [1, 2, 3, 4, 5]
   my_dict = {x: x**2 for x in numbers if x % 2 == 0}
   print(my_dict)
   ```

   - a) `{1: 1, 3: 9, 5: 25}`
   - b) `{2: 4, 4: 16}`
   - c) `{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}`

   <details><summary>Respuesta</summary>

   b) Las claves del diccionario son los valores pares de la lista `numbers`, y los valores asociados son sus cuadrados.

   </details>

<!-- pregunta: CPL-ch10-m05-p05 -->

2. ¿Cuál es la salida de la siguiente comprensión de diccionario?
   
   ```python
   names = ["Alice ", "Bob ", "Charlie "]
   name_lengths = {name: len(name) for name in names}
   print(name_lengths)
   ```

   - a) `{ "Alice ": 5, "Bob ": 3, "Charlie ": 7}`
   - b) `{5: "Alice ", 3: "Bob ", 7: "Charlie "}`
   - c) `{ "A ": 5, "B ": 3, "C ": 7}`

   <details><summary>Respuesta</summary>

   a) Las claves del diccionario son los valores de cadena de la lista `names`, y los valores asociados son la longitud de cada cadena.

   </details>

<!-- pregunta: CPL-ch10-m05-p06 -->

3. ¿Cuál es la salida de la siguiente comprensión de diccionario?
   
   ```python
   my_dict = {i: i**2 for i in range(4)}
   print(my_dict)
   ```

   - a) `{0: 0, 1: 1, 2: 4, 3: 9}`
   - b) `{0: 0, 1: 1, 2: 4}`
   - c) `{1: 1, 2: 4, 3: 9}`

   <details><summary>Respuesta</summary>

   a) El diccionario se crea a partir de valores de clave desde 0 hasta 3 inclusive. Los valores asociados son los cuadrados de las claves.

   </details>

**Pruébalo: Precios de productos**

Supón que tienes un diccionario de precios de productos, donde las claves son los nombres de los productos y los valores son sus respectivos precios en dólares. Escribe un programa de Python que use la comprensión de diccionario para crear un nuevo diccionario con las mismas claves que el original, pero cuyos valores sean los precios en euros. Supón que el tipo de cambio es 1 dólar = 0.85 euros.

<!-- coderunner: ch10/CodeRunner_10_06_07_Product-prices -->

**Pruébalo: Reestructurar los datos de la empresa**

Supón que tienes un diccionario que contiene información sobre los empleados de una empresa. Cada empleado se identifica con un número de ID, y su información incluye su nombre, departamento y salario. Quieres crear un diccionario anidado que agrupe a los empleados por departamento, de modo que puedas ver fácilmente los nombres y los salarios de todos los empleados de cada departamento. Escribe un programa de Python que, dado un diccionario `employees`, produzca un diccionario anidado, `dept_employees`, que agrupe a los empleados por departamento.

```python norun
Input:
employees = {
  1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
  1002: {"name": "Bob", "department": "Sales", "salary": 50000},
  1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
  1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
  1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}
```

```python norun
Resulting dictionary:

{
"Engineering": {1001: {"name": "Alice", "salary": 75000}, 1003: {"name":
"Charlie", "salary": 80000}},
"Sales": {1002: {"name": "Bob", "salary": 50000}, 1005: {"name": "Eve",
"salary": 55000}},
"Marketing": {1004: {"name": "Dave", "salary": 60000}}
}
```

<!-- coderunner: ch10/CodeRunner_10_06_08_Restructuring-the-company-data -->

<!-- modulo: m00079 -->

## Resumen del capítulo

Los puntos más destacados de este capítulo son:

- Un diccionario en Python es un objeto contenedor que incluye pares clave-valor.
- El tipo `dict` implementa un diccionario en Python.
- Un diccionario no puede tener claves duplicadas.
- Un diccionario es un objeto mutable, pero las claves del diccionario deben ser objetos inmutables.
- Un diccionario se puede crear usando llaves o la función `dict()`.
- Los valores de un diccionario se pueden obtener mediante la notación con corchetes o el método `get()`.
- Los elementos, las claves y los valores de un diccionario se pueden obtener con los métodos `items()`, `keys()` y `values()`, respectivamente.
- Los elementos existentes se pueden modificar, o se pueden agregar elementos nuevos a un diccionario, usando la notación con corchetes o el método `update()`.
- Los elementos se pueden eliminar de un diccionario mediante la palabra clave `del` o el método `pop()`.
- Las instrucciones condicionales se pueden usar con un diccionario para comprobar si contiene claves, valores o pares clave-valor específicos.
- El bucle sobre un diccionario se puede hacer iterando sobre las claves, los valores o los elementos.
- Los diccionarios anidados son diccionarios que se almacenan como valores dentro de otro diccionario.
- Con la comprensión de diccionario, los elementos de un objeto iterable se transforman en pares clave-valor.

En este punto, deberías poder usar diccionarios en tus programas. La práctica de programación siguiente reúne la mayoría de los temas presentados en el capítulo.

**Referencia del capítulo 10.**

| Concepto | Descripción |
|---|---|
| Creación de un diccionario con llaves | ` my_dict = {key1:value1, key2:value2} ` |
| Creación de un diccionario con la función `dict()` | ```python<br># Usando una lista<br>my_list = [(key1, value1), (key2, value2)]<br>my_dict = dict(my_list)<br><br># Usando argumentos con nombre<br>my_dict = dict(key1=value1, key2=value2)<br><br># A partir de otro diccionario<br>old_dict = {key1: value1, key2: value2}<br>new_dict = dict(old_dict)<br>``` |
| Acceso a los elementos de un diccionario | ```python<br>my_dict = {key1: value1, key2: value2}<br><br># Acceso a un elemento con la notación de corchetes<br>my_dict[key1]<br><br># Acceso a un elemento con el método get()<br>my_dict.get(key1)<br>``` |
| Acceso a todos los elementos de un diccionario | ` my_dict.items() ` |
| Acceso a todas las claves de un diccionario | ` my_dict.keys() ` |
| Acceso a todos los valores de un diccionario | ` my_dict.values() ` |
| Agregar un nuevo par clave-valor o actualizar un par clave-valor existente | ```python<br>my_dict = {key1: value1, key2: value2}<br><br># Actualizar un elemento con la notación de corchetes<br>my_dict[key1] = new_value<br># Agregar un nuevo par clave-valor con la notación de corchetes<br>my_dict[key3] = value3<br><br># Actualizar un elemento con el método update()<br>my_dict.update({key1: new_value})<br># Agregar un nuevo par clave-valor con el método update()<br>my_dict.update({key3: value3})<br>``` |
| Eliminar un par clave-valor de un diccionario | ```python<br>my_dict = {key1: value1, key2: value2}<br><br># Usando la palabra clave del<br>del my_dict[key1]<br><br># Usando el método pop()<br>deleted_value = my_dict.pop(key1)<br>``` |
| Iterar sobre un diccionario | ```python<br>for key in dictionary: # Expresión del bucle<br>  # Instrucciones que se ejecutan en el bucle<br><br>#Instrucciones que se ejecutan después del bucle<br>``` |
| Diccionarios anidados | ```python<br>{<br>key_1:{key11:value11, key12:value12},<br>key_2:{key21:value21, key22:value22}<br>}<br>``` |
| Comprensión de diccionario | ` {key_expression: value_expression for element in iterable} ` |

**Pruébalo: Valores pares e impares**

Dada una lista, crea un diccionario con dos claves, `"even"` y `"odd"`. Los valores asociados con cada clave deben ser la lista de los valores pares e impares correspondientes de la lista dada.

```python norun
Input:
input_list = [3, 5, 6, 1]
```

```text
Prints {"even": [6], "odd":[3, 5, 1]}
```

<!-- coderunner: ch10/CodeRunner_10_07_09_Even-and-odd-values -->
