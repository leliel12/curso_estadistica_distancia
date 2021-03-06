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
ACTIVIDADES INTEGRADORAS  - MÓDULOS  X, XI y XII
================================================

:Autor: Juan B Cabral
:DNI: 28818383
:Email: jbc.develop@gmail.com


**Nota** Todos los test se ejecutaron con una confianza de 0.95, que es el valor
por defecto tanto de SPSS como de PSPP.


|hamster| Actividad nro. 1
--------------------------

a. Describa situaciones donde es conveniente utilizar la metodología conocida
   como test de comparación de medias en dos muestras apareadas.

   .. class:: underline

        El objetivo del apareamiento consiste en hacer más precisa la
        comparación entre los tratamientos, teniendo en cuenta que los miembros
        del par sean lo más parecido posible y que la única diferencia que se
        encuentre en las mediciones efectuadas sobre ellos se deba
        exclusivamente al tratamiento en estudio.

b. ¿Cuáles son los supuestos que se deben establecer para aplicar un test t
   de comparación de medias en el caso de muestras independientes y muestras
   dependientes?

   .. class:: underline

        **Muestras independientes**

        Los errores :math:`e_{i}` se distribuyen normalmente con media 0
        y varianza :math:`{\sigma^2}_{e}`

        Las variables :math:`t_{j}` y :math:`e_{i}` deben ser variables
        no correlacionadas.

        Igualdad de varianzas para los dos grupos en estudio.

        **Muestras dependientes o apareadas**

        Los errores ei se distribuyen normalmente con media 0 y varianza
        :math:`{\sigma^2}_{\theta}`

        Las variables :math:`t_{j}` y :math:`e_{i}` deben ser variables
        no correlacionadas.

c. ¿Cuándo se deben comparar más de dos medias?, ¿por qué es conveniente
   utilizar la metodología conocida como análisis de la varianza y no
   realizar comparaciones de a pares de medias por medio de tests t?

   .. class:: underline

        Cuando el investigador desea comparar varias poblaciones,
        la primera idea que puede surgir es la de efectuar todas las
        comparaciones  posibles considerando las medias de a pares.
        Es decir, si compara, por ejemplo, 5 marcas de herbicida, digamos A,
        B, C,  D y E, podría efectuar las comparaciones de la siguiente manera:

        :math:`\mu_{A} - \mu_{B}, \mu_{A} - \mu_{C} , \mu_{A} - \mu_{D} , \mu_{B} - \mu_{C} , \mu_{B} - \mu_{D}` , etc.

        Luego, si el investigador cuenta con 5 muestras, deberá realizar 10
        test o tantos como :math:`{C^2}_{5} = 10`.

        Pero, aunque el investigador se tome el trabajo de realizar 10 test de
        hipótesis no podría generalizar simultáneamente sus resultados a las
        5 poblaciones de las cuales se extrajeron las muestras.

        Puede demostrarse que este tedioso procedimiento conduce a conclusiones
        erróneas.

d. ¿Por qué en el análisis de la varianza se utiliza un test F de comparación
   de varianzas cuando la hipótesis a probar está referida a la igualdad de
   medias poblacionales?

   .. class:: underline

        Devido a que la característica, tal vez más importante, del
        análisis de la varianza es que mediante este procedimiento
        "inferimos" la igualdad de medias a través de la igualdad de varianzas


e. ¿Qué diferencias presentan los Modelos I y II del análisis de la varianza?

   .. class:: underline

        Cuando el ANOVA considera fectos fijados por el investigador, el
        análisis se denomina ANOVA Modelo I.

        Por otro lado el ANOVA Modelo II en el que los efectos añadidos
        para cada grupo no son tratamientos fijados deliberadamente por el
        investigador sino efectos aleatorios.

f. En un modelo de análisis de la varianza, ¿cuál es la variable dependiente y
   cuál la variable independiente?

   .. class:: underline

        :math:`t_{j}` es la variable dependiente.

        :math:`e_{ij}` es la variable independiente.


