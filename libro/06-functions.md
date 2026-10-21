# Capítulo 6: Funciones

<!-- modulo: m00043 -->

## Introducción

![vista aérea de máquinas de videojuegos de arcade con personas jugando](media/Python_06_00_000.jpg)

*crédito: modificación de la obra «IMG_3037», de Jay Roc/Flickr, dominio público*

Las funciones son el siguiente paso para crear código optimizado como desarrollador de software. Si el mismo bloque de código se reutiliza repetidamente, una función permite al programador escribir el bloque una sola vez, ponerle un nombre y usar el código tantas veces como sea necesario llamando al bloque por su nombre. Las funciones pueden recibir valores y devolver valores para realizar tareas, incluidos cálculos complejos.

Al igual que las instrucciones de ramificación que se explicaron en el capítulo sobre decisiones, las funciones permiten distintos caminos de ejecución a través de un programa, y este capítulo analiza con más detalle el flujo de control y el ámbito de las variables.

<!-- modulo: m00044 -->

## 6.1 Definición de funciones

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar llamadas a función en un programa.
- Definir una función sin parámetros que muestre cadenas.
- Describir los beneficios de usar funciones.

### Llamar a una función

A lo largo del libro se han llamado funciones para realizar tareas. Por ejemplo, `print()` imprime valores y `sqrt()` calcula la raíz cuadrada. Una **función** es un bloque de código con nombre y reutilizable que realiza una tarea cuando se le llama.

**Video:** [Example: Simple math program](https://www.openstax.org/r/simple-math)

**Conceptos en práctica: Identificar llamadas a función**

<!-- pregunta: CPL-ch06-m01-p01 -->

1. ¿Qué línea tiene una llamada a función?
   
   ```python
   input_num = 14
   offset_num = input_num - 10
   print(offset_num)
   ```

   - a) línea 1
   - b) línea 2
   - c) línea 3

   <details><summary>Respuesta</summary>

   c) Se llama a la función `print()` para mostrar la variable `offset_num`.

   </details>

<!-- pregunta: CPL-ch06-m01-p02 -->

2. ¿Cuántas veces se llama a `print()`?
   
   ```python norun
   print("Please log in")
   username = input("Username:")
   password = input("Password:")
   print("Login successful")
   print("Welcome,", username)
   ```

   - a) 1
   - b) 3
   - c) 5

   <details><summary>Respuesta</summary>

   b) Las líneas 1, 4 y 5 llaman cada una a `print()` una vez. Las líneas 2 y 3 llaman a otra función, `input()`.

   </details>

<!-- pregunta: CPL-ch06-m01-p03 -->

3. ¿Cuántas llamadas a función hay?
   
   ```python norun
   # Usa float() para convertir la entrada del cálculo del área
   width = float(input("Enter width:"))
   height = float(input("Enter height:"))
   print("Area is", width*height)
   ```

   - a) 3
   - b) 5
   - c) 6

   <details><summary>Respuesta</summary>

   b) La línea 1 es un comentario que no se ejecuta. Las líneas 2 y 3 llaman cada una a `float()` y a `input()`. La línea 3 llama a `print()`, para un total de cinco llamadas a función.

   </details>

### Definir una función

Una función se define con la palabra clave **def**. La primera línea contiene `def` seguida del nombre de la función (en snake_case), paréntesis (con los parámetros, si los hay, que se explicarán más adelante) y dos puntos. El cuerpo con sangría comienza con una cadena de documentación (docstring) que describe la tarea de la función y contiene las instrucciones de la función. Una función debe definirse antes de llamarla.

**Video:** [Example: Welcome message function](https://www.openstax.org/r/welcome-message)

**Conceptos en práctica: Definir funciones**

<!-- pregunta: CPL-ch06-m01-p04 -->

1. ¿Qué tiene de malo la primera línea de la definición de la función?
   
   ```python norun
   def water_plant:
   ```

   - a) Un docstring debería ir después de los dos puntos.
   - b) Deberían ir paréntesis después de `water_plant`.
   - c) `def` debería ser `define` antes de `water_plant`.

   <details><summary>Respuesta</summary>

   b) La línea corregida es `def water_plant():`.

   </details>

<!-- pregunta: CPL-ch06-m01-p05 -->

2. ¿Cuál es la salida?
   
   ```python norun
   def print_phone_num():
     print("Phone: (", 864, ")", 555, "-", 0199)
   
   print("User info:")
   print_phone_num()
   ```

   - a) `Phone: ( 864 ) 555 - 1000`
      `User info:`
      `Phone: ( 864 ) 555 - 1000`
   - b) `User info:`
   - c) `User info:`
      `Phone: ( 864 ) 555 - 1000`

   <details><summary>Respuesta</summary>

   c) El programa principal muestra `"User info:"` y luego llama a `print_phone_num()`, que muestra el número de teléfono.

   </details>

<!-- pregunta: CPL-ch06-m01-p06 -->

3. ¿Qué instrucción llama a una función llamada `print_pc_specs()`?

   - a) `print_pc_specs`
   - b) `print_pc_specs()`
   - c) `print_pc_specs():`

   <details><summary>Respuesta</summary>

   b) Una llamada a función incluye el nombre de la función y los paréntesis.

   </details>

<!-- pregunta: CPL-ch06-m01-p07 -->

4. ¿Cuál es un nombre apropiado para una función que calcula los impuestos de un usuario?

   - a) `calc_tax`
   - b) `calculate user tax`
   - c) `c_t`

   <details><summary>Respuesta</summary>

   a) `calc_tax` es conciso, está en snake_case e indica la tarea de la función.

   </details>

### Beneficios de las funciones

Una función favorece la modularidad al reunir en un grupo separado las instrucciones de código relacionadas con una sola tarea. El cuerpo de una función puede ejecutarse repetidamente con varias llamadas a función, por lo que una función favorece la reutilización. El código modular y reutilizable es más fácil de modificar y puede compartirse entre programadores para evitar reinventar la rueda.

