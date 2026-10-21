# Segunda revisión del texto

Revisión completa del prefacio y los 15 capítulos (sprint 2, octubre de 2026). La primera traducción la hicieron modelos y se revisó por muestreo (una sección de cada cinco). En esta segunda pasada se leyó cada capítulo entero con el original en inglés al lado.

- **Método:** un revisor por capítulo con una lista de comprobación común (naturalidad, términos del glosario, erratas, fidelidad, coherencia y código). Después, una revisión de coordinación de todos los cambios (`git diff`), con al menos dos cambios comprobados a mano por capítulo.
- **Criterio:** solo se corrige lo que está mal o lo que mejora claramente la lectura. Las erratas del original se corrigen cuando son evidentes (p. ej. `min()` descrito como «máximo»). Si cambiarlas alteraría un ejercicio, se dejan y se anotan en «Dudas».
- **Norma de comillas:** « » en la prosa; las cadenas de Python van como código en línea (`"admin"`).
- **Comprobación:** `python3 herramientas/comprobar.py` (glosario sin incoherencias, todos los bloques `python` corren y cada `salida` coincide, claves de respuesta). Con `--fuente`, también la estructura frente al original.

## Capítulo 00: Prefacio

- Secciones revisadas: 1 de 1.
- Cambios: 5 (naturalidad 1, términos 0, erratas 4, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 45, 69, 71, 92 | "…" | «…» | errata: comillas inglesas en la prosa (×4) |
| 180 | recomendamos enormemente visitar | recomendamos encarecidamente visitar | calco: «highly recommend» |

Glosario: sin propuestas.
Dudas: ninguna.

## Capítulo 01: Instrucciones

- Secciones revisadas: 9 de 9 (introducción, 1.1 a 1.8 y resumen; 10 con el resumen).
- Cambios: 22 (naturalidad 2, términos 3, erratas 12, fidelidad 5, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 34, 97, 284, 327, 620, 670, 1031, 1402, 1591 (×2) | "entre bambalinas", "py", "prompt", "six", "@", "H"…, "-4 al cuadrado", "comenta", "A brief history…" | «…» | errata: comillas de la prosa (×10); los textos en inglés de los enlaces se conservan |
| 103 | [Pandas] | [pandas] | término: glosario (nombre propio en minúscula) |
| 192 | …personalizar la salida.  muestra ejemplos… | …La tabla siguiente muestra ejemplos… | fidelidad: referencia a la tabla perdida (el original también la pierde), doble espacio |
| 458 | El carácter `=` solo es el operador… | El carácter `=` por sí solo es el operador… | fidelidad: «single `=`»; «solo» era ambiguo |
| 508 | almacena un valor de `median` | almacena un valor de mediana | naturalidad: calco |
| 1070 | multiplicando `meter` por `meter2feet` | multiplicando `meters` por… | fidelidad: la variable se llama `meters` (error del original) |
| 1388 | Aunque, en un programa de tres líneas, … generalmente es innecesario | Por otra parte, … suele ser innecesario | naturalidad: «Then again» mal traducido, adverbio calcado |
| 1462 | Los docstrings deben ser una cadena válida | Un docstring debe ser una cadena válida | errata: concordancia |
| 1597, 1601 | …en línea.  muestra… | El primer / El segundo gráfico muestra… | fidelidad: referencias a las figuras perdidas (también en el original), doble espacio |
| 1603, 1607 | Diagrama de dispersión | Gráfico de dispersión | término: glosario (scatter plot) |
| 1705 | instrucción print | instrucción `print` | errata: formato de código |

Glosario: sin propuestas.
Dudas: línea 1595 «Python se ha convertido en una organización sin fines de lucro» es literal del original (se refiere a la Python Software Foundation); no lo cambié. Las respuestas a las preguntas y los números cuadran con el original.

## Capítulo 02: Expresiones

- Secciones revisadas: 9 de 9 (introducción, 2.1 a 2.8 y resumen).
- Cambios: 16 (naturalidad 2, términos 0, erratas 10, fidelidad 4, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 182 | Las operaciones comunes actualizan una variable de modo que hay que cambiar su tipo… | Con frecuencia, una operación actualiza una variable y obliga a cambiar su tipo… | calco: «de modo que hay que» |
| 603 | …f-string, que se presentan en… | …f-string; estas se presentan en… | naturalidad: concordancia ambigua |
| 9, 84, 751 (×2), 1158 | "…" en la prosa (×6) | «…» | errata: comillas |
| 190, 203 | `book_rating'` | `book_rating` | errata: apóstrofo sobrante |
| 1199 | línea suelta «``» | (eliminada) | errata: resto de marcado |
| 1054, 1062 | π*r*2 | π*r*² | fidelidad: el exponente se había perdido |
| 838 | Para convertir horas a minutos… | Para convertir minutos a horas… | fidelidad: la pregunta es minutos a horas (el original se contradice) |
| 1435, 1437 | «.  muestra algunos…» | «. La primera/segunda tabla muestra algunos…» | fidelidad: referencia a figura vacía en el original, frase rota |

Glosario: sin propuestas
Dudas: las cinco citas de Guido (líneas 1409-1413) están traducidas al español dentro de un bloque `text`; el original las tiene en inglés y el ejercicio imprime texto, no las toqué. El comentario «Round-off error; … 0.999» de la tabla de math.tan es del original (el valor real es 0.9999999999999999), tampoco lo cambié.

Añadido en la revisión del coordinador: comillas rectas restantes en la prosa pasadas a « » o a código en línea (por coherencia en todo el libro).

## Capítulo 03: Objetos

- Secciones revisadas: 6 de 6 (introducción, 3.1 a 3.5 y resumen).
- Cambios: 2 (naturalidad 0, términos 0, erratas 1, fidelidad 1, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 758 | «…primer elemento de `tuple_1'`?» | «…primer elemento de `tuple_1`?» | errata: apóstrofo suelto heredado del original |
| 911 | «Obtiene el primer elemento `("a")` de `my_tuple`» | «…de `my_list`» | fidelidad/coherencia: la fila es `my_list[0]` (el original también lo dice mal) |

Glosario: sin propuestas.
Dudas: (1) línea 905, `f"{number:.02d}"` viene así del original, pero `.02d` lanza error con enteros (sería `02d`); no lo toqué por ser código/etiqueta. (2) línea 692, la pregunta dice `cardList` y las opciones `card_list` (incoherencia del original). (3) El capítulo usa comillas rectas "…" en la prosa, como el resto del libro (solo 4, 6 y 11 usan « »); no lo cambié.

Añadido en la revisión del coordinador: comillas rectas de la prosa pasadas a « » ×6 (crédito de la imagen, «9:05», «9:5», las dos opciones de Python Tutor y «dividir»), por coherencia con el resto del libro.

Añadido en la revisión del coordinador: comillas rectas restantes en la prosa pasadas a « » o a código en línea (por coherencia en todo el libro).

## Capítulo 04: Decisiones

- Secciones revisadas: 8 de 8 (introducción, 4.1–4.7 y resumen).
- Cambios: 13 (naturalidad 1, términos 3, erratas 9, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | "Fork In The Road" | «Fork In The Road» | comillas rectas en la prosa |
| 189, 249, 621, 623, 867 | "0", "admin", "f", "c", "Good driving"… | `"0"`, `"admin"`, `"f"`… (código en línea) | comillas rectas de valores de código en la prosa; también `unit`, `temp`, `==` en código |
| 609 | `x'` | `x` | errata (también en el original) |
| 681 | `hrs_to close` | `hrs_to_close` | errata de nombre de variable |
| 686 | False and True es… | `False and True` es… | formato de código |
| 725 | es `true` | es `True` | errata: palabra clave sin mayúscula |
| 801 | puede hacer una condición más legible y que sirve… | hace más legible una condición y sirve… | calco del orden inglés |
| 1063 | menor prioridad | menor precedencia | término: glosario (precedencia) |
| 1080-1081 | párrafo fusionado | párrafo separado por línea en blanco | errata de estructura (alinea con el original) |
| 1113, 1128, 1155, 1173, 1533-1561 | `Body N` | `Cuerpo N` (×15) | coherencia con los comentarios de código ya traducidos |
| 1378 | gancho de crochet | ganchillo | término: coherencia con el título «ganchillo» |
| 1544 | `x =118` | `x = 118` | errata de espaciado |
| 1682 | …else y`" | …else y` | errata: comilla suelta |
| 1720 | si hours > 12… fee + 10… 2 | `hours > 12`, `fee + 10`, `2` | formato de código |

Glosario: sin propuestas.
Dudas: ninguna. Números, opciones y respuestas verificados contra el original sin discrepancias.

Añadido en la revisión del coordinador: comillas rectas restantes en la prosa pasadas a « » o a código en línea (por coherencia en todo el libro).

## Capítulo 05: Bucles

- Secciones revisadas: 7 de 7 (introducción, 5.1 a 5.5 y resumen).
- Cambios: 7 (naturalidad 3, términos 1, erratas 3, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | obra "Quantum Computing" | obra «Quantum Computing» | errata: comillas rectas en la prosa |
| 81 | se puede realizar usando un contador… | se puede realizar con un contador… | calco: gerundio |
| 472 | caracteres "*" | caracteres «*» | errata: comillas |
| 533 | Ej.: (dos espacios de ancho cero) iterar | Ej.: iterar | errata: caracteres invisibles |
| 918 | se imprime la instrucción `"Found 10!"` | se imprime el mensaje `"Found 10!"` | términos: es una cadena, no una instrucción |
| 1036 | "`Not all…`" | «`Not all…`» | errata: comillas |
| 1050 | Los puntos destacados de este capítulo incluyen: | Estos son los puntos destacados de este capítulo: | calco: sujeto inanimado «incluyen» |

Glosario: sin propuestas
Dudas: línea 1036 (y original): dice «mayor que 5» cuando el código usa `>= 5`; se conserva por fidelidad. Línea 236: la frase de la respuesta tiene el formato roto también en el original; no se toca.

## Capítulo 06: Funciones

- Secciones revisadas: 6 de 6 (más introducción y resumen).
- Cambios: 7 (naturalidad 3, términos 0, erratas 4, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | "IMG_3037" | «IMG_3037» | comillas rectas en la prosa |
| 57 | print() | `print()` | nombre de Python sin formato de código |
| 179 | promueve la modularidad… promueve la reutilización | favorece… favorece | calco de «promotes» |
| 389 | para mantener la modularidad de que cada función realice una sola tarea | para que cada función realice una sola tarea y se mantenga así la modularidad | calco / frase forzada |
| 1446-1447 | "Anonymous", "" | `"Anonymous"`, `""` | comillas rectas en la prosa (valores literales) |

Glosario: sin propuestas
Dudas: ninguna (la traducción era fiel; los textos en inglés dentro del código y las salidas se dejaron como en el original)

## Capítulo 07: Módulos

- Secciones revisadas: 5 de 5 (más introducción y resumen).
- Cambios: 15 (naturalidad 1, términos 0, erratas 12, fidelidad 0, código 2).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 134 | `rea.cube(5)` | `area.cube(5)` | errata (también en el original) |
| 152-153 | «Area of a basketball court…» | «Área de una cancha de baloncesto…» | código: la salida no coincidía con el código traducido |
| 520-523 | `print(f"Nice to meet you…` etc. | `¡Mucho gusto…`, `¿Dónde vives? `… | código: cadenas mezcladas en inglés y español en el mismo bloque |
| 829 | «deben accederse mediante» | «A la función… se accede mediante» | calco: construcción pasiva con «acceder» |
| 1010 | `calendar.SUNDAY?` | `calendar.SUNDAY`? | errata: signo de cierre dentro del código |
| 9, 221, 635, 639, 650, 945, 958, 975, 1038, 1090 (×12) | comillas rectas "…" en la prosa | « » | errata: comillas del libro |

Glosario: sin propuestas
Dudas: 7.1 y otras líneas con «Ej.: El…» (mayúscula tras «Ej.:») se dejaron igual por ser patrón uniforme del libro; el título «Concepts…» y los textos en inglés de salidas `text` (p. ej. 229-234, 1125-1133) se mantienen porque coinciden con el ejercicio original.

## Capítulo 08: Cadenas

- Secciones revisadas: 8 de 8 (introducción, 8.1 a 8.5 y resumen).
- Cambios: 12 (naturalidad 1, términos 1, erratas 8, fidelidad 2, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 7, 9, 336, 1312 | comillas rectas "…" en la prosa | «…» | errata: comillas ×4 |
| 63 | «el prefijo `"aa"` de longitud 1» | «el prefijo de longitud 1 de `"aa"`, que es `"a"`» | fidelidad: el prefijo de longitud 1 es `"a"` (error del original, hace falta para que cuadre) |
| 594 | `aaa".count("a")` | `"aaa".count("a")` | errata: falta la comilla de apertura |
| 732 | «no existe en la cadena `"ooo"`» | «…`"school"`» | fidelidad: la cadena de la pregunta es `"school"` (error del original) |
| 785 | «incluye especificar reglas… y modificarla… ejemplos de cadenas de formato son…» | «incluye la especificación de reglas… y su modificación… ejemplos son…» | naturalidad: calco |
| 1149 | `002:00` | `002.00` | errata del original: la salida es 002.00 |
| 1180 | `["1", "2', "3"]` | `["1", "2", "3"]` | errata: comillas desparejadas |
| 1218 | `>['This', 'is a', 'test']` | `['This', 'is a', 'test']` | errata: «>» sobrante |
| 1326 | «Empalme de cadenas.» | «Rebanado de cadenas.» | término: glosario (string slicing) |

Glosario: sin propuestas.
Dudas: en la tabla de alineación (líneas 1010-1012) el código y la salida están aplanados en una sola línea, tal como en el original; no lo toqué. Las respuestas de 732 y 1339 dicen «devuelve un ValueError» (el original dice returns); técnicamente se lanza, pero lo dejé.

## Capítulo 09: Listas

- Secciones revisadas: 7 de 7 (introducción, 9.1 a 9.5 y resumen).
- Cambios: 16 (naturalidad 9, términos 0, erratas 6, fidelidad 1, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 92 | «El remove se aplica…» | «La operación remove se aplica…» | calco: sustantivo suelto |
| 143 | «termina en 1 menos que el segundo valor» | «termina una unidad antes del segundo valor» | calco: «1 menos que» |
| 260, 268, 360, 363 (×4) | «# Configurar una lista de…» | «# Crear una lista de…» | calco de «Setup»; solo comentarios, la salida no cambia |
| 691 | «se ejecuta tres iteraciones» | «se ejecuta tres veces» | calco |
| 697 | «el producto de la multiplicación de matrices de las matrices» | «el producto matricial de las matrices» | calco, redundante |
| 914 | «en orden de diccionario» | «según el orden del diccionario» | naturalidad y coherencia con 201 y 419 |
| 7, 9 | "Budget", "Budget and Bills" | «Budget», «Budget and Bills» | comillas rectas en prosa |
| 201 | "bat", "cat", "b", "c" | «bat», «cat», «b», «c» | comillas rectas en prosa |
| 246 | "h", "k" | «h», «k» | comillas rectas en prosa |
| 912, 914 | "A" | «A» | comillas rectas en prosa |
| 943 | «elemento máximo» (en `min(list)`) | «elemento mínimo» | fidelidad: error del original («maximum»), corregido a propósito |

Glosario: sin propuestas.
Dudas: (1) En 761 el original dice que el `for` se escribe «sobre `poem_lines`» (en realidad es sobre `words_list`) y se dice «línea 6»; se mantuvo por fidelidad. (2) El bloque ```text de la línea 285 muestra comillas dobles pero Python imprimiría simples; es igual que el original y no es bloque `salida`, no se tocó. (3) En 879 `'i''` y en 360 `snum_list` son erratas del original dentro de código/opciones; no se tocaron.

## Capítulo 10: Diccionarios

- Secciones revisadas: 5 de 5 (más introducción y resumen).
- Cambios: 6 (naturalidad 0, términos 2, erratas 1, fidelidad 2, código 1).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | "Dictionary" | «Dictionary» | comillas rectas en la prosa |
| 489 | # Salida: | # Imprime: | coherencia con los demás comentarios del bloque (código norun, sin salida afectada) |
| 870 | sus potencias de dos | sus cuadrados | x**2 son cuadrados; «potencias de dos» sería 2^n (el original dice «powers of two») |
| 909 | las potencias de dos de las claves | los cuadrados de las claves | igual que la anterior |
| 958, 975 | el método `dict()` | la función `dict()` | términos: el capítulo la llama función (10.2) |

Glosario: sin propuestas
Dudas: el título «Ejemplo: Formato con plantillas de cadena para solicitudes de inscripción a cursos» (línea 370) es fiel al original, que parece un título copiado por error de otro capítulo; no lo cambié.

## Capítulo 11: Clases

- Secciones revisadas: 5 de 5 (más introducción y resumen).
- Cambios: 7 (naturalidad 0, términos 0, erratas 7, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | "Fresh, bright apples newly picked" | «Fresh, bright apples newly picked» | errata: comillas del libro |
| 188 | `in __init__()` | en `__init__()` | errata: «in» sin traducir dentro del código |
| 208 | `___init___()` | `__init__()` | errata: guiones bajos de más (también en el original) |
| 302 | `order_3.cup_size. order_1.cup_size` | `order_3.cup_size`. `order_1.cup_size` | errata: cierre del código mal colocado |
| 558 | `count'` | `count` | errata: apóstrofo del posesivo inglés dentro del código |
| 568 | `max'` | `max` | errata: ídem |
| 862 | `Account'` | `Account` | errata: ídem |

Glosario: sin propuestas
Dudas: «Ej.:» seguido de minúscula/mayúscula se deja como patrón del libro; `&lt;=` (línea 789) y `<`/`>` sin código en 783/814 se dejan igual que el original; las comillas rectas de los textos en `código` (p. ej. `"Refilled"`) se conservan por ser literales de salida.

## Capítulo 12: Recursión

- Secciones revisadas: 6 de 6 (introducción, 12.1 a 12.5 y resumen).
- Cambios: 3 (naturalidad 2, términos 0, erratas 1, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 9 | "Rings from the Ocean" | «Rings from the Ocean» | comillas rectas en prosa |
| 14 | una poderosa técnica | una potente técnica | calco del inglés (powerful) |
| 882 | incluyen: | son: | calco: «los puntos… incluyen» |

Glosario: sin propuestas
Dudas: ninguna

## Capítulo 13: Herencia

- Secciones revisadas: 5 de 5 (más introducción y resumen).
- Cambios: 36 (naturalidad 2, términos 0, erratas 32, fidelidad 2, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| varias ×18 | `CarryOn'`, `SuperClass'`, `Tax'`, `ContractTaxDE's`, `Rectangle'`, `C'`… | sin apóstrofo | errata: apóstrofo del posesivo inglés dentro del código (133, 181, 272, 324, 352, 393, 427, 499, 504-505, 527, 704, 916, 930, 944, 1007, 1068…) |
| 9 | "Don't stare…" | «Don't stare…» | errata: comillas del libro |
| 242 | `Employee`.`__init__()` | `Employee.__init__()` | errata: cierre del código |
| 499 | `super()`.`__init__(4)` | `super().__init__(4)` | errata: ídem |
| 837 | `B(2`, 0) | `B(2, 0)` | errata: cierre del código (también en el original) |
| 360 | ingredients … ["butter"…] … frosting … "buttercream" | con `código` | errata: identificadores y literales sin formato |
| 432, 505, 513, 683, 760 | self, length y width, side, *, Employee | con `código` | errata: nombres de Python sin formato |
| 873-874 | "unknown", "wood" | «unknown», «wood» | errata: comillas del libro |
| 593/601 | Total tax: $150.00 | Total tax: $150.0 | fidelidad: la salida real del código es 150.0 |
| 865 | hereda `d_attr` | hereda `a_attr` | fidelidad: B hereda de A, así que d_inst hereda a_attr (error también en el original) |
| 352 | se acceden de la misma manera | se accede a ellos de la misma manera | calco: pasiva refleja con sujeto plural |
| 1068 | y es llamado por `process_order()` | y al que llama `process_order()` | calco: pasiva |

Glosario: sin propuestas (la tabla de sinónimos superclase/clase base/clase padre se conserva)
Dudas: la línea 248 dice «línea 13» pero el código tiene 12 líneas (igual en el original, depende del bloque del libro); respuestas con `class VenusFlyTrap(Plant)` sin «:» (1007-1056) y `def calc_tax():` son errores intencionados del original; «Ej.:» se deja como patrón del libro.

## Capítulo 14: Archivos

- Secciones revisadas: 5 de 5 (más introducción y resumen).
- Cambios: 3 (naturalidad 0, términos 0, erratas 2, fidelidad 0, código 1).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 56 | «Se crea el archivo "input.txt".» | «Se crea el archivo «input.txt».» | comillas rectas en la prosa |
| 119 | `# Uso de read()` (segundo bloque) | `# Uso de readlines()` | comentario erróneo (el bloque usa readlines); error ya presente en el original; bloque norun, sin efecto en salidas |
| 725 | `` `1,` `` | `` `1`, `` | puntuación dentro del código |

Glosario: sin propuestas
Dudas: ninguna

## Capítulo 15: Ciencia de datos

- Secciones revisadas: 6 de 6.
- Cambios: 7 (naturalidad 1, términos 0, erratas 6, fidelidad 0, código 0).
- Comprobador: OK

| Línea | Antes | Después | Motivo |
|---|---|---|---|
| 136 | "Archivo > Guardar una copia en Drive" | «Archivo > Guardar una copia en Drive» | comillas rectas en prosa |
| 366 | "pandas", "panel data" | «pandas», «panel data» | comillas rectas en prosa |
| 609 | Ej.: En la expresión … que se pasa | Ej.: en la expresión … que se le pasa | mayúscula tras «Ej.:» y concordancia del pronombre (naturalidad) |
| 673 | "¿Por qué faltan los datos?", … | «¿Por qué faltan los datos?», … | comillas rectas en prosa (×3) |
| 883 | "Box Plot of Random Values" | «Box Plot of Random Values» | comillas rectas en el texto alternativo |

Glosario: sin propuestas.
Dudas: l.440 «Las funciones clave de DataFrame que analizan este código» es un calco torpe pero fiel al original (que ya es ambiguo); no lo toqué. Código de l.688 (`np.NAN`) y l.843 (comilla desigual en `plt.title`) vienen así del original; bloques `norun`/de tabla, no los toqué.

