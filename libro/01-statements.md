# Capítulo 1: Instrucciones

<!-- modulo: m00001 -->

## Introducción

![Foto de un teclado mecánico y una pantalla de computadora, con parte del documento de especificación de Python en la pantalla.](media/CPL_01_00_000.jpg)

*crédito: Larissa Chu, CC BY 4.0*

Las computadoras y los programas están en todas partes en el mundo actual. Los programas influyen en muchos aspectos de la vida diaria y de la sociedad en su conjunto. Las personas dependen de los programas para comunicarse, comprar, entretenerse, recibir atención médica y para otras innumerables necesidades. Aprender a programar computadoras abre la puerta a muchas carreras y oportunidades para construir un mundo mejor.

Los programas constan de instrucciones que se ejecutan una tras otra. Una **instrucción** describe alguna acción que debe llevarse a cabo.

La instrucción `print("Good morning")` le indica a Python que muestre el mensaje `"Good morning"` al usuario. La instrucción `count = 0` le indica a Python que asigne el entero `0` a la variable `count`.

Este capítulo presenta instrucciones para la entrada y la salida, la asignación de variables y la aritmética básica. Cometer errores es una parte normal de la programación, y el capítulo incluye consejos para entender los mensajes de error. El capítulo termina con una breve historia de Python y explica por qué Python se ha vuelto tan popular hoy en día.

<!-- modulo: m00002 -->

## 1.1 Antecedentes

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Nombrar dos ejemplos de programas de computadora en la vida cotidiana.
- Explicar por qué Python es un buen lenguaje de programación para aprender.

### Programas de computadora

Una **computadora** es un dispositivo electrónico que almacena y procesa información. Algunos ejemplos de computadoras son los teléfonos inteligentes, las tabletas, las laptops, las computadoras de escritorio y los servidores. Técnicamente, un **programa** es una secuencia de instrucciones que una computadora puede ejecutar. Los programas ayudan a las personas a realizar tareas cotidianas, crear nueva tecnología y divertirse.

El objetivo de este libro es enseñar programación introductoria y resolución de problemas. Escribir programas es una actividad creativa, útil por sí misma y gratificante. No se necesitan conocimientos previos de informática para leer este libro. Existen muchos tipos de programas, como se muestra en la ilustración siguiente. Este libro se centrará en los programas de propósito general que normalmente se ejecutan «entre bambalinas».

**Video:** [Online music streaming](https://www.openstax.org/r/music-streaming)

**Conceptos en práctica: Computadoras y programas**

<!-- pregunta: CPL-ch01-m01-p01 -->

1. ¿Cuántos tipos de programas se describieron en la animación?

   - a) 3
   - b) 4
   - c) 5

   <details><summary>Respuesta</summary>

   b) Cada imagen de la animación representa un tipo distinto de programa de computadora.

   </details>

<!-- pregunta: CPL-ch01-m01-p02 -->

2. ¿Qué tipo de programa explicará este libro cómo escribir?

   - a) una herramienta que resume las preferencias musicales de una persona
   - b) una aplicación móvil para administrar y compartir listas de reproducción de canciones
   - c) un sitio web que muestra los artistas más escuchados de los últimos cinco años

   <details><summary>Respuesta</summary>

   a) Este tipo de análisis requiere conocimientos básicos de programación.

   </details>

<!-- pregunta: CPL-ch01-m01-p03 -->

3. ¿Cuál de los siguientes dispositivos es un ejemplo de computadora?

   - a) unos audífonos con cable que se conectan a un teléfono inteligente
   - b) un control remoto que pausa o salta la canción actual
   - c) un altavoz wi-fi que transmite música desde Amazon

   <details><summary>Respuesta</summary>

   c) Al igual que las aplicaciones móviles, los altavoces wi-fi ejecutan pequeños programas que se conectan a servidores.

   </details>

<!-- pregunta: CPL-ch01-m01-p04 -->

4. Leer este libro requiere una sólida formación en matemáticas.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   b) Este libro supone que los lectores comprenden los fundamentos del álgebra, pero nada demasiado difícil.

   </details>

**Para saber más**

Los capítulos posteriores de este libro muestran cómo escribir programas de análisis con datos reales. Algunos ejemplos de bibliotecas que dan acceso a servicios de transmisión en línea son [**Spotipy**](https://openstax.org/r/100spotipy), [**Pytube**](https://openstax.org/r/100pytube) y [**Pydora**](https://openstax.org/r/100pydora). Las herramientas relacionadas con Python suelen tener las letras «py» en su nombre.

### El lenguaje Python

Este libro presenta [Python](https://openstax.org/r/100python), uno de los principales lenguajes de programación de la actualidad. Grandes empresas tecnológicas como Google, Apple, la NASA, Instagram, Pixar y otras usan Python extensamente.

Una de las razones por las que Python es popular es que existen muchas bibliotecas para hacer trabajo real. Una **biblioteca** es una colección de código que se puede usar en otros programas. Python incluye una extensa [biblioteca estándar](https://openstax.org/r/100pythlibrary) para resolver problemas informáticos cotidianos, como extraer datos de archivos y crear informes resumidos. Además, la comunidad desarrolla muchas otras bibliotecas para Python. Ej.: [pandas](https://openstax.org/r/100pandas) es una biblioteca muy usada para el análisis de datos.

Otra razón por la que Python es popular es que su sintaxis es concisa y directa. La **sintaxis** de un lenguaje define cómo debe estructurarse el código. Las reglas de sintaxis definen las palabras clave, los símbolos y el formato que se usan en los programas. En comparación con otros lenguajes de programación, Python es más conciso y directo.

**Ejemplo: Hola mundo en Python y Java**

Por tradición, [Hello World](https://openstax.org/r/100helloworld) es el primer programa que se escribe al aprender un lenguaje nuevo. Este programa simplemente muestra el mensaje `"Hello, World!"` al usuario. El programa hola mundo tiene una sola línea en Python:

```python
print("Hello, World!")
```

En cambio, el programa hola mundo tiene cinco líneas en Java (un lenguaje distinto).

```python norun
public class Hello {
  public static void main(String[] args) {
   System.out.println("Hello, World!");
  }
}
```

Sin embargo, la concisión no es la única consideración al elegir un lenguaje. En diferentes situaciones, distintos lenguajes pueden ser más apropiados. Ej.: Java se usa a menudo en el desarrollo para Android.

**Video:** [Counting lines in a file](https://www.openstax.org/r/counting-lines)

**Conceptos en práctica: Sintaxis de Python frente a Java**

<!-- pregunta: CPL-ch01-m01-p05 -->

1. En general, los programas de Python son _____ que los programas de Java.

   - a) más rápidos
   - b) más largos
   - c) más cortos

   <details><summary>Respuesta</summary>

   c) La sintaxis de Python es más concisa que la de Java.

   </details>

<!-- pregunta: CPL-ch01-m01-p06 -->

2. En los programas de ejemplo anteriores, ¿qué sintaxis que exige Java no exige Python?

   - a) punto y coma
   - b) paréntesis
   - c) comillas

   <details><summary>Respuesta</summary>

   a) Python no exige un punto y coma al final de cada línea. Tampoco exige llaves.

   </details>

**Pruébalo: Canción favorita**

El programa siguiente pide tu nombre y muestra un saludo amistoso. Ejecuta el programa y observa qué sucede. En el mensaje de error, EOF significa End of File (fin de archivo).

- Muchos de los programas de este capítulo esperan una entrada del usuario. Escribe tu nombre en el cuadro Input que está debajo del código. Ejecuta el programa de nuevo y observa qué cambia.
- Copia las siguientes líneas al final del programa:

  ```python norun
  print("What is your favorite song?")

song = input()

print("Cool! I like", song, "too.")
  ```
- El programa modificado lee dos líneas de entrada: `name` y `song`. Agrega tu canción favorita al cuadro Input, debajo de tu nombre, y ejecuta el programa de nuevo.

La siguiente sección del libro explicará cómo funcionan `print()` e `input()`. Siéntete libre de experimentar con este código hasta que estés listo para continuar.

<!-- coderunner: ch1/CodeRunner_01_02_01_Favorite-song -->

