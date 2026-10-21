# Capítulo 3: Objetos

<!-- modulo: m00020 -->

## Introducción

![contenedores de carga en un puerto](media/Python_03_00_000.jpg)

*crédito: modificación de la obra «Port of Melbourne», de Chris Phutully/Flickr, CC BY 2.0*

Un **objeto** es una unidad individual de datos en un programa de Python. Hasta ahora, este libro ha presentado tres tipos de objetos: cadenas, enteros y floats. Este capítulo examina más de cerca cómo se representan las cadenas y cómo se pueden formatear los enteros y los floats. Para comprender mejor qué es realmente un objeto, se hace hincapié en la relación entre las variables y los objetos. El capítulo también presenta dos tipos de contenedores: las listas y las tuplas. Un **contenedor** es un objeto que puede almacenar una cantidad arbitraria de otros objetos. Al final de este capítulo, podrás resolver problemas más complejos usando menos variables.

<!-- modulo: m00021 -->

## 3.1 Repaso de las cadenas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Extraer un carácter específico de una cadena mediante un índice.
- Usar secuencias de escape para representar caracteres especiales.

### Índices

Una cadena es una secuencia de cero o más caracteres. Cada carácter tiene un índice que indica la posición del carácter. Los índices se numeran de izquierda a derecha, comenzando en 0. Los índices también se numeran de derecha a izquierda, comenzando en -1.

**Video:** [String indexes](https://www.openstax.org/r/string-indexes)

**Conceptos en práctica: Índices de cadenas**

<!-- pregunta: CPL-ch03-m01-p01 -->

1. ¿Cuál es el índice del segundo carácter de una cadena?

   - a) 1
   - b) 2
   - c) -2

   <details><summary>Respuesta</summary>

   a) Como los valores de los índices comienzan en 0, el índice 1 se refiere al segundo carácter de la cadena.

   </details>

<!-- pregunta: CPL-ch03-m01-p02 -->

2. Si `s = "Python!"`, ¿cuál es el valor de `s[1] + s[-1]`?

   - a) `"P!"`
   - b) `"y!"`
   - c) `"yn"`

   <details><summary>Respuesta</summary>

   b) El carácter en el índice 1 es `y`, y el carácter en el índice -1 es `!`.

   </details>

<!-- pregunta: CPL-ch03-m01-p03 -->

3. Si `s = "Python!"`, ¿de qué tipo de objeto es `s[0]`?

   - a) carácter
   - b) entero
   - c) cadena

   <details><summary>Respuesta</summary>

   c) El resultado de `s[0]` es `"P"`, que es una cadena de longitud 1.

   </details>

### Unicode

Python usa **Unicode**, el estándar internacional para representar texto en las computadoras. Unicode define un número único, llamado **punto de código**, para cada carácter posible. Ej.: `"P"` tiene el punto de código 80, y `"!"` tiene el punto de código 33.

La función integrada `ord()` convierte un carácter en un punto de código. Ej.: `ord("P")` devuelve el entero 80. De manera similar, la función integrada `chr()` convierte un punto de código en un carácter. Ej.: `chr(33)` devuelve la cadena `"!"`.

Unicode es una extensión de **ASCII**, el Código Estándar Estadounidense para el Intercambio de Información (American Standard Code for Information Interchange). Originalmente, ASCII definía solo 128 puntos de código, suficientes para admitir el idioma inglés. Unicode define más de un millón de puntos de código y admite la mayoría de los idiomas escritos del mundo.

**Valores de los caracteres.**