**Video:** [Improving a program with a function](https://www.openstax.org/r/improving-with-functions)

**Conceptos en práctica: Mejorar programas con funciones**

<!-- pregunta: CPL-ch06-m01-p08 -->

1. Si los puntos pasaran de floats a enteros, ¿cuántas instrucciones habría que cambiar en el programa original y en el revisado, respectivamente?

   - a) 3, 1
   - b) 4, 4
   - c) 12, 4

   <details><summary>Respuesta</summary>

   c) Cada cálculo usa cuatro instrucciones para leer los valores x, y de un par de puntos. El programa original realiza tres cálculos repitiendo código, para un total de 12 instrucciones de entrada. El programa revisado realiza tres cálculos ejecutando las cuatro instrucciones de entrada varias veces mediante llamadas a función.

   </details>

<!-- pregunta: CPL-ch06-m01-p09 -->

2. ¿Cuántas veces se puede llamar a `calc_distance()`?

   - a) 1
   - b) 3
   - c) muchas

   <details><summary>Respuesta</summary>

   c) El beneficio de la reutilización de una función se aprecia en que muchas llamadas a función reducen drásticamente la cantidad de código desordenado y redundante. Llamar a `calc_distance()` 10 veces equivale a 60 instrucciones en el programa original.

   </details>

**Pruébalo: Puesto de comida del cine**

Escribe una función, `concessions()`, que imprima las opciones de comida y bebida de un cine.

Dado:

```python norun
concessions()
```

La salida es:

```python norun
Food/Drink Options:
Popcorn: $8-10
Candy: $3-5
Soft drink: $5-7
```

<!-- coderunner: ch6/CodeRunner_06_02_01_Cinema-concession-stand -->

**Pruébalo: Indicador de términos y condiciones**

Escribe una función, `terms()`, que pida al usuario aceptar los términos y condiciones, lea `Y/N` y muestre una respuesta. En el programa principal, lee la cantidad de usuarios y llama a `terms()` para cada usuario.

Dadas las entradas `1` y `"Y"`, la salida es:

```text
Do you accept the terms and conditions?
Y
Thank you for accepting.
```

Dadas las entradas `2`, `"N"` y `"Y"`, la salida es:

```text
Do you accept the terms and conditions?
N
Have a good day.
Do you accept the terms and conditions?
Y
Thank you for accepting.
```

<!-- coderunner: ch6/CodeRunner_06_02_02_Terms-and-conditions-prompt -->

<!-- modulo: m00045 -->

## 6.2 Flujo de control

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar el flujo de control de un programa.
- Describir cómo se mueve el flujo de control entre instrucciones y llamadas a función.

### Flujo de control y funciones

El **flujo de control** es la secuencia de ejecución de un programa. El flujo de control de un programa comienza en el programa principal, pero rara vez sigue una secuencia estricta. Por ejemplo, el flujo de control salta líneas cuando no se ejecuta una instrucción condicional.

Cuando la ejecución llega a una llamada a función, el flujo de control pasa al lugar donde se define la función y ejecuta las instrucciones de la función. Luego, el flujo de control vuelve al lugar donde se llamó a la función y continúa la secuencia.

**Video:** [Calling a brunch menu function](https://www.openstax.org/r/brunch-menu)

**Conceptos en práctica: Seguir el flujo de control**

<!-- pregunta: CPL-ch06-m02-p01 -->

1. ¿Qué línea se ejecuta primero?
   
   ```python norun
   def park_greet():
     """Output greeting."""
     print("Welcome. Open sunrise to sunset.")
   
   car_count = 1
   park_greet()
   if car_count > 50:
     # Direct to extra parking lot
   ```

   - a) 1
   - b) 3
   - c) 5

   <details><summary>Respuesta</summary>

   c) La línea 5 es el inicio del programa principal, que no tiene sangría. `park_greet()` se llama en la línea 6 y se ejecuta.

   </details>

<!-- pregunta: CPL-ch06-m02-p02 -->

2. El flujo de control pasa a la línea 9 y se llama a `park_greet()`. ¿A qué línea pasa el flujo de control a continuación?
   
   ```python norun
   def extra_lot():
     # Function definition
   
   def park_greet():
     """Output greeting."""
     print("Welcome. Open sunrise to sunset.")
   
   car_count = 1
   park_greet()
   if car_count > 50:
     extra_lot()
   ```

   - a) 1
   - b) 4
   - c) 10

   <details><summary>Respuesta</summary>

   b) El flujo de control pasa al lugar donde se define `park_greet()`, en la línea 4.

   </details>

<!-- pregunta: CPL-ch06-m02-p03 -->

3. El flujo de control pasa a la línea 12 y se llama a `extra_lot()`. ¿A qué línea pasa el flujo de control después de ejecutar la línea 3?
   
   ```python
   def extra_lot():
     """Output extra parking lot info."""
     print("Take the second right to park.")
   
   def park_greet():
     """Output greeting."""
     print("Welcome. Open sunrise to sunset.")
   
   car_count = 1
   park_greet()
   if car_count > 50:
     extra_lot()
   ```

   - a) 5
   - b) 8
   - c) 12

   <details><summary>Respuesta</summary>

   c) El flujo de control regresa a la línea que llamó a la función. La línea 12 contiene la llamada a función a `extra_lot()`, así que el flujo de control regresa a la línea 12.

   </details>

<!-- pregunta: CPL-ch06-m02-p04 -->

4. ¿Cuál es la salida?
   
   ```python
   def park_greet():
     """Output greeting."""
     print("Welcome to the park")
   print("Open sunrise to sunset")
   
   park_greet()
   ```

   - a) `Welcome to the park`
   - b) `Welcome to the park`
      `Open sunrise to sunset`
   - c) `Open sunrise to sunset`
      `Welcome to the park`

   <details><summary>Respuesta</summary>

   c) El programa tiene un error de sangría. `print("Open ...")` no tiene sangría, así que la instrucción no forma parte de `park_greet()` y se ejecuta primero. Luego se llama a `park_greet()` y se ejecuta `print("Welcome ...")`.

   </details>

### Funciones que llaman a funciones

