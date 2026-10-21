# Capítulo 15: Ciencia de datos

<!-- modulo: m00108 -->

## Introducción

![Una persona sentada frente a una laptop con un gráfico en la pantalla.](media/Python_15_00_000.jpg)

*crédito: modificación de la obra de Sebastian Sikora/Flickr, CC BY 2.0*

La **ciencia de datos** brinda la capacidad de obtener conocimiento y tomar decisiones informadas a partir de los datos. La ciencia de datos ayuda a las personas a tomar decisiones en disciplinas tan diversas como la salud, los negocios, la educación, la política, las ciencias ambientales y las ciencias sociales.

Este capítulo busca ofrecer una introducción al campo de la ciencia de datos y al ciclo de vida de la ciencia de datos. Los recursos que se presentan en este capítulo están pensados para guiar a los lectores que usan Python a explorar más a fondo la ciencia de datos.

<!-- modulo: m00109 -->

## 15.1 Introducción a la ciencia de datos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir la ciencia de datos.
- Identificar las diferentes etapas del ciclo de vida de la ciencia de datos.
- Nombrar herramientas y software de ciencia de datos.
- Usar Google Colaboratory para ejecutar código.

### Ciclo de vida de la ciencia de datos

La **ciencia de datos** es un campo multidisciplinario que combina la recopilación, el procesamiento y el análisis de grandes volúmenes de datos para extraer conocimiento e impulsar la toma de decisiones informadas. El **ciclo de vida de la ciencia de datos** es el marco que siguen los científicos de datos para completar un proyecto de ciencia de datos. El ciclo de vida de la ciencia de datos es un proceso iterativo que comienza con la adquisición de datos, seguida de la exploración de datos. La etapa de adquisición de datos puede implicar obtener datos de una fuente o recopilarlos mediante encuestas y otros medios de recolección de datos propios de cada dominio. Durante la etapa de exploración de datos, los científicos de datos se aseguran de que los datos tengan el formato correcto para la etapa de análisis de datos mediante la limpieza de datos, y también pueden visualizarlos para inspeccionarlos con más detalle. Una vez que los datos están limpios, los científicos de datos pueden realizar el análisis de datos, cuyos resultados se comparten con las partes interesadas mediante informes y presentaciones. La etapa de **análisis de datos** consiste en usar los datos para generar conocimiento o crear un modelo predictivo. La ciencia de datos se adopta cada vez más en muchos campos distintos, como la salud, la economía, la educación y las ciencias sociales, por nombrar algunos. La siguiente animación muestra las diferentes etapas del ciclo de vida de la ciencia de datos.

**Video:** [Data science life cycle](https://www.openstax.org/r/data-science-life-cycle)

**Conceptos en práctica: ¿Qué es la ciencia de datos?**

<!-- pregunta: CPL-ch15-m01-p01 -->

1. ¿Cuál es la primera etapa de cualquier ciclo de vida de la ciencia de datos?

   - a) visualización de datos
   - b) limpieza de datos
   - c) adquisición de datos

   <details><summary>Respuesta</summary>

   c) La adquisición de datos es la primera etapa del ciclo de vida de la ciencia de datos. Los datos pueden ser recopilados por el científico de datos o reunidos previamente y entregados al científico de datos.

   </details>

<!-- pregunta: CPL-ch15-m01-p02 -->

2. ¿Cuántas etapas tiene el ciclo de vida de la ciencia de datos?

   - a) 3
   - b) 4
   - c) 5

   <details><summary>Respuesta</summary>

   b) El ciclo de vida de la ciencia de datos tiene cuatro etapas: 1) adquisición de datos, 2) exploración de datos, 3) análisis de datos y 4) elaboración de informes.

   </details>

<!-- pregunta: CPL-ch15-m01-p03 -->

3. ¿Qué hace un científico de datos en la etapa de exploración de datos?

   - a) documentar el conocimiento obtenido y las visualizaciones
   - b) analizar los datos
   - c) limpieza y visualización de datos

   <details><summary>Respuesta</summary>

   c) La etapa de exploración de datos incluye la limpieza y la visualización de datos.

   </details>

### Herramientas de ciencia de datos

En la ciencia de datos se usan comúnmente varias herramientas y programas. Estos son algunos ejemplos.

- Lenguaje de programación Python: Python se usa ampliamente en la ciencia de datos. Cuenta con un gran sistema de bibliotecas diseñadas para el análisis de datos, el aprendizaje automático y la visualización. Algunas bibliotecas populares de Python para la ciencia de datos son NumPy, pandas, Matplotlib, Seaborn y scikit-learn. En este capítulo explorarás algunas de estas bibliotecas.
- Lenguaje de programación R: R se usa comúnmente en la computación estadística y el análisis de datos, y ofrece una amplia variedad de paquetes y bibliotecas adaptados a la manipulación de datos, el modelado estadístico y la visualización.
- Jupyter Notebook/JupyterLab: **Jupyter Notebook** y **JupyterLab** son entornos de computación interactiva basados en la web que admiten varios lenguajes de programación, entre ellos Python y R. Permiten a un programador crear documentos que contienen código, visualizaciones y texto, lo que los hace adecuados para la exploración de datos, el análisis y la elaboración de informes.
- Google Colaboratory: **Google Colaboratory** es un entorno de Jupyter Notebook basado en la nube que permite a un programador escribir, ejecutar y compartir código de Python en línea. En este capítulo usarás Google Colaboratory para practicar los conceptos de ciencia de datos.
- Kaggle Kernels: **Kaggle Kernels** es una plataforma de ciencia de datos en línea que ofrece un entorno colaborativo para crear y ejecutar código. Kaggle Kernels admite Python y R, y ofrece acceso a conjuntos de datos, bibliotecas preinstaladas y recursos computacionales. Kaggle también organiza competencias de ciencia de datos y ofrece una plataforma para compartir y descubrir proyectos de ciencia de datos.
- Excel/Sheets: **Microsoft Excel** y **Google Sheets** son aplicaciones de hojas de cálculo ampliamente usadas que ofrecen capacidades básicas de análisis y visualización de datos. Pueden ayudar a los principiantes a empezar con la manipulación de datos, los cálculos estadísticos básicos y las visualizaciones sencillas.

**Video:** [Google Colaboratory ecosystem](https://www.openstax.org/r/google-colab-eco)

**Conceptos en práctica: Herramientas y software de ciencia de datos**

<!-- pregunta: CPL-ch15-m01-p04 -->

1. Entre Python, R y Java, ¿cuál es el lenguaje más popular en la ciencia de datos?

   - a) Python
   - b) R
   - c) Java

   <details><summary>Respuesta</summary>

   a) Python es el lenguaje de programación más popular en la ciencia de datos.

   </details>

<!-- pregunta: CPL-ch15-m01-p05 -->

2. ¿Cuál de las siguientes es una biblioteca de Python relacionada con la ciencia de datos?

   - a) list
   - b) NumPy
   - c) array

   <details><summary>Respuesta</summary>

   b) NumPy es una biblioteca de Python que se usa en el análisis de datos numéricos.

   </details>

<!-- pregunta: CPL-ch15-m01-p06 -->