|  |  |  |
|---|---|---|
| ```python<br>32  (space)<br>33  !<br>34  "<br>35  #<br>36  $<br>37  %<br>38  &<br>39  '<br>40  (<br>41  )<br>42  *<br>43  +<br>44  ,<br>45  -<br>46  .<br>47  /<br>48  0<br>49  1<br>50  2<br>51  3<br>52  4<br>53  5<br>54  6<br>55  7<br>56  8<br>57  9<br>58  :<br>59  ;<br>60  <<br>61  =<br>62  ><br>63  ?<br>``` | ```python<br>64  @<br>65  A<br>66  B<br>67  C<br>68  D<br>69  E<br>70  F<br>71  G<br>72  H<br>73  I<br>74  J<br>75  K<br>76  L<br>77  M<br>78  N<br>79  O<br>80  P<br>81  Q<br>82  R<br>83  S<br>84  T<br>85  U<br>86  V<br>87  W<br>88  X<br>89  Y<br>90  Z<br>91  [<br>92  \<br>93  ]<br>94  ^<br>95  _<br>``` | ```python<br> 96  `<br> 97  a<br> 98  b<br> 99  c<br>100  d<br>101  e<br>102  f<br>103  g<br>104  h<br>105  i<br>106  j<br>107  k<br>108  l<br>109  m<br>110  n<br>111  o<br>112  p<br>113  q<br>114  r<br>115  s<br>116  t<br>117  u<br>118  v<br>119  w<br>120  x<br>121  y<br>122  z<br>123  {<br>124  \|<br>125  }<br>126  ~<br>127  (delete)<br>``` |

*Esta tabla muestra los puntos de código del 32 al 127 según los definen ASCII y Unicode. Los puntos de código del 0 al 31 son caracteres no imprimibles que se usaban para las telecomunicaciones.*

**Conceptos en práctica: ord() y chr()**

<!-- pregunta: CPL-ch03-m01-p04 -->

1. ¿Cuál es el punto de código de la letra A?

   - a) 1
   - b) 65
   - c) 97

   <details><summary>Respuesta</summary>

   b) Los puntos de código del 65 al 90 se usan para las letras mayúsculas.

   </details>

<!-- pregunta: CPL-ch03-m01-p05 -->

2. ¿Qué valor devuelve `ord("0")`?

   - a) `0`
   - b) `48`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) El punto de código del carácter `"0"` es 48.

   </details>

<!-- pregunta: CPL-ch03-m01-p06 -->

3. ¿Qué devuelve `chr(126)`?

   - a) `~`
   - b) `"~"`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) La tilde (~) es el carácter del punto de código 126. La función `chr()` devuelve una cadena de longitud uno.

   </details>

### Caracteres especiales

Una **secuencia de escape** usa una barra invertida (\) para representar un carácter especial dentro de una cadena.

**Secuencias de escape comunes.**

| Secuencia de escape | Significado | Ejemplo | Salida en pantalla |
|---|---|---|---|
| `\n` | Un carácter de salto de línea que indica el final de una línea de texto. | `print("Escape\nsequence!")` | `Escape`  <br>`sequence!` |
| `\t` | Un carácter de tabulación; útil para sangrar párrafos o alinear texto en varias líneas. | `print("Escape\tsequence!")` | `Escape    sequence!` |
| `\'` | Una comilla simple; una alternativa a encerrar la cadena entre comillas dobles. | `print('I\'ll try my best!')` | `I'll try my best` |
| `\"` | Una comilla doble; una alternativa a encerrar la cadena entre comillas simples. | `print("I heard you said \"Yes\"")` | `I heard you said "Yes"` |
| `\\` | Un carácter de barra invertida. | `print("This prints a \\")` | `This prints a \` |

**Conceptos en práctica: Tabulaciones y saltos de línea**

<!-- pregunta: CPL-ch03-m01-p07 -->

1. ¿Cuál de las siguientes es una secuencia de escape?

   - a) `t`
   - b) `/t`
   - c) `\t`

   <details><summary>Respuesta</summary>

   c) Una secuencia de escape tiene dos caracteres de longitud y comienza con una barra invertida (\).

   </details>

<!-- pregunta: CPL-ch03-m01-p08 -->

2. ¿Qué instrucción imprime una barra invertida (\) en la pantalla?

   - a) `print(\\)`
   - b) `print(\"\")`
   - c) `print("\\")`

   <details><summary>Respuesta</summary>

   c) La primera barra invertida indica una secuencia de escape, y la segunda barra invertida indica el carácter.

   </details>

<!-- pregunta: CPL-ch03-m01-p09 -->

3. ¿Qué instrucción imprime Enter y here en líneas separadas?

   - a) `print("Enter here")`
   - b) `print("Enter" + \n + "here")`
   - c) `print("Enter" + "\n" + "here")`

   <details><summary>Respuesta</summary>

   c) La secuencia de escape `\n` produce un salto de línea. `print("Enter\nhere")` produce el mismo resultado.

   </details>

**Pruébalo: Cita de Hopper**

