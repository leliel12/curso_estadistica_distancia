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

.. =============================================================================
.. FOOTER
.. =============================================================================

.. [#] Este tipo de preguntas esta muy condicionada a la herramienta que se
       utiliza en mi caso; utilizo matplotlib

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###