3. Google Colaboratory se puede usar para elaborar informes y compartir conocimiento.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   a) Google Colaboratory es un documento de Google que se puede compartir con otras cuentas de Google para ver o editar su contenido.

   </details>

### Práctica de programación con Google

Abre el documento de Google Colaboratory que aparece a continuación. Para abrirlo, debes iniciar sesión en una cuenta de Google, si tienes una, o crear una cuenta de Google. Ejecuta todas las celdas. También puedes intentar crear celdas nuevas o modificar las existentes. Para guardar una copia de tus cambios, ve a «Archivo > Guardar una copia en Drive», y el archivo editado se almacenará en tu propio Google Drive.

[Documento de Google Colaboratory](https://openstax.org/r/100colabdoc)

<!-- modulo: m00110 -->

## 15.2 NumPy

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir la biblioteca NumPy.
- Crear un objeto arreglo de NumPy.
- Elegir las funciones adecuadas de NumPy para procesar arreglos de datos numéricos.

### La biblioteca NumPy

**NumPy** (Numerical Python) es una biblioteca de Python que ofrece soporte para operaciones numéricas eficientes sobre arreglos grandes y multidimensionales, y sirve como un bloque fundamental para el análisis de datos en Python. El alias convencional para importar NumPy es `np`. En otras palabras, NumPy se importa como `import numpy as np`. NumPy implementa el objeto **ndarray**, que permite crear un arreglo multidimensional de tipos de datos homogéneos (columnas con el mismo tipo de datos) y procesar datos de manera eficiente. Un objeto `ndarray` puede tener cualquier número de dimensiones y puede almacenar elementos de varios tipos de datos numéricos. Para crear un objeto `ndarray` de NumPy, se puede usar una de las siguientes opciones:

- Crear un `ndarray` convirtiendo una lista o tupla de Python con la función `np.array()`.
- Usar funciones integradas como `np.zeros()` y `np.ones()` para crear un arreglo de solo 0 o de solo 1, respectivamente.
- Generar un arreglo con números aleatorios usando `np.random.rand(n, m)`, donde `n` y `m` son el número de filas y de columnas, respectivamente.
- Cargar datos desde un archivo. Ej.: `np.genfromtxt('data.csv', delimiter=',')`.

**Video:** [Creating an ndarray object](https://www.openstax.org/r/dictionary-object)

**Conceptos en práctica: La biblioteca NumPy**

<!-- pregunta: CPL-ch15-m02-p01 -->

1. ¿Cuál de las siguientes crea un objeto `ndarray` con una fila y dos columnas?

   - a) `np.array([2, 3])`
   - b) `np.zeros(1, 2)`
   - c) `np.zeros((1, 2))`

   <details><summary>Respuesta</summary>

   c) Para crear una matriz de `m` por `n` con todos los valores en cero, se puede usar `np.zeros((m,n))`.

   </details>

<!-- pregunta: CPL-ch15-m02-p02 -->

2. ¿Cuál de los siguientes es un tipo de datos de NumPy?

   - a) `ndarray`
   - b) `list`
   - c) `array`

   <details><summary>Respuesta</summary>

   a) `ndarray` es un tipo de datos que admite NumPy. Al imprimir el tipo de un objeto `ndarray`, se imprime `<'numpy.ndarray'>`.

   </details>

<!-- pregunta: CPL-ch15-m02-p03 -->

3. ¿Cuál es la ventaja de usar un objeto `ndarray` en comparación con una lista?

   - a) eficiencia computacional
   - b) computación orientada a arreglos
   - c) eficiencia de memoria
   - d) todas las anteriores

   <details><summary>Respuesta</summary>

   d) Los arreglos de NumPy están optimizados para la eficiencia computacional y de memoria, y además ofrecen computación orientada a arreglos.

   </details>

### Operaciones de NumPy

Además del tipo de datos `ndarray`, las operaciones de NumPy ofrecen un rendimiento optimizado para cálculos a gran escala. Las características clave de NumPy son:

- Operaciones matemáticas: NumPy ofrece una variedad de funciones y operaciones matemáticas que se pueden aplicar a arreglos completos o a elementos específicos. Estas operaciones incluyen funciones aritméticas, trigonométricas, exponenciales y logarítmicas.
- Manipulación de arreglos: NumPy ofrece diversas funciones para manipular la forma, el tamaño y la estructura de los arreglos. Entre ellas están cambiar la forma, transponer, concatenar, dividir, y agregar o quitar elementos de los arreglos.
- Operaciones de álgebra lineal: NumPy ofrece un conjunto de funciones de álgebra lineal para operaciones con matrices, como la multiplicación de matrices, la inversión de matrices, los valores propios y los vectores propios.

**Video:** [NumPy array operations](https://www.openstax.org/r/NumPy-operations)

**Conceptos en práctica: Operaciones de NumPy**

<!-- pregunta: CPL-ch15-m02-p04 -->

1. ¿Cuál es la salida del siguiente código?
   
   ```python
   import numpy as np
   
   arr = np.array([[1, 2], [3, 4]])
   out = 2 * arr
   print(out)
   ```

   - a)

     ```python norun
     [[2 4]
     [8 16]]
     ```

   - b)

     ```python norun
     [[2 4]
     [6 8]]
     ```

   - c)

     ```python norun
     [[1 2]
     [3 4]]
     ```

   <details><summary>Respuesta</summary>

   b) `2 * arr` multiplica todos los elementos por 2, con el resultado:
   
   ```python norun
   [[2 4]
   [6 8]]
   ```

   </details>

<!-- pregunta: CPL-ch15-m02-p05 -->

2. ¿Cuál de los siguientes produce un `ndarray` de 2 por 3?

   - a)

     ```python norun
     import numpy as np
     arr = np.array(2, 3)
     ```

   - b)

     ```python
     import numpy as np
     arr = np.array([[1, 2], [1, 2], [1, 2]])
     ```

   - c)

     ```python
     import numpy as np
     arr = np.array([[1, 2], [1, 2], [1, 2]]).T
     ```

   <details><summary>Respuesta</summary>

   c) `np.array([[1, 2], [1, 2], [1, 2]])` crea un `ndarray` de 3 por 2. El operador `T` transpone el arreglo. El operador de transposición toma un arreglo de `m` por `n` y lo convierte en un arreglo de `n` por `m`. El resultado de aplicar el operador de transposición al arreglo dado es un arreglo de 2 por 3.

   </details>

<!-- pregunta: CPL-ch15-m02-p06 -->

3. La función `np.multiply(arr1, arr2)` recibe dos objetos `ndarray`, `arr1` y `arr2`, con las mismas dimensiones, y realiza una multiplicación elemento por elemento. ¿Cuál es la salida del siguiente código?
   
   ```python
   import numpy as np
   
   arr1 = np.array([[1, 2], [3, 4]])
   arr2 = np.array([[1, 0], [0, 1]])
   out = np.multiply(arr1, arr2)
   print(out)
   ```

   - a)

     ```python norun
     [[1 0]
     [0 4]]
     ```

   - b)

     ```python norun
     [[1 2]
     [3 4]]
     ```

   - c)

     ```python norun
     [[2 2]
     [3 5]]
     ```

   <details><summary>Respuesta</summary>

   a) El resultado de la multiplicación elemento por elemento entre `arr1` y `arr2` es:
   
   ```python norun
   [[1 0]
   [0 4]]
   ```

   </details>

