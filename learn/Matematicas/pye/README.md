
# Probabilidad y estadística <!-- omit in toc -->

> Mejora de habilidades para el pensamiento

## Tabla de Contenido<!-- omit in toc -->
- [Libros digitales](#libros-digitales)
- [Conceptos](#conceptos)
- [Introducción](#introducción)
  - [Investigación](#investigación)
    - [Propositos](#propositos)
    - [Proceso](#proceso)
    - [Pasos en el proceso de investigación](#pasos-en-el-proceso-de-investigación)
- [Muestra](#muestra)
- [Escalas de medición](#escalas-de-medición)
  - [Variables cualitativas:](#variables-cualitativas)
  - [Variables cuantitativas](#variables-cuantitativas)
  - [Ejemplos](#ejemplos)
- [Estadística descriptiva univariada](#estadística-descriptiva-univariada)
  - [Los tres análisis descriptivos fundamentales](#los-tres-análisis-descriptivos-fundamentales)
    - [Tablas de frecuencias](#tablas-de-frecuencias)
    - [Gráficos](#gráficos)
      - [Pastel](#pastel)
      - [Histograma](#histograma)
      - [Resúmenes numéricos](#resúmenes-numéricos)
        - [Medidas de tendencia central (centralización)](#medidas-de-tendencia-central-centralización)
        - [Medidas de dispersión](#medidas-de-dispersión)
      - [Resumiendo](#resumiendo)
  - [Datos agrupados con frecuencias](#datos-agrupados-con-frecuencias)
    - [Datos agrupados y no agrupados (agregaciones)](#datos-agrupados-y-no-agrupados-agregaciones)
  - [Medidas de posición](#medidas-de-posición)
    - [Los cuartiles (Q)](#los-cuartiles-q)
  - [Los deciles](#los-deciles)
  - [Los percentiles (Pp)](#los-percentiles-pp)
  - [Diagrama de bigotes](#diagrama-de-bigotes)
  - [Asimetría](#asimetría)
    - [Coeficiente de Karl Pearson**](#coeficiente-de-karl-pearson)
    - [Medida de Yule Bowley o medida cuaartílica](#medida-de-yule-bowley-o-medida-cuaartílica)
    - [Medida de fisher](#medida-de-fisher)
  - [Ejercicios](#ejercicios)
- [Estadística bidimensional o bivariada](#estadística-bidimensional-o-bivariada)
  - [Dos variables aleatorias](#dos-variables-aleatorias)
  - [Tabla de doble entrada o tabla de contingencia](#tabla-de-doble-entrada-o-tabla-de-contingencia)
  - [Relación entre dos variables](#relación-entre-dos-variables)
    - [Distribuciones bidimensionales](#distribuciones-bidimensionales)
    - [Regresión líneal](#regresión-líneal)
    - [Medidas de relación entre dos variables](#medidas-de-relación-entre-dos-variables)
  - [Covarianza](#covarianza)
  - [Correlación](#correlación)
    - [Correlación directa o positiva](#correlación-directa-o-positiva)
    - [Correlación inversa o negativa](#correlación-inversa-o-negativa)
    - [Correlación nula](#correlación-nula)
    - [Coeficiente de correlación lineal de pearson](#coeficiente-de-correlación-lineal-de-pearson)
  - [Regresión líneal simple](#regresión-líneal-simple)
    - [Coeficiente de determinación](#coeficiente-de-determinación)
  - [Ejercicios y explicaciones](#ejercicios-y-explicaciones)
- [Probabilidades](#probabilidades)
  - [Evento o suceso aleatorio](#evento-o-suceso-aleatorio)
  - [Leyes de Morgan](#leyes-de-morgan)
  - [Probabilidad](#probabilidad)
    - [Enfoques / Interpretaciones](#enfoques--interpretaciones)
      - [Probabilidad clásica (regla de laplace)](#probabilidad-clásica-regla-de-laplace)
      - [Enfoque frecuentista](#enfoque-frecuentista)
      - [Probabilidad subjetiva](#probabilidad-subjetiva)
    - [Axiomas (Requisito que tiene que cumplir cierta función para ser una probabilidad)](#axiomas-requisito-que-tiene-que-cumplir-cierta-función-para-ser-una-probabilidad)
    - [Consecuencias de los axiomas](#consecuencias-de-los-axiomas)
    - [Ejemplo del dado](#ejemplo-del-dado)
  - [Probabilidad condicionada](#probabilidad-condicionada)
    - [Ejemplo](#ejemplo)
  - [Sucesos independientes](#sucesos-independientes)
  - [Teorema de la probabilidad total](#teorema-de-la-probabilidad-total)
    - [Ejemplo](#ejemplo-1)
    - [Teorema de bayes](#teorema-de-bayes)
      - [Ejemplo](#ejemplo-2)
  - [Ejercicios](#ejercicios-1)
- [Distribuciones](#distribuciones)
  - [Distribución de probabilidad](#distribución-de-probabilidad)
  - [Distribuciones de variable discreta](#distribuciones-de-variable-discreta)
  - [Distribuciones de variable continua](#distribuciones-de-variable-continua)
  - [Histogramas](#histogramas)
  - [Función de Masa de Probabilidad](#función-de-masa-de-probabilidad)
  - [Función de distribución acumulada](#función-de-distribución-acumulada)
  - [Función de Densidad de Probabilidad](#función-de-densidad-de-probabilidad)
  - [Principales distribuciones](#principales-distribuciones)
    - [Variable aleatoria discreta](#variable-aleatoria-discreta)
    - [Función de probabilidad (suma=1)](#función-de-probabilidad-suma1)
    - [Función de distribución](#función-de-distribución)
    - [Media y varianza con la función de probabilidad](#media-y-varianza-con-la-función-de-probabilidad)
  - [Distribución para variables aleatorias continuas](#distribución-para-variables-aleatorias-continuas)
    - [Distribución de Binomial y Bernoulli](#distribución-de-binomial-y-bernoulli)
  - [Distribución de POISSON](#distribución-de-poisson)
    - [Ejemplo](#ejemplo-3)

# Libros digitales

https://joanby.github.io/bookdown-probabilidad/

https://joanby.github.io/bookdown-estadistica-inferencial/

https://www.odiolaestadistica.com/estadistica-python/

**Contenido complementario**

[DataScience](../pye/DataScience.pdf)

[Series temporales](../pye/SeriesTemporales.pdf)

# Conceptos

* **Valor aleatorio** - Valores que cambian en un rango determinado
* **Valor deterministico** - Asume un valor puntual

# Introducción

> La estadística está muy **involucrada en la toma de decisiones**

* Pensamiento inteligente
* Aprendizaje práctico
* Observaciones con sentido

> Es un conjunto de procedimientos para **reunir, medir, codificar, computar, analizar y resumir información númerica adquirida sistemáticamente.**

Su fuente principal son los **datos**, siguiendo los procedimientos científicos. Recolectar datos tiene diferentes propositos:

* **Estadística descriptiva** - Datos sobre categorías, personas u objetos y resumir la información en pocas cifras, matemáticas exactas, tablas y gráficas. 
* **Estadística inferencial** - Observaciones registradas y que tan frecuente ocurrieron en los datos de cada observación. Extraer conclusiones sobre las relaciones matemáticas, relaciones causa-efecto, prueba de hipótesis y teorias, entre las características de un grupo de personas u objetos.

## Investigación
Proceso que sigue una serie de pasos utilizando herramientas en situaciones de nuestra vida cotidiana.

* Rigurosa
* Organizada
* Sistemática
* Empírica
* Crítica

### Propositos
* Producir conocimientos
* Resolver problemas prácticos

### Proceso
* Organizar ideas
* Hacer predicciones
* Reunir datos

### Pasos en el proceso de investigación
* Específicar la(s) pregunta(s)
  * ¿Cuáles son las variables? (dependiente e independientes)
  * ¿Cuáles son las causas y los efectos?
  * ¿Qué se quiere resolver?
  * ¿Por qué sucede algo?
  * ¿Cuál es la influencia?
* Revisar la literatura
* Proponer una teoría y formular una hipótesis
  * Indicadores, métricas y parámetros
* Seleccionar un diseño de investigación
  * Tipo, nivel y diseño
* Recolectar los datos
  * Ir a los hechos
  * Aplicar métodos de extracción
  * Utilizar herramientas
* Análizar los datos y sacar herramientas
* Difundir los resultados
  * Defender tu investigación
  * Aprobar o rechazar hipotesis

# Muestra

Todo subconjunto de la población es una muestra, está tiene qu ser

* **Aleatoria** - Todos los elementos deben tener la misma probabilidad de ser elegidos
* **Representativa**

<div align="center">
  <img src="img/muestra-estadistica.jpg">
</div>

**Variable aleatoria**

* Es una característica de la población
* Sigue un determinado comportamiento **"Distribución"**
  * **Discreta** - valores enteros, contables, númerables, opciones finitas (Ciudades)
  * **Continua** - númericos Valores reales (peso), altura

Ejemplo

<div align="center">
  <img src="img/1.png">
</div>

* Nos interesa una característica, que va a ser la **variable aleatoria**
  * Puede ser discreta o continua
* Se mide la característica en una población, pero es demasiado grande, se toma una muestra representativa de esa característica en la pobleción
* Obtenemos información de esa población

#  Escalas de medición

Existen cuatro escalas, organizadas de la que brinda menos información a la que brinda más información:

## Variables cualitativas:
* **Nominal:** Ocurre cuando sólo podemos decir que **dos valores son distintos.** Usualmente son **categorías** o **identificadores**.
* **Ordinal:** Ocurre cuando podemos decir que **un valor es mayor o menor que otro.** Dicho de otra manera, podemos ordenar o establecer **relaciones de orden entre los valores** de la variable. Sin embargo, no podemos cuantificar la diferencia entre un valor y otro.

<div align="center">
  <img src="img/escalas-de-medicion.jpg">
</div>

## Variables cuantitativas

* **Intervalo:** Tienen lo que se conoce como un cero por convención, o un cero que existe porque se convino que ese valor sea cero pero NO implica ausencia de la variable. Esto hace que tenga sentido calcular la **diferencia o intervalo entre dos valores distintos**, pero no la razón entre valores. Por ejemplo, la **fecha** es una variable medida en escala de intervalo, puesto que tiene sentido calcular la diferencia entre valores, pero no tiene sentido decir, por ejemplo, que una fecha es dos veces más que otra, ya que el cero es una fecha que se estableció por convención y no se puede interpretar como ausencia.
* **Razón:** Utilizamos esta escala cuando la variable cuantitativa tiene un cero absoluto, o cuando el cero significa efectivamente ausencia. Esto implica que sí tiene sentido calcular razones entre valores. Por ejemplo, **si medimos el número de habitantes de un país, si el valor es cero, esto implicaría ausencia de habitantes, y tiene todo el sentido del mundo decir que un país tiene el doble de habitantes que otro.**

## Ejemplos

**Nombre** -	Nominal
**Edad** -	Razón
**Fecha de nacimiento** -	Intervalo
**Estatura** -	Razón
**Peso** -	Razón
**Color de cabello** -	Nominal
**Lugar de nacimiento** -	Nominal
**Número de pasaporte** -	Nominal
**Estrato socioeconómico** -	Ordinal

# Estadística descriptiva univariada

## Los tres análisis descriptivos fundamentales

Tiene como característica resumir, analizar y sacar conclusiones de un conjunto de datos
* Tabla de frecuencias
* Gráficas
* Resumenes númericos

### Tablas de frecuencias

<div align="center">
  <img src="img/2.png">
</div>

<div align="center">
  <img src="img/3.png">
</div>

### Gráficos

#### Pastel
<div align="center">
  <img src="img/4.png">
</div>

#### Histograma
<div align="center">
  <img src="img/5.png">
</div>

<div align="center">
  <img src="img/6.png">
</div>

#### Resúmenes numéricos

##### Medidas de tendencia central (centralización)

Media o promedio
<div align="center">
  <img src="img/7.png">
</div>

<div align="center">
  <img src="img/8.png">
</div>

<div align="center">
  <img src="img/9.png">
</div>

Ejercicios

Calcular la media y la mediana

<div align="center">
  <img src="img/10.png">
</div>

Para la mediana, ordenar los datos de menor a mayor y escoger el del medio

<div align="center">
  <img src="img/11.png">
</div>

##### Medidas de dispersión

Varianza y desviación típica: Cuán alejados están los datos de la media

La varianza es el promedio de las distancias hacia la media

<div align="center">
  <img src="img/12.png">
</div>

La desviación típica es la raíz de la varianza

<div align="center">
  <img src="img/13.png">
</div>

#### Resumiendo

* Las tablas de frecuencias: informaición numérica sobre los datos
* Los gráficos son información visual
* Los resúmenes numéricos: media, mediana, varianza, desviación típica, etc.

[Formulas](../pye/Formulas1.pdf)

## Datos agrupados con frecuencias

Se ha solicitado a un grupo de 50 individuos información sobre el número de horas que dedican diariamente a dormir. La clasificación de las respuestas ha permitido elaborar la siguiente tabla

<div align="center">
  <img src="img/14.png">
</div>

### Datos agrupados y no agrupados (agregaciones)

Es una forma distinta de representar y analizar la información que se ha reunido.

* Los **datos no agrupados** es el conjunto de observaciones que se presentan en su forma original tal y como fueron recolectados, para obtener información directamente de ellos
* Los **datos agrupados** es cuando tenemos los valores o **intervalos de valores** (buckets) que toma la variable y la **frecuencia de ocurrencia**. Es una forma más compacta de ver los datos

Para calcular la media o promedio

<div align="center">
  <img src="img/15.png">
</div>

Para calcular la mediana

La media es el valor central de los datos ordenados. Al ser un valor par 50, la mitad es 25, hay dos valores centrales. Posición 25 y 26 y hay que obtener la media de ellos. Para ello podemos usar la frecuencia absoluta acumulada

<div align="center">
  <img src="img/16.png">
</div>

Para la moda

Con la frecuencia absoluta tenemos el valor que más se repite:

<div align="center">
  <img src="img/17.png">
</div>

En el caso de que las clases estén representadas con intervalos, hablaremos de 

Desviación típica y la varianza

<div align="center">
  <img src="img/18.png">
</div>

<div align="center">
  <img src="img/19.png">
</div>

Ejemplo

Se tienen los siguientes datos de peso en kg de 100 individuos

<div align="center">
  <img src="img/20.png">
</div>

Para calcular la media

<div align="center">
  <img src="img/21.png">
</div>

Para la mediana se encuentra en n/2

<div align="center">
  <img src="img/22.png">
</div>

n/2=100/2=50, en este caso el intervalo de la mediana es (66,69)

<div align="center">
  <img src="img/23.png">
</div>

Para la moda

<div align="center">
  <img src="img/24.png">
</div>

<div align="center">
  <img src="img/25.png">
</div>

<div align="center">
  <img src="img/26.png">
</div>

[Ejercicio](../pye/Ejercicio1.pdf)

## Medidas de posición

Se llaman en general **cuantiles** y se pueden clasificar en tres grandes grupos

* **Cuartiles** (25%, 50%, 75%)
* **Quintiles** (20%, 40%, 60%, 80%)
* **Deciles** (10%, 20%, 30% ... 90%)

Dividen a una distribución ordenada en partes iguales

Para calcular las medidas de posición es necesario que los datos estén ordenados de menor a mayor

### Los cuartiles (Q)
Son los tres valores de la variable de una distribución que la dividen en cuatro partes iguales

<div align="center">
  <img src="img/27.png">
</div>

Para calcularlos se debe seguir lo siguiente:

1. Se ordenan los datos, entonces el primer valor será el mínimo y el último el máximo
2. Se determina la posición que ocupa cada cuartil, se puede usar la fórmula:
   * Q1 es el que deja por debajo un 25%
   * Q2 es el que deja por debajo un 50%, **coincide con la mediana**
   * Q3 es el que deja por debajo un 75%
<div align="center">
  <img src="img/28.png">
</div>

Ejemplo

<div align="center">
  <img src="img/29.png">
</div>

## Los deciles

Corresponden a los 9 valores que dividen a los datos en 10 partes iguales, es decir, 10%, 20% .... 90%

<div align="center">
  <img src="img/30.png">
</div>

## Los percentiles (Pp)

Son los noventa y nueve valores de la variable que la dividen en cien partes, se designan por P1, P2 ... P99

> P50 coincide con la mediana

El percentil p(pp) es un valor de la variable tal que el p% de la muestra está por debajo

Se calcula de la siguiente manera

<div align="center">
  <img src="img/31.png">
</div>

* Sí es decimal **se aproxima al entero más cercano superior**
* Buscamos este valor en la columna de la frecuencia acumulada
* El primer valor de x cuya frecuencia acumulada sobrepasa el resultado de este cálculo es el percentil buscado
* También se puede hacer con frecuencias relativas acumuladas

Ejemplo

<div align="center">
  <img src="img/32.png">
</div>

<div align="center">
  <img src="img/33.png">
</div>

<div align="center">
  <img src="img/34.png">
</div>

<div align="center">
  <img src="img/35.png">
</div>

Para este caaso entre las notas 3 y 7 hay un 50%. El intervalo estaría centrado en la evaluación 5 que es la mediana

## Diagrama de bigotes

Son una representación visual que describe varias características importantes, al mismo tiempo, tales como la dispersión y la simetría

* Se representan los 3 cuartiles, Q1, Q2 (mediana) y Q3

<div align="center">
  <img src="img/36.png">
</div>

<div align="center">
  <img src="img/37.png">
</div>

<div align="center">
  <img src="img/38.png">
</div>

<div align="center">
  <img src="img/39.png">
</div>

* Podemos encontrar datos mucho más grandes o mucho más pequeños que el resto de los datos. Esos valores son llamados atípicos o outliers
* Se representan con un punto y pueden estar en cualquiera de los dos extremos del diagrama

**Regla para encontrar valores atipicos:**

* Mayor que Q3 por al menos 1.5 veces el rango intercuartilico (RI)
* Menor que Q1 por al menos 1.5 veces el rango intercuartilico (RI)

A estos dos límites a partir de los cuales vamos a decir que un datos es atípico, les llamaremos barreras

<div align="center">
  <img src="img/40.png">
</div>

Viendo otro ejemplo:

<div align="center">
  <img src="img/41.png">
</div>


## Asimetría

Se dice así cuando la media, mediana y la moda no coinciden, por ende son asimetricas

<div align="center">
  <img src="img/42.png">
</div>

La **Simetría** se da cuando hay aproximadamente la misma cantidad de los datos a ambos lados de la media aritmética. La media aritmética, la mediana y la moda son iguales

<div align="center">
  <img src="img/43.png">
</div>

### Coeficiente de Karl Pearson**

<div align="center">
  <img src="img/44.png">
</div>

### Medida de Yule Bowley o medida cuaartílica

<div align="center">
  <img src="img/45.png">
</div>

### Medida de fisher

<div align="center">
  <img src="img/46.png">
</div>

## Ejercicios

Ejercicio 1

<div align="center">
  <img src="img/47.png">
</div>

Ejercicio 2

<div align="center">
  <img src="img/48.png">
</div>

Identificando los cuartiles

<div align="center">
  <img src="img/49.png">
</div>

<div align="center">
  <img src="img/50.png">
</div>

[Ejercicios de la unidad](../pye/Ejercicio2.pdf)

# Estadística bidimensional o bivariada

## Dos variables aleatorias

Es una variable en la que cada individuo está definida por un par de características (x,y)

Estás dos son a su vez variables aleatorias en las que existe relación entre ellas, **una de las dos es la variable independiente y la otra la variable dependiente**

<div align="center">
  <img src="img/51.png">
</div>

<div align="center">
  <img src="img/52.png">
</div>

## Tabla de doble entrada o tabla de contingencia

Es una tabla de fecuencias conjuntas donde se ponen en las columnas los valores de una de las variables, y en las filas los valores de la otra variabl. Puede ser con frecuencias absolutas y también con frecuencias relativas

**Con frecuencias absolutas**

<div align="center">
  <img src="img/53.png">
</div>

¿Cuál es el número de estudiantes mujeres del Dpto que están haciendo un doctorado PhD?

<div align="center">
  <img src="img/54.png">
</div>

**Con frecuencias relativas (Porcentajes)**

<div align="center">
  <img src="img/55.png">
</div>

¿Cuál es el procentaje de estudiantes hombres que están haciendo un master?

<div align="center">
  <img src="img/56.png">
</div>

Dividiendo por el total de la fila

<div align="center">
  <img src="img/57.png">
</div>

Del total de chicas ¿Cuántas de ellas están haciendo un master?
Del total de chicos ¿Cuántos están haciendo un master?

<div align="center">
  <img src="img/58.png">
</div>

## Relación entre dos variables

x e y están relacionadas estadísticamente cuando conocida una de ellas se puede estimar aproximadamente el valor de la otra

* Ingresos y gastos de una familia
* Producción y ventas de una fábrica
* Gastos en publicidad y beneficios de una empresa
* Altura y peso
* Notas de un examen y nivel de estrés

### Distribuciones bidimensionales

Son aquellas en las que a cada individuo le corresponden los valores de dos variables, las representamos por el par (x,y)

Si representamos cada par de valores como las coordenadas de un punto, el  conjunto de todos los individuos representados de esta forma se llama **nube de puntos** y el gráfico se llama **diagrama de dispersión**

Si las variables tienen una tendencia lineal positiva (una crece cuando la otra decrece) o negativa una decrece cuando la otra crece, entonce sobre la nube de puntos puede trazarse una recta que se ajusta a ellos lo mejor posible, llamada **recta de regresión**

### Regresión líneal

Supongamos que las notas de 12 alumnos de una clase en Matemáticas y Física son las siguientes:

<div align="center">
  <img src="img/59.png">
</div>

Se muestra una tendencia líneal positiva

<div align="center">
  <img src="img/60.png">
</div>

### Medidas de relación entre dos variables

La **covarianza** de una variable bidimensional (x,y) es la media aritmética de los productos de las desviaciones de cada una de las variables respecto a sus medias respectivas

Si hablamos de covarianza como parámetro **muestral** se denota como
<div align="center">
  <img src="img/61.png">
</div>
En cambio si es como parámetro poblacional se denota como
<div align="center">
  <img src="img/62.png">
</div>

Infica el sentido de la relación

<div align="center">
  <img src="img/63.png">
</div>

<div align="center">
  <img src="img/64.png">
</div>

> Su valor depende de la escala elegida por los ejes

Para evitar los problemas de escala y unidades de medida de las dos variables en cuestión, se utilizo una medida llamada **correlación** que trata de establecer **la relación o dependencia que existe entre las dos variables que intervienen en una distribución bidimensional sin depender de su escala**

Si los cambios en una de las variables influyen en los cambios de la otra, diremos que las variables están correlacionadas o que hay correlación entre ellas

<div align="center">
  <img src="img/65.png">
</div>

## Covarianza

**Para datos no agrupados**

Es la media aritméticad de los productos de las desviaciones de cada una de las variables respecto a sus medias respectivas

<div align="center">
  <img src="img/66.png">
</div>

Ejemplo: las notas de 12 alumnos de la clase de Matemáticas y Física son las siguientes:

<div align="center">
  <img src="img/67.png">
</div>

**Para datos agrupados**

<div align="center">
  <img src="img/68.png">
</div>

<div align="center">
  <img src="img/69.png">
</div>

<div align="center">
  <img src="img/70.png">
</div>

<div align="center">
  <img src="img/71.png">
</div>

## Correlación

Trata de establecer la relación o dependencia lineal que existe entre las dos variables que intervienen: x e y

### Correlación directa o positiva

<div align="center">
  <img src="img/72.png">
</div>

### Correlación inversa o negativa

<div align="center">
  <img src="img/73.png">
</div>

### Correlación nula

Sucede cuándo no hay dependencia entre las variables. La nube de puntos tiene una forma redondeada

Puede que no haya una dependencia lineal entre las variables pero si exista otro tipo de dependencia, como cuadrática exponencial, etc. Es decir, que la correlación sea nula no necesaria mente implica independencia entre las dos variables

<div align="center">
  <img src="img/74.png">
</div>

En caso de que haya correlación líneal. El **grado de correlación** indica la proximidad que hay entre los puntos y lo que seria la recta de regresión que representa la tendencia

<div align="center">
  <img src="img/75.png">
</div>

### Coeficiente de correlación lineal de pearson

<div align="center">
  <img src="img/76.png">
</div>

<div align="center">
  <img src="img/77.png">
</div>

<div align="center">
  <img src="img/78.png">
</div>

Para datos no agrupados

<div align="center">
  <img src="img/79.png">
</div>

Para datos agrupados

<div align="center">
  <img src="img/80.png">
</div>

<div align="center">
  <img src="img/81.png">
</div>

## Regresión líneal simple

La recta de regresión es la que mejor se ajusta a la nube de puntos

<div align="center">
  <img src="img/82.png">
</div>

Para el ejemplo de los alumnos de matemáticas

<div align="center">
  <img src="img/83.png">
</div>

<div align="center">
  <img src="img/84.png">
</div>

<div align="center">
  <img src="img/85.png">
</div>

### Coeficiente de determinación

Una medida de cuán bueno es el modelo de regresión es el siguiente:

<div align="center">
  <img src="img/86.png">
</div>

## Ejercicios y explicaciones

[Ejercicios de la unidad](../pye/Ejercicio3.pdf)

[Explicación coeficiente de variación](../pye/coeficienteVariacion.pdf)

[Formulas de regresión](../pye/Formulas2.pdf)

# Probabilidades

## Evento o suceso aleatorio

Un suceso cuyo resultado es **incierto**, no lo sabemos a priori

* Lanzamiento de una moneda
* El caudal de un fluido que cicula por una tubería
* El tiempo de atención al cliente de una sucursal bancaria
* El número de articulos defectuosos de un lote de materia prima

**Ejemplo del dado**

<div align="center">
  <img src="img/87.png">
</div>

<div align="center">
  <img src="img/88.png">
</div>

<div align="center">
  <img src="img/89.png">
</div>

<div align="center">
  <img src="img/90.png">
</div>

## Leyes de Morgan

<div align="center">
  <img src="img/91.png">
</div>

## Probabilidad

> Tiramos un dado equilibrado

Usamos la intuición
* Es menos probable  que salga un 1 a que salga un número mayor que 1
* Es igual de probable que salga un 4 a que salga un 6
* Es improbable que salga un 7
* La probabilidad de que salga un número positivo es máxima

> La probabilidad de un suceso es una medida de la confianza que tenemos a priori en que el suceso ocurra cuando se realice el experimento aleatorio
> A mayor probabilidad de un suceso, más probabilidad de que ocurra

### Enfoques / Interpretaciones

#### Probabilidad clásica (regla de laplace) 

Considera un experimento en el que los sucesos elementales son equiprobables. Si el suceso A tiene n(A) elementos entonces se define la probabilidad de A como:

<div align="center">
  <img src="img/92.png">
</div>

#### Enfoque frecuentista

Si repitieramos el experimento muchas veces, la frecuencia relativa con que ocurriria el suceso A convergería a su probabilidad

<div align="center">
  <img src="img/93.png">
</div>

#### Probabilidad subjetiva

Depende de la información de la que dispongamos

<div align="center">
  <img src="img/94.png">
</div>

### Axiomas (Requisito que tiene que cumplir cierta función para ser una probabilidad)

<div align="center">
  <img src="img/95.png">
</div>

### Consecuencias de los axiomas

<div align="center">
  <img src="img/96.png">
</div>

### Ejemplo del dado

<div align="center">
  <img src="img/97.png">
</div>

<div align="center">
  <img src="img/98.png">
</div>

## Probabilidad condicionada

<div align="center">
  <img src="img/103.png">
</div>

### Ejemplo

Se clasifica un grupo de 100 ejecutivos según su peso y al hecho de si sufren o no hipertensión:

<div align="center">
  <img src="img/99.png">
</div>

**Experimento aleatorio**: se selecciona de forma equiprobable a uno de los 100 ejecutivos y se observa su clasificación de tensión y peso

<div align="center">
  <img src="img/100.png">
</div>

<div align="center">
  <img src="img/101.png">
</div>

<div align="center">
  <img src="img/102.png">
</div>

## Sucesos independientes

Intuitivamente: el saber si uno de ellos ha ocurrido no nos da ninguna información sobre si el otro ha ocurrido

Dos sucesos A y B son **Independientes** sí:

<div align="center">
  <img src="img/104.png">
</div>

Se lanza un dado equilibrado
* **Suceso A:** Sale un resultado par
* **Suceso B:** Sale un resultado mayor que 2

Nos dicen que al tirar un dado ocurrió B. Sabiendo esto, ¿CUál es la probabilidad condicionada de que el resultado haya sido par?

<div align="center">
  <img src="img/105.png">
</div>

Los sucesos A y B son independientes

## Teorema de la probabilidad total

<div align="center">
  <img src="img/106.png">
</div>

<div align="center">
  <img src="img/107.png">
</div>

### Ejemplo

<div align="center">
  <img src="img/108.png">
</div>

<div align="center">
  <img src="img/109.png">
</div>

### Teorema de bayes

<div align="center">
  <img src="img/110.png">
</div>

<div align="center">
  <img src="img/111.png">
</div>

#### Ejemplo

Se dispone de un test clínico para una enfermedad rara que afecta a una de cada 10000 personas

  El test da positivo (detecta la enfermedad) en 99 de cada 100 personas que la padecen y da negativo (no la detecta) en 97 de cada 100 personas que no la padecen

> Se aplica el test a una persona elegida al azar y da positivo ¿Cuál es la probabilidad de que padezca la enfermedad?

<div align="center">
  <img src="img/112.png">
</div>

<div align="center">
  <img src="img/113.png">
</div>

## Ejercicios

[Probabilidades](../pye/probabilidades.pdf)
[Hoja de Probabilidades](../pye/HojaProbabilidades.pdf)
[Soluciones hoja de probabilidades](../pye/SolucionesHojaProbabilidades.pdf)

# Distribuciones

Las variables aleatorias han llegado a desempeñar un papel importante en casi todos los campos de estudio: en la Física, la Química y la Ingeniería; y especialmente en las ciencias biológicas y sociales. **Estas variables aleatorias son medidas y analizadas en términos de sus propiedades estadísticas y probabilísticas**, de las cuales una característica subyacente es su **función de distribución**. A pesar de que el número potencial de distribuciones puede ser muy grande, en la práctica, un número relativamente pequeño se utilizan; ya sea porque tienen características matemáticas que las hace fáciles de usar o porque se asemejan bastante bien a una porción de la realidad, o por ambas razones combinadas.

Las distribuciones de probabilidad teóricas **son útiles en la inferencia estadística porque sus propiedades y características son conocidas.** Si la distribución real de un conjunto de datos dado es razonablemente cercana a la de una distribución de probabilidad teórica, muchos de los cálculos se pueden realizar en los datos reales utilizando hipótesis extraídas de la distribución teórica.

## Distribución de probabilidad

En teoría de la probabilidad y estadística, **la distribución de probabilidad de una variable aleatoria es una función que asigna a cada suceso definido sobre la variable la probabilidad de que dicho suceso ocurra.** 

> La distribución de probabilidad **está definida sobre el conjunto de todos los sucesos y cada uno de los sucesos es el rango de valores de la variable aleatoria.** También puede decirse que tiene una relación estrecha con las **distribuciones de frecuencia.** De hecho, una distribución de probabilidades puede comprenderse como una **frecuencia teórica**, ya que **describe cómo se espera que varíen los resultados**.

La distribución de probabilidad está completamente especificada por la **función de distribución**, cuyo valor en cada **x real es la probabilidad de que la variable aleatoria sea menor o igual que x.**

## Distribuciones de variable discreta

**Se denomina distribución de variable discreta a aquella cuya función de probabilidad solo toma valores positivos en un conjunto de valores de X finito o infinito numerable.** A dicha función se le llama **función de masa de probabilidad.** En este caso la distribución de probabilidad es la suma de la función de masa, por lo que tenemos entonces que: 

<div align="center">
  <img src="img/133.png">
</div>

## Distribuciones de variable continua

**Se denomina variable continua a aquella que puede tomar cualquiera de los infinitos valores existentes dentro de un intervalo.** En el caso de variable continua la distribución de probabilidad es la integral de la función de densidad, por lo que tenemos entonces que:

<div align="center">
  <img src="img/134.png">
</div>

## Histogramas

Una de las mejores maneras de describir una variable es representar los valores que aparecen en el conjunto de datos y el número de veces que aparece cada valor. La representación más común de una distribución es un histograma, que **es un gráfico que muestra la frecuencia de cada valor.**

<div align="center">
  <img src="img/hist.png">
</div>

## Función de Masa de Probabilidad

Otra forma de representar a las **distribuciones discretas** es utilizando su **Función de Masa de Probabilidad o FMP**, la cual relaciona **cada valor con su probabilidad en lugar de su frecuencia**. **Esta función es normalizada de forma tal que el valor total de probabilidad sea 1**. 

> La ventaja que nos ofrece utilizar la FMP es que **podemos comparar dos distribuciones** sin necesidad de ser confundidos por las diferencias en el tamaño de las muestras. También debemos tener en cuenta que FMP **funciona bien si el número de valores es pequeño**; pero a medida que el número de valores aumenta, la probabilidad asociada a cada valor se hace cada vez más pequeña y el efecto del ruido aleatorio aumenta. Veamos un ejemplo con Python.

## Función de distribución acumulada

Si queremos evitar los problemas que se generan con **FMP cuando el número de valores es muy grande**, podemos recurrir a utilizar la **Función de Distribución Acumulada o FDA**, para representar a nuestras distribuciones, tanto discretas como continuas. 

> Esta función relaciona los valores con su correspondiente percentil; es decir que va a describir la probabilidad de que una variable aleatoria X sujeta a cierta ley de distribución de probabilidad se sitúe en la zona de valores menores o iguales a x.

## Función de Densidad de Probabilidad

Por último, el equivalente a la FMP para distribuciones continuas es la Función de Densidad de Probabilidad o FDP. **Esta función es la derivada de la Función de Distribución Acumulada.**



https://blog.adrianistan.eu/estadistica-python-distribucion-binomial-normal-poisson-parte-vi

Con que probabilidad toma esos valores la **distribución**

https://es.wikipedia.org/wiki/Distribuci%C3%B3n_de_probabilidad

## Principales distribuciones

### Variable aleatoria discreta

<div align="center">
  <img src="img/114.png">
</div>

### Función de probabilidad (suma=1)

Para una variable aleatoria discreta X, definimos la función de probabilidad como la que le asocia a cada valor de la viable una probabilidad

<div align="center">
  <img src="img/115.png">
</div>

### Función de distribución

La función de distribución le asigna a cada valor de la variable la probabilidad de que la variable sea menor o igual que ese valor, es decir, acumula todas las probabilidades de los valores anteriores hacia el

<div align="center">
  <img src="img/116.png">
</div>

### Media y varianza con la función de probabilidad

Cuáando hablamos de **función de probabilidad estamos caracterizando** a la población

Podemos definir media y varianza poblacionales en el concepto de **esperanza matemática** o **valor esperado de la variable aleatoria: E(x)**

<div align="center">
  <img src="img/117.png">
</div>

## Distribución para variables aleatorias continuas

El método para describir la distribución de las v.a discretas es inadecuada para describir una v.a. continua, no se puede asociar a cada valor de la v.a su probabilidad

La **función de densidad** describe la distribución de probabilidad de una variable aleatoria continua

<div align="center">
  <img src="img/118.png">
</div>

No hay harea de t a t por lo tanto es 0

<div align="center">
  <img src="img/119.png">
</div>

Definimos como función de distribución a la que a cada valor de la variable aleatoria le asocia la probabilidad de que la variable sea menor o igual a él:

<div align="center">
  <img src="img/120.png">
</div>

<div align="center">
  <img src="img/121.png">
</div>

[Propiesdades valor esperado](../pye/PropiedadesValorEsperado.pdf)

### Distribución de Binomial y Bernoulli

Un ensayo de Bernouilli se **define como un experimento donde puede darse un éxito o fracaso** y donde cada ensayo es independiente del anterior. Por ejemplo, un ensayo de Bernoulli de parámetro 0.5 sería lanzar una moneda a cara o cruz (mitad de posibilidades de cara, mitad de posibilidades de cruz).

**Si repetimos N veces los ensayos de Bernouilli tenemos una distribución binomial.**

Supongamos que estamos en una fabrica de bombillas. Tomamos una muestra de 10 bombillas y nos interesa saber si son defectuosas o no

Definir una variable aleatoria

> X: Número de bombillas defectuosas dentro del lote de 10 unidades

**¿Cuál es la distribución de X?**

> Denotemos **p** la probabilidad de que una bombilla sea defectuoosa y como **n** el tamaño de la muestra que tenemos

y es una variable aleatoria que **vale 1, cuando la bombilla es defectuosa** **y vale 0 cuando no es defectuosa** 

Entonces la variable aleatoria Y tiene una distribución que se denomina **Bernoulli. Notación y~Bernoulli(p)**

La función de probabilidad de Y es de la forma:

<div align="center">
  <img src="img/122.png">
</div>

**La suma debe de ser 1**

La media y la varianza de Y son:

<div align="center">
  <img src="img/123.png">
</div>

El número **de bombillas defectuosas entre 10** va a ser la siguiente v.a

<div align="center">
  <img src="img/124.png">
</div>

<div align="center">
  <img src="img/125.png">
</div>

La distribución de **X se llama Binomial, Notación X~Binomial(n,p)**

<div align="center">
  <img src="img/126.png">
</div>

Si tenemos **n = 10 bombillas** y sabemos que la probabilidad de que alguna de ellas sea defectuosa es **p = 0.1**

¿Cuál es la probabilidad de encontrarnos con 4 bombillas defectuosas dentro del lote de 10 bombillas?

<div align="center">
  <img src="img/127.png">
</div>

¿Cuál es el número esperado de bombillas defectuosas dentro del lote de 10 bombillas?

<div align="center">
  <img src="img/128.png">
</div>

## Distribución de POISSON

La distribución de Poisson **recoge sucesos independientes** que ocurren en un soporte continuo.**El número medio de sucesos por unidad de soporte se le conoce como λ** y caracteriza la distribución. poisson nos permite crear distribuciones de este tipo.

> Concretamente, se especializa en la probabilidad de ocurrencia de sucesos con probabilidades muy pequeñas, o sucesos «raros».

* En una variable aleatoria de tipo discreto
* Nos permite calcular las probabilidades de sucesos independienes que aparecen de manera estable en un **intervalo de tiempo**, sabiendo el **promedio**

**Algunos ejemplos de distribuciones de Poisson:** número de clientes que llegan cada hora a cierto puesto de servicio, número de averías diarias de un sistema informático, número de vehículos que pasan diariamente por un túnel, número de defectos por kilómetro de cable, ...


**x~Poisson(lambda)**

El rango de valores que toma la variable es: rx = {0,1,2,...}

La función de probabilidad es:

<div align="center">
  <img src="img/129.png">
</div>

### Ejemplo

Sabiendo que el número promedio de clientes que llegan en una hora a un banco es 10 ¿Cuál sería la probabilidad de que llegaran 15 clientes en una hora?

<div align="center">
  <img src="img/130.png">
</div>

¿Y la probabilidad de que lleguen 15 en dos horas?

<div align="center">
  <img src="img/131.png">
</div>

¿Y la probabilidad de que lleguen menos de dos personas en una hora?

<div align="center">
  <img src="img/132.png">
</div>