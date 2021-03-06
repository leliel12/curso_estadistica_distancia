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

================================================
ACTIVIDADES INTEGRADORAS  - MÓDULOS  V, VI Y VII
================================================

:Autor: Juan B Cabral
:DNI: 28818383
:Email: jbc.develop@gmail.com


Esta actividad integradora comprende una serie de ejercicios relacionados,
principalmente, con los conocimientos teóricos que nos servirán para comprender
los conceptos que se desarrollarán a partir del Módulo VIII. Por este motivo
muchos de los ejercicios incluidos en esta actividad no estarán asociados con
las bases de datos, pues su finalidad es solamente la ejercitación y
comprensión de los conceptos. Tal es el caso de las distribuciones de
probabilidad como la distribución binomial, Poissón, distribución normal,
t de Student, Chi-cuadrado y F que, hasta aquí, han sido presentadas en cuanto
a sus características principales, los supuestos en que se basan, el manejo de
las tablas correspondientes a cada una de ellas y su importancia y aplicación
en inferencia estadística.

Donde sí podemos utilizar la base de datos con la que hemos estado trabajando
es en el cálculo de probabilidades. Para ello utilizaremos el archivo EPH.xls
porque ya estamos familiarizados con las variables de esta encuesta. Ya hemos
comprendido de la lectura del material del curso que la teoría clásica de
probabilidad se utiliza fundamentalmente en los juegos de azar en los cuales
se conocen todos los resultados posibles de la experiencia. Pero como el mundo
real no siempre responde a esta condición, necesitamos determinar cómo calcular
probabilidades de eventos para los cuales sólo contamos con datos muestrales.
Teniendo en cuenta entonces que la probabilidad se puede asimilar a la
frecuencia relativa si se repite un experimento aleatorio un gran número de
veces, aplicaremos estos conceptos sobre algunas de las variables de la
encuesta.

.. class:: dedication

+----------------------------------+-------------------------+
|                                  | .. image:: imgs/arr.png |
| Puede acceder al archivo EPH.xls |     :align: right       |
| desde el aula virtual del curso. |     :scale: 100 %       |
|                                  |                         |
+----------------------------------+-------------------------+


**Actividades**


|hamster| Actividad nro. 1
--------------------------

A partir de las distribuciones de frecuencias de las variables SEXO (3),
ESTADO CIVIL (4), ESTUDIOS QUE CURSA O CURSÓ (10) y TIPO DE VIVIENDA (12)
calculadas en el Ejercicio 2 de la actividad integradora Nro. 1, determine:

.. image:: imgs/note1.png
    :align: right
    :scale: 100 %

a) La probabilidad de que un individuo seleccionado aleatoriamente de esta
   población sea varón es :underline:`0.46`.
b) La probabilidad de que un jefe de hogar seleccionado aleatoriamente sea
   casado es :underline:`0.33`.
c) La probabilidad de que un jefe de hogar tenga estudios técnicos
   es :underline:`0.06`.
d) Hay una probabilidad de :underline:`0.03` de que un encuestado seleccionado
   aleatoriamente sea inquilino.


|hamster| Actividad nro. 2
--------------------------

A partir de la tabla de frecuencias de la variable EDAD1 obtenida en el
ejercicio 5 de la actividad integradora Nro. 1, determine:

a) La probabilidad de que un jefe de hogar tenga entre 30 y 39
   años es :underline:`0.22`.
b) La probabilidad de encontrar un jefe de hogar de menos de 10 años es
   :underline:`0 (el primer grupo empieza con 10 años)`.
c) La probabilidad de que un jefe de hogar no tenga entre 40 y 49 años es
   :underline:`0.25`
d) La probabilidad de que un jefe de hogar sea mayor a 70 años es
   :underline:`0 (el ultimo grupo termina en 69 años)`.


|hamster| Actividad nro. 3
--------------------------

Realice tablas de frecuencia de las variables CANTIDAD DE HS.
TRABAJADAS EN LA SEMANA, ANTIGÜEDAD EN LA OCUPACIÓN Y SUELDO, y determine:

.. csv-table:: Cantidad de hs. trabajadas
    :header-rows: 1
    :file: tables/act3_cant_hs_tab.csv

.. csv-table:: Antigüedad en la ocupación
    :header-rows: 1
    :file: tables/act3_antig.csv

.. csv-table:: Sueldo
    :header-rows: 1
    :file: tables/act3_sueldo.csv


a) La probabilidad de que un jefe de hogar trabaje 20 hs. diarias es de
   :underline:`0.1`.
b) Hay 15 jefes de hogares que trabajan 35 hs. semanales en la muestra.
   Esto indica que la probabilidad de encontrar un jefe de hogar que trabaje
   35 hs. semanales es de :underline:`0.65`.