**Para saber más**

Consulta la guía del usuario de NumPy para obtener más información sobre la biblioteca NumPy.

- [NumPy User Guide](https://openstax.org/r/100numpyguide)

### Práctica de programación con Google

Usa el documento de Google Colaboratory que aparece a continuación para practicar las funcionalidades de NumPy y extraer conocimiento estadístico de un conjunto de datos.

[Documento de Google Colaboratory](https://openstax.org/r/100numpycolab)

<!-- modulo: m00111 -->

## 15.3 pandas

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir la biblioteca pandas.
- Crear un DataFrame y un objeto Series.
- Elegir las funciones adecuadas de pandas para obtener conocimiento a partir de datos heterogéneos.

### La biblioteca pandas

**pandas** es una biblioteca de Python de código abierto que se usa para la limpieza, el procesamiento y el análisis de datos. pandas ofrece estructuras de datos y herramientas de análisis de datos para analizar datos estructurados de manera eficiente. El nombre «pandas» proviene del término «panel data» (datos de panel), que se refiere a conjuntos de datos estructurados multidimensionales. Las características clave de pandas son:

- Estructura de datos: pandas implementa dos estructuras de datos principales:

  - Series: una **Series** es un arreglo unidimensional con etiquetas.
  - DataFrame: un **DataFrame** es una estructura de datos bidimensional con etiquetas que consta de columnas y filas. Un DataFrame se puede considerar como una estructura de datos similar a una hoja de cálculo, donde cada columna representa una Series. Un DataFrame es una estructura de datos heterogénea en la que cada columna puede tener un tipo de datos distinto.
- Funcionalidad de procesamiento de datos: pandas ofrece diversas funcionalidades para el procesamiento de datos, como la selección, el filtrado, el rebanado, el ordenamiento, la combinación, la unión y la reestructuración de datos.
- Integración con otras bibliotecas: pandas se integra bien con otras bibliotecas de Python, como NumPy. Esta capacidad de integración permite el intercambio de datos entre distintas herramientas de análisis y visualización de datos.

El alias convencional para importar pandas es `pd`. En otras palabras, pandas se importa como `import pandas as pd`. A continuación se muestran ejemplos de objetos DataFrame y Series.

| Ejemplo de DataFrame | Ejemplo de Series |
|---|---|
| \|  \| Name \| Age \| City \|<br>\|---\|---\|---\|---\|<br>\| 0 \| Emma \| 15 \| Dubai \|<br>\| 1 \| Gireeja \| 28 \| London \|<br>\| 2 \| Sophia \| 22 \| San Jose \| | \|  \|  \|<br>\|---\|---\|<br>\| 0 \| Emma \|<br>\| 1 \| Gireeja \|<br>\| 2 \| Sophia \|<br>\| dtype: \| object \| |

### Entrada y salida de datos

Un DataFrame se puede crear a partir de un diccionario, una lista, un arreglo de NumPy o un archivo CSV. Los nombres y los tipos de datos de las columnas se pueden especificar al momento de crear el DataFrame.

**Creación de un DataFrame.**

| Descripción | Ejemplo | Salida | Explicación |
|---|---|---|---|
| DataFrame a partir de un diccionario | ```python<br>import pandas as pd<br><br># Crear un diccionario de columnas<br>data = {<br>  "Name": ["Emma", "Gireeja", "Sophia"],<br>  "Age": [15, 28, 22],<br>  "City": ["Dubai", "London", "San Jose"]<br>}<br><br># Crear un DataFrame a partir del diccionario<br>df = pd.DataFrame(data)<br><br># Mostrar el DataFrame<br>df<br>``` | \|  \| Name \| Age \| City \|<br>\|---\|---\|---\|---\|<br>\| 0 \| Emma \| 15 \| Dubai \|<br>\| 1 \| Gireeja \| 28 \| London \|<br>\| 2 \| Sophia \| 22 \| San Jose \| | La función `pd.DataFrame()` recibe un diccionario y lo convierte en un DataFrame. Las claves del diccionario serán las etiquetas de las columnas y los valores se almacenan en las columnas respectivas. |
| DataFrame a partir de una lista | ```python<br>import pandas as pd<br><br># Crear una lista de filas<br>data = [<br>  ["Emma", 15, "Dubai"],<br>  ["Gireeja", 28, "London"],<br>  ["Sophia", 22, "San Jose"]<br>]<br><br># Definir las etiquetas de las columnas<br>columns = ["Name", "Age", "City"]<br><br># Crear un DataFrame a partir de la lista usando las etiquetas de las columnas<br>df = pd.DataFrame(data, columns=columns)<br><br># Mostrar el DataFrame<br>df<br>``` | \|  \| Name \| Age \| City \|<br>\|---\|---\|---\|---\|<br>\| 0 \| Emma \| 15 \| Dubai \|<br>\| 1 \| Gireeja \| 28 \| London \|<br>\| 2 \| Sophia \| 22 \| San Jose \| | La función `pd.DataFrame()` recibe una lista que contiene los registros de las distintas filas de un DataFrame, junto con una lista de etiquetas de columnas, y crea un DataFrame con las filas y las etiquetas de columnas dadas. |
| DataFrame a partir de un arreglo de NumPy | ```python<br>import numpy as np<br>import pandas as pd<br><br># Crear un arreglo de NumPy<br>data = np.array([<br>  [1, 0, 0],<br>  [0, 1, 0],<br>  [2, 3, 4]<br>])<br><br># Definir las etiquetas de las columnas<br>columns = ["A", "B", "C"]<br><br># Crear un DataFrame a partir del arreglo de NumPy<br>df = pd.DataFrame(data, columns=columns)<br><br># Mostrar el DataFrame<br>df<br>``` | \|  \| A \| B \| C \|<br>\|---\|---\|---\|---\|<br>\| 0 \| 1 \| 0 \| 0 \|<br>\| 1 \| 0 \| 1 \| 0 \|<br>\| 2 \| 2 \| 3 \| 4 \| | Un arreglo de NumPy, junto con las etiquetas de las columnas, se pasa a la función `pd.DataFrame()` para crear un objeto DataFrame. |
| DataFrame a partir de un archivo CSV | ```python<br>import pandas as pd<br><br># Leer el archivo CSV en un DataFrame<br>df = pd.read_csv("data.csv")<br><br># Mostrar el DataFrame<br>df<br>``` | El contenido del archivo CSV se imprimirá en formato de tabla. | La función `pd.read_csv()` lee un archivo CSV en un DataFrame y organiza el contenido en formato de tabla. |
| DataFrame a partir de un archivo de Excel | ```python<br>import pandas as pd<br><br># Leer el archivo de Excel en un DataFrame<br>df = pd.read_excel("data.xlsx")<br><br># Mostrar el DataFrame<br>df<br>``` | El contenido del archivo de Excel se imprimirá en formato de tabla. | La función `pd.read_excel()` lee un archivo de Excel en un DataFrame y organiza el contenido en formato de tabla. |

**Conceptos en práctica: Conceptos básicos de pandas**

<!-- pregunta: CPL-ch15-m03-p01 -->

1. ¿Cuál de las siguientes es una estructura de datos de pandas?

   - a) Series
   - b) diccionario
   - c) lista

   <details><summary>Respuesta</summary>

   a) Series es una estructura de datos de pandas que representa datos unidimensionales con etiquetas.

   </details>

