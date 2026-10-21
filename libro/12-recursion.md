# Capítulo 12: Recursión

<!-- modulo: m00087 -->

## Introducción

![Foto de una concha marina que muestra un patrón de espiral recursivo.](media/Python_12_00_000.jpg)

*crédito: modificación de la obra «Rings from the Ocean», de Sue Corbisez/Flickr, CC BY 2.0*

La recursión es una potente técnica de programación para escribir soluciones de forma compacta. La recursión simplifica los programas al llamar a versiones más pequeñas de un problema dado, que se usan para generar la solución del problema general.

En la programación avanzada, algunos programas son difíciles de escribir sin usar recursión. Por eso la recursión es también un estilo de programación que nos permite simplificar los programas.

La recursión permite que un fragmento de código, una función, llame al mismo fragmento de código, la misma función, con parámetros diferentes.

<!-- modulo: m00088 -->

## 12.1 Conceptos básicos de la recursión

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir el concepto de recursión.
- Demostrar cómo la recursión usa soluciones sencillas para construir una solución mejor.

### Recursión

La **recursión** es una técnica de resolución de problemas que usa la solución de una versión más simple del problema para resolver el problema más grande. A su vez, la misma técnica se puede aplicar a la versión más simple.

**Video:** [Tres torres](https://www.openstax.org/r/towers)

**Conceptos en práctica: Tres torres y la recursión**

<!-- pregunta: CPL-ch12-m01-p01 -->

1. ¿Cómo se resuelve con recursión el problema de mover dos anillos?

   - a) Mover el anillo pequeño a la torre del medio, mover el anillo más grande a la torre de destino y mover el anillo pequeño a la torre de destino.
   - b) Mover dos anillos de la torre de origen a la torre de destino.
   - c) No se puede resolver con recursión.

   <details><summary>Respuesta</summary>

   a) El movimiento del anillo más pequeño, que es un problema más pequeño, se realiza dos veces en el camino hacia la solución de los dos anillos en conjunto. La tarea de mover los tres anillos se descompone en tareas más pequeñas: mover un anillo a la vez.

   </details>

<!-- pregunta: CPL-ch12-m01-p02 -->

2. ¿Cómo se resuelve con recursión el problema de mover tres anillos?

   - a) Mover tres anillos de la torre de origen a la torre de destino.
   - b) Mover dos anillos a la torre del medio, luego mover el anillo más grande a la torre de destino y, por último, mover dos anillos a la torre de destino.
   - c) No se puede resolver con recursión.

   <details><summary>Respuesta</summary>

   b) La solución de dos anillos de la pregunta 1 se usa en la solución de tres anillos.

   </details>

<!-- pregunta: CPL-ch12-m01-p03 -->

3. ¿Cuántas veces se usa la solución de dos anillos con tres anillos?

   - a) 1
   - b) 2
   - c) 0

   <details><summary>Respuesta</summary>

   b) Una vez para mover dos anillos a la torre del medio siguiendo las reglas, y luego para mover dos anillos a la torre de destino.

   </details>

### Recursión para hallar una solución completa

El proceso de recursión continúa hasta que el problema es lo bastante pequeño como para que la solución se conozca o se pueda hallar con facilidad. Entonces, la solución más grande se puede construir de forma sistemática, creando sucesivamente soluciones cada vez mayores hasta resolver el problema completo.

**Video:** [Resolución de las tres torres](https://www.openstax.org/r/solving-3-towers)

**Conceptos en práctica: Resolución de las tres torres**

<!-- pregunta: CPL-ch12-m01-p04 -->

1. ¿Cuántos pasos en total se necesitan para resolver dos anillos?

   - a) 1
   - b) 2
   - c) 3

   <details><summary>Respuesta</summary>

   c) El anillo pequeño se mueve a la torre del medio. El anillo más grande se mueve a la torre de destino. Luego, el anillo pequeño se mueve del medio al destino.

   </details>

