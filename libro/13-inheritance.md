# Capítulo 13: Herencia

<!-- modulo: m00094 -->

## Introducción

![Una oveja adulta y un pequeño cordero están de pie, uno junto al otro, en un pasto verde y vibrante, ambos mirando directamente a la cámara con expresión tranquila.](media/Python_13_00_000.jpg)

*crédito: modificación de la obra «Don't stare...only sheep dogs stare...», de Bernard Spragg. NZ/Flickr, dominio público*

Las entidades del mundo real suelen describirse en relación con otras entidades. Ej.: un pinzón es un tipo de ave. De manera similar, las clases, que representan tipos de entidades del mundo real, pueden estar relacionadas entre sí.

La herencia describe la relación en la que una clase es un tipo de otra clase. Las clases dentro de una relación de herencia pueden heredar atributos y métodos de otras clases sin necesidad de volver a definir todo. Así, la herencia en la programación orientada a objetos reduce la redundancia y promueve la modularidad.

<!-- modulo: m00095 -->

## 13.1 Conceptos básicos de la herencia

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Identificar las relaciones es-un y tiene-un entre clases.
- Diferenciar entre una subclase y una superclase.
- Crear una superclase, una subclase e instancias de cada una.

### Relaciones es-un frente a tiene-un

Las clases se relacionan entre sí. Una relación es-un existe entre una subclase y una superclase. Ej.: un narciso es una planta. Una clase `Daffodil` hereda de una superclase, `Plant`.

Las relaciones es-un pueden confundirse con las relaciones tiene-un. Una relación tiene-un existe entre una clase que contiene a otra clase. Ej.: un empleado tiene una computadora portátil proporcionada por la empresa. Nota: la computadora portátil no es un empleado.

**Video:** [is-a relationship between Employee and Developer](https://www.openstax.org/r/is-a-relationship)

**Conceptos en práctica: Relaciones entre clases**

<!-- pregunta: CPL-ch13-m01-p01 -->

1. ¿Cuál es la relación entre una clase `Doughnut` y una clase `Pastry`?

   - a) es-un
   - b) tiene-un

   <details><summary>Respuesta</summary>

   a) Una dona es un tipo de pastelito, por lo que `Doughnut` hereda de `Pastry`.

   </details>

<!-- pregunta: CPL-ch13-m01-p02 -->

2. ¿Cuál es la relación entre una clase `Kitchen` y una clase `Freezer`?

   - a) es-un
   - b) tiene-un

   <details><summary>Respuesta</summary>

   b) Una cocina tiene un congelador, por lo que una clase `Kitchen` contendría una instancia de `Freezer`. Una relación tiene-un también se llama composición.

   </details>

<!-- pregunta: CPL-ch13-m01-p03 -->

3. Un portero es un jugador. Portero es una clase ______. Jugador es una clase ______.

   - a) super; sub
   - b) sub; super

   <details><summary>Respuesta</summary>

   b) La clase `Goalkeeper` hereda de la clase `Player`.

   </details>

### Herencia en Python

La herencia usa una relación es-un para heredar una clase de una superclase. La subclase hereda todos los atributos y métodos de la superclase, y amplía su funcionalidad.

En Python, una subclase se crea incluyendo el nombre de la superclase entre paréntesis en la parte superior de la definición de la subclase:

```python norun
class SuperClass:
    # atributos y métodos de SuperClass

class SubClass(SuperClass):
    # atributos y métodos de SubClass
```

**Video:** [Using inheritance to create subclasses](https://www.openstax.org/r/inheritance-subclasses)

**Conceptos en práctica: Crear subclases**

<!-- pregunta: CPL-ch13-m01-p04 -->

1. ¿Cómo se define una clase `Daisy` que hereda de la clase `Plant`?

   - a)

     ```python norun
     class Plant(Daisy):
     ```

   - b)

     ```python norun
     class Daisy(Plant):
     ```

   - c)

     ```python norun
     class Daisy:
     class Plant:
     ```

   <details><summary>Respuesta</summary>

   b) El nombre de la subclase va seguido del nombre de la superclase entre paréntesis.

   </details>

<!-- pregunta: CPL-ch13-m01-p05 -->

2. Supón que una clase CarryOn hereda de una clase Luggage. ¿Cómo se crea una instancia de CarryOn?

   - a) `small_bag = CarryOn()`
   - b) `small_bag = Luggage(CarryOn)`
   - c) `small_bag = CarryOn(Luggage)`

   <details><summary>Respuesta</summary>

   a) Derivar `CarryOn` de `Luggage` se especifica en la definición de la clase `CarryOn`. Ej.: `class CarryOn(Luggage):`. Las instancias de una subclase, como `CarryOn`, se crean como las de otras clases y no requieren el nombre de la clase base.

   </details>

