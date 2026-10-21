# Capítulo 11: Clases

<!-- modulo: m00080 -->

## Introducción

![una fotografía de manzanas de distintos colores, separadas en diferentes canastas](media/Python_11_00_000.jpg)

*crédito: modificación de la obra «Fresh, bright apples newly picked», de Colorado State University Extension/Flickr, dominio público*

Un programador puede modelar entidades del mundo real como objetos para lograr un mejor diseño y una mejor organización del programa. Una clase define un tipo de objeto con atributos y métodos. Se pueden crear muchas instancias de un tipo de clase para representar varios objetos en un programa.

Las clases promueven la reutilización. Las clases añaden beneficios como la abstracción de datos y el encapsulamiento, que organizan el código para que sea más fácil de usar y de extender.

<!-- modulo: m00081 -->

## 11.1 Conceptos básicos de la programación orientada a objetos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir el paradigma de la programación orientada a objetos (POO).
- Describir los conceptos de encapsulamiento y abstracción en relación con la POO, e identificar el valor de cada uno.

### Agrupar en objetos

La **programación orientada a objetos** (POO) es un estilo de programación que agrupa campos relacionados, o miembros de datos, y procedimientos en objetos. Las entidades del mundo real se modelan como objetos individuales que interactúan entre sí. Ej.: una cuenta de redes sociales puede seguir a otras cuentas, y las cuentas pueden enviarse mensajes entre sí. Una cuenta puede modelarse como un objeto en un programa.

**Video:** [Using objects to model social media](https://www.openstax.org/r/model-social-media)

**Conceptos en práctica: POO**

<!-- pregunta: CPL-ch11-m01-p01 -->

1. Considera el ejemplo anterior. ¿Cuál es un campo en la publicación de Ellis del 18/12/23?

   - a) La lista de seguidores de Ellis
   - b) El nombre de usuario de Ellis

   <details><summary>Respuesta</summary>

   b) El nombre de usuario de Ellis representa al creador de la publicación.

   </details>

<!-- pregunta: CPL-ch11-m01-p02 -->

2. ¿Qué modela normalmente un objeto en la programación orientada a objetos?

   - a) código de programa
   - b) una entidad del mundo real

   <details><summary>Respuesta</summary>

   b) Un objeto modela una entidad del mundo real con campos y procedimientos.

   </details>

### Encapsulamiento

El **encapsulamiento** es un concepto clave de la POO que consiste en envolver los datos y los procedimientos que operan sobre ellos en una sola unidad. El acceso a los datos de la unidad está restringido para evitar que otras unidades los modifiquen directamente. Ej.: un sitio web de venta de entradas gestiona todas las transacciones de un concierto y lleva la cuenta de las entradas vendidas y de las que aún están disponibles para evitar una sobreventa accidental.

**Video:** [Encapsulating concert ticket information](https://www.openstax.org/r/encapsulating-info)

**Conceptos en práctica: Encapsulamiento**

<!-- pregunta: CPL-ch11-m01-p03 -->

1. Considera el ejemplo anterior. Supón que hay que cambiar el lugar del evento debido al mal tiempo. ¿Cómo debería cambiar un programador el objeto del sitio web para permitir cambios en el campo `Venue`?

   - a) Añadir un procedimiento para cambiar el campo.
   - b) Permitir a los usuarios el acceso directo al campo.
   - c) No hay una forma válida de permitir cambios en el campo.

   <details><summary>Respuesta</summary>

   a) Un procedimiento, como `Change venue`, puede hacer cambios en el campo y proteger el campo de accesos inadecuados.

   </details>

<!-- pregunta: CPL-ch11-m01-p04 -->

2. ¿Cuál es un beneficio del encapsulamiento al desarrollar programas complejos?

   - a) Todos los objetos pueden acceder fácilmente a los datos de los demás y modificarlos.
   - b) Los datos de cada objeto están restringidos para un acceso intencional.

   <details><summary>Respuesta</summary>

   b) Limitar el acceso a los datos evita cambios accidentales y hace más claras las relaciones entre los objetos.

   </details>

### Abstracción

La **abstracción** es un concepto clave de la POO en el que el funcionamiento interno de una unidad se oculta a los usuarios y a otras unidades que no necesitan conocerlo. Ej.: un conductor normalmente no necesita saber la temperatura numérica exacta del motor de su automóvil. Por eso el automóvil tiene un indicador que muestra si la temperatura del motor está dentro de un rango apropiado.