<!-- pregunta: CPL-ch15-m03-p02 -->

2. Un objeto DataFrame se puede considerar como una colección de objetos Series.

   - a) verdadero
   - b) falso

   <details><summary>Respuesta</summary>

   a) Un objeto DataFrame se puede considerar una colección de objetos unidimensionales con etiquetas, representados por objetos Series.

   </details>

<!-- pregunta: CPL-ch15-m03-p03 -->

3. ¿Cuáles son las ventajas de pandas sobre NumPy?

   - a) pandas ofrece integración con otras bibliotecas.
   - b) pandas admite datos heterogéneos, mientras que NumPy admite datos numéricos homogéneos.
   - c) pandas admite estructuras de datos tanto unidimensionales como bidimensionales.

   <details><summary>Respuesta</summary>

   b) Un DataFrame de pandas puede almacenar columnas de distintos tipos de datos, mientras que NumPy solo admite tipos de datos numéricos.

   </details>

### pandas para la manipulación y el análisis de datos

La biblioteca pandas ofrece funciones y técnicas para explorar, manipular y obtener conocimiento a partir de los datos. Las funciones clave de DataFrame que analizan este código se describen en la siguiente tabla.

```python
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
days = {
  'Season': ['Summer', 'Summer', 'Fall', 'Winter', 'Fall', 'Winter'],
  'Month': ['July', 'June', 'September', 'January', 'October', 'February'],
  'Month-day': [1, 12, 3, 7, 20, 28],
  'Year': [2000, 1990, 2020, 1998, 2001, 2022]
}
df = pd.DataFrame(days)
```

|  | Season | Month | Month-day | Year |
|---|---|---|---|---|
| 0 | Summer | July | 1 | 2000 |
| 1 | Summer | June | 12 | 1990 |
| 2 | Fall | September | 3 | 2020 |
| 3 | Winter | January | 7 | 1998 |
| 4 | Fall | October | 20 | 2001 |
| 5 | Winter | February | 28 | 2022 |

**Funciones de DataFrame.**

| Nombre de la función | Explicación | Ejemplo | Salida |
|---|---|---|---|
| `head(n)` | Devuelve las primeras `n` filas. Si no se pasa un valor, se mostrarán las primeras 5 filas. | `df.head(4)` | \|  \| Season \| Month \| Month-day \| Year \|<br>\|---\|---\|---\|---\|---\|<br>\| 0 \| Summer \| July \| 1 \| 2000 \|<br>\| 1 \| Summer \| June \| 12 \| 1990 \|<br>\| 2 \| Fall \| September \| 3 \| 2020 \|<br>\| 3 \| Winter \| January \| 7 \| 1998 \| |
| `tail(n)` | Devuelve las últimas `n` filas. Si no se pasa un valor, se mostrarán las últimas 5 filas. | `df.tail(3)` | \|  \| Season \| Month \| Month-day \| Year \|<br>\|---\|---\|---\|---\|---\|<br>\| 3 \| Winter \| January \| 7 \| 1998 \|<br>\| 4 \| Fall \| October \| 20 \| 2001 \|<br>\| 5 \| Winter \| February \| 28 \| 2022 \| |
| `info()` | Proporciona un resumen del DataFrame, que incluye los nombres de las columnas, los tipos de datos y el número de valores no nulos. La función también devuelve el uso de memoria del DataFrame. | `df.info()` | ```python<br><class 'pandas.core.frame.DataFrame'><br>RangeIndex: 6 entries, 0 to 5<br>Data columns (total 4 columns):<br> #    Column        Non-Null Count    Dtype<br>---   ------        --------------    -----<br> 0    Season        6 non-null        object<br> 1    Month         6 non-null        object<br> 2    Month-day     6 non-null        int64<br> 3    Year          6 non-null        int64<br>dtypes: int64(2), object(2)<br>memory usage: 320.0+ bytes<br>``` |
| `describe()` | Genera el conteo de columnas, la media, la desviación estándar, el mínimo, el máximo y los cuartiles. | `df.describe()` | \|  \| Month-day \| Year \|<br>\|---\|---\|---\|<br>\| count \| 6.000000 \| 6.000000 \|<br>\| mean \| 11.833333 \| 2005.166667 \|<br>\| std \| 10.457852 \| 12.875040 \|<br>\| min \| 1.000000 \| 1990.000000 \|<br>\| 25% \| 4.000000 \| 1998.500000 \|<br>\| 50% \| 9.500000 \| 2000.500000 \|<br>\| 75% \| 18.000000 \| 2015.250000 \|<br>\| max \| 28.000000 \| 2022.000000 \| |
| `value_counts()` | Cuenta las apariciones de los valores únicos de una columna cuando se pasa una columna como argumento, y las presenta en orden descendente. | `df.value_counts \('Season')` | ```python<br>Season<br>Fall  2<br>Summer  2<br>Winter  2<br>dtype: int64<br>``` |
| `unique()` | Devuelve un arreglo con los valores únicos de una columna cuando se llama sobre una columna. | `df['Season'] \.unique()` | `​​['Summer' 'Fall' 'Winter']` |

**Conceptos en práctica: Operaciones con DataFrame**

<!-- pregunta: CPL-ch15-m03-p04 -->

1. ¿Cuál de las siguientes devuelve las cinco primeras filas de un DataFrame?

   - a) `df.head()`
   - b) `df.head(5)`
   - c) ambas

   <details><summary>Respuesta</summary>

   c) La función `head()` devuelve las primeras filas de un DataFrame. Si no se especifica un argumento, el número predeterminado de filas devueltas es cinco.

   </details>

<!-- pregunta: CPL-ch15-m03-p05 -->

2. ¿Qué hace la función `unique()` en un DataFrame cuando se aplica a una columna?

   - a) devuelve el número de columnas únicas
   - b) devuelve el número de valores únicos de la columna dada
   - c) devuelve los valores únicos de la columna dada

   <details><summary>Respuesta</summary>

   c) La función `unique()`, cuando se aplica a una columna, devuelve los valores únicos (filas) de la columna dada.

   </details>

<!-- pregunta: CPL-ch15-m03-p06 -->

3. ¿Qué función genera información estadística de las columnas con tipos de datos numéricos?

   - a) `describe()`
   - b) `info()`
   - c) `unique()`

   <details><summary>Respuesta</summary>

   a) Cuando la función `describe()` se aplica a un DataFrame, se generan estadísticas de resumen de las columnas numéricas.

   </details>

**Para saber más**

Consulta la guía del usuario de pandas para obtener más información sobre la biblioteca pandas.

