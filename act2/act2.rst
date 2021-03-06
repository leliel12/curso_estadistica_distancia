.. =============================================================================
.. ROLES AND INLINE IMAGES
.. =============================================================================

.. role:: underline
.. role:: strike

.. |hamster| image:: imgs/hamster.png
                :scale: 15 %


.. =============================================================================
.. HEADER
.. =============================================================================

.. header::
    .. image:: imgs/head.png
        :scale: 100 %


.. =============================================================================
.. ACTIVITIES
.. =============================================================================

=============================================
ACTIVIDADES INTEGRADORAS  - MODULOS  III Y IV
=============================================

.. class:: dedication

+---------------------------------------------------+-------------------------+
| Para la realización de las siguientes actividades | .. image:: imgs/arr.png |
| integradoras, se deberá utilizar el **archivo**   |     :align: right       |
| **EPH.xls**. Puede acceder a la base EPH desde el |     :scale: 100 %       |
| aula virtual del curso.                           |                         |
+---------------------------------------------------+-------------------------+

:Autor: Juan B Cabral
:DNI: 28818383
:Email: jbc.develop@gmail.com



**Actividades**


|hamster| Actividad nro. 1
--------------------------

1. Con la variable EDAD agrupada en los siguientes intervalos, complete la
   siguiente tabla de frecuencias:

.. csv-table:: Tabla de frecuencia de EDAD
    :file: tables/act1_edad.csv
    :header-rows: 1

.. csv-table:: Tabla de medidas de posición y dispersión de la variable EDAD
    :file: tables/act1_edad_meds.csv
    :header-rows: 1

2. Con los datos de la nueva variable que llamamos EDAD 1, responda las
   siguientes preguntas:

    a) El intervalo de edad más frecuente es el que abarca las edades de
       :underline:`20` a :underline:`29` años.

    b) El promedio de edad de los jefes de hogar es de :underline:`37.9` años.
       ¿El promedio pertenece al intervalo que contiene la mediana?
       :underline:`Sí`.

    c) La desviación estándar de la edad de los jefes de hogar es de
       :underline:`13.8` años y significa
       :underline:`La variabilidad promedio de las edades de los jefes de hogar`
       :underline:`es aproximadamente 14 años`.


|hamster| Actividad nro. 2
--------------------------

1. Con los datos originales de la variable EDAD, realice el gráfico Box Plot o
   diagrama de Caja y Brazo. Responda:

.. figure:: figs/act2_boxplot_edad.png
    :align: center
    :scale: 100 %

    Boxplot de la variable edad (Cuartiles: [18.0, 25.75, 37.0, 46.25]).

    a) ¿Existen valores de EDAD considerados extremos? :underline:`Sí`

    b) Observe el gráfico Box-Plot. Vea cómo aparece representada esta misma
       tendencia por la posición de la caja central. La caja está limitada por
       el cuartil :underline:`25.75` en el extremo inferior y por el cuartil
       :underline:`37` en el superior. La línea dentro de la caja representa
       la :underline:`mediana` de EDAD. El largo de las patillas indica
       :underline:`los valores adjacentes`. Se puede observar que la patilla
       superior es (más/menos) :underline:`más` larga que la inferior, lo que
       significa que :underline:`que hay una menor concentración de datos en la`
       :underline:`parte izquierda de la distribución`.


|hamster| Actividad nro. 3
--------------------------

1. Realice el grafico Box plot para la variable edad, por grupo de hombres y
   mujeres (realice un solo grafico con ambos box plot). Observe las posibles
   diferencias en la distribución de edades de ambos grupos.

.. figure:: figs/act3_boxplot_edad.png
    :align: center
    :scale: 100 %

    Boxplot de la variable edad por sexo.


2. Responda las siguientes preguntas:

    a) ¿Son las gráficas de distribución de edades iguales para varones y
       mujeres? (Sí/No). :underline:`No`.
      La diferencia más destacada está en el ancho de la caja, lo que indica que
      la distribución de edades de los varones es más (dispersa/homogénea)
      :underline:`homogénea` que la de las mujeres.

    b) La línea central representada por la
       :underline:`la línea dentro de la caja`
       indica que los varones tienen una edad mediana (mayor/menor)
       :underline:`menor` que las mujeres encuestadas.

    c) El largo de la patilla superior indica que la edad máxima de los
       encuestados fue (mayor/menor) :underline:`mayor` en las
       :underline:`mujeres` que en los varones.


|hamster| Actividad nro. 4
--------------------------

1. Realice los gráficos Box-Plot de las variables ``HS. TRA`` y ``ANTIGUE``
   también separando ambos sexos.

.. figure:: figs/act4_boxplot_hstra.png
    :align: center
    :scale: 100 %

    Boxplot de la variable horas trabajadas por sexo.