g. ¿Cuáles son los supuestos a considerar en un Modelo I de análisis de la
   varianza y en un Modelo II?

   .. class:: underline

        **Modelo I**

        :math:`\mu` es constante para todos los tratamientos y todas las
        mediciones. La componente :math:`\mu` en el Modelo I es una
        componente desconocida.

        :math:`t_{j}` es constante para todas las mediciones dentro de un
        nivel de tratamiento pero puede diferir para otros niveles de
        tratamiento.

        :math:`e_{ij}` es una variable aleatoria distribuida normal e
        independientemente con media 0 y varianza constante
        :math:`\sigma^2` para todo j.

        **Modelo II**

        Los supuestos del modelo estadístico son los mismos que se han
        explicado en el caso de Modelo I. La única distinción es que se ha
        agregado ahora el supuesto de que la variable aleatoria se
        distribuye normalmente con media 0 y varianza :math:`{\sigma^2}_{a}`


|hamster| Actividad nro. 2
--------------------------

Un grupo de 4 pares de hermanos gemelos se los dividió en dos grupos. A uno
de los hermanos se les enseñó una técnica nueva para resolver ciertos
problemas matemáticos y al otro grupo se les aplicó la técnica estándar que
se venía utilizando. Los resultados en un examen realizado después de cierto
tiempo de aprendizaje fueron los siguientes:

 .. csv-table::
    :header-rows: 1

    Técnica estándar, Técnica nueva
    63, 62
    75, 80
    60,71
    85, 92


¿Qué puede decir acerca de los resultados obtenidos en cada uno de los grupos
considerados?

.. figure:: figs/act2.png
    :align: center
    :scale: 50 %

    Salida de PSPP

.. class:: underline

    Calculando T'=14 y T''=22 se rechaza la hipótesis nula  con lo cual
    concluimos que la técnica nueva genera una diferencia en el rendimiento
    a la técnica est'andar.


|hamster| Actividad nro. 3
--------------------------

Los siguientes datos representan los tiempos que demoran cajas de velocidad
desde la línea de producción hasta el almacenamiento en lugares previamente
especificados. Se rastrean muestras de 5 embarques por día y se anota el
tiempo que tardan en recorrer este ciclo. Las muestras se seleccionan a
ciertas horas elegidas al azar y se registra el tiempo en minutos.
El objetivo consiste en estudiar la variabilidad del proceso de
almacenamiento. Los datos registrados durante 10 días fueron los siguientes:

.. csv-table:: Datos
    :header-rows: 1

    Día,Hora 1,Hora 2,Hora 3,Hora 4,Hora 5
    1,27,43,49,32,36
    2,34,29,34,31,41
    3,36,32,48,35,33
    4,31,41,51,51,34
    5,43,35,30,32,31
    6,28,42,35,40,37
    7,38,37,41,34,44
    8,28,44,44,34,50
    9,44,36,38,44,24
    10,30,43,37,29,21

a) ¿Qué conclusiones puede obtener de estos registros?

.. figure:: figs/act3.png
    :align: center
    :scale: 150 %

    Salida de PSPP

.. class:: underline

    No ve ninguna diferencia significativa entre las diferentes horas que
    fueron tomadas las demoras.

b) Explique detalladamente la metodología que utiliza y
   justifique su utilización.

.. class:: underline

    Se decidió utilizar el modelo I de ANOVA. Ya que los días solamente se
    usaron para enumerar las mediciones, y por lo que se describe ni siquiera
    se menciona si esos días fueron consecutivos o pertenecen a algún ciclo
    importante.


|hamster| Actividad nro. 4
--------------------------

Un estudio de comprensión de lectura en niños tuvo como objetivo la
comparación de 3 métodos de enseñanza. Como es común en este tipo de estudio,
varias variables pretest fueron medidas antes de que se de alguna instrucción.
El propósito de uno de los pretest fue ver si los tres grupos de niños eran
similares en cuanto a sus habilidades de comprensión. Se usaron tres métodos
llamados basal, DRTA y estrategias. A cada método que mide la habilidad de
comprensión se asignaron al azar 22 niños.

Los puntajes obtenidos fueron los siguientes:

.. csv-table:: Datos
    :header-rows: 1

    Basal,DRTA,Estrategias
    4,7,11
    6,7,7
    9,12,4
    12,10,7
    16,16,7
    15,15,6
    14,9,11
    12,8,14
    12,13,13
    8,12,9
    13,7,12
    9,6,13
    12,8,4
    12,9,13
    12,9,6
    10,8,12
    8,9,6
    12,13,11
    11,10,14
    8,8,8
    7,8,5
    9,10,8