Con frecuencia las funciones llaman a otras funciones para que cada función realice una sola tarea y se mantenga así la modularidad. Por ejemplo, una función que calcula el total de un pedido puede llamar a una función que calcula el impuesto sobre las ventas. Cuando una función llamada desde otra función termina su ejecución, el flujo de control regresa a la función que la llamó.

**Video:** [Example: Book club email messages](https://www.openstax.org/r/email-messages)

**Conceptos en práctica: Funciones que llaman a funciones**

<!-- pregunta: CPL-ch06-m02-p05 -->

1. ¿Cuántas llamadas a función ocurren durante la ejecución del programa?

   - a) 2
   - b) 3
   - c) 6

   <details><summary>Respuesta</summary>

   c) El bucle `for` tiene tres iteraciones. Cada iteración llama a `print_book_club()`, que a su vez llama a `print_conf()`. Así que el programa llama a `print_book_club()` tres veces y a `print_conf()` tres veces.

   </details>

<!-- pregunta: CPL-ch06-m02-p06 -->

2. Cuando se alcanza y se ejecuta la línea 3, ¿a qué línea regresa el flujo de control?

   - a) 1
   - b) 11
   - c) 16

   <details><summary>Respuesta</summary>

   b) El flujo de control regresa a la línea 11, que llamó a `print_conf()`. Luego `print_book_club()` termina y el flujo de control regresa a la línea 16, que llamó a `print_book_club()`.

   </details>

**Pruébalo: Indicador actualizado de términos y condiciones**

Escribe una función actualizada, `terms()`, que pida al usuario aceptar los términos y condiciones, lea `Y/N` y muestre una respuesta llamando a `accepted()` o `rejected()`. `accepted()` imprime `"Thank you for accepting the terms."` y `rejected()` imprime `"You have rejected the terms. Thank you."`.

Dadas las entradas `2`, `"Y"` y `"N"`, la salida es:

```text
Do you accept the terms and conditions?
Y
Thank you for accepting the terms.
```

Dada una llamada a la función `terms()` y la entrada `"N"`, la salida es:

```text
Do you accept the terms and conditions?
N
You have rejected the terms. Thank you.
```

<!-- coderunner: ch6/CodeRunner_06_03_03_Updated-terms-and-conditions-prompt -->

**Pruébalo: Información de una lavandería**

Escribe un programa que use tres funciones para imprimir información sobre una lavandería, Liam's Laundry:

- `laundromat_info()`: imprime el nombre, Liam's Laundry, y el horario de atención, 7a - 11p, y llama a `washers_open()` y a `dryers_open()`
- `washers_open()`: lee un entero, lo asigna a `washer_count` y imprime `washer_count`
- `dryers_open()`: lee un entero, lo asigna a `dryer_count` y imprime `dryer_count`

El programa principal solo debe llamar a `laundromat_info()`.

Dadas las entradas `50` y `40`, la salida es:

```python norun
Liam's Laundry
7a - 11p
 Open washers: 50
 Open dryers: 40
```

<!-- coderunner: ch6/CodeRunner_06_03_04_Laundromat-information -->

<!-- modulo: m00046 -->

## 6.3 Ámbito de las variables

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar el ámbito de las variables de un programa.
- Analizar el impacto del ámbito de una variable.

### Ámbito global

El **ámbito** de una variable es la parte de un programa donde se puede acceder a la variable. Una variable creada fuera de una función tiene **ámbito global** y se puede acceder a ella en cualquier parte del programa. Un programa de Python comienza en el ámbito global, y el ámbito global dura toda la ejecución del programa.

**Video:** [Global variables in a program with a function](https://www.openstax.org/r/global-variables)

**Conceptos en práctica: Variables globales**

<!-- pregunta: CPL-ch06-m03-p01 -->

1. ¿Qué variables son globales?
   
   ```python norun
   num = float(input())
   num_sq = num * num
   print(num, "squared is", num_sq)
   ```

   - a) solo `num`
   - b) solo `num_sq`
   - c) `num` y `num_sq`

   <details><summary>Respuesta</summary>

   c) Tanto `num` como `num_sq` se crean fuera de las funciones y son variables globales.

   </details>

<!-- pregunta: CPL-ch06-m03-p02 -->

2. ¿Qué variables tienen ámbito global?
   
   ```python norun
   def print_square():
     num_sq = num * num
     print(num, "squared is", num_sq)
   
   num = float(input())
   print_square()
   ```

   - a) solo `num`
   - b) solo `num_sq`
   - c) `num` y `num_sq`

   <details><summary>Respuesta</summary>

   a) `num` se crea fuera de una función y es global. `num_sq` se crea en `print_square()` y no es global.

   </details>

<!-- pregunta: CPL-ch06-m03-p03 -->

3. ¿Qué funciones pueden acceder a `num`?
   
   ```python norun
   def print_double():
     num_d = num * 2
     print(num, "doubled is", num_d)
   
   def print_square():
     num_sq = num * num
     print(num, "squared is", num_sq)
   
   num = float(input())
   print_double()
   print_square()
   ```

   - a) `print_double()`
   - b) `print_square()`
   - c) `print_double()` y `print_square()`

   <details><summary>Respuesta</summary>

   c) `num` es global y se puede acceder a ella en cualquier parte del programa, incluidas `print_double()` y `print_square()`.

   </details>

### Ámbito local

Una variable creada dentro de una función tiene **ámbito local** y solo existe dentro de la función. No se puede acceder a una variable local fuera de la función en la que se creó. Cuando una función termina de ejecutarse, las variables locales de la función dejan de existir.

**Video:** [Global and local variables in a program with a function](https://www.openstax.org/r/global-and-local-variables)

**Conceptos en práctica: Variables locales**

<!-- pregunta: CPL-ch06-m03-p04 -->

1. ¿Qué variables son locales?
   
   ```python norun
   def print_time():
     out_str = "Time is " + str(hour) + ":" + str(min)
     print(out_str)
   
   hour = int(input())
   min = int(input())
   print_time()
   ```

   - a) `hour` y `min`
   - b) `out_str`
   - c) `hour`, `min` y `out_str`

   <details><summary>Respuesta</summary>

   b) `out_str` es la única variable declarada en `print_time()` y es una variable local.

   </details>