[Grace Hopper](https://openstax.org/r/100gracehopper) (1906–1992) fue una famosa científica de la computación (¡y contraalmirante de la Marina de los EE. UU.!) que ideó los lenguajes de programación independientes de la máquina. Imaginó un lenguaje de programación basado en el inglés e hizo muchas contribuciones que allanaron el camino para los lenguajes de programación modernos, incluido Python.

Escribe un programa que imprima el siguiente texto, incluidas las comillas. Tu programa no puede usar comillas simples (') en ninguna parte del código. La última línea debe estar sangrada con un carácter de tabulación.

```python norun
"To me programming is more than an important practical art.
It is also a gigantic undertaking in the foundations of knowledge."
    -- Grace Hopper
```

<!-- coderunner: ch3/CodeRunner_03_02_01_Hopper-quote -->

**Pruébalo: Cifrado por desplazamiento**

Durante el Imperio romano, Julio César (100–44 a. C.) usaba una técnica sencilla para cifrar mensajes privados. Cada letra del mensaje se reemplazaba por la tercera letra siguiente del alfabeto. Ej.: si el mensaje era CAT, la C se convertía en F, la A en D y la T en W, lo que daba como resultado el mensaje FDW. Esta técnica se conoce como cifrado por desplazamiento porque cada letra se desplaza una cierta cantidad. En el caso de César, la cantidad era tres, pero otras cantidades (además de 0) también funcionarían.

Escribe un programa que pida al usuario que ingrese los dos valores siguientes (entrada de ejemplo en negrita):

```text
Enter a 3-letter word: CAT
Shift by how many letters? 3
```

Luego, el programa debe desplazar cada letra de la palabra según la cantidad indicada. Con base en el ejemplo anterior, la salida sería:

```text
The secret message is: FDW
```

Pista: usa la función `ord()` para convertir cada letra en un entero, suma la cantidad de desplazamiento a cada entero, usa la función `chr()` para convertir cada entero en un carácter y concatena los caracteres resultantes.

<!-- coderunner: ch3/CodeRunner_03_02_02_Shift-cipher -->

<!-- modulo: m00022 -->

## 3.2 Cadenas con formato

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar f-strings para simplificar la salida con varios valores.
- Dar formato a números con ceros a la izquierda y precisión fija.

### F-strings

Un **literal de cadena con formato** (o **f-string**) es un literal de cadena que lleva el prefijo `"f"` o `"F"`. Un **campo de reemplazo** es una expresión entre llaves (`{}`) dentro de una f-string. Ej.: la cadena `f"Good morning, {first} {last}!"` tiene dos campos de reemplazo: uno para el nombre y otro para el apellido. Las f-strings ofrecen una manera cómoda de combinar varios valores en una sola cadena.

**Video:** [Printing an f-string](https://www.openstax.org/r/printing-f-string)

**Conceptos en práctica: f-strings básicas**

<!-- pregunta: CPL-ch03-m02-p01 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   animal = "dog"
   says = "bark"
   print(f"My {animal} says {says} {says} {says}")
   ```

   - a) `My dog bark bark bark bark`
   - b) `My dog says bark bark bark`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) La misma variable, `says`, se usa en tres campos de reemplazo.

   </details>

<!-- pregunta: CPL-ch03-m02-p02 -->

2. ¿Cuál es la salida del siguiente código?
   
   ```python
   temp = "hot"
   food = "potato"
   print("{temp} {food}")
   ```

   - a) `{temp} {food}`
   - b) `hot potato`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) La cadena no es una f-string, por lo que los caracteres de llaves (alrededor de temp y food) se imprimen literalmente.

   </details>

<!-- pregunta: CPL-ch03-m02-p03 -->

3. ¿Cómo se puede reescribir el siguiente código usando una f-string?
   
   ```python norun
   print(x, "+", y, "=", x + y)
   ```

   - a) `print(f"x + y = {x+y}")`
   - b) `print(f"{x + y} = {x + y}")`
   - c) `print(f"{x} + {y} = {x+y}")`

   <details><summary>Respuesta</summary>

   c) Usar una f-string permite especificar toda la salida sin comas ni comillas adicionales.

   </details>

### Formato de números

Los programas suelen necesitar mostrar números con un formato específico. Ej.: al mostrar la hora, los minutos se formatean como enteros de dos dígitos. Si la hora es 9 y el minuto es 5, entonces la hora es «9:05» (no «9:5»).

En una f-string, un campo de reemplazo puede incluir un especificador de formato introducido por dos puntos. Un **especificador de formato** define cómo se debe dar formato a un valor para mostrarlo. Ej.: en la cadena `f"{hour}:{minute:02d}"`, el especificador de formato de `minute` es `02d`.

**Ejemplos de especificadores de formato.**

| Formato | Descripción | Ejemplo | Resultado |
|---|---|---|---|
| `d` | Entero decimal (formato de entero predeterminado). | `f"{12345678:d}"` | `'12345678'` |
| `,d` | Entero decimal, con comas como separadores. | `f"{12345678:,d}"` | `'12,345,678'` |
| `10d` | Entero decimal, de al menos 10 caracteres de ancho. | `f"{12345678:10d}"` | `'  12345678'` |
| `010d` | Entero decimal, de al menos 10 caracteres de ancho, con ceros a la izquierda. | `f"{12345678:010d}"` | `'0012345678'` |
| `f` | Punto fijo (el valor predeterminado es 6 decimales). | `f"{math.pi:f}"` | `'3.141593'` |
| `.4f` | Punto fijo, redondeado a 4 decimales. | `f"{math.pi:.4f}"` | `'3.1416'` |
| `8.4f` | Punto fijo, redondeado a 4 decimales, de al menos 8 caracteres de ancho. | `f"{math.pi:8.4f}"` | `'  3.1416'` |
| `08.4f` | Punto fijo, redondeado a 4 decimales, de al menos 8 caracteres de ancho, con ceros a la izquierda. | `f"{math.pi:08.4f}"` | `'003.1416'` |

*La tabla muestra formas comunes de dar formato a los números. Hay muchas más opciones de formato, descritas en el [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) de Python.*

**Conceptos en práctica: Formato de números**

<!-- pregunta: CPL-ch03-m02-p04 -->

1. ¿Qué f-string da formato a una fecha como `MM/DD/YYYY`?

   - a) `f"{month:02d}/{day:02d}/{year}"`
   - b) `f"{month:2d}/{day:2d}/{year}"`
   - c) `f"{month}/{day}/{year}"`

   <details><summary>Respuesta</summary>

   a) El especificador de formato `02d` agrega un 0 al principio del entero cuando este tiene un solo dígito.

   </details>

<!-- pregunta: CPL-ch03-m02-p05 -->

2. ¿Qué instrucción muestra la variable `money` redondeada a dos decimales?

   - a) `print(f"{money:2d}")`
   - b) `print(f"{money:2f}")`
   - c) `print(f"{money:.2f}")`

   <details><summary>Respuesta</summary>

   c) El especificador de formato `".2f"` (con un punto) significa punto fijo, redondeado a dos decimales.

   </details>

<!-- pregunta: CPL-ch03-m02-p06 -->

3. ¿Qué especificador de formato muestra un número de punto flotante con comas como separadores y redondeado a dos decimales?

   - a) `.2,f`
   - b) `,.2f`
   - c) `,d.2f`

   <details><summary>Respuesta</summary>

   b) Este especificador de formato es útil para mostrar grandes cantidades de dinero.

   </details>

**Pruébalo: Mad lib (f-string)**

Un [mad lib](https://openstax.org/r/100fstring) es una historia divertida que usa palabras proporcionadas por un usuario. El siguiente mad lib se basa en cuatro palabras (entrada del usuario en negrita):

```text
Enter a name: Buster
Enter a noun: dog
Enter an adjective: super
Verb ending in -ing: swimming

Buster, the super dog, likes to go swimming.
```

Gran parte del código de este mad lib ya está escrito. Completa el código siguiente escribiendo la f-string.

<!-- coderunner: ch3/CodeRunner_03_03_03_Mad-lib-(f-string) -->

**Pruébalo: Calculadora de salario**

Acabas de conseguir un trabajo de medio tiempo y quieres calcular cuánto dinero ganarás. Escribe un programa que pida la hora a la que empiezas a trabajar, la hora a la que terminas y tu tarifa por hora (entrada de ejemplo en negrita):

```text
Starting hour: 9
Starting minute: 30
Stopping hour: 11
Stopping minute: 0
Hourly rate: 15
```

Con base en la entrada del usuario, tu programa debe calcular y mostrar los siguientes resultados:

```text
Worked 9:30 to 11:00
Total hours: 1.5
Payment: $22.50
```

Para este ejercicio, debes escribir código que (1) calcule el pago total y (2) dé formato a las tres líneas de salida. Usa f-strings y especificadores de formato para mostrar los minutos con dos dígitos, las horas con un decimal y el pago con dos decimales. El código de entrada se proporciona como punto de partida.

Supón que se usa un reloj de 24 horas. Ej.: se usa 16:15 en lugar de 4:15 p. m.

<!-- coderunner: ch3/CodeRunner_03_03_04_Wage-calculator -->

<!-- modulo: m00023 -->

## 3.3 Repaso de las variables

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Distinguir entre variables, objetos y referencias.
- Dibujar diagramas de memoria con enteros, floats y cadenas.

### Referencias a objetos

En Python, cada variable hace referencia a un objeto. La instrucción de asignación `message = "Hello"` hace que la variable `message` haga referencia al objeto `"Hello"`. Varias variables pueden hacer referencia al mismo objeto. Ej.: `greeting = message` hace que `greeting` haga referencia al mismo objeto que `message`. Un **diagrama de memoria** muestra la relación entre las variables y los objetos.

**Video:** [Example memory diagram](https://www.openstax.org/r/memory-diagram)

**Conceptos en práctica: Variables y objetos**

<!-- pregunta: CPL-ch03-m03-p01 -->

1. ¿Cuántas instrucciones de asignación hay en la animación anterior?

   - a) 2
   - b) 3
   - c) 4

   <details><summary>Respuesta</summary>

   b) Cada línea del programa de la animación es una instrucción de asignación.

   </details>

<!-- pregunta: CPL-ch03-m03-p02 -->

2. ¿Cuál de las siguientes opciones describe mejor los objetos asignados?

   - a) dos objetos float
   - b) dos objetos int, un objeto float
   - c) un objeto int, un objeto float

   <details><summary>Respuesta</summary>

   c) El programa asigna el objeto int `10` y el objeto float `9.7`, como se muestra en el diagrama de memoria.

   </details>

<!-- pregunta: CPL-ch03-m03-p03 -->

3. ¿Qué símbolo se usa para mostrar el valor actual de una variable?

   - a) una flecha
   - b) un cuadro negro pequeño
   - c) un cuadro redondeado

   <details><summary>Respuesta</summary>

   a) Una flecha muestra a qué objeto hace referencia una variable en ese momento.

   </details>

**Para saber más**

[Python Tutor](https://openstax.org/r/100pythontutor) es una herramienta gratuita en línea para visualizar la ejecución de código. Un usuario puede ingresar cualquier código de Python, hacer clic en Visualize Execution y luego hacer clic en el botón Next para ejecutar el código una línea a la vez. Aquí está el [ejemplo de calificación y puntaje](https://openstax.org/r/100ratingscore) de la animación anterior.

Python Tutor también es útil para dibujar diagramas de memoria similares a los de este libro. Antes de hacer clic en Visualize Execution, cambia la opción del medio de «inline primitives, don't nest objects [default]» a «render all objects on the heap (Python/Java)», como se muestra en la siguiente captura de pantalla:

![Captura de pantalla de la configuración de Python Tutor, con la lista desplegable del medio abierta en la última opción.](media/Python_03_03_001.jpg)

### Propiedades de los objetos

Todo objeto tiene una identidad, un tipo y un valor:

- La **identidad** de un objeto es un entero único asociado con el objeto. Por lo general, este entero se refiere a la ubicación de memoria donde se almacena el objeto. Una vez creado, la identidad de un objeto nunca cambia. La función integrada `id()` devuelve la identidad del objeto.
- El **tipo** de un objeto determina los valores y las operaciones posibles del objeto. Ej.: los enteros y los floats se pueden «dividir» con el operador `/`, pero las cadenas no. La función integrada `type()` devuelve el tipo del objeto.
- El **valor** de un objeto representa el estado actual del objeto. Muchos objetos, como los números y las cadenas, no se pueden modificar una vez creados. Algunos objetos, como las listas (que se presentan más adelante), están diseñados para modificarse.

**Video:** [Identity, type, and value](https://www.openstax.org/r/identity-type-value)

**Conceptos en práctica: id() y type()**

<!-- pregunta: CPL-ch03-m03-p04 -->

1. ¿Qué valor podría devolver `id(rating)`?

   - a) `9793344`
   - b) `<class 'float'>`
   - c) `10.0`

   <details><summary>Respuesta</summary>

   a) La identidad de un objeto es un entero que representa la ubicación de memoria.

   </details>

<!-- pregunta: CPL-ch03-m03-p05 -->

2. ¿Qué valor podría devolver `type(rating)`?

   - a) `10.0`
   - b) `"float"`
   - c) `<class 'float'>`

   <details><summary>Respuesta</summary>

   c) La función type devuelve el nombre de la clase de un objeto, como int, float o str.

   </details>

<!-- pregunta: CPL-ch03-m03-p06 -->

3. ¿Qué expresión devuelve el valor de un objeto?

   - a) `value(rating)`
   - b) `rating`
   - c) `"rating"`

   <details><summary>Respuesta</summary>

   b) Una variable hace referencia a un objeto, por lo que el valor de la variable es el valor del objeto.

   </details>

**Para saber más**

Como se muestra en un diagrama de memoria, las variables y los objetos son dos ideas distintas. Llamar a una función como `id()` o `type()` devuelve información sobre un objeto, no sobre una variable. De hecho, una variable no tiene identidad ni tipo, como se muestra en este ejemplo:

```python norun
>>> rating = 10  # Objeto entero en algún lugar de la memoria.
>>> type(rating)
<class 'int'>
>>> id(rating)
9793344
>>> rating = "ten"  # Objeto cadena en otro lugar de la memoria.
>>> type(rating)
<class 'str'>
>>> id(rating)
140690967388272
```

Se podría pensar, de forma incorrecta, que el tipo o la identidad de la variable rating cambia. Sin embargo, lo único que cambia es a qué objeto hace referencia la variable rating.

**Pruébalo: Tres variables**

1. Dibuja un diagrama de memoria para el siguiente código:

   ```python norun
   a = 1
b = 2
c = b
b = a
a = c
   ```
2. Ejecuta el código en [Python Tutor](https://openstax.org/r/100pythruncode) para comprobar tu respuesta.
3. Con base en tu diagrama, responde estas preguntas:

   - ¿Cuál es el valor final de `a`, `b` y `c`?
   - ¿Cuántos objetos enteros se crean?

**Pruébalo: Diferentes tipos**

1. Dibuja un diagrama de memoria para el siguiente código:

   ```python norun
   name = "Chocolate"
length = len(name)
price = 1.99
lower = min(length, price)
product = name
name = name * 2
   ```
2. Ejecuta el código en [Python Tutor](https://openstax.org/r/100pythruncode) para comprobar tu respuesta.
3. Con base en tu diagrama, responde estas preguntas:

   - ¿Cuál es el tipo y el valor de cada objeto?
   - ¿A qué objeto hace referencia cada variable?

<!-- modulo: m00024 -->

## 3.4 Conceptos básicos de las listas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar índices para acceder a elementos individuales de una lista.
- Usar índices para modificar elementos individuales de una lista.
- Usar la función `len()` para encontrar la longitud de una lista.
- Demostrar que las listas se pueden cambiar después de su creación.

### Listas

Un objeto lista se puede usar para agrupar elementos en Python. Una lista se define con corchetes `[]` y valores separados por comas dentro de los corchetes. Ej.: `list_1 = [1, 2, 4]`.

Las listas vacías se pueden definir de dos maneras:

- `list_1 = []`
- `list_1 = list()`

Las listas pueden estar formadas por elementos de cualquier tipo. Pueden contener enteros, cadenas, floats o cualquier otro tipo. Las listas también pueden contener una combinación de tipos. Ej.: `[2, "Hello", 2.5]` es una lista válida.

Las listas de Python permiten a los programadores cambiar el contenido de la lista de varias maneras.

**Video:** [Lists](https://www.openstax.org/r/lists)

**Conceptos en práctica: Listas**

<!-- pregunta: CPL-ch03-m04-p01 -->

1. ¿Cuál es la forma correcta de crear una lista con los números 3, 4 y 5?

   - a) `new_list == [3, 4, 5]`
   - b) `new_list = [3, 4, 5]`
   - c) `new_list = (3, 4, 5)`

   <details><summary>Respuesta</summary>

   b) Una lista de números se puede crear usando un operador de asignación.

   </details>

<!-- pregunta: CPL-ch03-m04-p02 -->

2. ¿Cuál de las siguientes no es una forma válida de especificar una lista en Python?

   - a) `my_list = [2, 2 3, 23]`
   - b) `my_list = ["Jimmy", 2, "times"]`
   - c) `my_list = ["C", "C++", "Python", "Java", "Rust", "Scala"]`

   <details><summary>Respuesta</summary>

   a) Los elementos individuales de una lista deben estar separados por una coma. Python no entiende qué se quiere decir con `2 3`.

   </details>

### Uso de índices

Se puede acceder directamente a los elementos individuales de una lista mediante un índice. Los índices comienzan en 0 y terminan en uno menos que la longitud de la secuencia. Ej.: en una secuencia de 50 elementos, la primera posición es 0 y la última posición es 49.

El número de índice se coloca entre corchetes `[]` y se adjunta al final del nombre de la lista para acceder al elemento deseado. Ej.: `new_list[3]` accede al cuarto elemento de `new_list`. También se puede usar como índice una expresión que se evalúe como un número entero. Al igual que con las cadenas, también se pueden usar índices negativos para acceder a elementos individuales. Ej.: el índice -1 se refiere al último elemento y el -2 al penúltimo.

La función `len()`, cuando se llama sobre una lista, devuelve la longitud de la lista.

**Ejemplo: Índices de listas y la función len()**

El siguiente código muestra el uso de los índices de listas y de la función `len()`. La línea 6 muestra el uso de la función `len()` para obtener la longitud de la lista. La línea 10 muestra cómo acceder a un elemento mediante un índice. La línea 14 muestra cómo modificar un elemento de una lista mediante un índice.

```python
# Crear una lista de números
num_list = [2, 3, 5, 9, 11]
print(num_list)

# Imprimir la longitud de la lista
print("Length: ", len(num_list))

# Imprimir el cuarto elemento de la lista
# El número 3 se usa para referirse al cuarto elemento
print("4th element:", num_list[3])

# En realidad, el valor deseado del cuarto elemento es 7
# Actualizar el valor del cuarto elemento a 7
num_list[3] = 7

# La lista de los primeros 5 números primos
print(num_list)
```

La salida del código anterior es:

```text
[2, 3, 5, 9, 11]
Length: 5
4th element: 9
[2, 3, 5, 7, 11]
```

**Conceptos en práctica: Índices de listas y la función len()**

<!-- pregunta: CPL-ch03-m04-p03 -->

1. ¿Cuál es la forma correcta de acceder al elemento 17 de una lista llamada `cardList`?

   - a) `card_list[17]`
   - b) `card_list(16)`
   - c) `card_list[16]`

   <details><summary>Respuesta</summary>

   c) Como los índices comienzan en 0, el número necesario es uno menos que la posición a la que se accede.

   </details>

<!-- pregunta: CPL-ch03-m04-p04 -->

2. ¿Cuál es la forma correcta de modificar el elemento `"Tom"` a `"Tim"` en la siguiente lista?
   
   ```python
   name_list = ["Carla", "Monique", "Westin", "Tom"]
   ```

   - a) `name_list[-1] = "Tim"`
   - b) `name_list[4] = "Tim"`
   - c) `name_list[end] = "Tim"`

   <details><summary>Respuesta</summary>

   a) El índice -1 siempre se refiere al último elemento de una lista. Aquí también se puede usar la expresión `len(name_list)-1`, que se evalúa como `3` y se refiere al último elemento de una lista de 4 elementos, en lugar de -1.

   </details>

**Pruébalo: Conceptos básicos de listas**

Escribe un programa que haga lo siguiente:

1. Crea una lista con los siguientes elementos: 2, 23, 39, 6, -5.
2. Cambia el tercer elemento de la lista (índice 2) a 35.
3. Imprime la lista resultante y la longitud de la lista.

<!-- coderunner: ch3/CodeRunner_03_05_05_List-basics -->

<!-- modulo: m00025 -->

## 3.5 Conceptos básicos de las tuplas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir las características y los beneficios de una tupla.
- Desarrollar un programa que cree y use una tupla correctamente.
- Identificar y analizar la mutabilidad de una tupla.

### Creación de tuplas y acceso a los elementos

Una **tupla** es una secuencia de valores separados por comas que puede contener elementos de diferentes tipos. Una tupla debe crearse con comas entre los valores y, por convención, la secuencia se encierra entre paréntesis. Se accede a cada elemento mediante su índice, empezando por el primer elemento en el índice 0.

**Ejemplos de tuplas.**

|  |  |
|---|---|
| ```python<br>tuple_1 = (2, 3, 4)<br>print(f'tuple_1: {tuple_1}')<br>print(tuple_1[1])<br>print()<br>data_13 = ('Aimee Perry', 96, [94, 100, 97, 93])<br>print(f'data_13: {data_13}')<br>print(data_13[2])<br>``` | ```python<br>tuple_1: (2, 3, 4)<br>3<br><br>data_13: ('Aimee Perry', 96, [94, 100, 97, 93])<br>[94, 100, 97, 93]<br>``` |

**Conceptos en práctica: Creación de tuplas y acceso a los elementos**

<!-- pregunta: CPL-ch03-m05-p01 -->

1. Considera el ejemplo anterior. ¿Cuál accede al primer elemento de `tuple_1`?

   - a) `tuple_1[0]`
   - b) `tuple_1[1]`
   - c) `tuple_1[2]`

   <details><summary>Respuesta</summary>

   a) El primer elemento, `2`, está en el índice 0.

   </details>

<!-- pregunta: CPL-ch03-m05-p02 -->

2. ¿Cuál crea una tupla válida?

   - a) `tuple_2 = (42, 26, 13)`
   - b) `tuple_3 = (42, 26, 13.5)`
   - c) ambas

   <details><summary>Respuesta</summary>

   c) Las tuplas pueden tener elementos del mismo tipo, así como elementos de tipos diferentes.

   </details>

<!-- pregunta: CPL-ch03-m05-p03 -->

3. ¿Cuál crea una tupla con tres elementos?

   - a) `my_tuple = 'a', 'b', 'c'`
   - b) `my_tuple = ['a', 'b', 'c']`
   - c) `my_tuple = ('a', 'b', 'c')`

   <details><summary>Respuesta</summary>

   a) Una tupla debe crearse usando comas. Los paréntesis son opcionales, pero se recomiendan. Los tres elementos son `"a"`, `"b"` y `"c"`.

   </details>

### Propiedades de las tuplas

¿Cómo se comparan las tuplas con las listas? Las tuplas están ordenadas y permiten duplicados, como las listas, pero tienen una mutabilidad diferente. Un objeto **inmutable** no se puede modificar después de su creación. Un objeto **mutable** se puede modificar después de su creación. Las tuplas son inmutables, mientras que las listas son mutables.

**Video:** [Mutability of a tuple vs. a list](https://www.openstax.org/r/mutability-tuple-list)

**Conceptos en práctica: Uso de tuplas**

<!-- pregunta: CPL-ch03-m05-p04 -->

1. Considera el programa final del ejemplo anterior. ¿Cuál es el valor de `my_tuple`?

   - a) `(0.693, 0.414, 3.142)`
   - b) `(0.693, 1.414, 3.142)`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) A `my_tuple` se le asigna inicialmente la tupla `(0.693, 0.414, 3.142)`. Luego se le asigna la nueva tupla `(0.693, 1.414, 3.142)` para corregir un error en el segundo elemento.

   </details>

<!-- pregunta: CPL-ch03-m05-p05 -->

2. ¿Por qué el siguiente código produce un error?
   
   ```python norun
   tuple_1 = ('alpha', 'bravo', 'charlie')
   tuple_1.append('charlie')
   ```

   - a) No se permite usar append.
   - b) No se permiten duplicados.
   - c) No se permiten cadenas.

   <details><summary>Respuesta</summary>

   a) Las tuplas son inmutables. No se pueden hacer cambios, incluido agregar elementos, después de crear la tupla.

   </details>

<!-- pregunta: CPL-ch03-m05-p06 -->

3. Un programador quiere crear una secuencia de constantes para consultarlas fácilmente y que no se puedan cambiar en ninguna parte del programa. ¿Qué secuencia sería la más adecuada?

   - a) lista
   - b) tupla

   <details><summary>Respuesta</summary>

   b) Las tuplas son inmutables, por lo que los intentos de cambio producen errores. Usar una tupla protegería las constantes de cambios accidentales.

   </details>

**Mutabilidad y rendimiento**

Las tuplas son inmutables y tienen un tamaño fijo, por lo que usan menos memoria. En general, las tuplas son más rápidas de crear y de acceder, lo que se traduce en un mejor rendimiento que puede notarse con grandes cantidades de datos.

**Pruébalo: Crear una tupla a partir de una lista**

Supón que un programador quiere crear una tupla a partir de una lista para evitar cambios futuros. La función `tuple()` crea una tupla a partir de un objeto como una lista. Ej.: `my_tuple = tuple(my_list)` crea una tupla a partir de la lista `my_list`. Actualiza el siguiente programa para crear una tupla `final_grades` a partir de la lista grades.

<!-- coderunner: ch3/CodeRunner_03_06_06_Creating-a-tuple-from-a-list -->

**Pruébalo: Crear una tupla con entrada del usuario**

Escribe un programa que lea dos cadenas y dos enteros de la entrada y cree una tupla, `my_data`, con los cuatro valores.

Dada la entrada:

```text
x
y
15
20
```

La salida es:

```text
my_data: ('x', 'y', 15, 20)
```

<!-- coderunner: ch3/CodeRunner_03_06_07_Creating-a-tuple-with-user-input -->

<!-- modulo: m00026 -->

## Resumen del capítulo

Los puntos principales de este capítulo son:

- Una **cadena** es una secuencia de valores que representa puntos de código Unicode.
- Un **índice** se refiere a la posición de un valor en una secuencia (cadena, lista, tupla).
- Los índices positivos van de 0 a longitud–1. Los índices negativos van de –1 a –longitud.
- Las f-strings son una forma cómoda de imprimir varias salidas y dar formato a enteros y floats.
- Las variables hacen referencia a objetos. Los diagramas de memoria son útiles para dibujar variables y objetos.
- Un objeto lista se puede usar para hacer referencia a varios objetos, por índice, usando la misma variable.
- Una tupla es similar a una lista, pero usa paréntesis y no se puede cambiar una vez creada.

**Referencia del capítulo 3.**

| Código | Descripción |
|---|---|
| `ord(c)` | Obtiene un entero que representa el punto de código Unicode de un carácter. |
| `chr(i)` | Convierte un punto de código Unicode (entero) en una cadena de un solo carácter. |
| `'\n'` | Secuencia de escape del carácter de salto de línea. |
| `'\t'` | Secuencia de escape del carácter de tabulación. |
| `f"{number:.02d}"` | Crea una cadena dando formato a un entero para que tenga al menos dos dígitos. |
| `f"{number:.2f}"` | Crea una cadena dando formato a un float para que tenga dos decimales. |
| `id(object)` | Obtiene la identidad (ubicación de memoria) de un objeto. |
| `type(object)` | Obtiene el tipo (nombre de la clase) de un objeto. |
| `my_list = ["a", "b", "c"]` | Crea una lista de tres cadenas. |
| `my_tuple = ("a", "b", "c")` | Crea una tupla de tres cadenas. |
| `my_list[0]` | Obtiene el primer elemento `("a")` de `my_list`. |
| `my_tuple[-1]` | Obtiene el último elemento `("c")` de `my_tuple`. |