.. figure:: figs/act4_boxplot_antigue.png
    :align: center
    :scale: 100 %

    Boxplot de la variable antigüedad por sexo.


2. Responda:

    a) La cantidad de horas trabajadas por hombres y mujeres es
       (diferente/ igual/parecida) :underline:`diferente`.
       Esto se observa por (describir las semejanzas y/o diferencias)
       :underline:`los límites superiores e inferiores de tiempo que trabajan`
       :underline:`las mujeres es superior al de los hombres (reflejado en las`
       :underline:`patillas). Por otro lado los los hombres presentan una`
       :underline:`concentración mas homogénea de horas (caja mas chica) y con`
       :underline:`una mediana también menor.`

    b) Los varones trabajan entre aproximadamente 15 hs. semanales y
       :underline:`25` hs. semanales.
       Sin embargo hay varones que trabajan hasta :underline:`64` hs. lo que
       hace una gran diferencia con las mujeres.
       Éstas trabajan entre :underline:`10` hs. y 50 hs. semanales.

    c) El 50% central de las horas trabajadas por los varones (caja) se
       encuentra entre aproximadamente 25 hs. y :underline:`43` hs. semanales,
       mientras que el 50% central de las hs. semanales trabajadas por
       las mujeres se encuentra entre :underline:`20` hs. y :underline:`40` hs.

    d) Respecto a la antigüedad en la ocupación, lo primero que podemos ver es
       que las cajas de varones y mujeres (No/Sí) :underline:`no` son iguales.
       Esto indica que los varones tienen (mayor/menor) :underline:`menor`
       dispersión respecto a los años de antigüedad comparados con las mujeres.

    e) Sobresale un circulo por encima de la patilla superior con el valor 40
       al costado. Este valor, indica un punto "outlier" es decir un punto
       :underline:`que esta fuera de los valores adyacentes`.

    f) El número 40 que acompaña al valor outlier indica que el jefe de
       hogar identificado con ese número en la base de datos tiene una
       antigüedad de :underline:`36` años.


|hamster| Actividad nro. 5
--------------------------

1. Realice un análisis descriptivo de las variables; CANTIDAD DE HS.
   TRABAJADAS EN LA SEMANA, ANTIGÜEDAD EN LA OCUPACIÓN y SUELDO.

    .. class:: underline

        Las personas encuestadas trabajan semanalmente desde 10 hasta 64 horas
        por semana siendo el promedio unas 34 horas aproximadamente.
        El valor mas común así como la media es de 35 horas semanales.
        Con esto vemos que los valores forman una distribución ligeramente
        asimétrica ya que su media mediana y moda están bastante cerca.

    .. class:: underline

        Por el lado de la antigüedad en la ocupación existen jefes de hogar
        sin antigüedad así como personas que están hace 36 años en su trabajo.
        La mitad de los jefes trabajan hace menos de 8 años en su actual puesto
        y es lo mas común que estén hace 1 año en su ubicación.
        El promedio es de 11.28 años. Por estos valores vemos una distribución
        radicalmente asimétrica.

    .. class:: underline

        Al hablar de Sueldos vemos que hay jefes de familia sin ingresos
        mientras que el tope máximo es de $2200 pesos con un promedio de $625.
        El sueldo mas común es de $320 y la mitad cobra mas de $450.
        La distribución de valores es asimétrica.


2. Calcule los siguientes estadísticos:

.. csv-table::
    :header-rows: 1
    :file: tables/act5_1.csv

.. csv-table::
    :header-rows: 1
    :file: tables/act5_2.csv

.. csv-table::
    :header-rows: 1
    :file: tables/act5_3.csv

a) En base a los datos de la variable HS. TRABAJADAS, ¿Qué porcentaje de casos
   de la muestra trabajan exactamente 40 hs. semanales?
   :underline:`13` %
   ¿Qué porcentaje trabaja menos de 40 hs. semanales?
   :underline:`75` %.
   Y 41 o más hs. semanales?
   :underline:`25` %.

b) Es sorprendente notar que hay
   :underline:`9` personas (un :underline:`9` % del total de encuestados)
   que declaran trabajar 54 hs. o más en la semana. La mayoría de
   las personas encuestadas trabajan :underline:`35` hs. por semana y el número
   mínimo de hs. trabajadas es de :underline:`10` hs. semanales.
   El promedio de hs. trabajadas es de :underline:`33.47` hs. que es
   (mayor/menor) :underline:`menor` a la mediana de hs. trabajadas.

   Esto indica una distribución (simétrica, asimétrica derecha/izquierda)
   :underline:`asimétrica izquierda` de los datos.
   El rango indica que la diferencia entre la mayor cantidad de hs.
   trabajadas :underline:`64` hs. y la menos cantidad de hs.
   trabajadas :underline:`10` hs. es de :underline:`54` hs.