<!-- pregunta: CPL-ch06-m03-p05 -->

2. ¿Qué variables son locales?
   
   ```python norun
   def print_greeting():
     print(out_str)
   
   hour = int(input())
   min = int(input())
   if hour < 12:
     out_str = "Good morning"
   else:
     out_str = "Good day"
   print_greeting()
   ```

   - a) `hour` y `min`
   - b) `out_str`
   - c) ninguna

   <details><summary>Respuesta</summary>

   c) Se accede a `out_str` en `print_greeting()`, pero se crea en instrucciones fuera de `print_greeting()`.

   </details>

<!-- pregunta: CPL-ch06-m03-p06 -->

3. ¿Qué funciones acceden directamente a `out_str`?
   
   ```python norun
   def print_greeting():
     print("Good day,")
     print_time()
   
   def print_time():
     out_str = "Time is " + str(hour) + ":" + str(min)
     print(out_str)
   
   hour = int(input())
   min = int(input())
   print_greeting()
   ```

   - a) `print_greeting()`
   - b) `print_time()`
   - c) `print_greeting()` y `print_time()`

   <details><summary>Respuesta</summary>

   b) `print_time()` crea `out_str` como variable local. `out_str` solo está en ámbito en `print_time()` y no se puede acceder a ella en otro lugar.

   </details>

### Usar variables locales y globales juntas

Python permite que las variables globales y locales tengan el mismo nombre, lo que puede provocar un comportamiento inesperado del programa. Una función trata como variable local una variable que se edita dentro de la función, a menos que se indique lo contrario. Para editar una variable global dentro de una función, la variable debe declararse con la palabra clave `global`.

**Video:** [Editing global variables in a program with a function](https://www.openstax.org/r/editing-global-variables)

**Conceptos en práctica: Usar variables locales y globales**

<!-- pregunta: CPL-ch06-m03-p07 -->

1. ¿Cuál es la salida?
   
   ```python norun
   def update_hour():
     tmp = hour
     if is_dst:
       tmp += 1
     else:
       tmp -= 1
   
   is_dst = True
   hour = int(input("Enter hour: "))
   update_hour()
   print("New hour:", hour)
   ```

   - a) `New hour: 9`
   - b) `New hour: 10`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) La variable global hour no se edita en `update_hour()`. La variable local que se edita es `tmp`. `tmp` se descarta cuando `update_hour()` termina.

   </details>

<!-- pregunta: CPL-ch06-m03-p08 -->

2. ¿Cuál es la salida?
   
   ```python norun
   def update_hour():
     new_hour = hour
     if is_dst:
       new_hour += 1
     else:
       new_hour -= 1
   
   is_dst = True
   hour = int(input("Enter hour: "))
   update_hour()
   print("New hour:", new_hour)
   ```

   - a) `New hour: 9`
   - b) `New hour: 10`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) `new_hour` es una variable local a la que la instrucción print intenta acceder después de que `update_hour()` termina. `new_hour` está fuera de ámbito, por lo que se produce un error.

   </details>

<!-- pregunta: CPL-ch06-m03-p09 -->

3. ¿Cuál es la salida?
   
   ```python norun
   def update_hour():
     global new_hour
     new_hour = hour
     if is_dst:
       new_hour += 1
     else:
       new_hour -= 1
   
   is_dst = True
   hour = int(input("Enter hour: "))
   update_hour()
   print("New hour:", new_hour)
   ```

   - a) `New hour: 9`
   - b) `New hour: 10`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) La palabra clave `global` se puede usar para crear una variable global desde dentro de una función. `new_hour` tiene ámbito global y se puede acceder a ella fuera de `update_hour()`.

   </details>

**Beneficios de limitar el ámbito**

Un programador podría preguntar: «¿Por qué no hacer globales todas las variables para evitar errores de acceso?». Hacer global cada variable puede volver desordenado un programa. Por ejemplo, un programador que depura un programa grande descubre que una variable tiene el valor incorrecto. Si todo el programa puede modificar la variable, el error podría estar en cualquier parte del programa. Limitar el ámbito de una variable a lo estrictamente necesario y restringir el uso de variables globales hacen que un programa sea más fácil de depurar, mantener y actualizar.

**Pruébalo: Lanzamiento de un juego battle royale**

Escribe un programa que lea el modo de juego seleccionado y llame a una de dos funciones para iniciar el juego. Si la entrada es `"br"`, llama a `battle_royale()`. En caso contrario, llama a `practice()`.

`battle_royale()`:

- Lee la cantidad de jugadores.
- Calcula la cantidad de compañeros de equipo que aún faltan. Un equipo completo tiene 3 jugadores.
- Llama a la función `find_teammates()` con el número calculado.
- Imprime `"Match starting . . ."`.

`practice()`:

- Lee una cadena que representa el mapa deseado.
- Imprime `"Launching practice on [desired map]"`.

Nota: `find_teammates()` ya está provista y no es necesario editarla.

Dada la entrada:

```text
br
1
```

La salida es:

```text
Finding 2 players...
Match starting...
```

Dada la entrada:

```text
p
Queen's Canyon
```

La salida es:

```text
Launching practice on Queen's Canyon
```

<!-- coderunner: ch6/CodeRunner_06_04_05_Battle-royale-game-launch -->

<!-- modulo: m00047 -->

## 6.4 Parámetros

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar los argumentos y los parámetros de una función.
- Describir cómo afecta la mutabilidad a la manera en que una función puede modificar argumentos.

### Argumentos y parámetros

¿Qué pasa si un programador quiere escribir una función que imprima el contenido de una lista? Una buena práctica es pasar los valores directamente a una función en lugar de depender de variables globales. Un **argumento** de función es un valor que se pasa como entrada durante una llamada a función. Un **parámetro** de función es una variable que representa la entrada en la definición de la función. Nota: los términos «argumento» y «parámetro» a veces se usan indistintamente en la conversación y en la documentación.