<!-- pregunta: CPL-ch13-m01-p06 -->

3. Dadas las siguientes `SuperClass` y `SubClass`, ¿a cuál de los siguientes elementos puede acceder una instancia de `SubClass`?
   
   ```python
   class SuperClass():
     def func_1(self):
       print('Superclass function')
   
   class SubClass(SuperClass):
     def func_2(self):
       print('Subclass function')
   ```

   - a) solo `func_1()`
   - b) solo `func_2()`
   - c) `func_1()` y `func_2()`

   <details><summary>Respuesta</summary>

   c) Una instancia de `SubClass` tiene acceso a `func_1()`, heredado de `SuperClass`, así como a `func_2()`, un método de `SubClass`.

   </details>

<!-- pregunta: CPL-ch13-m01-p07 -->

4. Dadas las siguientes `SuperClass` y `SubClass`, ¿a cuál de los siguientes elementos puede acceder una instancia de SuperClass?
   
   ```python
   class SuperClass():
     def func_1(self):
       print('Superclass function')
   
   class SubClass(SuperClass):
     def func_2(self):
       print('Subclass function')
   ```

   - a) solo `func_1()`
   - b) solo `func_2()`
   - c) `func_1()` y `func_2()`

   <details><summary>Respuesta</summary>

   a) Una instancia de `SuperClass` tiene acceso a `func_1()` de `SuperClass`, pero no tiene acceso a nada de `SubClass`, incluido `func_2()`.

   </details>

**Términos alternativos de herencia**

La documentación de Python sobre la herencia usa varios términos para referirse a la clase de la que se hereda y a la clase que hereda. Este libro usa superclase/subclase en todo momento por coherencia.

| Clase de la que se hereda | Clase que hereda |
|---|---|
| superclase | subclase |
| clase base | clase derivada |
| clase padre | clase hija |

**Pruébalo: Clases Employee y Developer**

Dada la clase `Employee`, crea una clase `Developer` que herede de `Employee`. La clase `Developer` tiene un método, `update_codebase()`, que imprime `"Employee has updated the codebase"`. Luego, usa la instancia de `Developer`, `python_dev`, para llamar a `print_company()` y `update_codebase()`.

<!-- coderunner: ch13/CodeRunner_13_02_01_Employee-and-Developer-classes -->

**Pruébalo: Clases Polygon**

Define tres clases: `Polygon`, `Rectangle` y `Square`:

- `Polygon` tiene el método `p_disp()`, que imprime `"object is a Polygon"`.
- `Rectangle` hereda de `Polygon` y tiene el método `r_disp()`, que imprime `"object is a Rectangle"`.
- `Square` hereda de `Rectangle` y tiene el método `s_disp()`, que imprime `"object is a Square"`.

Crea una instancia de cada clase. Luego, para cada instancia, llama a todos los métodos a los que la instancia tiene acceso.

<!-- coderunner: ch13/CodeRunner_13_02_02_Polygon-classes -->

<!-- modulo: m00096 -->

## 13.2 Acceso a atributos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Implementar una subclase que accede a los atributos heredados de la superclase.
- Escribir el `__init__()` de una subclase que hereda los atributos de instancia de la superclase y crea nuevos atributos de instancia.

### Crear una subclase simple

Las subclases tienen acceso a los atributos heredados de la superclase. Cuando el `__init__()` de la subclase no está definido explícitamente, se llama al método `__init__()` de la superclase. Acceder a ambos tipos de atributos usa la misma sintaxis.

**Video:** [Defining a simple subclass](https://www.openstax.org/r/simple-subclass)

**Conceptos en práctica: Uso de subclases simples**

<!-- pregunta: CPL-ch13-m02-p01 -->

1. Considera el ejemplo anterior de `Employee` y `Developer`. ¿Cuál es el valor de `dev_1.e_id`?

   - a) `1`
   - b) `2`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `dev_1` es el segundo `Employee` creado. Por lo tanto, `dev_1` es el segundo objeto que llama a `Employee.__init__()`, y a `dev_1.e_id` se le asigna `2`.

   </details>

<!-- pregunta: CPL-ch13-m02-p02 -->

2. Considera el siguiente ejemplo. La línea 13 se ejecuta y se llama a `SubClass()`. ¿A qué línea pasa el flujo de control?
   
   ```python
   class SuperClass:
     def __init__(self):
       self.feat_1 = 1
       self.feat_2 = ""
   
     def bc_display(self):
       print(f"Superclass: {self.feat_2}")
   
   class SubClass(SuperClass):
     def dc_display(self):
       print(f"Subclass: {self.feat_2}")
   
   dc_1 = SubClass()
   ```

   - a) 2
   - b) 10
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) El `__init__()` de `SubClass` no está definido explícitamente, por lo que se ejecuta el `__init__()` de `SuperClass`.

   </details>