**Video:** [Abstracting data in a countdown calculator](https://www.openstax.org/r/abstracting-data)

**Conceptos en práctica: Abstracción**

<!-- pregunta: CPL-ch11-m01-p05 -->

1. Considera el ejemplo del automóvil en el párrafo anterior. Supón que el diseñador decidiera eliminar el indicador de temperatura del motor. ¿Sería un buen uso de la abstracción?

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   b) Una abstracción correcta hace visible solo la información necesaria. Un motor sobrecalentado puede causar daños irreparables, por lo que el conductor necesita un indicador.

   </details>

<!-- pregunta: CPL-ch11-m01-p06 -->

2. ¿Cuál es un beneficio de la abstracción?

   - a) una mejor visualización de la información
   - b) una alta visibilidad de la información

   <details><summary>Respuesta</summary>

   a) Mostrar solo la información necesaria reduce el desorden y mejora la experiencia general.

   </details>

<!-- modulo: m00082 -->

## 11.2 Clases e instancias

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Crear una clase con atributos de instancia, atributos de clase y el método `__init__()`.
- Usar la definición de una clase para crear instancias de la clase que representen objetos.

### Clases e instancias

En la sección anterior, una entidad del mundo real, como el perfil de una persona en una red social, se modeló como un único objeto. ¿Cómo podría un programador desarrollar un sistema de software que gestione millones de perfiles? Sería fundamental contar con un plano que defina los campos y los procedimientos de un perfil.

En un programa de Python, una **clase** define un tipo de objeto con atributos (campos) y métodos (procedimientos). Una clase es un plano para crear objetos. Los objetos individuales creados a partir del tipo de la clase se llaman **instancias**.

**Video:** [Representing a coffee order with a class](https://www.openstax.org/r/representing-with-class)

**Conceptos en práctica: Clases e instancias**

<!-- pregunta: CPL-ch11-m02-p01 -->

1. ¿Cuál es el nombre de la clase?

   - a) `Cat`
   - b) `class Cat`
   - c) `self`

   <details><summary>Respuesta</summary>

   a) `Cat` sigue a la palabra clave class en la parte superior de la definición de la clase y es el nombre de la clase.

   </details>

<!-- pregunta: CPL-ch11-m02-p02 -->

2. ¿Cuál de las siguientes es una instancia de la clase `Cat`?

   - a) `__init__`
   - b) `name`
   - c) `pet_1`

   <details><summary>Respuesta</summary>

   c) `pet_1` es una instancia de la clase `Cat` creada al llamar a `Cat()`. La otra instancia es `pet_2`.

   </details>

<!-- pregunta: CPL-ch11-m02-p03 -->

3. ¿Cuál de los siguientes es un atributo?

   - a) `breed`
   - b) `pet_2`
   - c) `print_info`

   <details><summary>Respuesta</summary>

   a) `breed` es un atributo de instancia definido en `__init__()`. Los otros atributos de instancia son `name` y `age`.

   </details>

<!-- pregunta: CPL-ch11-m02-p04 -->

4. Supón que el programador quisiera cambiar la clase para representar a un gato mascota. ¿Cuál es el nombre apropiado según las recomendaciones de PEP 8?

   - a) `petcat`
   - b) `pet_cat`
   - c) `PetCat`

   <details><summary>Respuesta</summary>

   c) El estilo `CapWords`, con todas las palabras en mayúscula inicial y sin espacios entre ellas, es el recomendado para los nombres de clase. «Pet» y «cat» son palabras distintas, así que cada una lleva mayúscula inicial y una va justo a continuación de la otra.

   </details>

### Crear instancias con __init__()

`__init__()` es un método especial que se llama cada vez que se crea una nueva instancia de una clase. **self** hace referencia a la instancia de una clase y se usa en los métodos de la clase para acceder a la instancia específica que llamó al método. `__init__()` usa `self` para definir e inicializar los atributos de la instancia.

**Video:** [Creating multiple coffee orders and changing attributes](https://www.openstax.org/r/creating-changing-attributes)

**Conceptos en práctica: instancias y __init__()**

<!-- pregunta: CPL-ch11-m02-p05 -->

1. ¿Cuántas veces se llama a `__init__()`?

   - a) 1
   - b) 2
   - c) 3

   <details><summary>Respuesta</summary>

   b) Se crean dos instancias, `room_1` y `room_3`, al llamar a `Rectangle()`, lo que llama al constructor `__init__()`.

   </details>

<!-- pregunta: CPL-ch11-m02-p06 -->

2. Cuando se ejecuta la línea 11, el flujo de ejecución pasa a la línea 5. ¿Qué representa `self` en la línea 5?

   - a) el área de `room_1`
   - b) la instancia `room_1`
   - c) la clase `Rectangle`

   <details><summary>Respuesta</summary>

   b) `room_1` es la instancia que llamó al método `area()`, por lo que `self` representa a la instancia específica.

   </details>