- [Pandas User Guide](https://openstax.org/r/100pandaguide)

### Práctica de programación con Google

Usa el documento de Google Colaboratory que aparece a continuación para practicar las funcionalidades de pandas y extraer conocimiento de un conjunto de datos.

[Documento de Google Colaboratory](https://openstax.org/r/100googlecolab)

<!-- modulo: m00112 -->

## 15.4 Análisis exploratorio de datos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Describir el análisis exploratorio de datos.
- Inspeccionar las entradas de un DataFrame mediante una indexación adecuada.
- Usar el filtrado y el rebanado para obtener un subconjunto de un DataFrame.
- Identificar los valores `Null` en un DataFrame.
- Eliminar o reemplazar los valores `Null` en un DataFrame.

### Análisis exploratorio de datos

El **análisis exploratorio de datos (EDA)** es la tarea de analizar datos para obtener conocimiento, identificar patrones y comprender la estructura subyacente de los datos. Durante el EDA, los científicos de datos examinan los datos de forma visual y estadística para descubrir relaciones, anomalías y tendencias, y para generar hipótesis para análisis posteriores. El objetivo principal del EDA es familiarizarse con los datos y evaluar su calidad. Una vez que los datos se comprenden y se limpian, los científicos de datos pueden realizar la creación de características y la formulación de hipótesis. Una **característica** (feature) es una variable o atributo individual que se calcula a partir de los datos sin procesar del conjunto de datos.

La **indexación de datos** se puede usar para seleccionar y acceder a filas y columnas específicas. La indexación de datos es esencial para examinar un conjunto de datos. En pandas existen dos tipos de métodos de indexación:

- Indexación basada en etiquetas con `loc[]`: **loc[]** permite acceder a los datos de un DataFrame mediante etiquetas de filas y columnas. Ej.: `df.loc[row_label, column_label]` devuelve los datos específicos en la intersección de `row_label` y `column_label`.
- Indexación basada en enteros con `iloc[]`: **iloc[]** permite acceder a los datos de un DataFrame mediante índices enteros. Se pueden pasar índices enteros para recuperar datos específicos. Ej.: `df.iloc[row_index, column_index]` devuelve los datos específicos en el índice `row_index` y `column_index`.

**Video:** [Indexing a DataFrame](https://www.openstax.org/r/indexing-DataFrame)

**Conceptos en práctica: Indexación de un DataFrame**

<!-- pregunta: CPL-ch15-m04-p01 -->

1. ¿Cuál es la salida de `print(df.iloc[0, 0])`?

   - a) `a`
   - b) `b`
   - c) `IndexError`

   <details><summary>Respuesta</summary>

   a) El elemento de la primera fila y la primera columna es `a`.

   </details>

<!-- pregunta: CPL-ch15-m04-p02 -->

2. ¿Cuál es la salida de `print(df.iloc[1, 1])`?

   - a) `a`
   - b) `b`
   - c) `20`

   <details><summary>Respuesta</summary>

   c) El elemento de la segunda fila y la segunda columna es `20`.

   </details>

<!-- pregunta: CPL-ch15-m04-p03 -->

3. ¿Cuál es la salida de `print(df.loc[2, 'A'])`?

   - a) `c`
   - b) `C`
   - c) `b`

   <details><summary>Respuesta</summary>

   a) El elemento en la etiqueta de fila `2` y la etiqueta de columna `A` es `c`.

   </details>

### Rebanado y filtrado de datos

El rebanado y el filtrado de datos consisten en seleccionar subconjuntos específicos de datos según ciertas condiciones o rangos de índices o etiquetas. El **rebanado de datos** se refiere a seleccionar un subconjunto de filas y/o columnas de un DataFrame. El rebanado se puede realizar mediante rangos, listas o condiciones booleanas.

- Rebanado mediante rangos: Ej.: `df.loc[start_row:end_row, start_column:end_column]` selecciona las filas y columnas dentro de los rangos especificados.
- Rebanado mediante una lista: Ej.: `df.loc[[label1, label2, ...], :]` selecciona las filas que están en la lista `[label1, label2, ...]` e incluye todas las columnas, ya que el operador dos puntos selecciona todas las columnas.
- Rebanado basado en una condición: `df[condition]` selecciona solo las filas que cumplen la `condition` dada.

El **filtrado de datos** consiste en seleccionar filas o columnas según ciertas condiciones. Ej.: en la expresión `df[df['column_name'] > threshold]`, el DataFrame `df` se filtra mediante el operador de selección (`[]`) y la condición (`df['column_name'] > threshold`) que se le pasa. Se devolverán todas las entradas del DataFrame `df` en las que el valor correspondiente del DataFrame sea `True`.

**Video:** [Indexing on a flight dataset](https://www.openstax.org/r/indexing-flight-dataset)

**Conceptos en práctica: Rebanado y filtrado de un DataFrame**

<!-- pregunta: CPL-ch15-m04-p04 -->

1. ¿Cuál de las siguientes devuelve las tres primeras filas de la columna A?

   - a) `df.loc[1:3, "A"]`
   - b) `df.loc[0:2, "A"]`
   - c) `df.loc[0:3, "A"]`

   <details><summary>Respuesta</summary>

   b) `df.loc[0:2, "A"]` devuelve las filas de la 0 a la 2 (inclusive) de la columna A.

   </details>

<!-- pregunta: CPL-ch15-m04-p05 -->

2. ¿Cuál de las siguientes devuelve la segunda fila?

   - a) `df.iloc[2]`
   - b) `df[2]`
   - c) `df.loc[1]`

   <details><summary>Respuesta</summary>

   c) `loc[1]` devuelve la fila con la etiqueta `1`, que corresponde a la segunda fila del DataFrame.

   </details>

<!-- pregunta: CPL-ch15-m04-p06 -->

3. ¿Cuál de las siguientes devuelve la primera columna?

   - a) `df.loc[0, :]`
   - b) `df.iloc[:, 0]`
   - c) `df.loc["A"]`

   <details><summary>Respuesta</summary>

   b) `iloc[:, 0]` selecciona todas las filas correspondientes al índice de columna 0, lo que equivale a devolver la primera columna.

   </details>

<!-- pregunta: CPL-ch15-m04-p07 -->

4. ¿Cuál de las siguientes selecciona la segunda y la cuarta fila del DataFrame?

   - a) `df[df.loc[:, "A"] % 2 == 0]`
   - b) `df[df[:, "A"] % 2 == 0]`
   - c) `df[df.loc["A"] % 2 == 0]`

   <details><summary>Respuesta</summary>

   a) La condición devuelve todas las filas en las que el valor de la columna con etiqueta A es divisible entre 2.

   </details>

### Manejo de datos faltantes

Pueden aparecer valores faltantes en un conjunto de datos cuando los datos no están disponibles o no se registraron correctamente. Identificar y eliminar los valores faltantes es un paso importante de la limpieza y el preprocesamiento de datos. Un científico de datos debe tener en cuenta las consideraciones éticas durante todo el proceso de EDA, especialmente al manejar datos faltantes. Puede plantearse preguntas como «¿Por qué faltan los datos?», «¿De quién son los datos que faltan?» y «Considerando los datos faltantes, ¿sigue siendo el conjunto de datos una muestra representativa de la población en estudio?». Las siguientes funciones son útiles para comprender y analizar los datos faltantes.