<!-- pregunta: CPL-ch13-m02-p03 -->

3. Considera el siguiente ejemplo. ¿Qué atributos de instancia tiene `dc_1`?
   
   ```python
   class SuperClass:
     def __init__(self):
       self.feat_1 = 1
       self.feat_2 = ""
   
     def bc_display(self):
       print(f"Superclass: {self.feat_2}")
   
   class SubClass(SuperClass):
     def dc_display(self):
       print(f"Subclass: {self.feat_2}")
   
   dc_1 = SubClass()
   ```

   - a) `feat_2`
   - b) `feat_1` y `feat_2`
   - c) Ninguno

   <details><summary>Respuesta</summary>

   b) `dc_1` hereda `feat_1` y `feat_2` de `SuperClass`.

   </details>

### Usar __init__() para crear y heredar atributos de instancia

Un programador suele querer que una subclase tenga nuevos atributos de instancia además de los heredados de la superclase. Definir explícitamente el `__init__()` de una subclase implica definir atributos de instancia y asignar los atributos de instancia heredados de la superclase.

**Video:** [Defining __init__() in a subclass](https://www.openstax.org/r/init-in-a-subclass)

**Conceptos en práctica: Acceso a los atributos de una subclase**

<!-- pregunta: CPL-ch13-m02-p04 -->

1. ¿Cuál sería la salida de `dev_1.dev_display()`?

   - a) `Employee 2 hired in 2023`
   - b) `Proficient in ['Python', 'C++', 'Java']`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `dev_display()` es un método de `Developer` que accede al atributo de instancia `lang_xp` de `dev_1`.

   </details>

<!-- pregunta: CPL-ch13-m02-p05 -->

2. ¿Cuál sería la salida de `emp_1.dev_display()`?

   - a) `Employee 1 hired in 2023`
   - b) `Proficient in ['Python', 'C++', 'Java']`
   - c) `Error`

   <details><summary>Respuesta</summary>

   c) `dev_display()` es un método de `Developer`. `emp_1` no es una instancia de `Developer`, por lo que `emp_1` no puede acceder a `dev_display()`.

   </details>

<!-- pregunta: CPL-ch13-m02-p06 -->

3. Supón que `dev_display()` debe modificarse para mostrar el ID del desarrollador junto con sus competencias. Ej.: `dev_1.dev_display()` imprimiría `Employee 2 proficient in ['Python', 'C++', 'Java']`. ¿Cuál es la nueva llamada a `print()` adecuada en `dev_display()`?

   - a) `print(f"Employee {self.e_id} proficient in {self.lang_xp}")`
   - b) `print(f"Employee {self.Employee.e_id} proficient in {self.lang_xp}")`
   - c) `print(f"Employee 2 proficient in {self.lang_xp}")`

   <details><summary>Respuesta</summary>

   a) Los atributos de instancia heredados de `Employee`, la superclase, se accede a ellos de la misma manera que los atributos de instancia de la subclase `Developer`.

   </details>

**Pruébalo: Crear una subclase con un atributo de instancia**

Dada una clase `Dessert`, crea una clase, `Cupcake`, que herede de `Dessert`. Métodos de la clase `Cupcake`:

- `__init__(self)`: inicializa el atributo de instancia heredado `ingredients` con `["butter", "sugar", "eggs", "flour"]`, e inicializa el atributo de instancia `frosting` con `"buttercream"`
- `display(self)`: imprime los ingredientes y la cobertura de un cupcake

Luego, llama al método `display()` en un nuevo objeto `Cupcake`. La salida debe coincidir con:

```text
Made with ["butter", "sugar", "eggs", "flour"] and topped with buttercream frosting
```

<!-- coderunner: ch13/CodeRunner_13_03_03_Creating-a-subclass-with-an-instance-attribute -->

<!-- modulo: m00097 -->

## 13.3 Métodos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Escribir métodos sobrescritos para cambiar el comportamiento de métodos heredados.
- Usar `super()` para acceder a métodos de la superclase.
- Identificar aplicaciones del polimorfismo en el uso de métodos y funciones.

### Sobrescribir métodos

A veces un programador quiere cambiar las funciones que hereda una subclase. `Mint` es una subclase que tiene la misma funcionalidad que `Plant`, excepto por una función. Una subclase puede **sobrescribir** un método de la superclase definiendo un método con el mismo nombre que el método de la superclase.