<!-- pregunta: CPL-ch11-m02-p07 -->

3. ¿Qué línea inicializa el atributo de instancia length?

   - a) 3
   - b) 6
   - c) 9

   <details><summary>Respuesta</summary>

   a) La línea 3 está en `__init__()`, que inicializa length y los demás atributos de instancia de cada nueva instancia.

   </details>

<!-- pregunta: CPL-ch11-m02-p08 -->

4. Supón que la línea 2 se cambia por `def __init__():`. ¿A qué valores se inicializarían los atributos de `room_1`?

   - a) `length = 0`, `width = 0`
   - b) `length = 1`, `width = 1`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) `__init__()` tiene un parámetro obligatorio, llamado convencionalmente `self`, que permite al constructor acceder a la instancia.

   </details>

### Atributos de instancia frente a atributos de clase

Los atributos mostrados hasta ahora han sido atributos de instancia. Un **atributo de instancia** es una variable exclusiva de cada instancia de una clase y se accede a él con el formato `instance_name.attribute_name`. Otro tipo de atributo, el **atributo de clase**, pertenece a la clase y es compartido por todas las instancias de la clase. Se accede a los atributos de clase con el formato `class_name.attribute_name`.

**Video:** [Using class attributes for shared coffee order information](https://www.openstax.org/r/using-class-attributes)

**Conceptos en práctica: Atributos de instancia y de clase**

<!-- pregunta: CPL-ch11-m02-p09 -->

1. ¿Cuál es un atributo de instancia?

   - a) `loc`
   - b) `order_id`
   - c) `order_3`

   <details><summary>Respuesta</summary>

   b) `order_id` es un atributo de instancia definido en `__init__()`. El otro atributo de instancia es `cup_size`.

   </details>

<!-- pregunta: CPL-ch11-m02-p10 -->

2. Supón que se añade la línea `order_1.cup_size = 8` antes de `order_3.print_order()`. ¿Cuál es la nueva salida?

   - a) `Cafe Coffee Order 3 : 8 oz`
   - b) `Cafe Coffee Order 3 : 16 oz`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) Cambiar `order_1.cup_size` no afecta a `order_3.cup_size`. `order_1.cup_size` cambia a `8` y `order_3.cup_size` sigue siendo `16`.

   </details>

<!-- pregunta: CPL-ch11-m02-p11 -->

3. Supón que se añade la línea `CoffeeOrder.loc = 'Caffeine Cafe'` antes de `order_3.print_order()`. ¿Cuál es la nueva salida?

   - a) `Caffeine Cafe Order 3 : 16 oz`
   - b) `Cafe Coffee Order 3 : 16 oz`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) `order_1`, `order_2` y `order_3` comparten el atributo de clase `CoffeeOrder.loc`. Cambiar `loc` afecta a todas las instancias, por lo que se imprime `Caffeine Cafe` como ubicación.

   </details>

<!-- pregunta: CPL-ch11-m02-p12 -->

4. Supón que se añade la línea `self.cls_id = 5` al final de la definición de `__init__()`. ¿Cuál es la nueva salida?

   - a) `Cafe Coffee Order 5 : 16 oz`
   - b) `Cafe Coffee Order 3 : 16 oz`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) Intentar acceder a un atributo de clase mediante una instancia no es seguro. En `__init__()`, intentar acceder al atributo de clase crea un nuevo atributo de instancia llamado `cls_id`. Aunque es posible, los programadores deben evitar usar el mismo nombre para atributos de clase y atributos de instancia para evitar confusiones.

   </details>

**Pruébalo: Crear una clase para los boletos de vuelo de una aerolínea**

Escribe una clase, `FlightTicket`, como se describe a continuación. Los valores predeterminados aparecen después de los atributos. Luego crea un boleto de vuelo y asigna a cada atributo de instancia los valores leídos de la entrada.

Atributos de instancia:

- flight_num: 1
- airport: JFK
- gate: T1-1
- time: 8:00
- seat: 1A
- passenger: unknown

Atributos de clase:

- airline: Oceanic Airlines
- airline_code: OA

Método:

- `__init__()`: inicializa los atributos de instancia
- `print_info()`: imprime la información del boleto (incluido en la plantilla)

Entrada dada:

```text
2121
KEF
D22B
11:45
12B
Jules Laurent
```

La salida es:

```text
Passenger Jules Laurent departs on flight # 2121 at 11:45 from KEF D22B in seat 12B
```

<!-- coderunner: ch11/CodeRunner_11_03_01_Creating-a-class-for-an-airline_s-flight-tickets -->

**Pruébalo: Crear una clase para libros de fantasía**