<!-- modulo: m00003 -->

## 1.2 Entrada/salida

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Mostrar una salida con la función `print()`.
- Obtener la entrada del usuario con la función `input()`.

### Salida básica

La función **`print()`** muestra una salida al usuario. La **salida** es la información o el resultado que produce un programa. Se pueden usar las opciones `sep` y `end` para personalizar la salida. La tabla siguiente muestra ejemplos de `sep` y `end`.

Se pueden imprimir varios valores, separados por comas, en la misma instrucción. De forma predeterminada, cada valor se separa con un espacio en la salida. La opción `sep` permite cambiar este comportamiento.

De forma predeterminada, la función `print()` agrega un carácter de salto de línea al final de la salida. Un carácter de **salto de línea** le indica a la pantalla que pase a la línea siguiente. La opción `end` permite continuar imprimiendo en la misma línea.

**Ejemplos de uso de `print()`.**

| Código | Salida |
|---|---|
| `print("Today is Monday.")`  <br>`print("I like string beans.")` | `Today is Monday.`  <br>`I like string beans.` |
| `print("Today", "is", "Monday")`  <br>`print("Today", "is", "Monday", sep="...")` | `Today is Monday`  <br>`Today...is...Monday` |
| `print("Today is Monday, ", end="")`  <br>`print("I like string beans.")` | `Today is Monday, I like string beans.` |
| `print("Today", "is", "Monday", sep="? ", end="!!")`  <br>`print("I like string beans.")` | `Today? is? Monday!!I like string beans.` |

**Video:** [Displaying output to the user](https://www.openstax.org/r/displaying-output)

**Conceptos en práctica: La función print()**

<!-- pregunta: CPL-ch01-m02-p01 -->

1. ¿Qué línea de código imprime `Hello world!` como una sola línea de salida?

   - a) `print(Hello world!)`
   - b) `print("Hello", "world", "!")`
   - c) `print("Hello world!")`

   <details><summary>Respuesta</summary>

   c) El programa hola mundo es solo una línea de código.

   </details>

<!-- pregunta: CPL-ch01-m02-p02 -->

2. ¿Qué líneas de código imprimen `Hello world!` como una sola línea de salida?

   - a)

     ```python
     print("Hello")
     print(" world!")
     ```

   - b)

     ```python
     print("Hello")
     print(" world!", end="")
     ```

   - c)

     ```python
     print("Hello", end="")
     print(" world!")
     ```

   <details><summary>Respuesta</summary>

   c) La opción `end=""` elimina el carácter de salto de línea después de hello, y produce `Hello world!` en la misma línea.

   </details>

<!-- pregunta: CPL-ch01-m02-p03 -->

3. ¿Qué salida produce la siguiente instrucción?
   
   ```python
   print("555", "0123", sep="-")
   ```

   - a) `555 0123`
   - b) `5550123-`
   - c) `555-0123`

   <details><summary>Respuesta</summary>

   c) El carácter de espacio predeterminado que separa varios elementos se reemplazó por el guion.

   </details>

**¿De verdad importan los espacios?**

Los espacios y los saltos de línea no son importantes por sí mismos. Sin embargo, aprender a ser preciso es una habilidad esencial para programar. Fijarse en los pequeños detalles, como la forma en que se separan las palabras y cómo terminan las líneas, ayuda a los programadores principiantes a mejorar.

### Entrada básica

Los programas de computadora suelen recibir entradas del usuario. La **entrada** es lo que un usuario introduce en un programa. Una instrucción de entrada, `variable = input("prompt")`, tiene tres partes:

1. Una **variable** hace referencia a un valor almacenado en la memoria. En la instrucción anterior, *variable* puede reemplazarse con cualquier nombre que elija el programador.
2. La función **input()** lee una línea de entrada del usuario. Una función es un bloque de código con nombre y reutilizable que realiza una tarea cuando se llama. La entrada se almacena en la memoria de la computadora y se puede acceder a ella más adelante mediante la variable.
3. Un **indicador (prompt)** es un mensaje breve que señala que el programa está esperando una entrada. En la instrucción anterior, *«prompt»* se puede omitir o reemplazar con cualquier mensaje.

**Video:** [Obtaining input from the user](https://www.openstax.org/r/obtaining-input)

**Conceptos en práctica: La función input()**

<!-- pregunta: CPL-ch01-m02-p04 -->

1. ¿Qué línea de código obtiene y almacena correctamente la entrada del usuario?

   - a) `input()`
   - b) `today_is = input`
   - c) `today_is = input()`

   <details><summary>Respuesta</summary>

   c) La entrada del usuario se almacena en la memoria y se puede consultar mediante `today_is`.

   </details>

<!-- pregunta: CPL-ch01-m02-p05 -->

2. Una persona llamada Sophia escribe su nombre cuando se le pide con
   
   ```python norun
   print("Please enter your name: ")
   name = input()
   ```
   
    ¿Qué muestra `print("You entered:", name)`?

   - a) `You entered: name`
   - b) `You entered: Sophia`
   - c) `You entered:, Sophia`

   <details><summary>Respuesta</summary>

   b) La función `print()` imprime `"You entered:"` seguido de un espacio, seguido de los datos de entrada, `Sophia`, a los que hace referencia la variable name.

   </details>

<!-- pregunta: CPL-ch01-m02-p06 -->

3. ¿Cuál es la salida si el usuario escribe «six» como entrada?
   
   ```python norun
   print("Please enter a number: ")
   number = input()
   print("Value =", number)
   ```

   - a) `Value = six`
   - b) `Value = 6`
   - c) `Value = number`

   <details><summary>Respuesta</summary>

   a) La entrada se almacena exactamente como la escribe el usuario. Por lo tanto, el valor obtenido se muestra exactamente como lo escribió el usuario.

   </details>

**Pruébalo: Poema de Frost**

Escribe un programa que use varias instrucciones `print()` para mostrar el siguiente poema de [Robert Frost](https://openstax.org/r/100robertfrost). Cada instrucción `print()` debe corresponder a una línea de salida.

*Consejo:* No necesitas escribir todo el programa de una vez. Prueba escribiendo la primera instrucción `print()` y luego haz clic en el botón Run. Después escribe la siguiente instrucción `print()` y haz clic en Run de nuevo. Continúa escribiendo y probando el código de forma gradual hasta terminar el programa.

```text
I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I--
I took the one less traveled by,
And that has made all the difference.
```

<!-- coderunner: ch1/CodeRunner_01_03_02_Frost-poem -->

**Pruébalo: Nombre y gustos**

Escribe un programa que haga las dos preguntas siguientes (la entrada de ejemplo está en negrita):

```text
What is your name? Shakira
What do you like? singing
```

Muestra una línea en blanco después de leer la entrada. Luego muestra el siguiente mensaje según la entrada:

```text
Shakira likes singing
```

<!-- coderunner: ch1/CodeRunner_01_03_03_Name-likes -->

<!-- modulo: m00004 -->

## 1.3 Variables

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Asignar variables e imprimir variables.
- Explicar las reglas para nombrar variables.

### Instrucción de asignación

Las variables permiten que los programas hagan referencia a valores mediante nombres en lugar de ubicaciones de memoria. Ej.: `age` hace referencia a la edad de una persona, y `birth` hace referencia a su fecha de nacimiento.

Una instrucción puede asignar un valor a una variable mediante el **operador de asignación** (**=**). Ten en cuenta que esto es diferente del signo igual de las matemáticas. Ej.: `age = 6` o `birth = "May 15"`. El lado izquierdo de la instrucción de asignación es una variable, y el lado derecho es el valor que se le asigna.

**Video:** [Assigning and using variables](https://www.openstax.org/r/using-variables)

**Conceptos en práctica: Asignación y uso de variables**

<!-- pregunta: CPL-ch01-m03-p01 -->

1. ¿Qué línea de código recupera correctamente el valor de la variable `city` después de la siguiente asignación?
   
   ```python
   city = "Chicago"
   ```

   - a) `print("In which city do you live?")`
   - b) `city = "London"`
   - c) `print("The city where you live is", city)`

   <details><summary>Respuesta</summary>

   c) Esto produciría la cadena de salida `"The city where you live is Chicago"`.

   </details>