**Video:** [Global and local variables in a program with a function](https://www.openstax.org/r/more-global-and-local-variables)

**Conceptos en práctica: Argumentos y parámetros**

<!-- pregunta: CPL-ch06-m04-p01 -->

1. ¿Cuál es un argumento?

   - a) `name`
   - b) `username`
   - c) `name` y `username`

   <details><summary>Respuesta</summary>

   b) `username` es el argumento que se pasa a `print_welcome()`. `name` es el parámetro de `print_welcome()` al que se le asigna el valor de `username`.

   </details>

<!-- pregunta: CPL-ch06-m04-p02 -->

2. ¿Cuál es un parámetro?

   - a) `name`
   - b) `username`
   - c) `name` y `username`

   <details><summary>Respuesta</summary>

   a) `name` es el único parámetro definido en `print_welcome()`. `username` es el argumento que se pasa en la llamada a función de la línea 5.

   </details>

<!-- pregunta: CPL-ch06-m04-p03 -->

3. ¿Cuál es el ámbito de `name`?

   - a) solo `print_welcome()`
   - b) todo el programa

   <details><summary>Respuesta</summary>

   a) `name` es un parámetro que existe solo dentro de una llamada a `print_welcome()`.

   </details>

<!-- pregunta: CPL-ch06-m04-p04 -->

4. ¿Qué pasaría si `username` se cambiara por `name` en las líneas 4 y 5?

   - a) la misma salida
   - b) error/salida incorrecta

   <details><summary>Respuesta</summary>

   a) El programa se ejecutaría correctamente. Los argumentos y los parámetros pueden tener el mismo nombre, y aun así se crearía en `print_welcome()` una variable local llamada `name`. El ámbito puede ser confuso con variables del mismo nombre.

   </details>

### Múltiples argumentos y parámetros

Las funciones pueden tener varios parámetros. Por ejemplo, una función usa dos parámetros, largo y ancho, para calcular la superficie en pies cuadrados de una habitación. Las llamadas a función deben usar el orden y la cantidad correctos de argumentos para evitar comportamientos no deseados y errores (salvo que se usen argumentos opcionales o argumentos con nombre, como se explicará más adelante).

**Ejemplo: Usar varios argumentos en una llamada a función**

```python norun
def print_div(op_1, op_2):
  """ Prints division operation """
  print(f"{op_1}/{op_2} = {op_1/op_2}")

num_1 = 6
num_2 = 3
print_div(num_1, num_2) # Imprime "6/3 = 2.0"
print_div(num_2, num_1) # Imprime "3/6 = 0.5"
print_div(num_1) # Error: falta el argumento op_2
```

**Conceptos en práctica: Múltiples argumentos y parámetros**

<!-- pregunta: CPL-ch06-m04-p05 -->

1. ¿Cuál es un argumento?

   - a) `p1_x`
   - b) `x1`

   <details><summary>Respuesta</summary>

   a) `p1_x` es el primer argumento usado en la llamada a función de la línea 9. `x1` se define como el primer parámetro de `calc_distance()`.

   </details>

<!-- pregunta: CPL-ch06-m04-p06 -->

2. ¿Cuál es un parámetro?

   - a) `p1_y`
   - b) `y1`

   <details><summary>Respuesta</summary>

   b) `y1` se define como el segundo parámetro de `calc_distance()`. `p1_y` es el segundo argumento de la llamada a función de la línea 9.

   </details>

<!-- pregunta: CPL-ch06-m04-p07 -->

3. ¿Cuál sería el valor de `x2` en la llamada a función `calc_distance(2, 4, 3, 6)`?

   - a) `2`
   - b) `4`
   - c) `3`
   - d) `6`
   - e) `Error`

   <details><summary>Respuesta</summary>

   c) `3` es un literal que se pasa como tercer argumento, que corresponde a `x2`, el tercer parámetro.

   </details>

### Modificar argumentos y mutabilidad

En Python, una variable es un nombre que hace referencia a un objeto almacenado en memoria, es decir, una referencia a objeto, por lo que Python usa un sistema de **paso por referencia de objeto**. Si un argumento se cambia en una función, los cambios se conservan o se pierden según la mutabilidad del objeto. Un objeto **mutable** se puede modificar después de su creación. Los cambios que una función hace al objeto aparecen entonces fuera de la función. Un objeto **inmutable** no se puede modificar después de su creación. Por lo tanto, una función debe hacer una copia local para modificarlo, y los cambios de la copia local no aparecen fuera de la función.

Los programadores deben tener cuidado al modificar los argumentos de una función, ya que estos efectos secundarios pueden dificultar la depuración y el mantenimiento de los programas.

**Ejemplo: Convertir temperaturas**

¿Cuáles son los valores de `weekend_temps` y `type` después de que `convert_temps()` termina?

```python
def convert_temps(temps, unit):
  if unit == "F":
    for i in range(len(temps)):
      temps[i] = (temps[i]-32) * 5/9
    unit = "C"
  else:
    for i in range(len(temps)):
      temps[i] = (temps[i]*9/5) + 32
    unit = "F"

# Temperaturas del fin de semana en grados Fahrenheit.
wknd_temps = [49.0, 51.0, 44.0]
deg_sign = u"\N{DEGREE SIGN}" # Unicode
metric = "F"

# Convertir de Fahrenheit a Celsius.
convert_temps(wknd_temps, metric)
for temp in wknd_temps:
  print(f"{temp:.2f}{deg_sign}{metric}", end=" ")
```

La salida es `9.44°F 10.56°F 6.67°F`. `type` se cambió a `"C"` dentro de la función, pero no conservó el cambio fuera de la función. ¿Por qué se conserva el cambio del argumento de tipo lista y no el del argumento de tipo cadena? (Pista: una lista es mutable. Una cadena es inmutable.)