Escribe una clase, `Book`, como se describe a continuación. Luego crea dos instancias y asigna a cada atributo de instancia los valores leídos de la entrada.

Atributos de instancia:

- title: ''
- author: ''
- year: 0
- pages: 0

Atributo de clase:

- imprint: Fantasy Tomes

Método:

- `__init__()`: inicializa los atributos de instancia
- `print_info()`: imprime la información del libro (incluido en la plantilla)

Entrada dada:

```text
Lord of the Bracelets
Blake R. R. Brown
1999
423
A Match of Thrones
Terry R. R. Thomas
2020
761
```

La salida es:

```text
Lord of the Bracelets by Blake R. R. Brown published by Fantasy Tomes
in 1999 with 423 pages
A Match of Thrones by Terry R. R. Thomas published by Fantasy Tomes
in 2020 with 761 pages
```

<!-- coderunner: ch11/CodeRunner_11_03_02_Creating-a-class-for-fantasy-books -->

<!-- modulo: m00083 -->

## 11.3 Métodos de instancia

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Crear e implementar `__init__()` con varios parámetros, incluidos valores de parámetro predeterminados.
- Describir a qué información tiene acceso un método de instancia y qué puede modificar.

### Más sobre __init__()

En Python, `__init__()` es el método especial que crea instancias. `__init__()` debe tener como primer parámetro la instancia que llama, `self`, y puede tener cualquier cantidad de otros parámetros, con o sin valores de parámetro predeterminados.

**Video:** [Creating patient vital signs instances](https://www.openstax.org/r/creating-instances)

**Conceptos en práctica: Definir y usar __init__() con parámetros**

<!-- pregunta: CPL-ch11-m03-p01 -->

1. Supón que el programador quisiera hacer de la presión arterial un parámetro obligatorio en `__init__()`. ¿Cuál es el encabezado correcto del método `__init__()`?

   - a) `def __init__(p_id, bp, self, tmp=-1.0, hr=-1, rr=-1):`
   - b) `def __init__(self, p_id, bp, tmp=-1.0, hr=-1, rr=-1):`
   - c) `def __init__(self, p_id, bp=[-1,-1], tmp=-1.0, hr=-1, rr=-1):`

   <details><summary>Respuesta</summary>

   b) Quitar el valor de parámetro predeterminado hace que `bp` sea un parámetro obligatorio.

   </details>

<!-- pregunta: CPL-ch11-m03-p02 -->

2. ¿Cuál es una llamada correcta a `__init__()` para crear una instancia con `p_id=5241`?

   - a) `patient_10 = Vitals(self, 5241)`
   - b) `patient_10 = Vitals(5241)`
   - c) ambas

   <details><summary>Respuesta</summary>

   b) `self` es el primer parámetro en la definición de `__init__()`, no un argumento explícito. `self` no debe incluirse en la llamada.

   </details>

<!-- pregunta: CPL-ch11-m03-p03 -->

3. Supón que se añade otra definición de `__init__()` después de la primera, con el siguiente encabezado:
   
   ```python norun
   def __init__(self, p_id, bp, tmp, hr, rr)
   ```
   
    ¿Qué impacto tiene en el programa?

   - a) ningún cambio.
   - b) La segunda definición de `__init__()` produce un error.
   - c) Las dos primeras llamadas a `__init__()` producen un error.

   <details><summary>Respuesta</summary>

   c) La segunda definición sobrescribe a la primera, ya que no se permiten varias definiciones explícitas de `__init__()`. `__init__()` requiere todos los parámetros, por lo que las dos primeras llamadas a `__init__()`, para `patient_1` y `patient_2`, son incorrectas.

   </details>

### Métodos de instancia

Un **método de instancia** se usa para acceder a los atributos de instancia y a los atributos de clase, y para modificarlos. Todos los métodos mostrados hasta ahora, y la mayoría de los métodos definidos en la definición de una clase, son métodos de instancia.

**Ejemplo: Los métodos de instancia suelen usarse para obtener y establecer información de la instancia**

```python
class ProductionCar:
  def __init__(self, make, model, year, max_mph = 0.0):
    self.make = make
    self.model = model
    self.year = year
    self.max_mph = max_mph

  def max_kmh(self):
    return self.max_mph * 1.609344

  def update_max(self, speed):
    self.max_mph = speed

car_1 = ProductionCar('McLaren', 'Speedtail', 2020) # car_1.max_mph es 0.0
car_1.update_max(250.0) # car_1.max_mph es 250.0
print(car_1.make, car_1.model, 'reaches', car_1.max_mph, 'mph (',
  car_1.max_kmh(), 'km/h)') # Imprime McLaren Speedtail reaches 250.0 mph (402.336 km/h)
```