<!-- pregunta: CPL-ch01-m03-p02 -->

2. ¿Qué programa almacena y recupera una variable correctamente?

   - a)

     ```python norun
     print("Total =", total)
     total = 6
     ```

   - b)

     ```python
     total = 6
     print("Total =", total)
     ```

   - c)

     ```python norun
     print("Total =", total)
     total = input()
     ```

   <details><summary>Respuesta</summary>

   b) Estas dos líneas de código producirían la cadena de salida `"Total = 6"`.

   </details>

<!-- pregunta: CPL-ch01-m03-p03 -->

3. ¿Cuál es el operador de asignación?

   - a) `:`
   - b) `==`
   - c) `=`

   <details><summary>Respuesta</summary>

   c) El carácter `=` por sí solo es el operador de asignación.

   </details>

<!-- pregunta: CPL-ch01-m03-p04 -->

4. ¿Cuál es una asignación válida?

   - a) `temperature = 98.5`
   - b) `98.5 = temperature`
   - c) `temperature - 23.2`

   <details><summary>Respuesta</summary>

   a) Una instrucción de asignación tiene el nombre de la variable en el lado izquierdo y el valor en el lado derecho.

   </details>

### Reglas para nombrar variables

Un nombre de variable puede constar de letras, dígitos y guiones bajos, y tener cualquier longitud. El nombre no puede empezar con un dígito. Ej.: `101class` no es válido. Además, importa si las letras son mayúsculas o minúsculas. Ej.: `Total` es distinto de `total`. La guía de estilo de Python recomienda escribir los nombres de variables en **snake_case**, es decir, todo en minúsculas y con guiones bajos entre las palabras, como `first_name` o `total_price`.

Un nombre debe ser corto y descriptivo, por lo que en los programas se prefieren las palabras a los caracteres sueltos para facilitar la lectura. Ej.: una variable llamada `count` indica mejor su propósito que una llamada `c`.

Python tiene palabras reservadas, conocidas como **palabras clave**, que tienen funciones especiales y no se pueden usar como nombres de variables (ni de otros objetos).

**Palabras clave**

|  |  |  |  |  |
|---|---|---|---|---|
| `False` | `await` | `else` | `import` | `pass` |
| `None` | `break` | `except` | `in` | `raise` |
| `True` | `class` | `finally` | `is` | `return` |
| `and` | `continue` | `for` | `lambda` | `try` |
| `as` | `def` | `from` | `nonlocal` | `while` |
| `assert` | `del` | `global` | `not` | `with` |
| `asynch` | `elif` | `if` | `or` | `yield` |

**Conceptos en práctica: Nombres de variable válidos**

<!-- pregunta: CPL-ch01-m03-p05 -->

1. ¿Cuál se puede usar como nombre de variable?

   - a) median
   - b) class
   - c) import

   <details><summary>Respuesta</summary>

   a) `median` es un nombre descriptivo para una variable que almacena un valor de mediana.

   </details>

<!-- pregunta: CPL-ch01-m03-p06 -->

2. ¿Por qué el nombre `2nd_input` no es un nombre de variable válido?

   - a) contiene un guion bajo
   - b) empieza con un dígito
   - c) es una palabra clave

   <details><summary>Respuesta</summary>

   b) Un nombre de variable puede contener un dígito, pero no empezar con uno.

   </details>

<!-- pregunta: CPL-ch01-m03-p07 -->

3. ¿Cuál sería un buen nombre para una variable que almacena un código postal?

   - a) `z`
   - b) `var_2`
   - c) `zip_code`

   <details><summary>Respuesta</summary>

   c) El nombre indica claramente que el valor almacenado es un código postal.

   </details>

<!-- pregunta: CPL-ch01-m03-p08 -->

4. Dado el nombre de variable `DogBreed`, ¿qué mejora se ajusta a la guía de estilo de Python?

   - a) `dog_breed`
   - b) `dogBreed`
   - c) `dog-breed`

   <details><summary>Respuesta</summary>

   a) En snake_case cada palabra se separa con un guion bajo y solo se usan letras minúsculas.

   </details>

**Pruébalo: Marcador final**

Escribe un programa de computadora en Python que:

- Cree una variable, `team1`, con el valor `"Liverpool"`.
- Cree una variable, `team2`, con el valor `"Chelsea"`.
- Cree una variable `score1`, con el valor `4`.
- Cree una variable, `score2`, con el valor `3`.
- Imprima `team1`, `"versus"` y `team2` como una sola línea de salida.
- Imprima `"Final score: "`, `score1`, `"to"`, `score2` como una sola línea de salida.

<!-- coderunner: ch1/CodeRunner_01_04_04_Final-score -->

<!-- modulo: m00005 -->

## 1.4 Conceptos básicos de cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar la función integrada `len()` para obtener la longitud de una cadena.
- Concatenar literales de cadena y variables con el operador +.

### Comillas

Una cadena es una secuencia de caracteres encerrada entre comillas simples (') o dobles (") que coincidan. Ej.: `"Happy birthday!"` y `'21'` son cadenas.

Para incluir una comilla simple (') en una cadena, encierra la cadena entre comillas dobles (") que coincidan. Ej.: `"Won't this work?"` Para incluir una comilla doble ("), encierra la cadena entre comillas simples (') que coincidan. Ej.: `'They said "Try it!", so I did'`.

**Reglas para las cadenas.**

| Cadena válida | Cadena no válida |
|---|---|
| `"17" or '17'` | `17` |
| `"seventeen" or 'seventeen'` | `seventeen` |
| `"Where?" or 'Where?'` | `"Where?'` |
| `"I hope you aren't sad."` | `'I hope you aren't sad.'` |
| `'The teacher said "Correct!" '` | `"The teacher said "Correct!" "` |

**Conceptos en práctica: Cadenas válidas y no válidas**

<!-- pregunta: CPL-ch01-m04-p01 -->

1. ¿Cuál de las siguientes es una cadena?

   - a) `Hello!`
   - b) `29`
   - c) `"7 days"`

   <details><summary>Respuesta</summary>

   c) Una cadena encerrada entre comillas dobles que coincidan es una cadena válida. Ten en cuenta que `'7 days'` también es una cadena.

   </details>

<!-- pregunta: CPL-ch01-m04-p02 -->

2. ¿Qué línea de código asigna una cadena a la variable `email?`

   - a) `"fred78@gmail.com"`
   - b) `"email = fred78@gmail.com"`
   - c) `email = "fred78@gmail.com"`

   <details><summary>Respuesta</summary>

   c) La cadena `fred78@gmail.com` está encerrada entre comillas dobles que coinciden y se asigna a la variable `email`. Una cadena puede contener caracteres como «@» o «.» además de letras y números.

   </details>

<!-- pregunta: CPL-ch01-m04-p03 -->

3. ¿Cuál es una cadena válida?

   - a) `I know you'll answer correctly!`
   - b) `'I know you'll answer correctly!'`
   - c) `"I know you'll answer correctly!"`

   <details><summary>Respuesta</summary>

   c) La cadena tiene comillas dobles que coinciden. Como una comilla simple forma parte de esta cadena, hay que usar comillas dobles.

   </details>

<!-- pregunta: CPL-ch01-m04-p04 -->

4. ¿Cuál es una cadena válida?

   - a) `You say "Please" to be polite`
   - b) `"You say "Please" to be polite"`
   - c) `'You say "Please" to be polite'`

   <details><summary>Respuesta</summary>

   c) Ten en cuenta que las comillas simples (') que la encierran no forman parte de la cadena, pero las comillas dobles (") sí.

   </details>

### La función len()

Una operación común sobre un objeto de tipo cadena es obtener su longitud, es decir, el número de caracteres de la cadena. La función **len()**, cuando se llama sobre un valor de tipo cadena, devuelve la longitud de la cadena.

**Video:** [Using len() to get the length of a string](https://www.openstax.org/r/length-of-string)

**Conceptos en práctica: Aplicación de la función len() a valores de tipo cadena**

<!-- pregunta: CPL-ch01-m04-p105 -->

1. ¿Cuál es el valor de retorno de `len("Hi Ali")`?

   - a) `2`
   - b) `5`
   - c) `6`

   <details><summary>Respuesta</summary>

   c) La función `len()` devuelve el número de caracteres de la cadena. En `"Hi Ali"` hay 6 caracteres, que son «H», «i», « », «A», «l» e «i».

   </details>