<!-- pregunta: CPL-ch12-m01-p05 -->

2. ¿Cuántos pasos en total se necesitan para resolver tres anillos?

   - a) 3
   - b) 4
   - c) 7

   <details><summary>Respuesta</summary>

   c) Para resolverlo, la solución de dos anillos se usa dos veces y hay un paso adicional para mover el anillo más grande del origen al destino. Cada solución de dos anillos requiere tres pasos. Así que 3 + 1 + 3 = 7 pasos en total.

   </details>

<!-- pregunta: CPL-ch12-m01-p06 -->

3. ¿Cuántos pasos en total se necesitan para resolver cuatro anillos?

   - a) 15
   - b) 7
   - c) 3

   <details><summary>Respuesta</summary>

   a) El problema de cuatro anillos usa dos veces la solución de tres anillos. Los tres anillos más pequeños se mueven a la torre del medio, lo que toma siete pasos, como en la pregunta 2. Se necesita un paso para mover el anillo más grande del origen al destino. Se necesitan siete pasos más para mover los tres anillos más pequeños del medio al destino. El total es 7 + 1 + 7 = 15 pasos.

   </details>

<!-- modulo: m00089 -->

## 12.2 Recursión matemática sencilla

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar un caso recursivo y un caso base en un algoritmo recursivo.
- Demostrar cómo calcular una solución recursiva para la función factorial.

### Cálculo de un factorial

El factorial de un entero positivo se define como el producto de ese entero por los enteros positivos menores que él.

Ej.: `5! = 5 * 4 * 3 * 2 * 1`

Escrito como una ecuación general para un entero positivo `n:` ` n! = n * (n - 1) * (n - 2) * . . . * 1`

La fórmula anterior para el factorial de `n` da como resultado una fórmula recursiva: `n! = n * (n - 1)!`

Por lo tanto, el factorial de `n` depende del valor del factorial de `n - 1`. El factorial de `n` se puede hallar repitiendo el factorial de `n - 1` hasta que `(n - 1)! = 1!` (sabemos que `1! = 1`). Este resultado se puede usar para construir la solución general, como se ve en la animación siguiente.

**Video:** [Cálculo del factorial de 5](https://www.openstax.org/r/finding-factorial)

**Conceptos en práctica: Reconocimiento de la recursión**

<!-- pregunta: CPL-ch12-m02-p01 -->

1. 

<!-- pregunta: CPL-ch12-m02-p02 -->

2. 

<!-- pregunta: CPL-ch12-m02-p03 -->

3. 

<!-- pregunta: CPL-ch12-m02-p04 -->

4. 

### Definición de una función recursiva

Los algoritmos recursivos se escriben en Python como funciones. En una función recursiva se realizan acciones diferentes según el valor del parámetro de entrada. Una parte fundamental de una función recursiva es que la función debe llamarse a sí misma.

Un valor para el cual se aplica la recursión se llama **caso recursivo**. En el caso recursivo, la función se llama a sí misma con una porción más pequeña del parámetro de entrada. Ej.: en la función recursiva `factorial()`, el parámetro inicial es un entero `n`. En el caso recursivo de la función, el argumento que se pasa a `factorial()` es `n - 1`, que es menor que `n`.

Un valor de `n` para el cual se conoce la solución se llama **caso base**. El caso base detiene la recursión. Un algoritmo recursivo debe incluir un caso base; de lo contrario, el algoritmo puede dar lugar a un cálculo infinito.

Para calcular un factorial, se define una función recursiva, `factorial()`, con un parámetro de entrada entero, `n`. Cuando `n > 1`, se aplica el caso recursivo. La función `factorial()` se llama a sí misma con un argumento más pequeño, `n - 1`. Cuando `n == 1`, la solución se conoce porque `1!` es `1`; por lo tanto, `n == 1` es un caso base.

Nota: `0!` se define como `1`; por lo tanto, `n == 0` es un segundo caso base de `factorial()`. Cuando `n < 1`, se devuelve un error.

**Video:** [Factorial con recursión](https://www.openstax.org/r/factorial-recursion)

**Conceptos en práctica: Programación de la recursión**

<!-- pregunta: CPL-ch12-m02-p05 -->

1.

   ```python
   def rec_fact(n):
     return n * rec_fact(n - 1)
   ```

   - a) `355687428096000`
   - b) `0`
   - c) sin resultado / cálculo infinito

   <details><summary>Respuesta</summary>

   c) Falta un caso base, así que no hay un lugar donde termine la recursión.

   </details>