c) La probabilidad de encontrar un jefe de hogar que tenga más de 34 años de
   antigüedad es de :underline:`0.04`.
d) Observando la distribución de salarios de los jefes de hogar, es posible
   determinar que hay una probabilidad de
   :underline:`0.44` de encontrar un jefe que
   gane entre 300 y 500 pesos mensuales (inclusive),
   (es decir, que gane 300 ó 310 ó..... ó 500 pesos).
e) Parece que no es muy probable encontrar jefes de hogar que ganen más de
   2.000 pesos, dado que la probabilidad de que ello ocurra es de
   :underline:`0.03`.


|hamster| Actividad nro. 4
--------------------------

Consideremos ahora una tabla bidimensional es decir, donde relacionamos dos
variables y registramos la cantidad de individuos que responden a dos
categorías de las variables seleccionadas. Estas tablas nos permiten encontrar
probabilidades marginales y conjuntas. Consideremos la tabla bidimensional
donde se relaciona a las variables SEXO y SUELDOS.

En base a estos resultados complete:


.. csv-table:: Sexo X Sueldo
    :header-rows: 1
    :file: tables/act4_sexoXsueldo.csv


a) La probabilidad de que un jefe gane entre 600 y 999 pesos es de
   :underline:`0.21`. Este valor nos define una probabilidad (marginal/conjunta)
   :underline:`marginal`.
b) La probabilidad de que un jefe de hogar sea varón o gane entre 1.000 y 1.999
   pesos es de :underline:`0.51`.
c) Hay una probabilidad de :underline:`0.25` de encontrar un jefe de hogar que
   sea mujer y gane entre 300 y 599 pesos. Este valor nos define una
   probabilidad (marginal/conjunta) :underline:`conjunta`.
d) Hay una probabilidad de :underline:`0.07` de que un encuestado gane más de
   1.000 pesos y sea varón.
e) Hay una probabilidad de :underline:`0.84` de que un encuestado sea mujer o
   gane menos de 599 pesos.
f) ¿Cuál es la probabilidad de que habiendo seleccionado una mujer, ésta gane
   entre 1.000 y 1.999 pesos? :underline:`0.0925`.
g) ¿Cuál es la probabilidad de que habiendo seleccionado un jefe de hogar que
   gane más de 2.000 pesos, sea varón? :underline:`1`.


|hamster| Actividad nro. 5
--------------------------

Consideremos ahora la tabla que relaciona las variables SEXO y
ESTUDIO QUE CURSA O CURSÓ.

.. csv-table:: Estudio que cursa or cursó X Sexo
    :header-rows: 1
    :file: tables/act5_stud_sexo.csv

En base a estos resultados complete el siguiente cuestionario:

a) La probabilidad de que un jefe de hogar tenga estudios universitarios es de
   :underline:`0.16`. Este valor nos define una probabilidad (marginal/conjunta)
   :underline:`marginal`
b) La probabilidad de que un jefe de hogar sea varón o tenga estudio comercial
   es de :underline:`0.54`.
c) Hay una probabilidad de :underline:`0.07` de encontrar un jefe de hogar
   que sea mujer y que tenga sólo estudio primario.
d) Hay una probabilidad de :underline:`0.01` de que un encuestado tenga otra
   enseñanza media y sea varón.
e) Hay una probabilidad de :underline:`0.49` de que un encuestado sea mujer o no
   sepa leer ni escribir.
f) ¿Cuál es la probabilidad de que habiendo seleccionado una mujer ésta tenga estudio superior?
   :underline:`0.0925`.
g) Son independientes los eventos SEXO y ESTUDIOS QUE CURSA O CURSÓ (SÍ/NO)
   :underline:`si`. ¿Cómo lo comprueba?
   :underline:`Verifique que la probabilidad de que sea varón y tenga educación`
   :underline:`secundaria es igual a la multiplicación de la probabilidad que`
   :underline:`sea varón por la probabilidad de que tenga estudios universitarios`


|hamster| Actividad nro. 6
--------------------------

Un comercio que vende artículos electrónicos ofrece a cada cliente que compra
un televisor de 29 pulgadas un servicio de post venta de reparación gratuita.
Su experiencia sobre reparaciones de aparatos de este tipo indica que el tiempo
desde la compra hasta la primera reparación está normalmente distribuido con
media de 36 meses y una varianza de 144 meses cuadrados o N(36,144).

Responda:

a) ¿Cuál es la probabilidad de que un televisor seleccionado al azar no necesite
   una reparación hasta dentro de 4 años?
   :underline:`P(X >= 48) = P(Z >= 1) = 1 - P(Z <= 1) = 1 - 0.8413 = 0.1587`