<!-- pregunta: CPL-ch01-m04-p106 -->

2. ¿Cuál es la longitud de una variable de cadena vacía `("")`?

   - a) indefinida
   - b) 0
   - c) 2

   <details><summary>Respuesta</summary>

   b) La longitud de una cadena vacía es igual a 0.

   </details>

<!-- pregunta: CPL-ch01-m04-p107 -->

3. ¿Cuál es la salida del siguiente código?
   
   ```python
   number = "12"
   number_of_digits = len(number)
   print("Number", number, "has", number_of_digits, "digits.")
   ```

   - a) `Number 12 has 12 digits.`
   - b) `Number 12 has 2 digits.`
   - c) `Number 12 has number_of_digits digits.`

   <details><summary>Respuesta</summary>

   b) El valor de la variable `number_of_digits` es `2`, y por lo tanto la salida es `"Number 12 has 2 digits."`.

   </details>

### Concatenación

La concatenación es una operación que combina dos o más cadenas de forma secuencial con el operador de concatenación (+). Ej.: `"A"` + `"part"` produce la cadena `"Apart"`.

**Video:** [Concatenating multiple strings](https://www.openstax.org/r/concatenating-strings)

**Conceptos en práctica: Concatenación de cadenas**

<!-- pregunta: CPL-ch01-m04-p05 -->

1. ¿Qué produce la cadena `"10"`?

   - a) `1 + 0`
   - b) `"1 + 0"`
   - c) `"1" + "0"`

   <details><summary>Respuesta</summary>

   c) El `1` y el `0` están entre comillas, lo que indica que son cadenas válidas, y el + no lo está, lo que indica una operación de concatenación. Por lo tanto, se produce la cadena `"10"`. Ten en cuenta que el operador de concatenación no incluye ningún carácter separador predeterminado, como el espacio.

   </details>

<!-- pregunta: CPL-ch01-m04-p06 -->

2. ¿Qué produce la cadena `"Awake"?`

   - a) `"wake" + "A"`
   - b) `"A + wake"`
   - c) `"A" + "wake"`

   <details><summary>Respuesta</summary>

   c) `"A"` y `"wake"` son cadenas válidas, y el + no está entre comillas, lo que indica una operación de concatenación. Por lo tanto, se produce la cadena `"Awake"`. Ten en cuenta que el operador de concatenación no incluye ningún carácter separador predeterminado, como el espacio.

   </details>

<!-- pregunta: CPL-ch01-m04-p07 -->

3. Un usuario escribe `"red"` después de la siguiente línea de código.
   
   ```python norun
   color = input("What is your favorite color?")
   ```
   
    ¿Qué produce la salida `"Your favorite color is red!"`?

   - a) `print("Your favorite color is " + color + !)`
   - b) `print("Your favorite color is " + "color" + "!")`
   - c) `print("Your favorite color is " + color + "!")`

   <details><summary>Respuesta</summary>

   c) Ten en cuenta que los espacios deben incluirse explícitamente al usar el operador de concatenación.

   </details>

<!-- pregunta: CPL-ch01-m04-p08 -->

4. ¿Cuál de las siguientes asigna `"one-sided"` a la variable `holiday`?

   - a) `holiday = "one" + "sided"`
   - b) `holiday = one-sided`
   - c) `holiday = "one-" + "sided"`

   <details><summary>Respuesta</summary>

   c) Se asigna a la variable `holiday` la concatenación de las dos cadenas. Ten en cuenta que `"one-sided"` asignaría la misma cadena a `holiday`.

   </details>

**Pruébalo: Longitud del nombre**

Escribe un programa que pida al usuario que escriba su nombre y su apellido por separado. Usa los siguientes indicadores (prompts) (la entrada de ejemplo está en negrita):

```text
What is your first name? Alan
What is your last name? Turing
```

El programa debe mostrar entonces la longitud de cada nombre. Con la entrada de ejemplo anterior, la salida sería:

```text
Your first name is 4 letters long
Your last name is 6 letters long
```

<!-- coderunner: ch1/CodeRunner_01_05_06_Name-length -->

**Pruébalo: Puntuación**

Escribe un programa de computadora en Python que:

- Asigne la cadena `"Freda"` a una variable, `name`.
- Asigne la cadena `"happy"` a una variable, `feel`.
- Imprima la cadena `"Hi Freda!"` con una sola función `print()` usando la variable `name`.
- Imprima la cadena `"I'm glad you feel happy."` con una sola función `print()` usando la variable `feel`.

<!-- coderunner: ch1/CodeRunner_01_05_05_Punctuation -->

<!-- modulo: m00006 -->

## 1.5 Conceptos básicos de números

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar operadores aritméticos para hacer cálculos.
- Explicar la precedencia de los operadores aritméticos.

### Tipos de datos numéricos

Python admite dos formatos numéricos básicos: entero y de punto flotante. Un entero representa un número entero, y el formato de punto flotante representa un número decimal. El formato que usa un lenguaje para representar datos se llama **tipo de datos**. Además de los tipos entero y de punto flotante, los lenguajes de programación suelen tener un tipo cadena para representar texto.

**Video:** [Integer and floating-point](https://www.openstax.org/r/integer-and-floating-point)

**Conceptos en práctica: Enteros, floats y cadenas**

<!-- pregunta: CPL-ch01-m05-p01 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python norun
   print(x, type(x))
   ```

   - a) `1 'int'`.
   - b) `1.0 <class 'float'>`.
   - c) `1 <class 'int'>`.

   <details><summary>Respuesta</summary>

   c) `x = 1` es un entero, y al imprimir el tipo de una variable entera, la salida es `<class 'int'>`.

   </details>

<!-- pregunta: CPL-ch01-m05-p02 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python norun
   print(y, type(y))
   ```

   - a) `2.0 <class 'int'>`
   - b) `2.0 <class 'float'>`
   - c) `2 <class 'int'>`

   <details><summary>Respuesta</summary>

   b) `y = 2.0` es un número de punto flotante.

   </details>

<!-- pregunta: CPL-ch01-m05-p03 -->

3. ¿Cuál es el tipo del siguiente valor?
   
   ```python
   "12.0"
   ```

   - a) `string`
   - b) `int`
   - c) `float`

   <details><summary>Respuesta</summary>

   a) Cualquier valor definido entre comillas es un valor de tipo cadena, sea cual sea su contenido.

   </details>

### Aritmética básica

Los **operadores aritméticos** se usan para realizar operaciones matemáticas como la suma, la resta, la multiplicación y la división.

En Python existen cuatro operadores aritméticos básicos:

1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)

**Video:** [Examples of arithmetic operators](https://www.openstax.org/r/arithmetic-operators)

**Conceptos en práctica: Aplicación de operadores aritméticos**

<!-- pregunta: CPL-ch01-m05-p04 -->

1. Dadas las siguientes líneas de código, ¿cuál es la salida del código?
   
   ```python norun
   c = 0
   c = x - z
   c = c + 1
   print(c)
   ```

   - a) `1`
   - b) `5`
   - c) `6`

   <details><summary>Respuesta</summary>

   c) La línea 2 del código se evalúa así: `c = x - z = 7 - 2 = 5`. La línea 3 incrementa la variable `c` en 1, con lo que el total es igual a 6.

   </details>

<!-- pregunta: CPL-ch01-m05-p05 -->

2. ¿Cuál es el valor de `a`?
   
   ```python
   a = 3.5 - 1.5
   ```

   - a) `2`
   - b) `2.0`
   - c) `2.5`

   <details><summary>Respuesta</summary>

   b) El resultado de `3.5-1.5` es igual a `2.0`, que es un número de punto flotante.

   </details>

<!-- pregunta: CPL-ch01-m05-p06 -->

3. ¿Cuál es la salida de `print(x / z)`?

   - a) `3`
   - b) `3.0`
   - c) `3.5`

   <details><summary>Respuesta</summary>

   c) El resultado de la operación de división es un número de punto flotante que no se redondea hacia abajo. `7/2 = 3.5`.

   </details>