- `isnull()`: la función `isnull()` se puede usar para identificar las entradas Null de un DataFrame. El valor de retorno de la función es un DataFrame booleano, con las mismas dimensiones que el DataFrame original, con valores `True` donde existen valores faltantes.
- `dropna()`: la función `dropna()` se puede usar para eliminar las filas con valores `Null`.
- `fillna()`: la función `fillna()` se puede usar para reemplazar los valores `Null` por un valor sustituto dado. Ej.: `df.fillna(df.mean())` reemplaza todos los valores `Null` por el valor promedio de la columna correspondiente.

Para definir un valor `Null` en un DataFrame, puedes usar el valor `np.nan` de la biblioteca NumPy. Las funciones que ayudan a identificar y eliminar entradas nulas se describen en la tabla que sigue al código.

```python norun
import pandas as pd
import numpy as np

# Crear datos de ejemplo
data = {
  "Column 1": ["A", "B", "C", "D", "E"],
  "Column 2": [np.NAN, 200, 500, 0, -10],
  "Column 3": [True, True, False, np.NaN, np.NaN]
}

df = pd.DataFrame(data)
```

|  | Column 1 | Column 2 | Column 3 |
|---|---|---|---|
| 0 | A | NaN | True |
| 1 | B | 200.0 | True |
| 2 | C | 500.0 | False |
| 3 | D | 0.0 | NaN |
| 4 | E | -10.0 | NaN |

**Ejemplos de identificación y eliminación de valores nulos.**

| Función | Ejemplo | Salida | Explicación |
|---|---|---|---|
| `isnull()` | ` df.isnull() ` | \|  \| Column 1 \| Column 2 \| Column 3 \|<br>\|---\|---\|---\|---\|<br>\| 0 \| False \| True \| False \|<br>\| 1 \| False \| False \| False \|<br>\| 2 \| False \| False \| False \|<br>\| 3 \| False \| False \| True \|<br>\| 4 \| False \| False \| True \| | La función `df.isnull()` devuelve un arreglo booleano con valores booleanos que indican si cada entrada es `Null`. |
| `fillna()` | ```python<br>df["Column 2"] =\<br>df["Column 2"].fillna(df["Column 2"]<br>  .mean())<br>``` | \|  \| Column 1 \| Column 2 \| Column 3 \|<br>\|---\|---\|---\|---\|<br>\| 0 \| A \| 172.5 \| True \|<br>\| 1 \| B \| 200.0 \| True \|<br>\| 2 \| C \| 500.0 \| False \|<br>\| 3 \| D \| 0.0 \| NaN \|<br>\| 4 \| E \| -10.0 \| NaN \| | Los valores `Null` de `Column 2` se reemplazan por la media de los valores no `Null` de la columna. |
| `dropna()` | ```python<br># Se aplica después de ejecutar<br># la fila anterior<br>df = df.dropna()<br>``` | \|  \| Column 1 \| Column 2 \| Column 3 \|<br>\|---\|---\|---\|---\|<br>\| 0 \| A \| 172.5 \| True \|<br>\| 1 \| B \| 200.0 \| True \|<br>\| 2 \| C \| 500.0 \| False \| | Se eliminan del DataFrame todas las filas que contienen un valor `Null`. |

**Conceptos en práctica: Tratamiento de valores faltantes**

<!-- pregunta: CPL-ch15-m04-p08 -->

1. ¿Cuál de las siguientes se usa para comprobar si un DataFrame tiene valores `Null`?

   - a) `isnan()`
   - b) `isnull()`
   - c) `isnone()`

   <details><summary>Respuesta</summary>

   b) `isnull()` devuelve un DataFrame booleano que indica si las entradas de datos son `Null` o no.

   </details>

<!-- pregunta: CPL-ch15-m04-p09 -->

2. Suponiendo que se tiene un DataFrame `df`, ¿cuál de las siguientes reemplaza los valores `Null` por ceros?

   - a) `df.fillna(0)`
   - b) `df.replacena(0)`
   - c) `df.fill(0)`

   <details><summary>Respuesta</summary>

   a) `fillna()` reemplaza todos los valores `Null` por el valor dado como argumento.

   </details>

<!-- pregunta: CPL-ch15-m04-p10 -->

3. Suponiendo que se tiene un DataFrame `df`, ¿qué hace la expresión `df.isnull().sum()`?

   - a) Calcula la suma de los valores no `Null` de cada columna
   - b) Calcula el número de valores `Null` del DataFrame
   - c) Calcula el número de valores `Null` de cada columna

   <details><summary>Respuesta</summary>

   c) La función `sum()` se aplica a cada columna por separado y suma los valores de las columnas. El resultado es el número de valores `Null` de cada columna.

   </details>

### Práctica de programación con Google

Usa el documento de Google Colaboratory que aparece a continuación para practicar el EDA con un conjunto de datos dado.

[Documento de Google Colaboratory](https://openstax.org/r/100edapractice)

<!-- modulo: m00113 -->

## 15.5 Visualización de datos

### Objetivos de aprendizaje

Al terminar esta sección, deberías poder:

- Explicar por qué la visualización tiene un papel importante en la ciencia de datos.
- Elegir la visualización adecuada para una tarea dada.
- Usar bibliotecas de visualización de Python para crear visualizaciones de datos.

### ¿Por qué visualizar?

La visualización de datos tiene un papel crucial en la ciencia de datos para comprender los datos. La visualización de datos se puede usar en todas las etapas del ciclo de vida de la ciencia de datos para facilitar la exploración de datos, identificar anomalías, comprender relaciones y tendencias, y elaborar informes. Se usan comúnmente varios tipos de visualización:

**Tipos de visualización comunes.**

| Tipo de visualización | Descripción | Ventajas/uso común |
|---|---|---|
| Gráfico de barras | Barras rectangulares | Comparar valores entre distintas categorías. |
| Gráfico de líneas | Una serie de puntos de datos conectados por segmentos de línea | Visualizar tendencias y cambios. |
| Gráfico de dispersión | Puntos de datos individuales que representan la relación entre dos variables | Identificar correlaciones, grupos y valores atípicos. |
| Histograma | Barras rectangulares que representan la distribución de una variable continua al dividir el rango de la variable en intervalos y representar la frecuencia o el conteo de los datos dentro de cada intervalo | Resumir la distribución de los datos. |
| Diagrama de caja | Caja rectangular con bigotes que resume la distribución de una variable continua, incluidos la mediana, los cuartiles y los valores atípicos | Resumir la distribución de los datos y comparar diferentes variables. |

**Video:** [Visualization types](https://www.openstax.org/r/visualization-types)

**Conceptos en práctica: Comparación de métodos de visualización**

<!-- pregunta: CPL-ch15-m05-p01 -->

1. ¿Cuál de los siguientes tipos de gráfico es el más adecuado para comparar la distribución de una variable continua?

   - a) gráfico de dispersión
   - b) histograma
   - c) gráfico de líneas

   <details><summary>Respuesta</summary>

   b) Un histograma se usa para graficar la distribución de variables continuas.

   </details>

