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

===============================================
ACTIVIDADES INTEGRADORAS  - MÓDULOS  XIII y XIV
===============================================

:Autor: Juan B Cabral
:DNI: 28818383
:Email: jbc.develop@gmail.com


|hamster| Actividad nro. 1
--------------------------

Una determinación con un electrodo selectivo de iones (EIS) de sulfuro
procedente de sulfato reducido de bacterias se comparó con una determinación
gravimétrica. Los resultados obtenidos se expresaron en miligramos de sulfuro
tal como se presenta en la siguiente tabla:

.. csv-table:: Datos
    :header-rows: 1

    Muestra,Método ESI,Gravimetría
    1,108,105
    2,12,16
    3,152,113
    4,3,0
    5,106,108
    6,11,11
    7,128,141
    8,12,15
    9,160,182
    10,128,118


a) Grafique convenientemente los datos.

.. image:: figs/act1a.png
    :align: center
    :scale: 70 %


b) Calcule el grado de relación entre las mediciones:

.. class:: underline

    r = 0.96925194


c) Pruebe la significación de la medida calculada.

.. math::

    H_0) p = 0

.. math::

    H_1) p \neq 0

.. math::

    t = \frac{r \times \sqrt{n - 2}}{\sqrt{1 - r^2}} = \frac{2.74}{0.24} = 11.41

.. class:: underline

    t1 = -2.306 ; t2 = 2.306

d) Interprete el resultado.

.. class:: underline

    Como **11.41** esta fuera del rango **-2.306**, **2.306** se asume que las
    variables están muy correlacionadas.


|hamster| Actividad nro. 2
--------------------------

En un estudio de hombres de 25 años y más a los cuales se les preguntó el
último nivel educativo alcanzado, se obtuvieron los siguientes porcentajes:

.. csv-table:: Datos
    :header-rows: 1

    Nivel educativo,%
    Primario incompleto,18
    Primario completo,17
    Secundario incompleto,32
    Secundario completo,13
    Universitario incompleto,17
    Universitario completo,3

Después de 10 años de haber realizado este estudio, se seleccionó una muestra
de 200 hombres de 25 años y más a los cuales se les pregunto lo mismo,
obteniéndose los siguientes resultados:

.. csv-table:: Datos
    :header-rows: 1

    Nivel educativo,Frecuencia
    Primario incompleto,35
    Primario completo,40
    Secundario incompleto,83
    Secundario completo,16
    Universitario incompleto,26
    Universitario completo,0

El investigador desea saber si la distribución de hombres de 25 años o más
por nivel de educación alcanzado, es la misma que la de hace 10 años atrás.

¿Qué puede decir al respecto?

.. class:: underline

    Primero pasamos la segunda tabla a porcentajes

.. csv-table:: Datos 20 años después
    :header-rows: 1

    Nivel educativo,%
    Primario incompleto,17.5
    Primario completo,20
    Secundario incompleto,41.5
    Secundario completo,8.0
    Universitario incompleto,13
    Universitario completo,0.0

.. class:: underline

    Ingresamos esos valores a PSPP y adjuntamos la salida



|hamster| Actividad nro. 3
--------------------------

Una encuesta de opinión política realizada a 980 personas en condición de
votar, preguntó acerca de su preferencia por un partido político. Las
respuestas por sexo de las personas fueron las siguientes:

.. csv-table:: Sexo y Política
    :header-rows: 1

    Sexo,Radical,Justicialista,Otros
    Mujer,279,225,73
    Varón,165,191,47

¿Existe asociación entre el sexo del votante y su preferencia por un
partido político en particular? ¿Por qué?


.. figure:: figs/act3.png
    :align: center
    :scale: 200 %

    Salida PSPP

.. class:: underline

    Al parecer el test de Chi-cuadrado de Pearson devuelve un valor que indica
    que ambas muestras son independientes (0.16 > 0.05).


.. ============================================================================
.. FOOTER
.. ============================================================================

.. #

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###