<!-- pregunta: CPL-ch01-m05-p07 -->

4. ¿Cuál es la salida de `print(y / z)`?

   - a) `0`
   - b) `10`
   - c) `10.0`

   <details><summary>Respuesta</summary>

   c) El resultado de `20/2` es igual a `10.0` porque la operación de división da como resultado un float.

   </details>

<!-- pregunta: CPL-ch01-m05-p08 -->

5. ¿Cuál es la salida de `print(z * 1.5)`?

   - a) `2`
   - b) `3`
   - c) `3.0`

   <details><summary>Respuesta</summary>

   c) El resultado de un operador aritmético aplicado a cualquier operando de punto flotante es un valor de punto flotante. `2 * 1.5 = 3.0`.

   </details>

### Precedencia de operadores

Cuando un cálculo tiene varios operadores, cada operador se evalúa según su orden de **precedencia**. Ej.: `1 + 2 * 3` es `7` porque la multiplicación tiene precedencia sobre la suma. Sin embargo, `(1 + 2) * 3` es `9` porque los paréntesis tienen precedencia sobre la multiplicación.

**Precedencia de operadores, de mayor a menor.**

| Operador | Descripción | Ejemplo | Resultado |
|---|---|---|---|
| `()` | Paréntesis | `(1 + 2) * 3` | `9` |
| `**` | Exponenciación | `2 ** 4` | `16` |
| `+`, `-` | Positivo, negativo | `-math.pi` | `-3.14159` |
| `*`, `/` | Multiplicación, división | `2 * 3` | `6` |
| `+`, `-` | Suma, resta | `1 + 2` | `3` |

**Video:** [Order of operations in an arithmetic expression](https://www.openstax.org/r/order-of-operations)

**Conceptos en práctica: Varios operadores aritméticos**

<!-- pregunta: CPL-ch01-m05-p09 -->

1. ¿Cuál es el valor de `4 * 3 ** 2 + 1`?

   - a) `37`
   - b) `40`
   - c) `145`

   <details><summary>Respuesta</summary>

   a) 3 elevado a la potencia 2 es 9, por 4 es 36, más 1 es 37.

   </details>

<!-- pregunta: CPL-ch01-m05-p10 -->

2. ¿Qué parte de `(1 + 3) ** 2 / 4` se evalúa primero?

   - a) `4 ** 2`
   - b) `1 + 3`
   - c) `2 / 4`

   <details><summary>Respuesta</summary>

   b) Aunque la suma tiene menor precedencia que la exponenciación, los paréntesis hacen que `1 + 3` se evalúe primero.

   </details>

<!-- pregunta: CPL-ch01-m05-p11 -->

3. ¿Cuál es el valor de `-4 ** 2`?

   - a) `-16`
   - b) `16`

   <details><summary>Respuesta</summary>

   a) En Python, la exponenciación, o elevación a una potencia, tiene mayor precedencia que volver negativo un valor. El resultado `-16` de Python puede resultar confuso porque, en matemáticas, «-4 al cuadrado» es `16`.

   </details>

<!-- pregunta: CPL-ch01-m05-p12 -->

4. ¿Cuántos operadores hay en la siguiente instrucción?
   
   ```python
   result = -2 ** 3
   ```

   - a) 1
   - b) 2
   - c) 3

   <details><summary>Respuesta</summary>

   c) La instrucción usa el operador de asignación (`=`), el operador negativo (`-`) y el operador de exponenciación (`**`).

   </details>

**Pruébalo: Valores y tipos**

Escribe un programa de computadora en Python que:

1. Defina una variable entera llamada `'int_a'` y le asigne el valor `10`.
2. Defina una variable de punto flotante llamada `'float_a'` y le asigne el valor `10.0`.
3. Defina una variable de cadena llamada `'string_a'` y le asigne el valor de cadena `"10"`.
4. Imprima el valor de cada una de las tres variables junto con su tipo.

<!-- coderunner: ch1/CodeRunner_01_06_07_Values-and-types -->

**Pruébalo: Metros a pies**

Escribe un programa de computadora en Python que:

1. Asigne el valor entero `10` a una variable, `meters`.
2. Asigne el valor de punto flotante `3.28` a una variable, `meter2feet`.
3. Calcule 10 metros en pies multiplicando `meters` por `meter2feet`. Guarde el resultado en una variable, `feet`.
4. Imprima en la salida el contenido de la variable `feet`.

<!-- coderunner: ch1/CodeRunner_01_06_08_Meters-to-feet -->

<!-- modulo: m00007 -->

## 1.6 Mensajes de error

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar el tipo de error y el número de línea en los mensajes de error.
- Corregir errores de sintaxis, errores de nombre y errores de sangría.

### Cómo leer los errores

Cometer errores es una parte natural de la programación. Incluso los programadores con experiencia cometen errores al escribir código. Los errores pueden producirse cuando se cometen equivocaciones al escribir código. La computadora requiere instrucciones muy específicas que le indiquen qué hacer. Si las instrucciones no son claras, la computadora no sabe qué hacer y devuelve un error.

Cuando ocurre un error, Python muestra un mensaje con la siguiente información:

1. El número de línea del error.
2. El tipo de error (Ej.: `SyntaxError`).
3. Detalles adicionales sobre el error.

Ej.: escribir `print "Hello!"` sin paréntesis es un error de sintaxis. En Python se requieren paréntesis para usar `print`. Al intentar ejecutar `print "Hello!"`, Python muestra el siguiente error:

```python norun
Traceback (most recent call last):
  File "/home/student/Desktop/example.py", line 1
    print "Hello"
                ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello")?
```

El carácter de acento circunflejo (`^`) muestra dónde encontró Python el error. A veces el error puede estar una o dos líneas antes de donde aparece el símbolo, porque es posible que Python no lo haya descubierto hasta ese momento. Una **traza (traceback)** es un informe de Python sobre la ubicación y el tipo de un error. La palabra traceback sugiere que el programador rastree hacia atrás en el código para encontrar el error si no se ve de inmediato.

Aprender a leer los mensajes de error con atención es una habilidad importante. La cantidad de jerga técnica puede resultar abrumadora al principio. Pero esta información puede ser muy útil.

**Video:** [Incorrect variable name](https://www.openstax.org/r/incorrect-variable-name)

**Conceptos en práctica: Partes de un error**

<!-- pregunta: CPL-ch01-m06-p01 -->

1. ¿Cuál es el nombre de archivo del programa?

   - a) Desktop
   - b) example.py
   - c) test

   <details><summary>Respuesta</summary>

   b) El nombre del archivo se encuentra después de la última barra (/). Otros nombres, como Desktop, se refieren a carpetas.

   </details>

<!-- pregunta: CPL-ch01-m06-p02 -->

2. ¿En qué línea se encontró el error?

   - a) 1
   - b) 2
   - c) 3

   <details><summary>Respuesta</summary>

   b) La línea 2 se menciona inmediatamente después del nombre del archivo.

   </details>

<!-- pregunta: CPL-ch01-m06-p03 -->

3. ¿Qué tipo de error se encontró?

   - a) faltan paréntesis
   - b) `SyntaxError`
   - c) traza (traceback)

   <details><summary>Respuesta</summary>

   b) El tipo de error es siempre la primera palabra de la última línea del mensaje de error.

   </details>

### Tipos comunes de errores

Al ejecutar programas de Python pueden ocurrir distintos tipos de errores. Cuando ocurre un error, conocer su tipo ayuda a saber cómo corregirlo. La siguiente tabla muestra ejemplos de equivocaciones que cualquiera podría cometer al programar.

**Errores simples.**