**Video:** [Exploring a faulty function](https://www.openstax.org/r/faulty-function)

**Conceptos en práctica: Mutabilidad y argumentos de función**

<!-- pregunta: CPL-ch06-m04-p10 -->

1. En `convert_temps()`, `wknd_temps` y `temps` hacen referencia a ________ en memoria.

   - a) el mismo objeto
   - b) objetos distintos

   <details><summary>Respuesta</summary>

   a) Una lista es mutable, por lo que el objeto al que hacen referencia `wknd_temps` y `temps` se modifica sin necesidad de una copia local.

   </details>

<!-- pregunta: CPL-ch06-m04-p08 -->

2. Después de asignar `"C"` a `unit`, `metric` y `unit` hacen referencia a ________ en memoria.

   - a) el mismo objeto
   - b) objetos distintos

   <details><summary>Respuesta</summary>

   b) Una cadena es inmutable, por lo que `convert_temps()` crea un objeto nuevo al que `unit` hace referencia.

   </details>

<!-- pregunta: CPL-ch06-m04-p09 -->

3. `deg_sign` es una cadena cuyo valor no puede cambiar una vez creada. `deg_sign` es ________.

   - a) inmutable
   - b) mutable

   <details><summary>Respuesta</summary>

   a) El valor de un objeto inmutable no se puede cambiar.

   </details>

<!-- pregunta: CPL-ch06-m04-p11 -->

4. En la línea 16, `unit` ________.

   - a) hace referencia a un objeto con el valor `"C"`
   - b) no existe

   <details><summary>Respuesta</summary>

   b) `unit` ya no existe después de que `convert_temps()` termina y regresa a la línea 14.

   </details>

**Pruébalo: Imprimir el área de un triángulo rectángulo**

Escribe una función, `print_area()`, que reciba la base y la altura de un triángulo rectángulo e imprima el área del triángulo. El área de un triángulo rectángulo es (bh)/(2), donde b es la base y h es la altura.

Dada la entrada:

```text
3
4
```

La salida es:

```text
Triangle area: 6.0
```

<!-- coderunner: ch6/CodeRunner_06_05_06_Printing-right-triangle-area -->

**Pruébalo: Ajustar las calificaciones**

Escribe una función, `print_scores()`, que reciba una lista de calificaciones de un examen y un número que represente cuántos puntos sumar. Para cada calificación, imprime la calificación original y la suma de la calificación y la bonificación. Asegúrate de no cambiar la lista.

Dada la llamada a función:

```python norun
print_scores([67, 68, 72, 71, 69], 10)
```

La salida es:

```text
67 would be updated to 77
68 would be updated to 78
72 would be updated to 82
71 would be updated to 81
69 would be updated to 79
```

<!-- coderunner: ch6/CodeRunner_06_05_07_Curving-scores -->

<!-- modulo: m00048 -->

## 6.5 Valores de retorno

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar el valor de retorno de una función.
- Emplear instrucciones return en las funciones para devolver valores.

### Regresar de una función

Cuando una función termina, regresa y proporciona un resultado al código que la llamó. Una **instrucción return** termina la ejecución de la función y puede especificar un valor para devolver a quien la llamó. Las funciones presentadas hasta ahora no han tenido una instrucción `return`, lo cual equivale a devolver `None`, que representa la ausencia de valor.

**Video:** [Returning a value from a function](https://www.openstax.org/r/returning-value-from-function)

**Conceptos en práctica: Usar instrucciones return**

<!-- pregunta: CPL-ch06-m05-p01 -->

1. ¿Qué devuelve `calc_mpg(miles, gallons)`?
   
   ```python
   def calc_mpg(miles, gallons):
     mpg = miles/gallons
     return mpg
   ```

   - a) `mpg`
   - b) `None`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) `calc_mpg()` especifica con la instrucción `return` que se devuelva `mpg`.

   </details>

<!-- pregunta: CPL-ch06-m05-p02 -->

2. ¿Qué devuelve `calc_sqft()`?
   
   ```python
   def calc_sqft(length, width):
     sqft = length * width
     return
   ```

   - a) `sqft`
   - b) `None`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `return` es una instrucción válida para terminar la función y regresar al código que la llamó sin un valor especificado. `calc_sqft()` debería devolver `sqft` con la línea `return sqft`.

   </details>

<!-- pregunta: CPL-ch06-m05-p03 -->

3. ¿Cuál es la diferencia entre `hw_1()` y `hw_2()`?
   
   ```python
   def hw_1():
     print("Hello world!")
     return
   
   def hw_2():
     print("Hello world!")
   ```

   - a) `hw_1()` devuelve una cadena, `hw_2()` no
   - b) `hw_1()` devuelve `None`, `hw_2()` no
   - c) ninguna diferencia

   <details><summary>Respuesta</summary>

   c) Si no se especifica el valor de retorno ni la instrucción `return`, la función devuelve `None`.

   </details>

### Usar varias instrucciones return

Las funciones que tienen varios caminos de ejecución pueden usar varias instrucciones `return`. Por ejemplo, una función con una instrucción `if-else` puede tener dos instrucciones `return`, una para cada rama. Las instrucciones `return` siempre terminan la función y devuelven el flujo de control al código que la llamó.

En la tabla siguiente, `calc_mpg()` recibe las millas recorridas y los galones de gasolina usados, y calcula las millas por galón de un automóvil. `calc_mpg()` comprueba si los galones son `0` (para evitar la división entre 0) y, de ser así, devuelve `-1`, un valor que suele usarse para indicar un problema.

**Cálculo de millas por galón y comprobación de la división entre cero.**

|  |  |
|---|---|
| ```python<br>def calc_mpg(miles, gallons):<br>  if gallons > 0:<br>    mpg = miles/gallons<br>    return mpg<br>  else:<br>    print("Gallons can't be 0")<br>    return -1<br><br>car_1_mpg = calc_mpg(448, 16)<br>print("Car 1's mpg is", car_1_mpg)<br>car_2_mpg = calc_mpg(300, 0)<br>print("Car 2's mpg is", car_2_mpg)<br>``` | ```python<br>Car 1's mpg is 28.0<br>Gallons can't be 0<br>Car 2's mpg is -1<br>``` |

**Conceptos en práctica: Varias instrucciones return**