<!-- pregunta: CPL-ch12-m02-p06 -->

2.

   ```python
   def rec_fact(n):
     if n < 0:
       print("error")
     elif n == 0:
       return n
     else:
       return n * rec_fact(n - 1)
   ```

   - a) `355687428096000`
   - b) `0`
   - c) sin resultado / cálculo infinito

   <details><summary>Respuesta</summary>

   b) Esta definición de `rec_fact()` usa un caso base de `n == 0`, que funciona porque, igual que `1!`, `0! = 1`. Sin embargo, el caso base de `n == 0` devuelve `n`, que en este punto es `0`, y por lo tanto anula el resto del cálculo.

   </details>

<!-- pregunta: CPL-ch12-m02-p07 -->

3.

   ```python
   def rec_fact(n):
     if n < 0:
       print("error")
     elif n == 0:
       return 1
     else:
       return n * rec_fact(n - 1)
   ```

   - a) `355687428096000`
   - b) `0`
   - c) sin resultado / cálculo infinito

   <details><summary>Respuesta</summary>

   a) La función recursiva empieza a devolver valores correctamente en el caso base de `n == 0`. `0! = 1`.

   </details>

<!-- pregunta: CPL-ch12-m02-p08 -->

4.

   ```python
   def rec_fact(n):
     if n < 0:
       return -1
     else:
       return n * rec_fact(n - 1)
   ```

   - a) `355687428096000`
   - b) `0`
   - c) sin resultado / cálculo infinito

   <details><summary>Respuesta</summary>

   b) El caso base de `n == 1` no se usa en la función. Cuando `n` es `0`, la multiplicación total se vuelve `0`. La recursión empieza a devolver valores una vez que se alcanza el caso base `n < 0`, que inicialmente devuelve `-1`. Pero la llamada recursiva anterior devolvería `0`, anulando así todos los cálculos y dejando un resultado total de `0`.

   </details>

**Pruébalo: Suma recursiva**

Escribe un programa que use una función recursiva para calcular la suma de los números de 0 a un entero positivo `n` especificado por el usuario.

<!-- coderunner: ch12/CodeRunner_12_03_01_Recursive-summation -->

**Pruébalo: Dígitos**

Escribe un programa que calcule la suma de los dígitos de un entero positivo usando recursión.

Ej.: la suma de los dígitos de 6721 es 16.

Pista: hay 10 casos base, que se pueden comprobar fácilmente con la condición adecuada.

<!-- coderunner: ch12/CodeRunner_12_03_02_Digits -->

<!-- modulo: m00090 -->

## 12.3 Recursión con cadenas y listas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Demostrar el uso de la recursión para resolver un problema con cadenas.
- Demostrar el uso de la recursión para resolver un problema con listas.
- Usar la función integrada de listas `count()`.

### Recursión con cadenas

Una palabra que se escribe igual al derecho y al revés se llama palíndromo. Ej.: reconocer.

La recursión se puede usar para identificar si una palabra dada es un palíndromo.

**Video:** [Identificación de un palíndromo](https://www.openstax.org/r/identifying-palindrome)

**Conceptos en práctica: Recursión con cadenas**

<!-- pregunta: CPL-ch12-m03-p01 -->

1. ¿Cuál de las siguientes palabras reconoce `palindrome()` como palíndromo?

   - a) `madamm`
   - b) `madaM`
   - c) `madame`

   <details><summary>Respuesta</summary>

   b) Una vez convertida a minúsculas, la palabra `"madam"` es un palíndromo, por lo que la función la reconocerá como tal.

   </details>