| Error cometido | Mensaje de error | Explicación |
|---|---|---|
| `print("Have a nice day!"` | `SyntaxError: unexpected EOF while parsing` | Falta el paréntesis de cierre. A Python le sorprende llegar al fin del archivo (EOF) antes de que esta línea esté completa. |
| `word = input("Type a word: )` | `SyntaxError: EOL while scanning string literal` | Faltan las comillas de cierre. Como resultado, la cadena no termina antes del fin de la línea (EOL). |
| ```text<br>print("You typed:", wird)<br>``` | `NameError: name 'wird' is not defined` | `word` está mal escrito. El programador pulsó una tecla equivocada por accidente. |
| ```text<br>prints("You typed:", word)<br>``` | `NameError: name 'prints' is not defined` | `print` está mal escrito. El programador escribió una letra de más por accidente. |
| `   print("Hello") ` | `IndentationError: unexpected indent` | El programador escribió un espacio por accidente al comienzo de la línea. |
| `     print("Goodbye") ` | `IndentationError: unexpected indent` | El programador pulsó la tecla Tab por accidente al comienzo de la línea. |

**Conceptos en práctica: Tipos de errores**

<!-- pregunta: CPL-ch01-m06-p04 -->

1.

   ```python norun
   print("Breakfast options:")
    print("A. Cereal")
    print("B. Eggs")
    print("C. Yogurt")
   choice = input("What would you like? ")
   ```

   - a) `IndentationError`
   - b) `NameError`
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   a) Las tres líneas del medio tienen sangría. En Python, las líneas no pueden comenzar con espacios o tabulaciones de forma inesperada.

   </details>

<!-- pregunta: CPL-ch01-m06-p05 -->

2.

   ```python norun
   birth = input("Enter your birth date: )
   print("Happy birthday on ", birth)
   ```

   - a) `IndentationError`
   - b) `NameError`
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   c) Faltan las comillas al final del indicador (prompt) de entrada.

   </details>

<!-- pregunta: CPL-ch01-m06-p06 -->

3.

   ```python norun
   print("Breakfast options:")
   print(" A. Cereal")
   print(" B. Eggs")
   print(" C. Yogurt")
   choice = intput("What would you like? ")
   ```

   - a) `IndentationError`
   - b) `NameError`
   - c) `SyntaxError`

   <details><summary>Respuesta</summary>

   b) El nombre de `"input"` está mal escrito.

   </details>

**Pruébalo: Tres errores**

El siguiente programa tiene tres errores.

- Ejecuta el programa para encontrar el primer error y corrige la línea de código correspondiente.
- Luego ejecuta el programa de nuevo para encontrar y corregir el segundo error.
- Sigue ejecutando y corrigiendo el programa hasta que no se encuentren errores.

<!-- coderunner: ch1/CodeRunner_01_07_09_Three-errors -->

**Pruébalo: Símbolos incorrectos**

Este código se basa en un ejemplo anterior, pero contiene varias equivocaciones.

- A una línea le falta un signo de puntuación necesario, y otra línea usa símbolos incorrectos.
- Ejecuta el programa para encontrar el primer error y corrige la línea de código correspondiente.
- Sigue ejecutando y corrigiendo el programa hasta que no se encuentren errores.

<!-- coderunner: ch1/CodeRunner_01_07_10_Wrong-symbols -->

<!-- modulo: m00008 -->

## 1.7 Comentarios

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Escribir comentarios concisos y significativos que expliquen la funcionalidad prevista del código.
- Escribir una cadena de documentación (docstring), un comentario más extenso, que describa la funcionalidad del programa.

### El carácter de almohadilla

Los **comentarios** son frases cortas que explican lo que hace el código. Ej.: las líneas 1, 8 y 10 del siguiente programa contienen comentarios. Cada comentario comienza con un carácter de almohadilla (`#`). Todo el texto desde la almohadilla hasta el final de la línea se ignora al ejecutar el programa. En cambio, las almohadillas dentro de cadenas se tratan como texto normal. Ej.: la cadena `"Item #1: "` no contiene un comentario.

Al escribir comentarios:

- El carácter `#` debe ir seguido de un solo espacio. Ej.: `# End of menu` es más fácil de leer que `#End of menu`.
- Los comentarios deben explicar el propósito del código, no solo repetirlo. Ej.: `# Get the user's preferences` es más descriptivo que `# Input item1 and item2`.

**Ejemplo: Programa con tres comentarios**

```python norun
# Display the menu options
print("Lunch Menu")
print("----------")
print("Burrito")
print("Enchilada")
print("Taco")
print("Salad")
print() # End of menu

# Get the user's preferences
item1 = input("Item #1: ")
item2 = input("Item #2: ")
```

**Conceptos en práctica: Comentarios simples**

<!-- pregunta: CPL-ch01-m07-p01 -->

1. El propósito principal de escribir comentarios es _____.

   - a) evitar errores de sintaxis
   - b) explicar lo que hace el código
   - c) hacer que el código se ejecute más rápido

   <details><summary>Respuesta</summary>

   b) Los comentarios ayudan a explicar el propósito del código para que otros programadores entiendan lo que este pretende.

   </details>

<!-- pregunta: CPL-ch01-m07-p02 -->