c) Con respecto a la variable ANTIGÜEDAD EN LA OCUPACIÓN.
   El :underline:`40` % de los encuestados llevan 5 o menos años en la empresa,
   mientras que solamente un :underline:`4` % lleva 35 o más años de antigüedad.
   El valor modal de antigüedad es de :underline:`1` años,
   lo que indica que
   :underline:`la mayoria de los encuestados estan hace 1 año en su puesto`.
   En cambio el promedio de antigüedad es de :underline:`11.28` años que es
   (mayor/menor) :underline:`mayor` a la mediana. El Q1 (cuartil 1 o 25%)
   indica un valor para la antigüedad de :underline:`3`años y el Q3 (cuartil 3
   o 75%) es de :underline:`18` años.

d) Si analizarnos el sueldo de los encuestados podemos ver que el 25% cobra un
   sueldo inferior a :underline:`320` pesos. Que el sueldo más alto es
   de :underline:`2200` pesos lo que representa un :underline:`1` % del total.
   El sueldo promedio es de :underline:`625` pesos con una desviación estándar
   de :underline:`472.53` pesos, y un coeficiente de variación de
   :underline:`75.56` %.
   Esto indica que la distribución de los salarios es (muy
   variable/poco variable) :underline:`muy variable`.

e) Analizando el coeficiente de variación de las tres variables consideradas,
   puede decirse que la variable :underline:`ANTIGÜEDAD` es la que presenta la
   mayor variación y que la variable :underline:`HORAS TRABJADAS` es la más
   homogénea o  de menor variación.

f) El  coeficiente  de  variación  cuartílico  CVc  muestra  que  la
   variable :underline:`ANTIGÜEDAD` es la que presenta la mayor variabilidad en
   el 50% central de su distribución y que la variable
   :underline:`HORAS TRABAJADAS` es la más homogénea.

g) Los índices de simetría indican que la variable antigüedad es
   (simétrica/ asimétrica derecha-izquierda) :underline:`asimétrica der.`,
   mientras que la variable horas trabajadas es :underline:`asimétrica izq`.


|hamster| Actividad nro. 6
--------------------------

1. Lleve a cabo un análisis descriptivo de las variables: CANTIDAD DE HS.
   TRABAJADAS EN LA SEMANA, ANTIGÜEDAD EN LA OCUPACIÓN, EDAD y SUELDO, por SEXO.

    .. class:: underline

        Los varones trabajan entre 15 y 64 horas semanales con un promedio de
        36.72 hs semanales, mediana de 35.5 y moda de 35. En el caso de las
        mujeres, estas trabajan entre 10 y 50 horas semanales siendo su promedio
        30, su mediana 32.5 y su valor mas común 35.

        Por el lado de la antigüedad en la ocupación sucede que los hombres
        tienen un promedio de 9.3 años, con una mediana de 7 y un valor mas común
        de 1. También hay que mencionar que hay hombres que trabajan hasta
        36 horas y así como algunos que no trabajan. Si analizamos la mujeres
        están trabajan entre 1 y 35 horas semanales. Siendo sus medidas de
        posición 12.96 la media, 10 la mediana y 3 la moda.

        En el ámbito de las sueldo los en ambos sexos hay personas que
        no cobran nada. los hombres cobran hasta 2200 pesos y las mujeres
        hasta 2000 pesos. En los promedios los hombres cobran $678 mientras que
        las mujeres $590. La mediana y la moda para las mujeres son de $455 y
        $320 respectivamente; y en los hombres $440 y $320.

        La edad promedio de los hombres es de 34.22 y de las mujeres es de 39.53
        La mujer y el hombre mas joven tiene 18 años mientras que los mayores
        tienen 64 años para las mujeres y 69 para los hombres. El
        50% tiene menos de 33 años y medio en los varones y 41 en las mujeres.
        El valor mas común de edad en los hombres es de 26 años y de las mujeres
        de 21 años.

2. Calcule los siguientes estadísticos:

.. csv-table:: Para varones
    :header-rows: 1
    :file: tables/act6_varones.csv

.. csv-table:: Para mujeres
    :header-rows: 1
    :file: tables/act6_mujeres.csv

a) Compare las distintas mediciones para ambos grupos y saque conclusiones
   respecto a ambas distribuciones.

    .. class:: underline

        En las horas trabajadas por semana los varones presentan una asimetría
        derecha mientras que las mujeres es izquierda. Esto se evidencia por los
        cuartiles y el promedio. Ambos sexos son bastante homogéneos entre ellos

        En el caso de la antigüedad los varones tienden a cambiar mas de trabajo
        que las mujeres. Ambos grupos son bastante homogéneos y presentan
        concentraciones en los valores superiores.

        Por ultimo los sueldos en los varones tienden a cobrar mas que las
        mujeres por el mayor numero en su coeficiente de asimetría.