<!-- pregunta: CPL-ch06-m05-p04 -->

1. ¿Qué devuelve `yarn_weight(3)`?
   
   ```python
   def yarn_weight(num):
     if num == 0:
       return "lace"
     elif num == 1:
       return "sock"
     elif num == 2:
       return "sport"
     elif num == 3:
       return "dk"
     elif num == 4:
       return "worsted"
     elif num == 5:
       return "bulky"
     else:
       return "super bulky"
   ```

   - a) `"lace"`
   - b) `"dk"`
   - c) `"super bulky"`

   <details><summary>Respuesta</summary>

   b) `num == 3` es `True`, así que se ejecuta la instrucción `return "dk"`.

   </details>

<!-- pregunta: CPL-ch06-m05-p05 -->

2. ¿Cuál es la salida?
   
   ```python
   def inc_volume(level, max):
     if level < max:
       return level
       level += 1
     else:
       return level
   
   vol1 = inc_volume(9, 10)
   print(vol1)
   vol2 = inc_volume(10, 10)
   print(vol2)
   ```

   - a)

     ```python
     9
     10
     ```

   - b)

     ```python
     10
     10
     ```

   - c)

     ```python
     10
     11
     ```

   <details><summary>Respuesta</summary>

   a) En `inc_volume(9,10)`, `return level` devuelve `9`, y `level += 1` nunca se alcanza.

   </details>

### Usar funciones como valores

Las funciones son objetos que se evalúan como valores, por lo que las llamadas a función se pueden usar en expresiones. Una llamada a función se puede combinar con otras llamadas a función, variables y literales siempre que el valor de retorno sea compatible con la operación.

**Video:** [Using function calls in expressions](https://www.openstax.org/r/function-calls-in-expressions)

**Conceptos en práctica: Usar valores de función**

<!-- pregunta: CPL-ch06-m05-p06 -->

1. ¿Cuál es el valor actualizado de `bill`?
   
   ```python
   def tax(total):
     return .06 * total
   
   def auto_tip(total):
     return .2 * total
   
   bill = 100.0
   bill += tax(bill) + auto_tip(bill)
   ```

   - a) `26.0`
   - b) `126.0`

   <details><summary>Respuesta</summary>

   b) `bill += tax(bill) + auto_tip(bill)` se evalúa como `bill += 6.0 + 20.0`, luego como `bill = 100.0 + 6.0 + 20.0` y finalmente como 126.0.

   </details>

<!-- pregunta: CPL-ch06-m05-p07 -->

2. ¿Cuál es el valor de `val2`?
   
   ```python
   def sq(num):
     return num * num
   
   def offset(num):
     return num - 2
   
   val = 5
   val2 = sq(offset(val))
   ```

   - a) `9`
   - b) `23`

   <details><summary>Respuesta</summary>

   a) `val2 = sq(offset(5))` se evalúa como `val2 = sq(3)` y luego como 9.

   </details>

**Pruébalo: Días de vida estimados**

Escribe una función, `days_alive()`, que reciba una edad en años y muestre como entero la cantidad estimada de días que el usuario ha vivido. Supón que cada año tiene 365.24 días. Usa `round()`, que recibe un número y devuelve el número entero más cercano.

Luego escribe un programa principal que lea la edad de un usuario y muestre el resultado de `days_alive()`.

Dada la entrada:

```text
21
```

La salida es:

```text
You have been alive about 7670 days.
```

<!-- coderunner: ch6/CodeRunner_06_06_08_Estimated-days-alive -->

**Pruébalo: Promedio de listas**

Escribe una función, `avg_list()`, que reciba una lista y devuelva el promedio de los valores de la lista.

<!-- coderunner: ch6/CodeRunner_06_06_09_Averaging-lists -->

<!-- modulo: m00049 -->

## 6.6 Argumentos con nombre

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir la diferencia entre argumentos posicionales y argumentos con nombre.
- Crear funciones que usen argumentos posicionales, argumentos con nombre y valores de parámetro predeterminados.

### Argumentos con nombre

Hasta ahora, las funciones se han llamado con **argumentos posicionales**, que son argumentos que se asignan a los parámetros en orden. Python también permite **argumentos con nombre**, que son argumentos que usan los nombres de los parámetros para asignar valores en lugar del orden. Al mezclar argumentos posicionales y con nombre, los argumentos posicionales deben ir primero, en el orden correcto, antes de cualquier argumento con nombre.

**Video:** [Using keyword arguments](https://www.openstax.org/r/keyword-arguments)

**Conceptos en práctica: Usar argumentos con nombre y posicionales**

<!-- pregunta: CPL-ch06-m06-p01 -->

1. ¿Cuál es el argumento posicional en `greeting(count=1, name="Ash", msg="Hiya")`?

   - a) `count=1`
   - b) `name="Ash"`
   - c) `msg="Hiya"`
   - d) Ninguno

   <details><summary>Respuesta</summary>

   d) La llamada a función usa solo argumentos con nombre para asignar valores a los parámetros con nombre.

   </details>

<!-- pregunta: CPL-ch06-m06-p02 -->

2. ¿Cuál es la salida de `greeting(count=2, name="Ash", msg="Hiya")`?

   - a) `Ash Hiya`
      `Ash Hiya`
   - b) `Hiya Ash`
      `Hiya Ash`

   <details><summary>Respuesta</summary>

   b) `"Hiya"` es el valor de `msg` y `"Ash"` es el valor de `name` en la función.

   </details>

<!-- pregunta: CPL-ch06-m06-p03 -->

3. ¿Cuál es el argumento posicional en `greeting("Welcome", count=1, name="Anita")`?

   - a) `"Welcome"`
   - b) `count=1`
   - c) `name="Anita"`

   <details><summary>Respuesta</summary>

   a) `"Welcome"` no tiene nombre y se asigna correctamente a count. Los argumentos posicionales deben ir antes que los argumentos con nombre.

   </details>

<!-- pregunta: CPL-ch06-m06-p04 -->