**Conceptos en práctica: Métodos de instancia de CoffeeOrder**

<!-- pregunta: CPL-ch11-m03-p04 -->

1. ¿Qué representa `order_1` al final del programa?

   - a) un café de 8 oz
   - b) un café de 8 oz con leche
   - c) un café de 8 oz con azúcar

   <details><summary>Respuesta</summary>

   c) `order_1` es originalmente un café sin leche ni azúcar, pero la llamada a `change()` añade azúcar al pedido al asignar `True` a `order_1.with_sugar`.

   </details>

<!-- pregunta: CPL-ch11-m03-p05 -->

2. ¿Por qué `change()` es un método de instancia?

   - a) puede cambiar atributos
   - b) tiene varios parámetros
   - c) puede cambiar una instancia

   <details><summary>Respuesta</summary>

   c) El primer parámetro de un método de instancia indica que el método puede cambiar una instancia. `change()` permite cambiar si un pedido de café lleva leche o azúcar.

   </details>

<!-- pregunta: CPL-ch11-m03-p06 -->

3. ¿Se puede quitar la sangría de `print_order()`?

   - a) sí
   - b) no

   <details><summary>Respuesta</summary>

   b) Quitar la sangría de `print_order()` produciría un error. Un método de instancia debe estar definido dentro de la clase.

   </details>

**Pruébalo: Crear una clase para máquinas expendedoras**

Escribe una clase, `VendingMachine`, como se describe a continuación. Los valores predeterminados aparecen después de los atributos. Ej.: el valor predeterminado de `count` es `0`. Crea una máquina expendedora usando un valor leído de la entrada y llama a los métodos de instancia.

Atributos de instancia:

- count: 0
- max: 0

Métodos:

- `__init__(num)`: inicializa count y max con el parámetro `num`
- `refill()`: asigna a `count` el valor de `max` e imprime `"Refilled"`
- `sell(order)`: asigna a `count` el valor de `count` menos `order` e imprime `"Sold: [order]"`
- `print_stock()`: imprime `"Current stock: [count]"`

Entrada dada:

```python
100
25
```

La salida es:

```python norun
Current stock: 100
Sold: 25
Current stock: 75
Refilled
Current stock: 100
```

<!-- coderunner: ch11/CodeRunner_11_04_03_Creating-a-class-for-vending-machines -->

<!-- modulo: m00084 -->

## 11.4 Sobrecarga de operadores

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar los métodos mágicos y describir su propósito.
- Desarrollar operadores aritméticos y de comparación sobrecargados para clases definidas por el usuario.

### Métodos mágicos y personalización

Los **métodos mágicos** son métodos especiales que realizan acciones para los usuarios, normalmente fuera de su vista. Los métodos mágicos también se llaman métodos dunder, ya que deben empezar y terminar con doble guion bajo (__). Ej.: `__init__()` es un método mágico que se usa junto con `__new__()` para crear una nueva instancia e inicializar atributos con una línea sencilla como `eng = Engineer()`. Un programador puede definir explícitamente un método mágico en una clase definida por el usuario para personalizar el comportamiento del método.

**Video:** [Customizing __str__() in a user-defined class, Engineer](https://www.openstax.org/r/customizing-str-user-defined-class)

**Conceptos en práctica: Métodos mágicos**

<!-- pregunta: CPL-ch11-m04-p01 -->

1. ¿Cuál de los siguientes es un método mágico?

   - a) `add()`
   - b) `_add_()`
   - c) `__add__()`

   <details><summary>Respuesta</summary>

   c) `__add__()` es un método mágico, como indican los guiones bajos dobles al principio y al final del nombre del método.

   </details>

<!-- pregunta: CPL-ch11-m04-p02 -->

2. ¿Por qué son especiales los métodos mágicos?

   - a) el usuario no puede llamarlos
   - b) realizan acciones internas
   - c) tienen definiciones fijas

   <details><summary>Respuesta</summary>

   b) Los métodos mágicos están diseñados para invocarse internamente y realizar acciones entre bastidores que simplifican las tareas del usuario.

   </details>

<!-- pregunta: CPL-ch11-m04-p03 -->

3. Considera el ejemplo anterior e identifica el método o los métodos mágicos del programa actualizado.

   - a) `__init__()`
   - b) `__str__()`
   - c) `__init__()`, `__str__()`

   <details><summary>Respuesta</summary>

   c) El programador define `__init__()` para inicializar los atributos de instancia. El programador define `__str__()` para personalizar la representación en forma de cadena de una instancia de `Engineer`.

   </details>

### Sobrecarga de operadores aritméticos