**Video:** [Overriding a superclass method](https://www.openstax.org/r/overriding-superclass)

**Conceptos en práctica: Sobrescribir métodos**

<!-- pregunta: CPL-ch13-m03-p01 -->

1. Supón que un programador hace que la clase `ContractTax` herede de la clase `Tax` y quiere sobrescribir el `calc_tax()` de `Tax`. ¿Qué debe hacer el programador?

   - a) Definir otro método `calc_tax()` en `Tax`.
   - b) Definir un método `calc_tax()` en `ContractTax`.
   - c) Definir una función que reciba una instancia de `ContractTax`.

   <details><summary>Respuesta</summary>

   b) Sobrescribir implica definir un método de la subclase que tenga el mismo nombre que el método de la superclase.

   </details>

<!-- pregunta: CPL-ch13-m03-p02 -->

2. ¿Cuál es el error en el programa que intenta sobrescribir `calc_tax()` para `ContractTaxDE`?
   
   ```python norun
   class Tax:
     def calc_tax(self):
       print('Calculating tax')
   
   class ContractTax(Tax):
     def calc_tax(self):
       print('Calculating contract tax')
   
   class ContractTaxDE(ContractTax):
     def calc_tax():
       print('Calculating German contract tax')
   
   my_tax = ContractTaxDE()
   my_tax.calc_tax()
   ```

   - a) `ContractTaxDE` debe heredar de `Tax`, no de `ContractTax`.
   - b) A la definición de `calc_tax()` de `ContractTaxDE` le falta un parámetro.
   - c) `ContractTaxDE` no puede sobrescribir `calc_tax()` porque `ContractTax` ya lo hizo.

   <details><summary>Respuesta</summary>

   b) Falta el parámetro `self` en la definición del método sobrescrito.

   </details>

<!-- pregunta: CPL-ch13-m03-p03 -->

3. El siguiente programa no sobrescribe `calc_tax()`. ¿Por qué?
   
   ```python
   class Tax:
     def calc_tax(self):
       print('Calculating tax')
       total = 0 # Se reemplazará por el cálculo
       return total
   
   class ContractTax:
     def calc_tax(self):
       print('Calculating contract tax')
       total = 0 # Se reemplazará por el cálculo
       return total
   
   my_tax = ContractTax()
   my_tax.calc_tax()
   ```

   - a) Un método sobrescrito no puede devolver un valor.
   - b) `Tax` no especifica que `calc_tax()` pueda sobrescribirse.
   - c) `ContractTax` no hereda de `Tax`.

   <details><summary>Respuesta</summary>

   c) La definición de la clase no indica herencia. La definición debería ser `class ContractTax(Tax):`.

   </details>

### super()

`super()` es un método especial que proporciona una instancia temporal de objeto de la superclase para que la use una subclase. `super()` se usa comúnmente para llamar a métodos de la superclase desde una subclase. `super()` se usa comúnmente en el `__init__()` de una subclase para asignar atributos de instancia heredados. Ej.: `super().__init__()`.

**Video:** [Using super() to call the superclass __init__() method](https://www.openstax.org/r/using-super)

**Conceptos en práctica: Uso de super()**

<!-- pregunta: CPL-ch13-m03-p04 -->

1. Se ejecuta la línea 16 y se llama al `__init__()` de `Square` en la línea 12. Se ejecuta la línea 13 y se llama al `__init__()` de la superclase. ¿A qué línea pasa el flujo de control a continuación?

   - a) 2
   - b) 6
   - c) 14

   <details><summary>Respuesta</summary>

   b) La superclase de `Square` es `Rectangle`. Se llama al `__init__()` de `Rectangle` en la línea 6.

   </details>

<!-- pregunta: CPL-ch13-m03-p05 -->

2. Se ejecuta la siguiente línea. ¿A qué línea pasa el flujo de control a continuación?

   - a) 2
   - b) 6
   - c) 14

   <details><summary>Respuesta</summary>

   a) `super().__init__(4)` llama al `__init__()` de la superclase de `Rectangle`, `Polygon`. El control pasa a la línea 3, y `num_sides` se inicializa con `4`.

   </details>

<!-- pregunta: CPL-ch13-m03-p06 -->

3. La llamada al método regresa. Se ejecutan las líneas 8 y 9 para inicializar `length` y `width`, y el `__init__()` de `Rectangle` regresa. ¿A qué línea pasa el flujo de control a continuación?

   - a) 12
   - b) 14
   - c) 17

   <details><summary>Respuesta</summary>

   b) El atributo de instancia `side` se inicializa con `5`.

   </details>

<!-- pregunta: CPL-ch13-m03-p07 -->