<!-- pregunta: CPL-ch15-m05-p02 -->

2. ¿Cuál de los siguientes tipos de gráfico es el más adecuado para visualizar los valores atípicos y los cuartiles de una variable continua?

   - a) histograma
   - b) gráfico de barras
   - c) diagrama de caja

   <details><summary>Respuesta</summary>

   c) Un diagrama de caja se usa para mostrar la distribución de una variable continua, además de visualizar los valores atípicos, el mínimo, el máximo y los cuartiles.

   </details>

<!-- pregunta: CPL-ch15-m05-p03 -->

3. ¿Cuál de los siguientes tipos de gráfico es eficaz para mostrar tendencias y cambios a lo largo del tiempo?

   - a) gráfico de líneas
   - b) gráfico de barras
   - c) histograma

   <details><summary>Respuesta</summary>

   a) Un gráfico de líneas se usa para mostrar tendencias y cambios a lo largo del tiempo entre dos variables.

   </details>

### Herramientas de visualización de datos

Existen muchas bibliotecas de visualización de datos de Python que ofrecen una variedad de capacidades y características para crear diferentes tipos de gráficos. Algunos de los marcos más usados son Matplotlib, Plotly y Seaborn. Aquí se resumen algunas funcionalidades útiles de `Matplotlib`.

**Funcionalidades de Matplotlib.**

| Tipo de gráfico | Método |
|---|---|
| Gráfico de barras | La función `plt.bar(x, height)` recibe dos entradas, `x` y `height`, y grafica barras para cada valor de `x` con la altura dada en la variable `height`. |
| **Ejemplo** | **Salida** |
| ```python<br>import matplotlib.pyplot as plt<br><br># Datos<br>categories = ["Course A", "Course B", "Course C"]<br>values = [25, 40, 30]<br><br># Crear el gráfico de barras<br>fig = plt.bar(categories, values)<br><br># Personalizar el gráfico<br>plt.title("Number of students in each course')<br>plt.xlabel("Courses")<br>plt.ylabel("Number of students")<br><br># Mostrar el gráfico<br>plt.show()<br>``` | ![Ejemplo de gráfico de barras](media/Python_15_05_003.jpg) |

*Gráfico de barras.*

**Funcionalidades de Matplotlib.**

| Tipo de gráfico | Método |
|---|---|
| Gráfico de líneas | La función `plt.plot(x, y)` recibe dos entradas, `x` y `y`, y grafica líneas que conectan pares de valores `(x, y)`. |
| **Ejemplo** | **Salida** |
| ```python<br>import matplotlib.pyplot as plt<br><br># Datos<br>month = ["Jan", "Feb", "Mar", "Apr", "May"]<br>inflation = [6.41, 6.04, 4.99, 4.93, 4.05]<br><br># Crear el gráfico de líneas<br>plt.plot(month, inflation, marker="o",<br>linestyle="-", color="blue")<br><br># Personalizar el gráfico<br>plt.title("Inflation trend in 2023")<br>plt.xlabel("Month")<br>plt.ylabel("Inflation")<br><br># Mostrar el gráfico<br>plt.show()<br>``` | ![Ejemplo de gráfico de líneas](media/Python_15_05_002.jpg) |

*Gráfico de líneas.*

**Funcionalidades de Matplotlib.**

| Tipo de gráfico | Método |
|---|---|
| Gráfico de dispersión | La función `plt.scatter(x, y)` recibe dos entradas, `x` y `y`, y grafica puntos que representan pares `(x, y)`. |
| **Ejemplo** | **Salida** |
| ```python<br>import matplotlib.pyplot as plt<br><br># Datos<br>x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>y = [10, 8, 6, 4, 2, 5, 7, 9, 3, 1]<br><br># Crear el gráfico de dispersión<br>plt.scatter(x, y, marker="o", color="blue")<br><br># Personalizar el gráfico<br>plt.title("Scatter Plot Example")<br>plt.xlabel("X")<br>plt.ylabel("Y")<br><br># Mostrar el gráfico<br>plt.show()<br>``` | ![Ejemplo de gráfico de dispersión](media/Python_15_05_005.jpg) |

*Gráfico de dispersión.*

**Funcionalidades de Matplotlib.**

| Tipo de gráfico | Método |
|---|---|
| Histograma | La función `plt.hist(x)` recibe una entrada, `x`, y grafica un histograma de los valores de `x` para mostrar la distribución o la tendencia. |
| **Ejemplo** | **Salida** |
| ```python<br>import matplotlib.pyplot as plt<br>import numpy as np<br><br># Datos: 1000 muestras aleatorias<br>data = np.random.randn(1000)<br><br># Crear el histograma<br>plt.hist(data, bins=30, edgecolor="black")<br><br># Personalizar el gráfico<br>plt.title("Histogram of random values")<br>plt.xlabel("Values")<br>plt.ylabel("Frequency")<br><br># Mostrar el gráfico<br>plt.show()<br>``` | ![Ejemplo de histograma](media/Python_15_05_001.jpg) |

*Histograma.*

**Funcionalidades de Matplotlib.**

| Tipo de gráfico | Método |
|---|---|
| Diagrama de caja | La función `plt.boxplot(x)` recibe una entrada, `x`, y representa el mínimo, el máximo y el primer, segundo y tercer cuartiles, así como los valores atípicos de `x`. |
| **Ejemplo** | **Salida** |
| ```python<br>import matplotlib.pyplot as plt<br>import numpy as np<br><br># Datos: 100 muestras aleatorias<br>data = [np.random.normal(0, 5, 100)]<br><br># Crear el diagrama de caja<br>plt.boxplot(data)<br><br># Personalizar el gráfico<br>plt.title("Box Plot of random values")<br>plt.xlabel("Data Distribution")<br>plt.ylabel("Values")<br><br># Mostrar el gráfico<br>plt.show()<br>``` | ![Un diagrama de caja titulado «Box Plot of Random Values» ilustra la distribución de los datos. La mediana está cerca de -1, la caja abarca valores de -4 a 2, los bigotes se extienden de -12 a 7 y se ven dos valores atípicos por encima de 10.](media/Python_15_05_004.jpg) |

*Diagrama de caja.*

**Conceptos en práctica: Métodos de Matplotlib**

<!-- pregunta: CPL-ch15-m05-p04 -->

1. Dado el siguiente código, ¿cuál de las llamadas a función es adecuada para mostrar la asociación entre `x` y `y`?
   
   ```python
   import matplotlib.pyplot as plt
   
   # Datos
   x = [1, 2, 3, 4, 5]
   y = [10, 15, 12, 18, 20]
   ```

   - a) `plt.boxplot(x)`
   - b) `plt.hist(y)`
   - c) `plt.scatter(x, y)`

   <details><summary>Respuesta</summary>

   c) La llamada a la función `plt.scatter(x, y)` crea un gráfico de dispersión a partir de los datos almacenados en las variables `x` y `y`.

   </details>

<!-- pregunta: CPL-ch15-m05-p05 -->