|hamster| Actividad nro. 7
--------------------------

Trabajaremos ahora con las variables referidas a las características
habitacionales.

A partir de las variables TIPO DE VIVIENDA, CUANTAS HABITACIONES TIENE LA
VIVIENDA Y ES USTED.

a) Del total de encuestados hay :underline:`22` que viven en departamento, lo
   que representa un :underline:`22` % del total de la muestra.

b) El tipo de vivienda modal o que se presenta con la mayor frecuencia es
   :underline:`Casa` y representa un :underline:`65` % del total de encuestados.

c) No hay ningún encuestado en la categoría 5. Esto indica que ninguno de los
   jefes de hogar vive en :underline:`Hotel o pensión`.

d) Hay :underline:`58` encuestados que son propietarios de la vivienda y del
   terreno y que representan un :underline:`58` % del total de encuestados.
   Sólo hay :underline:`3` encuestados que son propietarios de la vivienda
   solamente, es decir un :underline:`3` % del total.

e) La mayoría de las viviendas tienen entre :underline:`2` y :underline:`5`
   habitaciones, representando un 87% del total de viviendas.

f) Hay un 86% de viviendas que tienen menos de :underline:`5` habitaciones.

g) El promedio de habitaciones por vivienda es de :underline:`3.09`
   habitaciones, el valor modal es de :underline:`3` habitaciones y
   la mediana es de :underline:`3` habitaciones. Estas medidas de posición
   indican que la cantidad de habitaciones por vivienda sigue una
   distribución (simétrica/asimétrica) :underline:`simétrica`.

h) El número mínimo de habitaciones por vivienda es de :underline:`1`
   habitaciones y el máximo es de :underline:`9` habitaciones, lo que determina
   un rango de :underline:`8` habitaciones en la muestra.

i) La varianza del número de habitaciones es de :underline:`1.84`, mientras que el
   coeficiente de variación es de :underline:`43.2` %. Luego la cantidad de
   habitaciones por vivienda es una variable (homogénea/dispersa)
   :underline:`homogénea`


|hamster| Actividad nro. 8
--------------------------

Tomando las variables TOTAL DE PERSONAS EN LA VIVIENDA, TOTAL DE PERSONAS
ECONÓMICAMENTE ACTIVAS y TOTAL DE PERSONAS NO ECONÓMICAMENTE ACTIVAS, responda
las siguientes preguntas:

a) La cantidad promedio de personas por hogar es de :underline:`3.68` personas.
   El promedio de las económicamente activas es de :underline:`1.67`
   personas por hogar y es (mayor/menor) :underline:`menor` al promedio de las
   no  económicamente activas.

b) En la mayoría de los hogares (moda) viven :underline:`4` personas,
   conformando un total de :underline:`22` hogares con esta cantidad de
   personas. La mayoría de los hogares (moda) tiene :underline:`1` personas
   económicamente activas y :underline:`2` personas no económicamente activas.
   Hay un 38% de hogares que tienen :underline:`2` [#]_ personas activas y un
   :underline:`84` % de hogares con 3 o menos personas no económicamente
   activas.

c) La cantidad de personas económicamente activas es (más/menos)
   :underline:`menos` variable que la cantidad de personas no económicamente
   activas. Esto se observa con los coeficientes de variación que toman los
   valores :underline:`41.99` % y :underline:`78.42` % respectivamente.

d) El 67% (le los hogares tiene menos de :underline:`5` personas. Hay 14 hogares
  con :underline:`3` personas económicamente activas y :underline:`21` hogares
  sin personas no económicamente activas.

e) ¿Qué conclusión general podernos efectuar en base al análisis de estas tres
   variables?

    .. class:: underline

        Se puede observar en estos valores que la mayoría de los hogares (86%)
        tienden a tener 2 personas que trabajan (Típica conformación familiar
        donde el padre y madre trabajan). El resto de los hogares tiene 3
        personas que trabajan. Por el lado de los no activos laboralmente
        se presenta dos claro outlier de dos casas donde hay 6 y 8 desocupados.
        También hay 21 viviendas donde no hay personas sin actividad laboral
        (parejas o personas solas)


.. =============================================================================
.. FOOTER
.. =============================================================================

.. [#] El 46% de los hogares tienen 1 persona activa, el 40% 2 y el 14% 3. En
       ningún momento se menciona el 38% buscado con lo cual la respuesta mas
       acertada es tomar el 40 %.

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###