4. El `__init__()` de `Square` regresa y el flujo de control pasa a la línea 17. ¿Cuál es la salida?

   - a) `3`
   - b) `4`
   - c) `5`

   <details><summary>Respuesta</summary>

   b) El `__init__()` de `Rectangle` siempre llama al `__init__()` de `Polygon` con `num_sides=4`.

   </details>

### Polimorfismo

El **polimorfismo** es el concepto de tener muchas formas. En programación, un mismo nombre puede usarse para varias funcionalidades. Dentro de la herencia, el polimorfismo es la base de la sobrescritura de métodos, ya que varios métodos tienen el mismo nombre.

**Ejemplo: Polimorfismo y herencia**

El nombre `display()` corresponde a varios métodos. El tipo de clase del objeto que llama determina qué método `display()` se ejecuta.

```python
class Plant:
  def display(self):
    print("Soy una planta")

class Mint(Plant):
  def display(self):
    print("Soy una menta")

class Lavender(Mint):
  def display(self):
    print("Soy una lavanda")

mint_1 = Mint()
mint_1.display()

lavender_1 = Lavender()
lavender_1.display()
```

La salida del código es:

```salida
Soy una menta
Soy una lavanda
```

El polimorfismo también puede usarse con métodos de clases no relacionadas. El tipo de clase del objeto que llama determina el método que se ejecuta.

**Ejemplo: Polimorfismo y métodos**

`Tax` y `ContractTax` son clases no relacionadas que definen cada una `calc_tax()`. `calc_tax()` no se sobrescribe porque `ContractTax` no hereda de `Tax`.

```python
class Tax:
  def __init__(self, value):
    self.value = value

  def calc_tax(self):
    print("Calculating tax")
    total = 0.10 * self.value  # Se reemplazará por el cálculo
    return total

class ContractTax:
  def __init__(self, value):
    self.value = value

  def calc_tax(self):
      print("Calculating contracts tax")
      total = 0.15 * self.value  # Se reemplazará por el cálculo
      return total

my_tax = ContractTax(value=1000)  # Reemplaza 1000 por cualquier valor
result = my_tax.calc_tax()
print(f"Total tax: ${result}")
```

La salida del código es:

```text
Calculating contracts tax
Total tax: $150.0
```

El polimorfismo permite llamar a los métodos con parámetros de distintos tipos. Muchos operadores y funciones integrados tienen esta utilidad.

**Ejemplo: Polimorfismo y funciones**

`len()` puede llamarse con varios tipos, incluidas listas y cadenas.

```python
tree_list = ["ash", "hazel", "oak", "yew"]
tree_1 = tree_list[0]
print(len(tree_list))
print(len(tree_1))
```

La salida del código es:

```salida
4
3
```

**Conceptos en práctica: Polimorfismo en la práctica**

<!-- pregunta: CPL-ch13-m03-p08 -->

1. Considera el ejemplo. ¿Cuál es la salida?
   
   ```python
   class Polygon:
     def print_type(self):
       print("Polygon type")
   
   class Rectangle(Polygon):
     def print_type(self):
       print("Rectangle type")
   
   class Square(Rectangle):
     def print_type(self):
       print("Square type")
   
   sq_1 = Square()
   sq_1.print_type()
   ```

   - a) `Polygon type`
   - b) `Rectangle type`
   - c) `Square type`

   <details><summary>Respuesta</summary>

   c) El polimorfismo permite sobrescribir `print_type()` en las subclases de `Polygon`.

   </details>

<!-- pregunta: CPL-ch13-m03-p09 -->

2. ¿Cuál es un ejemplo de polimorfismo para el operador de multiplicación?

   - a)

     ```python
     x = 3 * 4
     y = 3 * "la"
     ```

   - b)

     ```python
     x = 3 * 4
     y = str(x)
     ```

   - c)

     ```python
     x = 3 * 4
     y = x * x
     ```

   <details><summary>Respuesta</summary>

   a) El operador `*` puede usarse con operandos enteros, así como con cadenas y otros tipos.

   </details>

**Pruébalo: Sobrescribir métodos**

Dada la clase `Pet`, crea una clase `Bird` que herede de `Pet` y una clase `Finch` que herede de `Bird`. Sobrescribe el método `display()` en `Bird` y `Finch` de modo que la salida del programa sea:

```text
Pet type: Bird
Bird type: Finch
```

<!-- coderunner: ch13/CodeRunner_13_04_04_Overriding-methods -->

**Pruébalo: Uso de super()**

Dada la clase `Employee`, crea una clase `Developer` que herede de `Employee` con los métodos `__init__()` y `print_info()` de modo que:

`__init__()`