La **sobrecarga de operadores** consiste en personalizar la función de un operador integrado. Los operadores aritméticos suelen sobrecargarse para facilitar los cambios en las instancias de clases definidas por el usuario.

**Video:** [Overloading __add__() for a user-defined class, Account](https://www.openstax.org/r/overloading-add-user-defined-class)

**Operadores aritméticos y métodos mágicos.**

| Operador aritmético (Operación) | Método mágico |
|---|---|
| + (Suma) | `__add__(self, other)` |
| - (Resta) | `__sub__(self, other)` |
| * (Multiplicación) | `__mul__(self, other)` |
| / (División) | `__truediv__(self, other)` |
| % (Módulo) | `__mod__(self, other)` |
| ** (Potencia) | `__pow__(self, other)` |

**Conceptos en práctica: Sobrecarga de operadores aritméticos**

<!-- pregunta: CPL-ch11-m04-p04 -->

1. Un programador que define explícitamente el operador de módulo para su clase definida por el usuario está ___________ el operador.

   - a) sobrecargando
   - b) reescribiendo
   - c) implementando

   <details><summary>Respuesta</summary>

   a) Un programador puede sobrecargar un operador para personalizar la función del operador integrado.

   </details>

<!-- pregunta: CPL-ch11-m04-p05 -->

2. Dado el siguiente código, ¿qué argumento corresponde al parámetro `other` en la llamada a `Account.__add__()`?
   
   ```python norun
   acct_a = Account("Ashe", 6492)
   acct_b = Account("Bevins", 5210)
   
   acct_ab = acct_a + acct_b
   ```

   - a) `acct_a`
   - b) `acct_b`
   - c) `acct_ab`

   <details><summary>Respuesta</summary>

   b) La operación de suma asocia el operando izquierdo, `acct_a`, con el parámetro `self` y el operando derecho, `acct_b`, con el parámetro `other`.

   </details>

<!-- pregunta: CPL-ch11-m04-p06 -->

3. ¿Qué definición de `__sub__()` sobrecarga el operador - para que funcione el siguiente código?
   
   ```python norun
   class Pair:
     def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
     # Define __sub__()
   
   p1 = Pair(10, 2)
   p2 = Pair(8, 4)
   p3 = p1 - p2
   print(p3.x, p3.y)
   ```

   - a)

     ```python
     def __sub__(self):
       return Pair(self.x - other.x, self.y - other.y)
     ```

   - b)

     ```python
     def __sub__(self, other):
       return self.x - other.x, self.y - other.y
     ```

   - c)

     ```python
     def __sub__(self, other):
       return Pair(self.x - other.x, self.y - other.y)
     ```

   <details><summary>Respuesta</summary>

   c) - es un operador binario, por lo que `__sub__()` tiene dos parámetros. Se restan entre sí los atributos `x` e `y` de los parámetros, y los valores resultantes se convierten en un nuevo `Pair`.

   </details>

### Sobrecarga de operadores de comparación

Los operadores de comparación también pueden sobrecargarse, igual que los operadores aritméticos.

**Operadores de comparación y métodos mágicos.**

| Operador de comparación (Operación) | Método mágico |
|---|---|
| < (Menor que) | `__lt__(self, other)` |
| > (Mayor que) | `__gt__(self, other)` |
| <= (Menor o igual que) | `__le__(self, other)` |
| >= (Mayor o igual que) | `__ge__(self, other)` |
| == (Igual) | `__eq__(self, other)` |
| != (Distinto) | `__ne__(self, other)` |

**Ejemplo: Sobrecarga de operadores de comparación para la clase Account**

| Código | Salida |
|---|---|
| ```python<br>class Account:<br>  def __init__(self, name="", amount=0):<br>    self.name = name<br>    self.amount = amount<br><br>  def __str__(self):<br>    return f"{self.name}: ${self.amount}"<br><br>  def __lt__(self, other):<br>    return self.amount < other.amount<br><br>  def __gt__(self, other):<br>    return self.amount > other.amount<br><br>  def __eq__(self, other):<br>    return self.amount == other.amount<br><br>acct_a = Account("Ashe", 6492)<br>acct_b = Account("Bevins", 5210)<br><br>print(acct_a < acct_b)<br>print(acct_a > acct_b)<br>acct_a.amount = 5210<br>print(acct_a == acct_b)<br>``` | `False`  <br>`True`  <br>`True` |

**Conceptos en práctica: Sobrecarga de operadores de comparación**

<!-- pregunta: CPL-ch11-m04-p07 -->

1. ¿Cuántos operadores están sobrecargados?

   - a) 3
   - b) 4
   - c) 5

   <details><summary>Respuesta</summary>

   a) <, > y == están sobrecargados con `__lt__()`, `__gt__()` y `__eq__()`, respectivamente.

   </details>