Analice las salidas de computación que se dan al final de las actividades y
efectúe todos los comentarios posibles utilizando todos los conceptos
aprendidos en el estudio del análisis de la varianza.

.. class:: underline

    El primer gráfico muestra por la variación entre grupos, representados por
    las medias de cada grupo juntas en el mismo gráfico.
    Se observa poca variación entre los grupos concentrándose entre los
    valores ~9.2 y ~10.5

    El segundo gráfico muestra la variabilidad en cada grupo. Siendo la
    distribución más variable la de estrategias. Tanto Basal como DRTA tienen
    una variación parecida pero DRTA es marcadamente asimétrica positiva.

    El tercer gráfico demuestra que se cumple el supuesto de normalidad de
    errores. Ya que los residuales se ubican aprox a 45°.

    El último gráfico demuestra que se cumple el supuesto de independencia de
    errores. Ya que los valores no presentan un patrón en distribución.


|hamster| Actividad nro. 5
--------------------------

Los siguientes datos se refieren a una información ampliada del estudio de
métodos de lectura considerado en la actividad anterior. A los alumnos de cada
grupo se les tomaron 5 pretest cuyos puntajes se dan a continuación.

- B: Basal
- D: DRTA
- E: Estrategias

.. csv-table:: Datos
    :header-rows: 1

    Grupo,Pretest 1,Pretest 2,Pretest 3,Pretest 4,Pretest 5
    B,4,3,5,4,1
    B,6,5,9,5,1
    B,9,4,5,3,3
    B,12,6,8,5,6
    B,16,5,10,9,6
    B,15,13,9,8,5
    B,14,8,12,5,5
    B,12,7,5,5,2
    B,12,3,8,7,3
    B,8,8,7,7,9
    B,13,7,12,4,2
    B,9,2,4,4,5
    B,12,5,4,6,9
    B,12,2,8,8,4
    B,12,2,6,4,6
    B,10,10,9,10,9
    B,8,5,3,3,10
    B,12,5,5,5,5
    B,11,3,4,5,6
    B,8,4,2,3,10
    B,7,3,5,4,4
    B,9,6,7,8,2
    D,7,2,7,6,1
    D,7,6,5,6,10
    D,12,4,13,3,8
    D,10,1,5,7,10
    D,16,8,14,7,2
    D,15,7,14,6,8
    D,9,6,10,9,9
    D,8,7,13,5,3
    D,13,7,12,7,8
    D,12,8,11,6,3
    D,7,6,8,5,5
    D,6,2,7,0,5
    D,8,4,10,6,7
    D,9,6,8,6,3
    D,9,4,8,7,7
    D,8,4,10,11,10
    D,9,5,12,6,4
    D,13,6,10,6,1
    D,10,2,11,6,9
    D,8,6,7,8,7
    D,8,5,8,8,9
    D,10,6,12,6,9
    E,11,7,11,12,3
    E,7,6,4,8,7
    E,4,6,4,10,1
    E,7,2,4,4,9
    E,7,6,3,9,3
    E,6,5,8,5,5
    E,11,5,12,8,10
    E,14,6,14,12,8
    E,13,6,12,11,9
    E,9,5,7,11,2
    E,12,3,5,10,8
    E,13,9,9,9,2
    E,4,6,1,10,4
    E,13,8,13,1,8
    E,6,4,7,9,1
    E,12,3,5,13,3
    E,6,6,7,9,4
    E,11,4,11,7,8


a) Compare los puntajes promedios del pretest 1 y del pretest 2 para los
   alumnos considerados en el grupo basal.

   .. figure:: figs/act5a.png
       :align: center
       :scale: 150 %

       PSPP Output


.. class:: underline

    El promedio es superior en el ptest 1 es muy superior al 2.


b) Compare los puntajes promedios del pretest 2 y del pretest 3 para los
   alumnos considerados en el grupo DRTA.

   .. figure:: figs/act5b.png
       :align: center
       :scale: 150 %

       PSPP Output


.. class:: underline

    El promedio es superior en el ptest 3 es muy superior al 2.


c) Compare los puntajes promedios del pretest 3 y del pretest 5 para el grupo
   estrategias.

   .. figure:: figs/act5c.png
       :align: center
       :scale: 150 %

       PSPP Output


.. class:: underline

    El promedio es superior en el ptest 3 es muy superior al 5.