- Usa `super()` para llamar al `__init__()` de `Employee` y así inicializar `e_id` y `hire_year`.
- Asigna `lang_xp` con el parámetro de lista `lang_xp`.

`print_info()`

- Usa `super()` para imprimir `e_id` y `hire_year`.
- Imprime `"Language(s):"` seguido de `lang_xp`.

<!-- coderunner: ch13/CodeRunner_13_04_05_Using-super() -->

<!-- modulo: m00098 -->

## 13.4 Herencia jerárquica

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Etiquetar las relaciones entre clases como tipos de herencia.
- Construir clases que forman una herencia jerárquica.

### Conceptos básicos de la herencia jerárquica

La **herencia jerárquica** es un tipo de herencia en el que varias clases heredan de una sola superclase. La **herencia multinivel** es un tipo de herencia en el que una subclase se convierte en la superclase de otra clase. Combinar la herencia jerárquica y la multinivel crea una organización de clases en forma de árbol.

**Video:** [Hierarchical organization and types of inheritance](https://www.openstax.org/r/inheritance-types)

**Conceptos en práctica: Organización jerárquica**

<!-- pregunta: CPL-ch13-m04-p01 -->

1. ¿Cuál es un ejemplo de herencia jerárquica?

   - a) La clase B hereda de la clase A
      La clase C hereda de la clase A
   - b) La clase B hereda de la clase A
      La clase C hereda de la clase B
   - c) La clase B hereda de la clase A
      La clase C hereda de la clase D

   <details><summary>Respuesta</summary>

   a) `Class A` es la superclase de `Class B` y `Class C`.

   </details>

<!-- pregunta: CPL-ch13-m04-p02 -->

2. ¿Para qué grupo de clases es apropiada la herencia jerárquica?

   - a) `Cat`, `Dog`, `Bird`
   - b) `Employee`, `Developer`, `SalesRep`
   - c) `Dessert`, `BakedGood`, `ApplePie`

   <details><summary>Respuesta</summary>

   b) `Employee` sería una superclase apropiada para `Developer` y `SalesRep`. `Developer` y `SalesRep` no están relacionadas directamente.

   </details>

### Implementar la herencia jerárquica

Varias clases pueden heredar de una sola clase con solo incluir el nombre de la superclase en la definición de cada subclase.

**Ejemplo: Miembros de un coro**

```python
class ChoirMember:
  def display(self):
    print("Miembro actual del coro")

class Soprano(ChoirMember):
  def display(self):
    super().display()
    print("Cuerda: Soprano")

class Soprano1(Soprano):
  def display(self):
    super().display()
    print("División: Soprano 1")

class Alto(ChoirMember):
  def display(self):
    super().display()
    print("Cuerda: Alto")

class Tenor(ChoirMember):
  def display(self):
    super().display()
    print("Cuerda: Tenor")

class Bass(ChoirMember):
  def display(self):
    super().display()
    print("Cuerda: Bajo")

mem_10 = Alto()
mem_13 = Tenor()
mem_15 = Soprano1()

mem_10.display()
print()
mem_13.display()
print()
mem_15.display()
```

La salida del código es:

```salida
Miembro actual del coro
Cuerda: Alto

Miembro actual del coro
Cuerda: Tenor

Miembro actual del coro
Cuerda: Soprano
División: Soprano 1
```

**Conceptos en práctica: Implementar la herencia jerárquica**

<!-- pregunta: CPL-ch13-m04-p03 -->

1. ¿Cuál es el valor de `b_inst.b_attr`?

   - a) `0`
   - b) `2`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) `B(2)` se resuelve como `B(2, 0)`, ya que `b_attr` tiene un valor predeterminado de `0`. A `a_attr` se le asigna `2`.

   </details>

<!-- pregunta: CPL-ch13-m04-p04 -->

2. ¿A qué atributos tiene acceso `c_inst`?

   - a) `a_attr`
   - b) `a_attr`, `c_attr`
   - c) `c_attr`

   <details><summary>Respuesta</summary>

   b) `c_inst` tiene acceso al atributo de instancia de `C`, `c_attr`, así como al atributo heredado de `A`, `a_attr`.

   </details>

<!-- pregunta: CPL-ch13-m04-p05 -->

3. ¿A qué atributos tiene acceso `d_inst`?

   - a) `b_attr`, `d_attr`
   - b) `a_attr`, `b_attr`, `d_attr`
   - c) `d_attr`

   <details><summary>Respuesta</summary>

   b) `D` hereda de `B`, por lo que `d_inst` hereda `b_attr`. `B` también hereda de `A`, por lo que `d_inst` hereda `a_attr`.

   </details>

**Pruébalo: Sobrescribir métodos**