b) ¿Cuál es la probabilidad de que se necesite una reparación dentro de los primeros 2 años?
   :underline:`P(X <= 24) = P(Z <= -1) = P(Z >= 1) = 1 - P(Z <= 1) = 1 - 0.8413 = 0.1587`
c) Establecer un tiempo a tal que la probabilidad es 0,95 de que el consumidor
   necesitará una reparación antes de este tiempo, o sea: P(x ≤ a) = 0,95.
   :underline:`P(Z <= 1.645) = 0.95 entonces 36 + (1.645 · 12) = 55.74 meses (4 años y medio aprox)`

|hamster| Actividad nro. 7
--------------------------

La distribución de frecuencias resultante de una encuesta a familias donde una
de las preguntas se refería a la cantidad de hijos por familia fue la siguiente:

.. csv-table:: Cantidad de hijos por familia
    :header-rows: 1
    :file: static/act7.csv

a) Suponiendo que la variable cantidad de hijos por familia sigue una
   distribución de Poissón, calcule la probabilidad de que una familia
   seleccionada al azar tenga 5 hijos.

   :underline:`m = 1.5739 ~ 1.6`

   :underline:`P(x=5, m=1.6) = 0.0176`


|hamster| Actividad nro. 8
--------------------------

Se dice que un paciente tiene bajo nivel de potasio en sangre si el nivel del
mismo es de 3,5 o menos. El nivel de potasio de un individuo no es constante
sino que varía día a día. Además, el procedimiento de medición por si mismo
introduce alguna variación. Supongamos que la variación total sigue una
distribución normal.

Un paciente tiene un nivel medio de potasio de 3,8 con una desviación estándar
de 0,2. Si se miden los niveles de potasio de este paciente durante varios días:

a) ¿Cuál es la proporción de días donde la medición indicará hipocalemia
   (bajo nivel de potasio)?

   :underline:`P(X <= 3.5) = P(Z <= -1.5) = P(Z >= 1.5) = 1 - P(Z <= 1.5) = 1 - 0.9332 = 0.0667`


|hamster| Actividad nro. 9
--------------------------

Considere la variable aleatoria X = cantidad de personas que viven en una
vivienda. La distribución de probabilidad de esta variable aleatoria se da en
la siguiente tabla:

.. csv-table:: Cantidad de personas que viven en una vivienda
    :header-rows: 1
    :file: static/act9.csv

a) Verifique que es realmente una distribución de probabilidad de una
   variable discreta.

   :underline:`La variables corresponde a una distribución discreta del tipo`
   :underline:`**Poisson** ya que se define como la cantidad de eventos`
   :underline:`(cantidad de personas) que ocurren dentro de una unidad de`
   :underline:`espacio (vivienda).`

b) Represente gráficamente.

    .. image:: static/act9_chart.png
        :align: center
        :scale: 100 %

c) ¿Cuál es la probabilidad de que X ≥ 5? :underline:`P(X >= 5) = 0.126`
d) ¿Cuál es la probabilidad de que X > 5? :underline:`P(X > 5) = 0.059`
e) ¿Cuál es P(2 < X ≤ 4)? :underline:`P(2 < X ≤ 4) = 0.3320`
f) ¿Cuál es la P(X ≠ 1)? :underline:`P(X != 1) = 0.76`
g) Calcule la esperanza y la varianza de X (suponga que + de 7 equivale a 9
   personas que viven en una vivienda).

    :underline:`E(x) = 2.756`
    :underline:`V(x) = 6.4898`


|hamster| Actividad nro. 10
---------------------------

Los alumnos de Estadística tienen que realizar dos pruebas, una teórica y
otra práctica. La probabilidad de que un estudiante apruebe la parte teórica
es de 0,6; la probabilidad de que apruebe la parte práctica es de 0,8 y
la probabilidad de que apruebe ambas pruebas es 0,5.


Responda:

a) ¿Son independientes los sucesos aprobar la parte teórica y la parte práctica?

   .. class:: underline

    **T** = aprueba la parte teórica.

    **P** = aprueba la parte práctica

    **A** = aprueba ambas.

    P(T ∩ P) = P(A) = 0.5

    P(T) · P(P) = 0.6 * 0.8 = 0.48

    P(T ∩ P) != P(T) · P(P) = Son dependientes


b) ¿Cuál es la probabilidad de que un alumno no apruebe ninguno de los dos exámenes?

   .. class:: underline

    Siendo:

    P(T ∪ P) = La probabilidad de que apruebe almenos uno de los examenes

    1 - P(T ∪ P) = La probabilidad de que no apruebe ni un examen.

    1 - P(T ∪ P) = 1 - [P(T) + P(P) - P(T ∩ P)] = 1 - [P(T) + P(P) - P(A)] = 1 - [0.6 + 0.8 - 0.5]

    1 - P(T ∪) = 0.1