d) Compare los puntajes promedios del pretest 2 y del pretest 4 para el grupo
   basal.

   .. figure:: figs/act5d.png
       :align: center
       :scale: 150 %

       PSPP Output

.. class:: underline

    No parece haber una diferencia significativa en los dos tests.


|hamster| Actividad nro. 6 (OPTATIVA)
-------------------------------------

Un organismo dedicado a la actividad forestal desea determinar el efecto que
producen tres métodos de preparación del terreno sobre el crecimiento de pinos
en el primer año.

Para llevar a cabo la experiencia se seleccionaron 4 localidades y en cada una
de ellas se tomó un terreno al que se dividió en tres parcelas. Como se
esperaba que la fertilidad del suelo fuese más homogénea dentro de cada
localidad que entre las localidades, se utilizó un diseño en bloques
aleatorizados tomando las distintas localidades como bloques.

Los métodos de preparación del terreno fueron:

- **Método A:** ninguna preparación
- **Método B:** preparación ligera
- **Método C:** preparación fuerte

Las preparaciones del terreno fueron aplicadas al azar a las parcelas dentro
de cada localidad. En cada parcela se sembró la misma cantidad de árboles y
se observó su crecimiento promedio durante el primer año.

Los resultados obtenidos fueron:

.. csv-table:: Datos
    :header-rows: 1

    Preparación del terreno,Localidad 1,Localidad 2,Localidad 3,Localidad 4
    A,11,13,16,10
    B,15,17,20,12
    C,10,15,13,10


a) Proporcionan los datos suficiente evidencia que indique que hay diferencias
   entre los crecimientos medios correspondientes a las tres preparaciones del
   terreno?
b) Obtenga todas las conclusiones posibles del estudio.


|hamster| Actividad nro. 7 (OPTATIVA)
-------------------------------------

El Departamento de Control de Calidad de una fábrica dedicada a la confección
de camisas de hombres desea estudiar el efecto de dos factores sobre el teñido
de camisas de fibra sintética.

Los factores en estudio fueron:

- **Temperatura**: 300 "C y 350 "C
- **Tiempo del ciclo**: 40, 50 y 60 minutos

En cada combinación de los factores se analizaron 9 muestras de tejido y se
evaluó la calidad del teñido, asignando un índice de acuerdo a la comparación
con una calidad de teñido estándar.

Los resultados obtenidos fueron:

.. image:: figs/datos_act7.png
    :align: center
    :scale: 200 %

Efectúe un análisis conveniente de los datos y obtenga todas las conclusiones
posibles.


|hamster| Actividad nro. 8
--------------------------

Un investigador en biología está estudiando la evolución de la altura de
plantas sometidas a una fertilización en particular. Efectuando un experimento
en invernadero, siembra semillas de la planta en estudio en 9 macetas
previamente acondicionadas. El investigador efectúa mediciones de la altura de
cada planta (en cm.) a los 10, 15 y 20 días después de la germinación.

Los resultados obtenidos fueron:

.. csv-table:: DATOS
    :header-rows: 1

    Planta Nro.,10 días,15 días,20 días
    1,"3,2","3,7","4,2"
    2,"3,4","3,9","4,4"
    3,3,"3,3","3,6"
    4,"3,1","3,5",4
    5,"3,5","3,9","4,3"
    6,"3,3","3,7","4,1"
    7,"3,2","3,3","3,6"
    8,3,"3,1","3,5"
    9,"3,6",4,"4,4"

Aplique una metodología de análisis de la varianza conveniente para determinar
si existen diferencias significativas entre los promedios de altura de plantas
en los diferentes días considerados por el investigador.

.. class:: underline

    Se aplico ANOVA con dos factores con medias repetidas sobre la misma unidad
    experimental. La salida de SPSS se adjunta como *Apéndice - Actividad 8*

    Se observa un crecimiento en las medias y el desvio estandat de los
    Por otro lado se observa que los individuos no
    están creciendo igual ya que el residuo es mucho menor que los efectos.


|hamster| Actividad nro. 9
--------------------------

Los siguientes datos se obtuvieron en un estudio de nutrición donde se
asignaron pacientes aleatoriamente a dos dietas alimenticias.