<!-- pregunta: CPL-ch11-m04-p08 -->

2. ¿Qué código sobrecarga correctamente el operador &lt;=?

   - a)

     ```python
     def __le__(other):
       return self.amount <= other.amount
     ```

   - b)

     ```python
     def __le__(self, other):
       return self.amount <= other.amount
     ```

   - c)

     ```python
     def __le__(self, other):
       return other.amount <= self.amount
     ```

   <details><summary>Respuesta</summary>

   b) `__le__()` es el método mágico del operador <=. `__le__()` recibe dos parámetros, para el operando izquierdo y el derecho, y devuelve la comparación correcta de los dos valores de amount.

   </details>

<!-- pregunta: CPL-ch11-m04-p09 -->

3. ¿Qué tipo de valor devuelve `__gt__()`?

   - a) instancia de cuenta
   - b) booleano
   - c) entero

   <details><summary>Respuesta</summary>

   b) `__gt__()` sobrecarga el operador >, que hace una comparación y devuelve `True` o `False`.

   </details>

**Pruébalo: Combinar registros de ejercicio**

La clase `ExerciseLog` tiene dos atributos de instancia: `e_type`, el tipo de ejercicio, y `duration`, el tiempo dedicado al ejercicio.

Sobrecarga el operador + para combinar dos `ExerciseLogs` de modo que:

- Si los tipos de ejercicio son distintos, se combinen con `" and "` entre ellos. Si no, se use el mismo tipo sin duplicarlo.
- Se sumen las duraciones.

Entrada dada:

```text
walk
5
run
30
```

La salida es:

```text
walk and run: 35 minutes
```

<!-- coderunner: ch11/CodeRunner_11_05_04_Combining-exercise-logs -->

**Pruébalo: Ampliar la clase Account**

Usar `isinstance()` permite al programador definir comportamientos distintos según el tipo de un objeto. El primer parámetro es el objeto, y el segundo parámetro es el tipo o la clase. Ej.: `isinstance(my_var, int)` devuelve `True` si `my_var` es un entero.

Amplía el ejemplo existente de `Account` para que el operador de suma también pueda usarse para sumar un valor entero al atributo amount de `Account`.

<!-- coderunner: ch11/CodeRunner_11_05_05_Expanding-the-Account-class -->

<!-- modulo: m00085 -->

## 11.5 Uso de módulos con clases

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Construir una instrucción import que importe clases de forma selectiva.
- Crear un alias para importar un módulo.

### Importar clases desde módulos

Las instrucciones import, como se explicó en el capítulo Módulos, permiten importar a un programa código de otros archivos, incluidas clases. La forma de acceder a una clase importada depende de si se importa el módulo completo o solo partes seleccionadas.

Se pueden agrupar varias clases en un módulo. Para una buena organización, las clases deben agruparse en un módulo solo si la agrupación permite reutilizar el módulo, ya que un beneficio clave de los módulos es la reutilización.

**Video:** [Importing classes from files](https://www.openstax.org/r/importing-classes)

**Conceptos en práctica: Importar clases**

<!-- pregunta: CPL-ch11-m05-p01 -->

1. Considera el ejemplo anterior. ¿Cuántas clases se importan en el segundo *main.py*?

   - a) 1
   - b) 2
   - c) 3

   <details><summary>Respuesta</summary>

   b) `Level` y `XP` son clases importadas al programa desde el módulo character. Cualquier otra clase del módulo character no se importa.

   </details>

<!-- pregunta: CPL-ch11-m05-p02 -->

2. ¿Qué línea importa solo la clase `Level` de character?

   - a) `import Level from character`
   - b) `from character import Level`
   - c) `import Level`

   <details><summary>Respuesta</summary>

   b) Se puede importar una sola clase o varias clases de un módulo usando el `name` o los nombres de las clases.

   </details>

<!-- pregunta: CPL-ch11-m05-p03 -->

3. ¿Cuántas clases puede haber en un módulo?

   - a) ninguna
   - b) solo 1
   - c) cualquier cantidad

   <details><summary>Respuesta</summary>

   c) La cantidad de clases en un módulo es ilimitada, pero las clases deben agruparse en módulos de modo que se maximice la reutilización.

   </details>

### Uso de alias

El **uso de alias** permite al programador usar un nombre alternativo para los elementos importados. Ej.: `import triangle as tri` permite que el programa se refiera al módulo triangle como tri. El uso de alias es útil para evitar colisiones de nombres, pero debe usarse con cuidado para no causar confusión.

**Ejemplo: Usar un alias para importar character**

*character.py*