c) ¿Cuál es la probabilidad de que un alumno apruebe al menos uno de los dos exámenes?

   .. class:: underline

    P(T ∪ P) = P(T) + P(P) - P(T ∩ P) = P(T) + P(P) - P(A) = 0.6 + 0.8 - 0.5

    P(T ∪ P) = 0.9

d) Se sabe que un alumno aprobó la teoría. ¿Cuál es la probabilidad de que apruebe también la práctica?

   .. class:: underline

    P(P/T) = P(T ∩ P) / P(P) = P(A) / P(P) = 0.5 / 0.8

    P(P/T) = 0.625


|hamster| Actividad nro. 11
---------------------------

Una compañía de seguros hace una investigación sobre la cantidad de reclamos
de siniestros fraudulentos presentados por los asegurados.

Clasificando los seguros en tres clases, incendio, automóvil y "otros", se
obtiene la siguiente relación de datos:

    - El 6% son reclamos por incendios fraudulentos;
    - El 1% son reclamos de automóviles fraudulentos;
    - El 3% son "otros" reclamos fraudulentos;
    - El 14% son reclamos por incendio no fraudulentos;
    - El 29% son reclamos por automóvil no fraudulentos, y
    - El 47% son "otros" reclamos no fraudulentos.

a) Construya una tabla ordenando los datos anteriores y halle la probabilidad
   de que se realice un reclamo fraudulento y la probabilidad de que llegue un
   reclamo no fraudulento.

    .. csv-table:: Tabla de probabilidad con los datos ordenados
        :header-rows: 1
        :file: static/act11.csv


    .. class:: underline

        La probabilidad de que se realice un reclamo fraudulento es de 0.1, y
        la probabilidad de que sea no fraudulento es de 0.9

b) Calcule la probabilidad de que llegue un reclamo por incendio, un reclamo
   por automóvil y un reclamo por otros siniestros.

    .. class:: underline

        La probabilidad de que se realice un reclamo por incendio es de 0.2,
        por automóvil es de 0.3 y por otros siniestros de 0.5.


|hamster| Actividad nro. 12
---------------------------

Un artefacto doméstico tiene una duración (en horas) cuya función de densidad
de probabilidad es :math:`f(x) = 0,005 e^{-0,005x}` para x > 0.

a) Calcule la probabilidad de que el artefacto no supere las 100 horas de
   duración.

    .. class:: underline

        P(x < 100) = :math:`0,005 e^{-0,005 100)}` = 0.003


|hamster| Actividad nro. 13
---------------------------

La siguiente tabla muestra la función de distribución de la variable
aleatoria X.

.. csv-table:: Función de distribución de la variable aleatoria X
    :header-rows: 1
    :file: static/act13.csv

a) Determine:

1) La función de probabilidad

.. csv-table:: Función de probabilidad la variable aleatoria X
    :header-rows: 1
    :widths: 10, 10, 10, 10, 10, 10
    :file: static/act13c.csv

2) P(1 ≤ X ≤ 3) :underline:`3/4`
3) P(X ≤ 3) :underline:`3/4`
4) P(X < 3) :underline:`3/8`
5) P(X > 1) :underline:`1-1/8 = 7/8`

b) Calcule en primer lugar la función de cuantía correspondiente.

    :underline:`Resuelto en a1`

|hamster| Actividad nro. 14
---------------------------

Si la probabilidad de que un individuo sufra una reacción por una inyección de
un determinado suero, es 0,001:

a) Determine la probabilidad de que de un total de 2000 individuos sufran una
   reacción:

    1) Exactamente 3

        .. class:: underline

            m = np = 2000 · 0.001 = 2

            Por tabla ahora:

            P(x = 3) = 0.1804

    2) Más de 2 individuos tengan reacción.

        .. class:: underline

            P(X > 2) = P(X >=3) = 1 - P(X <= 2) = 0.6767


|hamster| Actividad nro. 15
---------------------------

Una centralita de teléfonos recibe un promedio de 600 llamadas durante 1 minuto
de congestión de las líneas. La centralita puede hacer un máximo de 20
conexiones por segundo.

a) ¿Cuál es la probabilidad de que la centralita quede rebasada durante un
   segundo dado?

    .. class:: underline

        m = 600/60 = 10

        por tabla

        P(X > 20) = P(X >= 21) = 1 - P(X <= 20) = 1 - 0.9984 = 0.0016


.. =============================================================================
.. FOOTER
.. =============================================================================

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###