<!-- pregunta: CPL-ch12-m03-p02 -->

2. ¿Qué pasaría si la condición de la línea 4 de `palindrome()` se cambiara a `if len(word) == 1:`?

   - a) Solo los palíndromos con una cantidad impar de letras se reconocerían correctamente.
   - b) Nada. La función funcionaría igual.
   - c) La función no reconocería ningún palíndromo.

   <details><summary>Respuesta</summary>

   a) Cuando un palíndromo tiene una cantidad par de letras, al final queda una cadena vacía a medida que se eliminan pares de letras. Por lo tanto, el caso base debe incluir `len(word) == 0`, lo cual se resuelve con la condición `len(word) <= 1`.

   </details>

<!-- pregunta: CPL-ch12-m03-p03 -->

3. ¿Qué pasaría si la condición de la línea 8 de `palindrome()` se cambiara a `if palindrome(word.strip(word[0]))`?

   - a) Nada. La función funcionaría igual: se eliminarían la primera y la última letra.
   - b) Algunas palabras, como `"madamm"`, se reconocerían incorrectamente como palíndromo.

   <details><summary>Respuesta</summary>

   b) La función `strip()` elimina una letra dada del principio y del final de la cadena, incluidas las letras repetidas. Cuando se usa `strip('m')` con `"madamm"`, la cadena resultante es `"ada"`.

   </details>

### Recursión con listas

La animación siguiente muestra una forma recursiva de comprobar si dos listas contienen los mismos elementos pero en distinto orden.

La función `count()` devuelve la cantidad de elementos de una lista que coinciden con el elemento dado, y devuelve `0` en caso contrario. Ej.: para `list_num = [1, 3, 3, 4]`, `list_num.count(3)` devuelve `2`.

**Video:** [Comprobación de permutaciones de listas](https://www.openstax.org/r/checking-list-permutations)

**Conceptos en práctica: Permutaciones de listas**

<!-- pregunta: CPL-ch12-m03-p04 -->

1.

   ```python
   list_num = [1, 7, 99, 2]
   other_list = [99, 7, 1, 2]
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) 

   </details>

<!-- pregunta: CPL-ch12-m03-p05 -->

2.

   ```python
   list_num = [22, 9, 15, 17, 15]
   other_list = [17, 9, 22, 22, 15]
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   b) 

   </details>

<!-- pregunta: CPL-ch12-m03-p06 -->

3.

   ```python
   honors_list = ["Bo", "Joe", "Sandy"]
   first_names_of_team_1 = ["Sandy", "Bo", "Joe"]
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) 

   </details>

<!-- pregunta: CPL-ch12-m03-p07 -->

4.

   ```python
   this_list = [1, 2, [3], [4], 5]
   that_list = [[3], 1, 5, [4], 2]
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) 

   </details>

<!-- pregunta: CPL-ch12-m03-p08 -->

5.

   ```python
   list_1 = [1, 2, 3]
   list_2 = [1, 2, 3]
   ```

   - a) `True`
   - b) `False`

   <details><summary>Respuesta</summary>

   a) 

   </details>

**Pruébalo: Eliminar duplicados**

Escribe una función recursiva `rem_dup()` que elimine los duplicados de una lista.

Ej.: la lista `[5, 5, 2, 1, 3, 1, 6]` debe dar como resultado la lista de salida `[5, 2, 1, 3, 6]`.

<!-- coderunner: ch12/CodeRunner_12_04_03_Remove-duplicates -->

<!-- modulo: m00091 -->

## 12.4 Más recursión matemática

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Definir una función recursiva para generar números de Fibonacci.

### Sucesión de Fibonacci con recursión