.. csv-table:: DATOS
    :header-rows: 1

    Dieta,Peso inicial,Peso final,Dieta,Peso inicial,Peso final
    A,"94,07","86,59",B,"88,02","84,12"
    A,"96,79","93,08",B,"88,22","86,13"
    A,"92,15","87,85",B,"103,45","101,21"
    A,"92,3","86,83",B,"82,94","79,08"
    A,"96,5","92,7",B,"89,71","86,19"
    A,"83,11","76,8",B,"94,83","91,93"
    A,"91,16","83,4",B,"81,93","78,97"
    A,"90,81","86,74",B,"83,41","78,89"
    A,"81,37","77,67",B,"73,59","69,76"
    A,"89,81","85,7",B,"108,47","104,2"
    A,"84,92","79,96",B,"72,67","70,01"
    A,"84,43","79,8",B,"96,84","93,66"
    A,"86,33","81,15",B,"88,48",87
    A,"87,6","81,92",B,"89,57","87,24"
    A,"81,08","76,32",B,"85,22","82,09"
    A,"92,07","90,2",B,"103,76","102,24"
    A,"81,14","73,34",B,"87,84","84,66"
    A,"96,87","93,58",B,"91,5","88,95"
    A,"99,59","92,36",B,"93,04","88,73"
    A,"83,9","77,23",B,"92,14","88,07"
    A,"89,41","85,45",B,"85,26","81,36"
    A,"85,31","84,59",B,"89,42","86,64"
    A,"89,25","84,89",B,"92,42","88,99"
    A,"93,2","93,1",B,"93,13","89,73"
    A,"89,17","86,87",B,"80,86","77,81"
    A,"93,51","86,36",B,"88,75","85,93"
    A,"88,85","83,24",B,"95,02","91,9"
    A,"88,4","81,2",B,"92,29","91,28"
    A,"82,45","77,18",B,"89,43","87,22"
    A,"96,47","88,61",B,"93,32","89,77"
    A,"99,48","94,67",B,"92,88","89,38"
    A,"99,95","93,87",B,"89,88",88
    A,"100,05","94,15",B,"82,25","80,81"
    A,"87,33","82,17",B,"88,99","86,87"
    A,"87,61","86,01",B,"82,07","79,74"
    A,"89,28","83,78",,,
    A,"89,72","83,56",,,
    A,"95,57","89,58",,,
    A,"97,71","91,35",,,
    A,"98,78","97,82",,,

Prueba efectividad de cada una de las dietas.

.. class:: underline

    Se procede con dos análisis de cada muestra por separado considerándolas
    apareadas para verificar la efectividad de cada dieta.

.. figure:: figs/act9a.png
    :align: center
    :scale: 150 %

    Salida PSPP Dieta A


.. figure:: figs/act9b.png
    :align: center
    :scale: 150 %

    Salida PSPP Dieta B

.. class:: underline

    Se observa que ambas dietas muestran una diferencia significativa en el
    cambio de peso de las personas. Sin embargo la dieta 8 mantiene menos
    variación al momento del descenso del peso (la disminución de peso fue mas
    uniforme en la dieta B en proporción que la dieta A). También la dieta
    B mostró un error mayor en sus estimaciones por ser de menor tamaño

|hamster| Actividad nro. 10
---------------------------

En el módulo 1 del curso aparece una publicación titulada “Riesgo
cardiovascular global de una población en un programa de prevención primaria”.
En la página 4, aparece una tabla cuyo título es: Media y desviación estándar
de parámetros evaluados en el total de la población según sexo. Pruebe si
existen diferencias significativas en los parámetros promedios según sexo.

En la página 7, aparece una tabla cuyo título es: Tabaquismo con respecto a
riesgo cardiaco global. Pruebe si la proporción de pacientes con riesgo
cardiaco medio es la misma en fumadores y no fumadores.

.. class:: underline

    **Primera Parte**

    Se adjunta la salida de SPSS como apéndice 10A.

    Con un enfoque de muestras apareadas en un anova de múltiples factores
    se verifica que no existe diferencias significativas, ni en cada factor
    por separado (medidas y sexo) ni en la interacción de los mismos. Todos
    los valores de sig dan > a 0.05.


.. figure:: figs/act10b.png
    :align: center
    :scale: 160 %

    Salida de PSPP para analisis de Wilcoxon y Mann-Withney


.. class:: underline

    **Segunda Parte**

    Al parecer el riesgo medio es el mismo tanto en fumadores como
    no fumadores.


.. ============================================================================
.. FOOTER
.. ============================================================================

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###