Define tres clases: `Instrument`, `Woodwind` y `String`.

- `Instrument` tiene el atributo de instancia `owner`, con valor predeterminado «unknown».
- `Woodwind` hereda de `Instrument` y tiene el atributo de instancia `material` con valor predeterminado «wood».
- `String` hereda de `Instrument` y tiene el atributo de instancia `num_strings`, con valor predeterminado 4.

La salida debe coincidir con:

```text
This flute belongs to unknown and is made of silver
This cello belongs to Bea and has 4 strings
```

<!-- coderunner: ch13/CodeRunner_13_05_06_Overriding-methods -->

<!-- modulo: m00099 -->

## 13.5 Herencia múltiple y clases mixin

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Construir una clase que hereda de varias superclases.
- Identificar el problema del diamante dentro de la herencia múltiple.
- Construir una clase mixin para añadir funcionalidad a una subclase.

### Conceptos básicos de la herencia múltiple

La **herencia múltiple** es un tipo de herencia en el que una clase hereda de varias clases. Una clase que hereda de varias clases tiene todas las superclases listadas en la lista de herencia de la definición de la clase. Ej.: `class SubClass(SuperClass_1, SuperClass_2)`.

**Video:** [Multiple inheritance organization](https://www.openstax.org/r/multiple-inheritance-organization)

**Conceptos en práctica: Implementar la herencia múltiple**

<!-- pregunta: CPL-ch13-m05-p01 -->

1. ¿Cuál es el valor de `c_inst.a_attr`?

   - a) `1`
   - b) `5`
   - c) `Error`

   <details><summary>Respuesta</summary>

   a) `1` es el argumento que se pasa al `__init__()` de `C` para `a_attr`.

   </details>

<!-- pregunta: CPL-ch13-m05-p02 -->

2. ¿Cuál es el valor de `c_inst.c_attr`?

   - a) `2`
   - b) `20`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) No se pasa un argumento al `__init__()` de `C` para `c_attr`, por lo que `c_attr` recibe el valor predeterminado, `20`.

   </details>

<!-- pregunta: CPL-ch13-m05-p03 -->

3. ¿Cuál es el valor de `b_inst.a_attr`?

   - a) `2`
   - b) `4`
   - c) `Error`

   <details><summary>Respuesta</summary>

   b) `2` corresponde a `b_attr` en el `__init__()` de `B`.

   </details>

### El problema del diamante y las clases mixin

La herencia múltiple debe implementarse con cuidado. El **problema del diamante** ocurre cuando una clase hereda de varias clases que comparten una superclase común. Ej.: `Dessert` y `BakedGood` heredan ambas de `Food`, y `ApplePie` hereda de `Dessert` y `BakedGood`.

****

![Un diagrama conceptual que ilustra una jerarquía de clasificación. 'ApplePie' aparece como subtipo de 'Dessert' y de 'BakedGood', que a su vez son ambos subtipos de 'Food'.](media/Python_13_05_001.png)

***El problema del diamante.** Si tanto `Dessert` como `BakedGood` sobrescriben un método de `Food`, el método sobrescrito de `Food` que hereda `ApplePie` es ambiguo. Por lo tanto, debe evitarse la herencia con forma de diamante.*

Las clases mixin promueven la modularidad y pueden eliminar el problema del diamante. Una clase mixin:

- No tiene superclase
- Tiene atributos y métodos que se añadirán a una subclase
- No se instancia (Ej.: dada la clase `MyMixin`, nunca debe usarse `my_inst = MyMixin()`.)

Las **clases mixin** se usan en la herencia múltiple para añadir funcionalidad a una subclase sin añadir problemas de herencia.

**Conceptos en práctica: Crear una clase mixin**

<!-- pregunta: CPL-ch13-m05-p04 -->

1. ¿Qué edición es la adecuada?

   - a) Mover `eat()` a otra clase.
   - b) Quitar `Plant` como superclase.

   <details><summary>Respuesta</summary>

   b) `eat()` solo se aplica a las plantas carnívoras, que son las que representan `Pitcher` y `VenusFlyTrap`.

   </details>

<!-- pregunta: CPL-ch13-m05-p05 -->

2. El programador edita el código como sigue. ¿Cómo se puede mejorar el programa?
   
   ```python norun
   class Plant:
     def photosynth(self):
       print("Photosynthesizing")
   
   class Rose(Plant):
     pass
   
   class Pitcher(Plant):
     def eat(self):
       print("Eating")
   
   class VenusFlyTrap(Plant)
     def eat(self):
       print("Eating")
   ```

   - a) Mover `photosynth()` a `Rose`.
   - b) Eliminar la redundancia de `eat()`.

   <details><summary>Respuesta</summary>

   b) `eat()` puede moverse a una clase mixin incluida en las listas de herencia de `Pitcher` y `VenusFlyTrap`.

   </details>