La sucesión de Fibonacci es una sucesión en la que cada número es la suma de los dos números anteriores. Los dos primeros números son 0 y 1. Así, a partir de 0 y 1, el tercer número es 0 + 1 = 1, y el siguiente es 1 + 1 = 2. La sucesión de números es 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... .

La recursión se puede usar para calcular el n-ésimo número de Fibonacci. Los casos base son 0 y 1. A partir de ahí, el n-ésimo número se obtiene sumando el (n - 1)-ésimo y el (n - 2)-ésimo. Así, `fib(n) = fib(n - 1) + fib(n - 2)`, que es una definición recursiva que termina en los casos base `f(0) = 0` y `f(1) = 1`.

En una recursión que llama a varias funciones en el caso recursivo, resulta útil rastrear cómo avanza la recursión. Una estructura que se usa para rastrear las llamadas que hace una función recursiva se llama **árbol de recursión**. La animación siguiente rastrea el árbol de recursión de una llamada a una función recursiva que calcula el número de Fibonacci para `n = 5`.

**Ejemplo: Hallar el n-ésimo número de Fibonacci**

La recursión de la función de Fibonacci es más compleja, ya que el valor en `n` depende de dos llamadas a función con valores más pequeños.

```python
""" Función recursiva de Fibonacci """

def fib(n):
  # Caso base
  if n == 0 or n == 1:
    return n
  # Caso recursivo
  elif n > 1:
    return fib(n - 1) + fib(n - 2)
  # Caso de error
  else:
    print("Los números de Fibonacci comienzan en 0.")
    return

# Código de prueba
print(fib(7))
```

La salida del código anterior es:

```salida
13
```

**Video:** [Función recursiva de Fibonacci](https://www.openstax.org/r/recursive-Fibonacci-function)

**Conceptos en práctica: Números de Fibonacci**

<!-- pregunta: CPL-ch12-m04-p01 -->

1. `fib(9)` da como resultado _____.

   - a) `13`
   - b) `21`
   - c) `34`

   <details><summary>Respuesta</summary>

   c) `fib(9)` = `fib(8)` +` fib(7)`. `fib(9)` `= fib(8) + fib(7) = 21 + 13 = 34`.

   </details>

<!-- pregunta: CPL-ch12-m04-p02 -->

2. ¿Cuántas llamadas a los casos base se realizan como resultado de llamar a `fib(5)`?

   - a) 2
   - b) 5
   - c) 8

   <details><summary>Respuesta</summary>

   c) Hay ocho llamadas a casos base, como se ve en la animación. Esas llamadas hacen que la recursión empiece a devolver valores y que se calcule el valor final.

   </details>

<!-- pregunta: CPL-ch12-m04-p03 -->

3. Una estructura que rastrea las llamadas a función realizadas como resultado de una llamada a una función recursiva compleja se llama _____.

   - a) árbol
   - b) árbol de recursión
   - c) árbol de iteración

   <details><summary>Respuesta</summary>

   b) La estructura que muestra qué llamadas a función se realizan se llama árbol de recursión. Un árbol de recursión se puede usar para rastrear cómo se calculan los valores finales.

   </details>

### Máximo común divisor (MCD)

El máximo común divisor (MCD) de dos enteros positivos es un entero que es divisor de ambos. Ej.: el MCD de 6 y 9 es 3 porque 3 x 2 = 6 y 3 x 3 = 9.

El MCD se halla fácilmente con el método de Euclides. El método de Euclides resta recursivamente el entero menor del entero mayor hasta llegar a un caso base con enteros iguales. El máximo común divisor es el valor entero al que se llega en el caso base.

**Ejemplo: Hallar el MCD**

```python
""" Hallar el MCD con una implementación recursiva del método de Euclides """

def gcd(a, b):
  if a == b: # Caso base
    return a
  elif a < b: # Caso recursivo
    return gcd(a, b - a)
  else:
    return gcd(a - b, a)

# Código de prueba
print(gcd(24, 30))
```

La salida del código anterior es:

