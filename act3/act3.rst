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
   :underline:`P(X >= 48) = P(Z >= 0.84) = 1 - P(Z <= 0.84) = 1 - 0.7995 = 0.2005`
b) ¿Cuál es la probabilidad de que se necesite una reparación dentro de los primeros 2 años?
   :underline:`P(X <= 24) = P(Z <= -0.08) = P(Z >= 0.08) = 1 - P(Z <= 0.08) = 1 - 0.5319 = 0.4680`
c) Establecer un tiempo a tal que la probabilidad es 0,95 de que el consumidor
   necesitará una reparación antes de este tiempo, o sea: P(x ≤ a) = 0,95.
   :underline:`P(Z <= 1.645) = 0.95 ... 36 + (1.645 · 144) = 272.88 meses`

|hamster| Actividad nro. 7
--------------------------

La distribución de frecuencias resultante de una encuesta a familias donde una
de las preguntas se refería a la cantidad de hijos por familia fue la siguiente:

.. csv-table:: Cantidad de hijos por familia
    :header-rows: 1
    :file: static/act7.csv


.. =============================================================================
.. FOOTER
.. =============================================================================

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###