4. ¿Qué llamada a función produciría un error?

   - a) `greeting("Morning", "Morgan", count=3)`
   - b) `greeting(count=1,"Hi", "Bea")`
   - c) `greeting("Cheers", "Colleagues", 10)`

   <details><summary>Respuesta</summary>

   b) Los argumentos posicionales, `"Hi"` y `"Bea"`, van después del argumento con nombre `count=1`, lo que produce un error.

   </details>

### Valores de parámetro predeterminados

Las funciones pueden definir valores de parámetro predeterminados para usarlos si no se proporciona un argumento posicional o con nombre para el parámetro. Por ejemplo, `def season(m, d, hemi="N"):` define el valor predeterminado `"N"` para el parámetro hemi. Nota: los valores de parámetro predeterminados se definen una sola vez para que la función los use, por lo que no se deben usar objetos mutables (como las listas) como valores predeterminados.

El siguiente ejemplo de física calcula el peso como una fuerza en newtons, dadas la masa en kilogramos y la aceleración en (m)/(s^2). La gravedad en la Tierra es de 9.8 (m)/(s^2), y la gravedad en Marte es de 3.7 (m)/(s^2).

**Video:** [Using default parameter values](https://www.openstax.org/r/default-parameter-values)

**Conceptos en práctica: Usar valores de parámetro predeterminados**

<!-- pregunta: CPL-ch06-m06-p05 -->

1. ¿Qué parámetros tienen valores predeterminados?

   - a) `msg`
   - b) `name` y `count`
   - c) todos

   <details><summary>Respuesta</summary>

   b) El valor predeterminado de `name` es `"Friend"`, y el valor predeterminado de `count` es `1`. `msg` no tiene valor predeterminado.

   </details>

<!-- pregunta: CPL-ch06-m06-p06 -->

2. ¿Qué llamada a función es correcta?

   - a) `greeting()`
   - b) `greeting(name="Gina")`
   - c) `greeting("Greetings")`

   <details><summary>Respuesta</summary>

   c) `msg` es un argumento obligatorio al que se asigna `"Greetings"`. `name` y `count` usan los valores predeterminados. Se imprime `"Greetings Friend"`.

   </details>

<!-- pregunta: CPL-ch06-m06-p07 -->

3. ¿Cuál es la salida de `greeting(count=0, msg="Hello")`?

   - a) `Hello Friend`
   - b) nada
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `msg="Hello"`, `name="Friend"` y `count=0`, así que la llamada es válida. La función se ejecuta, pero no entra en el bucle `for` porque `count=0`.

   </details>

**Recomendaciones de PEP 8: espaciado**

La guía de estilo PEP 8 recomienda no poner espacios alrededor de `=` al indicar argumentos con nombre y valores de parámetro predeterminados.

**Pruébalo: Donaciones en una transmisión**

Escribe una función, `donate()`, que permita a un espectador en línea enviar una donación a un streamer. `donate()` tiene tres parámetros:

- `amount`: monto a donar, valor predeterminado: 5
- `name`: nombre del donante, valor predeterminado: `"Anonymous"`
- `msg`: mensaje del donante, valor predeterminado: `""`

Dado:

```python norun
donate(10, "gg")
```

La salida es:

```text
Anonymous donated 10 credits: gg
```

Escribe llamadas a función que usen los valores predeterminados junto con argumentos posicionales y con nombre.

<!-- coderunner: ch6/CodeRunner_06_07_10_Stream-donations -->

<!-- modulo: m00050 -->

## Resumen del capítulo

Los puntos destacados de este capítulo incluyen:

- Las funciones son bloques de código con nombre que realizan tareas cuando se les llama y hacen que los programas estén más organizados y optimizados.
- El flujo de control es la secuencia de ejecución de un programa. El flujo de control se mueve entre el código que llama y el código de la función cuando se llama a una función.
- El ámbito de una variable se refiere a dónde se puede acceder a la variable. Se puede acceder a las variables globales en cualquier parte de un programa. Las variables locales tienen un ámbito limitado, por ejemplo, a una función.
- Los parámetros son las entradas de una función, definidas junto con la función. Los argumentos son valores que el código que llama pasa a la función como entrada. A los parámetros se les asignan los valores de los argumentos.
- Las llamadas a función pueden usar argumentos posicionales para asociar valores con parámetros en orden.
- Las llamadas a función pueden usar argumentos con nombre para asociar valores usando los nombres de los parámetros en cualquier orden.
- Las funciones pueden definir valores de parámetro predeterminados para permitir argumentos opcionales en las llamadas a función.
- Python usa un sistema de paso por referencia de objeto para asignar a los parámetros los valores de los objetos a los que hacen referencia los argumentos.
- Las funciones pueden usar instrucciones `return` para devolver valores al código que las llamó.

En este punto, deberías poder escribir funciones que tengan cualquier cantidad de parámetros y devuelvan un valor, y programas que llamen a funciones usando argumentos con nombre y argumentos opcionales.

**Referencia del capítulo 6.**

| Construcción | Descripción |
|---|---|
| Definición de función | ```python<br>def function_name():<br>  """Docstring"""<br>  # Cuerpo de la función<br>``` |
| Parámetro | ```python<br>def function_name(parameter_1):<br>  # Cuerpo de la función<br>``` |
| Argumento | ```python<br>def function_name(parameter_1):<br>  # Cuerpo de la función<br><br>function_name(argument_1)<br>``` |
| Instrucción return | ```python<br>def function_name():<br>  # Cuerpo de la función<br>  return result # Devuelve el valor de result a quien llama<br>``` |
| Variables (ámbito) | ```python<br>def function_name(parameter_1):<br>  # Cuerpo de la función<br>  local_var = parameter_1 * 5<br>  return local_var<br><br>global_var = function_name(arg_1)<br>``` |
| Argumentos con nombre | ```python<br>def function_name(parameter_1, parameter_2):<br>  # Cuerpo de la función<br><br>function_name(parameter_2 = 5, parameter_1 = 2)<br>``` |
| Valor de parámetro predeterminado | ```python<br>def function_name(parameter_1 = 100):<br>  # Cuerpo de la función<br>``` |