```salida
6
```

**Conceptos en práctica: MCD**

<!-- pregunta: CPL-ch12-m04-p04 -->

1. ¿Cuál es el MCD de 15 y 35?

   - a) 15
   - b) 20
   - c) 5

   <details><summary>Respuesta</summary>

   c) `5 * 3 = 15` y `5 * 7 = 35`, así que `5` es el máximo común divisor de `15` y `35`.

   </details>

<!-- pregunta: CPL-ch12-m04-p05 -->

2. ¿Cuántas llamadas recursivas se realizan con `gcd(24, 30)`?

   - a) 4
   - b) 1
   - c) 24

   <details><summary>Respuesta</summary>

   a) La primera llamada `gcd(24, 30)` da `30 - 24 = 6`, así que la siguiente llamada es `gcd(24, 6)`. Después, las otras llamadas son `gcd(18, 6)`, `gcd(12, 6)` y `gcd (6,6)`, para un total de cuatro llamadas recursivas después de la llamada inicial a la función.

   </details>

<!-- pregunta: CPL-ch12-m04-p06 -->

3. ¿Cuál es el MCD de 13 y 23?

   - a) 13
   - b) 1
   - c) 23

   <details><summary>Respuesta</summary>

   b) Cuando los dos números no tienen divisores comunes, el MCD es 1.

   </details>

<!-- pregunta: CPL-ch12-m04-p07 -->

4. ¿Cuántas llamadas recursivas se realizan con `gcd(13, 23)`?

   - a) 1
   - b) 8
   - c) 13

   <details><summary>Respuesta</summary>

   b) La primera llamada `gcd(13, 23)` da `23 - 13 = 10`, así que la siguiente llamada es `gcd(13, 10)`. Después, las otras llamadas son `gcd(10, 3)`, `gcd(7, 3)`, `gcd (4,3)`, `gcd(3,2)`, `gcd(2,1)` y `gcd(1,1)`, para un total de ocho llamadas.

   </details>

**Pruébalo: Potencia recursiva**

Escribe una función recursiva `power()` tal que, dados un entero `x` y un entero positivo `y`, `power(x, y)` devuelva `x` elevado a `y`.

Ej.: `power(3, 4)` devuelve `81`.

<!-- coderunner: ch12/CodeRunner_12_05_04_Recursive-power -->

**Pruébalo: Potencia recursiva (con cualquier potencia entera)**

Escribe una función recursiva `rec_pow()` tal que, dados dos enteros `x` e `y`, devuelva `x` elevado a `y`.

(Nota: esta es una ampliación del problema anterior, pero ahora funciona para cualquier valor entero de `y`, positivo o negativo. ¿Cómo debería cambiar la función recursiva para manejar un valor negativo de `y`?)

Ej.: `rec_pow(2, -4)` devuelve `0.0625`.

<!-- coderunner: ch12/CodeRunner_12_05_05_Recursive-power-(with-any-integer-power) -->

<!-- modulo: m00092 -->

## 12.5 Uso de la recursión para resolver problemas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Usar la recursión para buscar eficientemente en una lista.
- Demostrar una solución al problema de las tres torres.

### Búsqueda binaria

Buscar en una lista ordenada suele implicar revisar cada elemento. Si el elemento buscado no se encuentra, la búsqueda puede tardar mucho.

Una búsqueda binaria es un algoritmo recursivo que se usa para buscar eficientemente en listas ordenadas. En cada paso recursivo se descarta aproximadamente la mitad de los elementos por no ser posibles coincidencias, de modo que la búsqueda avanza mucho más rápido.

Una búsqueda binaria comienza comprobando el elemento central de la lista. Si se encuentra la clave de búsqueda, el algoritmo devuelve la posición coincidente (caso base). De lo contrario, la búsqueda se repite en aproximadamente la mitad de la lista. Si la clave es mayor que el elemento central, la clave debe estar en la mitad derecha, y viceversa. El proceso continúa comprobando el elemento central de la mitad restante de la lista.