<!-- pregunta: CPL-ch13-m05-p06 -->

3. El programador edita el código para crear una clase mixin que contiene `eat()`. ¿Qué nombre de clase, en lugar de `X`, es el más apropiado para el mixin?
   
   ```python norun
   class Plant:
     def photosynth(self):
       print("Photosynthesizing")
   
   class X:
     def eat(self):
       print("Eating")
   
   class Rose(Plant):
     pass
   
   class Pitcher(Plant, X):
     pass
   
   class VenusFlyTrap(Plant, X)
     pass
   ```

   - a) `CarnivClass`
   - b) `CarnivMixin`

   <details><summary>Respuesta</summary>

   b) Una buena práctica es que el nombre de una clase mixin termine en `"Mixin"` para identificar el propósito de la clase. La implementación final es:
   
   ```python norun
   class Plant:
     def photosynth(self):
       print("Photosynthesizing")
   
   class CarnivMixin:
     def eat(self):
       print("Eating")
   
   class Rose(Plant):
     pass
   
   class Pitcher(Plant, CarnivMixin):
     pass
   
   class VenusFlyTrap(Plant, CarnivMixin)
     pass
   ```

   </details>

**Pruébalo: Resolver el problema del diamante con una clase mixin**

El siguiente programa representa herencia múltiple y tiene el problema del diamante. Edita el programa para usar una clase mixin, `OnlineMixin`. `OnlineMixin`:

- Reemplaza a `OnlineShop`.
- Es una superclase de `FoodFast`.
- Tiene un método, `process_online()`, que imprime `"Connecting to server"` y al que llama `process_order()` de `FoodFast`.

La salida debe coincidir con:

```text
Processing meal order
Connecting to server
Enjoy your FoodFast order
```

<!-- coderunner: ch13/CodeRunner_13_06_07_Fixing-the-diamond-problem-with--a-mixin-class -->

<!-- modulo: m00100 -->

## Resumen del capítulo

Los puntos más destacados de este capítulo incluyen:

- La herencia describe una relación es-un entre clases. Una clase, la subclase, hereda de otra clase, la superclase.
- Las subclases pueden acceder directamente a los atributos y métodos heredados.
- Las subclases pueden sobrescribir métodos de la superclase para cambiar o añadir funcionalidad.
- `super()` permite que una subclase acceda a los métodos de la superclase.
- El polimorfismo describe una única representación para múltiples formas y en Python se aplica para definir varios métodos con el mismo nombre y permitir que un mismo método reciba distintos argumentos.
- La herencia jerárquica es un tipo de herencia en el que varias clases heredan de una sola superclase.
- La herencia múltiple es un tipo de herencia en el que una clase hereda de varias clases.
- Las clases mixin se usan en la herencia múltiple para añadir funcionalidad a una subclase sin añadir problemas de herencia.

En este punto, deberías poder escribir subclases que heredan atributos de instancia y métodos, y subclases que tienen atributos únicos y métodos sobrescritos. También deberías poder crear relaciones de herencia jerárquica y de herencia múltiple entre clases.

**Referencia del capítulo 13.**

| Tarea | Ejemplo |
|---|---|
| Definir una subclase | ```python<br>class SuperClass:<br>  pass<br><br>class SubClass(SuperClass):<br>  pass<br>``` |
| Definir el `__init__()` de una subclase usando `super()` | ```python<br>class SubClass(SuperClass):<br>  def __init__(self):<br>    super().__init__() # Llama al __init__() de la superclase<br>    # Inicializa los atributos de instancia de la subclase<br>``` |
| Sobrescribir un método de la superclase | ```python<br>class SuperClass:<br>  def display(self):<br>    print('Superclass method')<br><br>class SubClass(SuperClass):<br>  def display(self): # Mismo nombre que el método de la superclase<br>    print('Subclass method')<br>``` |
| Implementar herencia jerárquica | ```python<br>class SuperClass:<br>  def display(self):<br>    print('Superclass method')<br><br>class SubClass1(SuperClass):<br>  def display(self):<br>    print('Subclass 1 method ')<br>class SubClass2(SuperClass):<br>  def display(self):<br>  print('Subclass 2 method')<br><br>class SubClass3(SuperClass):<br>  def display(self):<br>    print('Subclass 3 method')<br>``` |
| Implementar herencia múltiple | ```python<br>class SuperClass1:<br>    pass<br><br>class SuperClass2:<br>    pass<br><br>class SubClass(SuperClass1, SuperClass2):<br>    pass<br>``` |