2. ¿Qué se grafica con el siguiente código?
   
   ```python
   import matplotlib.pyplot as plt
   
   # Datos
   categories = ['A', 'B', 'C', 'D']
   values = [10, 15, 12, 18]
   plt.bar(categories, values)
   ```

   - a) un histograma
   - b) un gráfico de barras
   - c) un gráfico de líneas

   <details><summary>Respuesta</summary>

   b) El código dado grafica un gráfico de barras con cuatro barras que representan las categorías dadas. La altura de las barras corresponde a los valores almacenados en la variable `values`.

   </details>

<!-- pregunta: CPL-ch15-m05-p06 -->

3. ¿Qué biblioteca de Python se usa más comúnmente para crear visualizaciones interactivas?

   - a) Matplotlib
   - b) Plotly
   - c) pandas

   <details><summary>Respuesta</summary>

   b) Plotly es una biblioteca que crea visualizaciones interactivas.

   </details>

**Para saber más**

Consulta las siguientes guías del usuario para obtener más información sobre las bibliotecas Matplotlib, Plotly y Seaborn.

- [Matplotlib User Guide](https://openstax.org/r/100matplotguide)
- [Plotly User Guide](https://openstax.org/r/100plotlyguide)
- [Seaborn User Guide](https://openstax.org/r/100seabornguide)

### Práctica de programación con Google

Usa el documento de Google Colaboratory que aparece a continuación para practicar una tarea de visualización con un conjunto de datos dado.

[Documento de Google Colaboratory](https://openstax.org/r/100visualization)

<!-- modulo: m00115 -->

## 15.6 Resumen del capítulo

Los puntos principales de este capítulo son:

- La ciencia de datos es un campo multidisciplinario que combina la recopilación, el procesamiento y el análisis de grandes volúmenes de datos para extraer conocimiento e impulsar la toma de decisiones informadas.
- El ciclo de vida de la ciencia de datos es el marco que siguen los científicos de datos para completar un proyecto de ciencia de datos.
- El ciclo de vida de la ciencia de datos incluye 1) adquisición de datos, 2) exploración de datos, 3) análisis de datos y 4) elaboración de informes.
- Google Colaboratory es un entorno de Jupyter Notebook basado en la nube que permite a los programadores escribir, ejecutar y compartir código de Python en línea.
- NumPy (Numerical Python) es una biblioteca de Python que ofrece soporte para operaciones numéricas eficientes sobre arreglos grandes y multidimensionales, y sirve como un bloque fundamental para el análisis de datos en Python.
- NumPy implementa un objeto `ndarray` que permite crear arreglos multidimensionales de tipos de datos homogéneos y procesar datos de manera eficiente.
- NumPy ofrece funcionalidades para operaciones matemáticas, manipulación de arreglos y operaciones de álgebra lineal.
- pandas es una biblioteca de Python de código abierto que se usa para la limpieza, el procesamiento y el análisis de datos.
- pandas ofrece las estructuras de datos Series y DataFrame, funcionalidad de procesamiento de datos e integración con otras bibliotecas.
- El análisis exploratorio de datos (EDA) es la tarea de analizar datos para obtener conocimiento, identificar patrones y comprender la estructura subyacente de los datos.
- Una característica es una variable o atributo individual que se calcula a partir de los datos sin procesar de un conjunto de datos.
- La indexación de datos se puede usar para seleccionar y acceder a filas y columnas específicas.
- El rebanado de datos se refiere a seleccionar un subconjunto de filas y/o columnas de un DataFrame.
- El filtrado de datos consiste en seleccionar filas o columnas según ciertas condiciones.
- Pueden aparecer valores faltantes en un conjunto de datos cuando los datos no están disponibles o no se registraron correctamente.
- La visualización de datos tiene un papel crucial en la ciencia de datos para comprender los datos.
- Los diferentes tipos de visualización incluyen el gráfico de barras, el gráfico de líneas, el gráfico de dispersión, el histograma y el diagrama de caja.
- Existen varias bibliotecas de visualización de datos de Python que ofrecen una variedad de capacidades y características para crear diferentes tipos de gráficos. Estas bibliotecas incluyen Matplotlib, Seaborn y Plotly.
- Los alias convencionales para importar NumPy, pandas y Matplotlib.pyplot son `np`, `pd` y `plt`, respectivamente.

A estas alturas, deberías poder escribir programas que creen estructuras de datos para almacenar distintos conjuntos de datos, y explorar y visualizar conjuntos de datos.

**Referencia del capítulo 15.**

| Función | Descripción |
|---|---|
| `np.array()` | Crea un `ndarray` a partir de una lista o tupla. |
| `np.zeros()` | Crea un arreglo de ceros. |
| `np.ones()` | Crea un arreglo de unos. |
| `np.random.rand(n, m)` | Crea un arreglo de números aleatorios con `n` filas y `m` columnas |
| `np.genfromtxt('data.csv', delimiter=',')` | Crea un arreglo a partir de un archivo CSV. |
| `pd.DataFrame()` | Crea un DataFrame a partir de una lista, un diccionario o un arreglo. |
| `pd.read_csv()` | Crea un DataFrame a partir de un archivo CSV. |
| `df.head()` | Devuelve las primeras filas de un DataFrame. |
| `df.tail()` | Devuelve las últimas filas de un DataFrame. |
| `df.info()` | Proporciona un resumen del DataFrame, que incluye los nombres de las columnas, los tipos de datos y el número de valores no `Null`. |
| `df.describe()` | Genera el conteo de columnas, la media, la desviación estándar, el mínimo, el máximo y los cuartiles. |
| `df.value_counts()` | Cuenta las apariciones de los valores únicos de una columna y las presenta en orden descendente. |
| `df.unique()` | Devuelve un arreglo con los valores únicos de una columna. |
| `loc[]` | Permite acceder a los datos de un DataFrame mediante etiquetas de filas y columnas. |
| `iloc[]` | Permite acceder a los datos de un DataFrame mediante índices enteros de filas y columnas. |
| `df[condition]` | Selecciona solo las filas que cumplen la `condition` dada. |
| `df.loc[start_row:end_row, start_column:end_column]` | Rebana mediante rangos de etiquetas. |
| `df.loc[[label1, label2, ...], :]` | Rebana las filas que están en la lista `[label1, label2, ...]`. |
| `df.isnull()` | Devuelve un arreglo booleano con valores booleanos que indican si cada entrada ha sido `Null`. |
| `fillna()` | Reemplaza los valores `Null`. |
| `dropna()` | Elimina todas las filas que contienen un valor `Null`. |
| `plt.bar(x, height)` | Recibe dos entradas, `x` y `height`, y grafica barras para cada valor de `x` con la altura dada en la variable `height`. |
| `plt.plot(x, y)` | Recibe dos entradas, `x` y `y`, y grafica líneas que conectan pares de valores `(x, y)`. |
| `plt.scatter(x, y)` | Recibe dos entradas, `x` y `y`, y grafica puntos que representan pares `(x, y)`. |
| `plt.hist(x)` | Recibe una entrada, `x`, y grafica un histograma de los valores de `x` para mostrar la distribución o la tendencia. |
| `plt.boxplot(x)` | Recibe una entrada, `x`, y representa el mínimo, el máximo y el primer, segundo y tercer cuartiles, así como los valores atípicos de `x`. |