**Ejemplo: Búsqueda binaria**

```python
""" Búsqueda binaria """

def binary_search(search_list, low, high, key):

  # Comprobar el caso base
  if high > low:
    mid = (high + low) // 2

    # Si el elemento está justo en el centro (caso base)
    if search_list[mid] == key:
      return mid

    # Caso recursivo: comprobar qué subarreglo debe revisarse
    # Subarreglo derecho
    elif key > search_list[mid]:
      return binary_search(search_list, mid + 1, high, key)

    # Subarreglo izquierdo
    else:
      return binary_search(search_list, low, mid - 1, key)

  else:
    # Clave no encontrada (otro caso base)
    return "No encontrado"

# Lista de prueba
in_list = [1, 3, 13, 16, 19, 22, 27, 32, 48, 66, 78, 99, 111, 122]

# Llamar a la función de búsqueda binaria
print(binary_search(in_list, 0, len(in_list)-1, 48)) # La clave existe en el índice 8

print(binary_search(in_list, 0, len(in_list)-1, 86)) # La clave no existe
```

La salida del código anterior es:

```salida
8
No encontrado
```

**Video:** [Búsqueda binaria](https://www.openstax.org/r/binary-search)

**Conceptos en práctica: Búsqueda binaria**

<!-- pregunta: CPL-ch12-m05-p01 -->

1. ¿Qué lista se puede buscar con el algoritmo de búsqueda binaria?

   - a) `[5, 2, 7, 1, 8]`
   - b) `[9, 8, 7, 6, 5]`
   - c) `[4, 5, 6, 7, 8]`

   <details><summary>Respuesta</summary>

   c) Este arreglo está ordenado de forma ascendente, como se requiere para usar el algoritmo de búsqueda binaria.

   </details>

<!-- pregunta: CPL-ch12-m05-p02 -->

2. Si la función `binary_search()` se llama con `low = 4` y `high = 7`, `mid` se calcula como _____.

   - a) `5`
   - b) `6`
   - c) `11`

   <details><summary>Respuesta</summary>

   a) `mid = (4 + 7) // 2 = 11 // 2 = 5`. El operador // se usa para la división entera.

   </details>

<!-- pregunta: CPL-ch12-m05-p03 -->

3. ¿Cuántas llamadas a la función `binary_search()` ocurren en la animación?

   - a) 3
   - b) 4
   - c) 8

   <details><summary>Respuesta</summary>

   a) La primera llamada hace que `mid` sea `3`, luego `mid` pasa a ser `5` y, por último, `mid` pasa a ser `4`. El elemento hallado en el índice 4 es igual a la clave `16`.

   </details>

<!-- pregunta: CPL-ch12-m05-p04 -->

4. ¿Cuántas llamadas a la función `binary_search()` ocurren en el ejemplo de código al buscar `86`?

   - a) 4
   - b) 14

   <details><summary>Respuesta</summary>

   a) La primera llamada hace que `mid` sea `(0 + 13) // 2 = 6`. La siguiente llamada tiene `mid (7 + 13) // 2 = 10`. La siguiente llamada tiene `mid (11 + 13) // 2 = 12`. En este punto, `86 < 99`, así que la última llamada es a `mid 11`, tras la cual ya no hay adónde ir.

   </details>

### Resolución de las tres torres

Como se explicó en una sección anterior, el problema de las tres torres se puede resolver con recursión. La solución depende de llamar dos veces a la solución del siguiente problema más pequeño. Como muestra el ejemplo de código siguiente, la solución recursiva puede resolver el problema para cualquier cantidad de anillos.

**Ejemplo: Resolución de N torres**

La solución de las tres torres es sencilla con recursión. En el código siguiente, los anillos están numerados de arriba hacia abajo. El anillo más pequeño es el 1, el siguiente anillo es el 2 y, al resolver para tres anillos, el anillo de abajo es el 3.