2. ¿Qué símbolo se usa para los comentarios en Python?

   - a) #
   - b) /*
   - c) //

   <details><summary>Respuesta</summary>

   a) La almohadilla indica el comienzo de un comentario.

   </details>

<!-- pregunta: CPL-ch01-m07-p03 -->

3. ¿Qué comentario tiene el formato correcto?

   - a) 0 espacios:
      `#Get the user input`
   - b) 1 espacio:
      `# Get the user input`
   - c) 2 espacios:
      `#  Get the user input`

   <details><summary>Respuesta</summary>

   b) Dejar un espacio después del # es el estándar de la comunidad.

   </details>

### Calidad del código

El programa de ejemplo anterior tenía dos partes: (1) mostrar las opciones del menú y (2) obtener las preferencias del usuario. En conjunto, las líneas en blanco y los comentarios muestran la estructura general del programa.

Los programadores dedican más tiempo a leer código que a escribirlo. Por eso es importante que el código sea más fácil de leer y entender para otras personas. Dos formas de mejorar la calidad del código son:

- Separar cada parte (líneas que tienen un propósito similar) con una línea en blanco.
- Escribir un comentario antes de cada parte. No todas las líneas necesitan un comentario.

**Video:** [Comments in a program](https://www.openstax.org/r/comments)

**Conceptos en práctica: Calidad del código**

<!-- pregunta: CPL-ch01-m07-p04 -->

1. ¿Qué comentario es más útil para el siguiente código?
   
   ```python norun
   print("You said:", adj1 + " " + noun1)
   ```

   - a) `# Append adj1 and noun1`
   - b) `# Print out a bunch of stuff`
   - c) `# Show the resulting phrase`

   <details><summary>Respuesta</summary>

   c) Este comentario explica la intención del código. Si el código tuviera un error, el programador que lee el comentario podría notarlo con más facilidad.

   </details>

<!-- pregunta: CPL-ch01-m07-p05 -->

2. ¿Dónde se debería insertar una línea en blanco?
   
   ```python norun
   name = input("Whose birthday is today? ")
   print("Happy birthday to", name)
   print("Everyone cheer for", name)
   ```

   - a) Después de la línea 1
   - b) Después de la línea 2
   - c) Después de la línea 3

   <details><summary>Respuesta</summary>

   a) Una línea en blanco separa la entrada de la salida.
    Por otra parte, en un programa de tres líneas, insertar una línea en blanco suele ser innecesario.

   </details>

<!-- pregunta: CPL-ch01-m07-p06 -->

3. Para evitar temporalmente que se ejecute una línea, se podría . . .

   - a) introducir un error de sintaxis en la línea.
   - b) quitar la línea del programa.
   - c) insertar un # al comienzo de la línea.

   <details><summary>Respuesta</summary>

   c) El símbolo # «comenta» la línea sin eliminarla de forma permanente.

   </details>

### Documentación

Los programas de Python pueden comenzar, opcionalmente, con una cadena conocida como docstring. Un **docstring** es documentación escrita para otras personas que usarán el programa, pero que no necesariamente leerán el código fuente. Gran parte de la documentación oficial de [docs.python.org](https://openstax.org/r/100docstrings) se genera a partir de docstrings.

La documentación puede ser extensa, por lo que los docstrings suelen escribirse como cadenas de varias líneas `(""")`. Los elementos comunes de un docstring son un resumen de una línea, una línea en blanco y una descripción más larga.

**Video:** [Vacations docstring](https://www.openstax.org/r/docstring)

**Conceptos en práctica: Documentación**

<!-- pregunta: CPL-ch01-m07-p07 -->

1. El propósito principal de escribir docstrings es . . .

   - a) resumir el propósito o el uso del programa.
   - b) explicar cómo funciona cada parte del código.
   - c) mantener una lista de ideas para nuevas funcionalidades.

   <details><summary>Respuesta</summary>

   a) El docstring se escribe principalmente para otras personas que usarán el programa.

   </details>

<!-- pregunta: CPL-ch01-m07-p08 -->

2. ¿Cuál de los siguientes NO es un docstring?

   - a)

     ```python
     """Vacations Madlib."""
     ```

   - b)

     ```python
     """Vacations Madlib.
     This program asks the user for two adjectives
     and two nouns, which are then used to print
     a funny story about a vacation.
     """
     ```

   - c)

     ```python
     # Vacations Madlib.
     #
     # This program asks the user for two adjectives
     # and two nouns, which are then used to print
     # a funny story about a vacation.
     ```

   <details><summary>Respuesta</summary>

   c) Un docstring debe ser una cadena válida, no un comentario de varias líneas. Los docstrings se guardan en la memoria del programa, pero los comentarios se ignoran.

   </details>

<!-- pregunta: CPL-ch01-m07-p09 -->

3. ¿Qué docstring es más útil para este programa?

   - a)

     ```python
     """Vacations Madlib."""
     ```

   - b)

     ```python
     """Vacations Madlib.
     
     This program asks the user for two adjectives
     and two nouns, which are then used to print
     a funny story about a vacation.
     """
     ```

   - c)

     ```python
     """Vacations Madlib.
     
     This program asks the user for two adjectives
     and two nouns, which are then used to print
     a funny story about a vacation. The code uses
     four variables to store the user input: two for
     the adjectives, and two for the nouns. The
     output is displayed on seven lines, beginning
     with a blank line after the input.
     """
     ```

   <details><summary>Respuesta</summary>

   b) La cantidad de información de este docstring es la justa. En la mayoría de los casos, el docstring no debería ser más largo que el código.

   </details>

**Pruébalo: De quién es el cumpleaños**

Agrega dos comentarios al siguiente programa: uno para la entrada y otro para la salida. Separa la entrada y la salida con una línea en blanco. Luego compara tus comentarios con la solución de muestra y hazte las siguientes preguntas:

- ¿Tus comentarios son más largos o más cortos? ¿Por qué?
- ¿Es correcto el formato de tus comentarios?

<!-- coderunner: ch1/CodeRunner_01_08_11_Whose-birthday -->

**Pruébalo: Cálculo de la gravedad**

Escribe un docstring para el siguiente programa. La primera línea del docstring debe explicar, en una oración corta, qué es el programa. La segunda línea del docstring debe estar en blanco. La tercera línea y las siguientes deben incluir una explicación más larga de lo que hace el programa. Al final del docstring, agrega una línea que diga `"Author: "` seguida de tu nombre.

<!-- coderunner: ch1/CodeRunner_01_08_12_Gravity-calculation -->

<!-- modulo: m00009 -->

## 1.8 ¿Por qué Python?

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Nombrar dos hechos históricos sobre cómo se creó Python por primera vez.
- Describir dos maneras en que Python se considera un lenguaje popular.

### Antecedentes históricos

Python tiene una historia interesante. En 1982, [Guido van Rossum](https://openstax.org/r/100vanRossum), el creador de Python, empezó a trabajar en el [CWI](https://openstax.org/r/100CWI), un instituto nacional de investigación de los Países Bajos. Se unió a un equipo que estaba diseñando un nuevo lenguaje de programación, llamado ABC, para la enseñanza y la creación de prototipos. La simplicidad de ABC era ideal para principiantes, pero al lenguaje le faltaban las características necesarias para escribir programas avanzados.

Varios años después, van Rossum se unió a otro equipo del CWI que trabajaba en un sistema operativo. El equipo necesitaba una forma más fácil de escribir programas para supervisar computadoras y analizar datos. Los lenguajes comunes en la década de 1980 eran (y siguen siendo) difíciles de usar para este tipo de programas. Van Rossum imaginó un nuevo lenguaje que tuviera una sintaxis simple, como ABC, pero que también ofreciera las funciones avanzadas que necesitarían los profesionales.

Al principio, van Rossum comenzó a trabajar en este nuevo lenguaje como pasatiempo, en su tiempo libre. Lo llamó Python porque era fanático del grupo de comedia británico [Monty Python](https://openstax.org/r/100MontyPython). Durante el año siguiente, él y sus colegas usaron Python con éxito muchas veces en trabajo real. Con el tiempo, van Rossum decidió compartir Python con la comunidad de programación en general a través de internet. Compartió libremente todo el código fuente de Python para que cualquiera pudiera escribir y ejecutar programas en Python.

La primera versión de Python, conocida como Versión 0.9.0, apareció en 1991, unos seis años después de C++ y cuatro años antes de Java. Las decisiones de van Rossum de hacer el lenguaje simple pero avanzado, adecuado para las tareas cotidianas y disponible libremente en línea contribuyeron al éxito de Python a largo plazo.

**Video:** [Key decisions](https://www.openstax.org/r/key-decisions)

**Conceptos en práctica: Historia de Python**

<!-- pregunta: CPL-ch01-m08-p01 -->

1. El lenguaje de programación Python recibió su nombre de un(a) _____.

   - a) grupo de comedia británico
   - b) programador holandés
   - c) serpiente no venenosa

   <details><summary>Respuesta</summary>

   a) El lenguaje recibió su nombre de Monty Python. Solo por diversión, la documentación oficial hace referencias sutiles a los sketches de comedia de Monty Python.

   </details>

<!-- pregunta: CPL-ch01-m08-p02 -->

2. ¿Qué lenguaje de programación surgió primero?

   - a) Java
   - b) Python

   <details><summary>Respuesta</summary>

   b) La primera versión de Python salió en 1991, tras desarrollarse a finales de la década de 1980.

   </details>

<!-- pregunta: CPL-ch01-m08-p03 -->

3. ¿Qué oración describe mejor los comienzos de Python?

   - a) El CWI contrató a Guido van Rossum para diseñar un nuevo lenguaje de programación que compitiera con C++.
   - b) Python comenzó como un pasatiempo y se convirtió en código abierto tras varios años de desarrollo.
   - c) Van Rossum publicó el código fuente de Python en línea después de trabajar en el lenguaje durante un año.

   <details><summary>Respuesta</summary>

   c) Hacer que Python fuera de código abierto desde el principio permitió que muchos programadores aportaran comentarios.

   </details>

**Para saber más**

Para obtener más detalles sobre la historia de Python, consulta «[A brief history of Python](https://openstax.org/r/100history)», de Vasilisa Sheromova, y «[History and Philosophy of Python](https://openstax.org/r/100sheromova)», de Bernd Klein.

### Popularidad de Python

Con los años, Python se ha convertido en una organización sin fines de lucro con una comunidad próspera. Millones de programadores de todo el mundo usan Python para todo tipo de proyectos interesantes. Se han publicado cientos de miles de bibliotecas de Python como software de código abierto. La comunidad de Python es muy activa y solidaria en línea: responde preguntas y comparte código.

Una forma de ver la popularidad de Python es el [índice TIOBE](https://openstax.org/r/100TIOBE). TIOBE es una empresa holandesa que ofrece productos y servicios para medir la calidad del código de software. Desde 2001, TIOBE sigue la popularidad de los lenguajes de programación y publica los resultados en línea. El primer gráfico muestra el índice TIOBE a lo largo del tiempo para cinco de los lenguajes más populares.

El índice TIOBE se basa en el número de resultados de motores de búsqueda para cada lenguaje. El porcentaje indica cuántos resultados pertenecen a ese lenguaje. Python ha estado entre los 10 primeros lenguajes todos los años desde 2004. En octubre de 2021, Python se convirtió en el lenguaje n.º 1 del índice TIOBE. Ningún otro lenguaje aparte de C y Java había sido el n.º 1 durante los 20 años anteriores.

Otra forma de ver la popularidad de Python es analizar con qué frecuencia se habla de Python en línea. [Stack Overflow](https://openstax.org/r/100overflow) es un sitio web de preguntas y respuestas para programadores. El segundo gráfico muestra el número de preguntas formuladas cada mes que se etiquetaron con Python, JavaScript, etcétera. En los últimos años, Python se ha convertido en el lenguaje sobre el que más se pregunta en los foros de programación.

![Gráfico de dispersión con cinco líneas que representan la popularidad de Python, JavaScript, Java, C++ y C. El eje x abarca los años 2016 a 2023. El eje y va del 0 % al 20 % y representa el porcentaje de resultados de motores de búsqueda. La línea de JavaScript es casi plana y ronda entre el 2 % y el 4 %. La línea de C++ también es relativamente plana y va del 4 % al 8 % hasta 2022, cuando C++ sube al 14 % en 2023. La línea de C comienza alrededor del 12 %, baja al 8 % a mediados de 2017, vuelve a subir al 17 % en 2021, pero luego cae al 12 % en 2022. La línea de Java comienza en el 21 % en 2016, cae al 12 % en 2018, se mantiene arriba hasta mediados de 2020 y luego cae al 12 %. La línea de Python ronda el 4 % de 2016 a 2018, pero luego aumenta de forma constante hasta el 16 % en 2022.](media/Python_01_08_001.jpg)

***Índice TIOBE de la comunidad de programación**. Fuente: [www.tiobe.com](https://www.tiobe.com/tiobe-index/)*

![Gráfico de dispersión con cinco líneas que representan la popularidad de Python, JavaScript, Java, C++ y C. El eje x abarca los años 2016 a 2023. El eje y va del 0 % al 20 % y representa el porcentaje de preguntas formuladas. C y C++ están abajo, y rondan el 2 % y el 4 % respectivamente. Java comienza alrededor del 8 % pero disminuye de forma constante hasta cerca del 5 % en 2023. JavaScript ronda entre el 12 % y el 8 % y es el lenguaje principal hasta que Python lo supera en 2018. Python comienza en el 7 %, sube de forma constante hasta el 17 % en 2022 y baja al 14 % en 2023.](media/Python_01_08_002.jpg)

***Preguntas por mes en Stack Overflow**. Fuente: [data.stackexchange.com](https://data.stackexchange.com/)*

**Conceptos en práctica: Popularidad de Python**

<!-- pregunta: CPL-ch01-m08-p04 -->

1. Según el índice TIOBE, ¿qué dos lenguajes fueron los más populares de 2001 a 2021?

   - a) C y C++
   - b) Java y C
   - c) Python y JavaScript

   <details><summary>Respuesta</summary>

   b) Durante 20 años, Java y C se alternaron como el lenguaje principal hasta que Python tomó el primer lugar en 2021.

   </details>

<!-- pregunta: CPL-ch01-m08-p05 -->

2. ¿En qué año se convirtió Python en el lenguaje sobre el que más se pregunta en Stack Overflow?

   - a) 2018
   - b) 2019
   - c) 2020

   <details><summary>Respuesta</summary>

   a) La línea de Python cruza la línea de JavaScript a mediados de 2018.

   </details>

<!-- pregunta: CPL-ch01-m08-p06 -->

3. ¿Cuánto tiempo lleva TIOBE siguiendo la popularidad de los lenguajes de programación?

   - a) desde 1991
   - b) desde 2001
   - c) desde 2015

   <details><summary>Respuesta</summary>

   b) TIOBE comenzó a seguir la popularidad de los lenguajes en 2001, varios años después de que los motores de búsqueda web se hicieran populares.

   </details>

<!-- modulo: m00114 -->

## Resumen del capítulo

Este capítulo presentó los fundamentos de la programación en Python, entre ellos:

- `print()` e `input()`.
- Variables y asignación.
- Cadenas, enteros y floats.
- Aritmética y concatenación.
- Mensajes de error comunes.
- Comentarios y docstrings.

En este punto, deberías poder escribir programas que pidan una entrada, realicen cálculos simples y muestren los resultados. La práctica de programación que sigue reúne la mayoría de los temas presentados en el capítulo.

**Referencia del capítulo 1.**

| Función | Descripción |
|---|---|
| `print(values)` | Muestra al usuario uno o más valores, separados cada uno por un espacio. |
| `input(prompt)` | Si está presente, `prompt` se muestra al usuario. Luego la función lee una línea de entrada del usuario. |
| `len(string)` | Devuelve la longitud (el número de caracteres) de una cadena. |
| `type(value)` | Devuelve el tipo (o clase) de un valor. Ej.: `type(123)` es `<class 'int'>`. |
| **Operador** | **Descripción** |
| `=`  <br>(Asignación) | Asigna (o actualiza) el valor de una variable. En Python, las variables comienzan a existir cuando se les asigna un valor por primera vez. |
| `+`  <br>(Concatenación) | Une el contenido de dos cadenas y da como resultado una cadena nueva. |
| `+`  <br>(Suma) | Suma los valores de dos números. |
| `-`  <br>(Resta) | Resta el valor de un número a otro. |
| `*`  <br>(Multiplicación) | Multiplica los valores de dos números. |
| `/`  <br>(División) | Divide el valor de un número entre otro. |
| `**`  <br>(Exponenciación) | Eleva un número a una potencia. Ej.: `3**2` es tres al cuadrado. |
| **Sintaxis** | **Descripción** |
| `#`  <br>(Comentario) | Todo el texto se ignora desde el símbolo # hasta el final de la línea. |
| `'` o `"`  <br>(Cadena) | Las cadenas se pueden escribir con cualquiera de los dos tipos de comillas. Ej.: `'A'` y `"A"` representan la misma cadena. Por convención, este libro usa comillas dobles (`"`) para la mayoría de las cadenas. |
| `"""`  <br>(Docstring) | Se usa para la documentación, a menudo en cadenas de varias líneas, para resumir el propósito o el uso de un programa. |

**Pruébalo: Datos curiosos**

Escribe un programa que asigne a una variable llamada `number` un entero cualquiera de tu elección. Ej.: `number = 74`. Luego usa esta variable para calcular y mostrar los siguientes resultados:

```text
74 squared is 5476
74 cubed is 405224
One tenth of 74 is 7.4
74 plus 123 is 197
74 minus 456 is -382
```

Ejecuta el programa varias veces, usando un entero distinto cada vez. Tu salida debe ser matemáticamente correcta para cualquier entero que elijas.

El objetivo de este ejercicio es realizar aritmética básica dentro de una instrucción `print`. No uses ninguna otra variable además de `number`. Tu programa debe tener una sola instrucción de asignación (al comienzo).

<!-- coderunner: ch1/CodeRunner_01_10_13_Fun-facts -->

**Pruébalo: Mad lib**

Un mad lib es un juego de palabras en el que una persona pide a otras palabras para sustituirlas en una historia ya escrita. Luego la historia se lee en voz alta con el objetivo de hacer reír a la gente.

Este ejercicio se basa en el [Vacations Mad Lib](https://openstax.org/r/100madlibs) disponible en la sección [Printables](https://openstax.org/r/100printable) de MadLibs.com. Escribe un programa que pida al usuario que escriba dos adjetivos y dos sustantivos (la entrada del usuario está en negrita):

```text
Adjective: tranquil
Adjective: scandalous
Noun: pancake
Noun: field
```

Usa `input()` para mostrar cada indicador (prompt) exactamente como se indica. La entrada del usuario debe quedar en la misma línea que el indicador. Después de cada dos puntos debe haber exactamente un espacio. Después de leer la entrada, el programa debe mostrar las siguientes tres líneas:

```text
A vacation is when you take a trip to some tranquil place with your scandalous family.
Usually you go to some place that is near a/an pancake or up on a/an field.
```

Observa que la primera línea debe estar completamente en blanco. Reemplaza las palabras en negrita (del ejemplo anterior) por las palabras que realmente escribió el usuario.

Tu programa final debe tener cuatro instrucciones de entrada, tres instrucciones print y al menos dos comentarios. Para que quede completo, escribe un docstring adecuado al comienzo del programa.

<!-- coderunner: ch1/CodeRunner_01_10_14_Mad-lib -->