```python
class Level:
  def __init__(self, level=1):
    self.level = level
    ...
  def level_up(self):
    ...
class XP:
  def __init__(self, XP=0):
    self.XP = XP
    ...
  def add_xp(self, num):
    ...
```

*main.py*

```python norun
import character as c

bard_level = c.Level(1)
bard_XP = c.XP(0)
bard_XP.add_xp(300)
bard_level.level_up()
...
```

**Conceptos en práctica: Usar un alias**

<!-- pregunta: CPL-ch11-m05-p04 -->

1. ¿Cómo crearía el programa una instancia de `Level`?

   - a) `rogue_level = character.Level()`
   - b) `rogue_level = game_char.Level()`
   - c) `rogue_level = character.game_char.Level()`

   <details><summary>Respuesta</summary>

   b) El módulo character tiene el alias `game_char`, por lo que character no está definido en el programa. Se usa `game_char` en lugar de character.

   </details>

<!-- pregunta: CPL-ch11-m05-p05 -->

2. ¿Qué código crea una colisión de nombres?

   - a) `character = 'Ranger'`
   - b) `Game_char = 'Ranger'`
   - c) `game_char = 'Ranger'`

   <details><summary>Respuesta</summary>

   c) `game_char` hacía referencia al módulo importado, pero al asignar `game_char` se reemplaza el módulo importado por la cadena `'Ranger'`. Ya no se puede usar `game_char` para acceder a las clases.

   </details>

**Pruébalo: Instrucción import faltante**

Añade la instrucción import que falta al principio del archivo. No hagas ningún cambio en el resto del código. Al final, el programa debe ejecutarse sin errores.

<!-- coderunner: ch11/CodeRunner_11_06_06_Missing-import-statement -->

**Pruébalo: Instrucción de importación de clase faltante**

Añade la instrucción de importación de clase que falta al principio del archivo. Importa solo una clase, no un módulo completo. No hagas ningún cambio en el resto del código. Al final, el programa debe ejecutarse sin errores.

<!-- coderunner: ch11/CodeRunner_11_06_07_Missing-class-import-statement -->

<!-- modulo: m00086 -->

## Resumen del capítulo

Los puntos más destacados de este capítulo son:

- La programación orientada a objetos consiste en agrupar campos y procedimientos relacionados en objetos mediante la abstracción de datos y el encapsulamiento.
- Las clases definen un tipo de objeto con atributos y métodos.
- Las instancias de un tipo de clase representan objetos y se crean usando `__init__()`.
- Los atributos pueden pertenecer a la instancia (exclusivos de cada instancia) o a la clase (compartidos por todas las instancias).
- Los métodos de instancia tienen `self` como primer parámetro para acceder a la instancia específica.
- Python usa métodos mágicos para realizar acciones «entre bastidores» para los usuarios. Los métodos mágicos siempre empiezan y terminan con doble guion bajo.
- Python permite sobrecargar operadores existentes para clases definidas por el usuario.
- Las clases pueden importarse desde módulos por su nombre o pueden renombrarse mediante alias.

En este punto, deberías poder escribir clases que tengan atributos de instancia, atributos de clase y métodos, e importar clases desde módulos. También deberías poder sobrecargar operadores al definir una clase.

**Referencia del capítulo 11.**

| Construcción | Descripción |
|---|---|
| Definición de clase | ```python<br>class ClassName:<br>  """Docstring"""<br>``` |
| `__init__()` | ```python<br>class ClassName:<br>  def __init__(self):<br>    # Initialize attributes<br>``` |
| Atributos | ```python<br>class ClassName:<br>  class_attr_1 = [value]<br>  class_attr_2 = [value]<br><br>  def __init__(self):<br>    instance_attr_1 = [value]<br>    instance_attr_2 = [value]<br>    instance_attr_3 = [value]<br>``` |
| Métodos (de instancia) | ```python<br>class ClassName:<br><br>  def __init__(self):<br>    instance_attr_1 = [value]<br>    instance_attr_2 = [value]<br>    instance_attr_3 = [value]<br><br>  def method_1(self, val1, val2):<br>    # Access/change attributes<br><br>  def method_2(self):<br>    # Access/change attributes<br>``` |
| Instancias | ```python<br>instance_1 = ClassName()<br>instance_1.instance_attr_1 = [new value]<br>instance_2 = ClassName()<br>instance_2.method_2()<br>``` |
| Operador de multiplicación sobrecargado | ```python<br>class ClassName:<br>  # Other methods<br><br>  def __mul__(self, other):<br>    return ClassName(self.instance_attr_3 * other.instance_attr_3)<br>``` |
| Importar una clase de un módulo con alias | ` from class_module import ClassName as ClassAlias` |