```python
""" Resolución recursiva del problema de las torres """

def three_towers(N, source_tower, dest_tower, temp_tower):
    # Caso base: simplemente mover el único anillo (el de abajo) de la torre de origen a la de destino
    if N==1:
        print("Mover anillo 1 de la torre", source_tower, "a la torre", dest_tower)
        return # Salir cuando se alcanza el caso base

    # Caso recursivo
    # Llamar a la versión más pequeña del problema:
    # para mover la pila de N-1 anillos a la torre del medio
    three_towers(N-1, source_tower, temp_tower, dest_tower)

    # Mover el anillo N a la torre de destino
    print("Mover anillo", N, "de la torre", source_tower, "a la torre", dest_tower)

    # Llamar a la versión más pequeña del problema:
    # para mover ahora la pila de N-1 anillos desde la torre del medio
    # hasta el destino
    three_towers(N-1, temp_tower, dest_tower, source_tower)

# Código de prueba
print("Solución para 3 anillos:")
three_towers(3, 't1', 't3', 't2') # t1, t2, t3 son las torres
```

La salida del código anterior es:

```salida
Solución para 3 anillos:
Mover anillo 1 de la torre t1 a la torre t3
Mover anillo 2 de la torre t1 a la torre t2
Mover anillo 1 de la torre t3 a la torre t2
Mover anillo 3 de la torre t1 a la torre t3
Mover anillo 1 de la torre t2 a la torre t1
Mover anillo 2 de la torre t2 a la torre t3
Mover anillo 1 de la torre t1 a la torre t3
```

**Conceptos en práctica: Resolución de las tres torres**

<!-- pregunta: CPL-ch12-m05-p05 -->

1. Para cuatro anillos, ¿cuántas líneas en total imprimirá `three_towers()`?

   - a) 7
   - b) 15

   <details><summary>Respuesta</summary>

   b) Como se vio en el ejemplo de código para tres anillos, la solución requiere siete pasos. Los siete pasos se llaman dos veces, junto con un paso adicional, para un total de 2 x 7 + 1 = 15.

   </details>

<!-- pregunta: CPL-ch12-m05-p06 -->

2. ¿Una solución iterativa del problema de las tres torres sería más compleja o menos compleja?

   - a) más compleja
   - b) menos compleja

   <details><summary>Respuesta</summary>

   a) La solución iterativa de las tres torres requiere bastante más código y usa capacidades de programación adicionales.

   </details>

**Pruébalo: Combinaciones de monedas**

Escribe una función recursiva `print_H_T()` que produzca todas las combinaciones posibles de caras (`"H"`) y cruces (`"T"`) para una cantidad dada de lanzamientos de moneda.

Ej.: para tres monedas, el programa debe imprimir la salida que se muestra a continuación.

```text
HHH
HHT
HTH
HTT
THH
THT
TTH
TTT
```

<!-- coderunner: ch12/CodeRunner_12_06_06_Coin-combinations -->

<!-- modulo: m00093 -->

## Resumen del capítulo

Los puntos más destacados de este capítulo son:

- Describir el concepto de recursión.
- Demostrar cómo la recursión usa soluciones más simples para construir una solución más grande.
- Identificar un caso recursivo y un caso base en un algoritmo recursivo.
- Demostrar cómo calcular una solución recursiva para la función factorial.
- Demostrar el uso de la recursión para resolver un problema con cadenas.
- Demostrar el uso de la recursión para resolver un problema con listas.
- Usar la función integrada de listas `count()`.
- Definir una función recursiva para generar números de Fibonacci.
- Usar la recursión para buscar eficientemente en una lista.
- Demostrar una solución al problema de las tres torres.

A estas alturas, deberías poder resolver problemas usando recursión.

**Referencia del capítulo 12.**

| Función | Descripción |
|---|---|
| `count(element)` | Devuelve la cantidad de veces que el elemento existe en la lista sobre la que se llama a la función `count()`. |
