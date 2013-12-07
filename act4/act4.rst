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

==============================================
ACTIVIDADES INTEGRADORAS  - MÓDULOS  VIII y IX
==============================================

:Autor: Juan B Cabral
:DNI: 28818383
:Email: jbc.develop@gmail.com



En estas actividades les proponemos revisar algunos conocimientos conceptuales
y aplicar conceptos, formas de razonamiento y de cálculo a la resolución de
casos. En cada caso justifique su respuesta en forma breve, pero concisa.


**Actividades**


|hamster| Actividad nro. 1
--------------------------

Algunos conceptos y relaciones sobre estimación de parámetros:

a) ¿En qué difieren la estimación puntual de un parámetro de la estimación por
   intervalo?

    .. class:: underline

        La estimación puntual es un proceso mediante el cual se estima el parámetro
        en un punto, dando un valor específico como estimación; mientras que
        la estimación por intervalos afirma, con una determinada probabilidad, que
        el intervalo (a, b) encierra el verdadero valor de¡ parámetro.
        (pag 29, mod 8)

b) ¿Cómo está relacionado el nivel de confianza con la precisión de la
   estimación?

    .. class:: underline

        Es la probabilidad de que un intervalo contenga el parámetro estimado.
        Por lo cual si aumentamos el nivel de confianza el intervalo crecerá y
        disminuirá su precisión. En otras palabras **b-a** será mas grande.

c) ¿Cómo afecta el tamaño de la muestra a la precisión de la estimación para un
   nivel de confianza dado?

    .. class:: underline

        Al aumentar el tamaño de la muestra, disminuye la amplitud del intervalo de
        confianza, logrando así una mayor precisión en la estimación.
        (pag 36, mod 8)

d) ¿Cree usted que es posible obtener una estimación que sea idéntica al
   parámetro que se estima? ¿Cómo lo puede verificar?

    .. class:: underline

        Desde el punto de vista práctico si es posible, en el punto de vista teórico
        siempre existirá la probabilidad de que no sea exactamente igual. La única
        forma de garantizar el parámetro es a través de un censo.


|hamster| Actividad nro. 2
--------------------------

Los limites de confianza del 95% para :math:`\mu` obtenidos de una muestra dada
fueron 3,84 y 6,24 gs.

a) ¿Es correcto decir que 95 veces de cada 100 la media de la población,
   :math:`\mu`, cae dentro del intervalo comprendido entre 3,81 y 6,24 gs.? Si
   usted no está de acuerdo con esta respuesta, ¿Cuál sería a su criterio la
   interpretación correcta?

    .. class:: underline

        Casi citando pag 32 mod 8; sería mas correcto decir:

        Sobre 100 muestras aleatorias de un cierto tamaño n de una población,
        si en cada una se calcula la medía muestral :math:`\overline{x}` y, a
        partir de ellas, se construyen 100 intervalos de confianza para el
        parámetro que se desea estimar 95 contendrán al verdadero valor
        del parámetro poblacional si ese intervalo esta definido por 3,84 y
        6,24 gs.


|hamster| Actividad nro. 3
--------------------------

Se supone que ciertos tubos de acero tienen un promedio de diámetro externo de
10 pulgadas con una desviación estándar de 0,018 pulgadas.

Se desea probar:
    - H0) :math:`\mu` = 10
    - H0) :math:`\mu` :math:`\neq` 10.

Una muestra aleatoria de 36 tubos determinó: :math:`\overline{x}` = 9,94 pulgadas.

a) Construya un intervalo de confianza del 99% para p.
b) ¿Indica este intervalo el rechazo o no rechazo de H0 con :math:`\alpha` = 0,01?


|hamster| Actividad nro. 4
--------------------------

El Director de Alumbrado Público de cierta ciudad debe efectuar una gran compra
de lámparas. Además del requerimiento de que posean larga vida, el Director
quiere asegurarse de que las lámparas tengan un alto grado de uniformidad.
En principio, basándose en su experiencia, establece que la varianza no debiera
exceder de 250 horas.

Una muestra de 20 lámparas de cierta marca mostró un promedio de vida de
1.000 horas, que se considera satisfactorio, pero una varianza de 300 (horas).

a) ¿Indica este resultado que el Director debe desechar la compra a esa empresa con :math:`\alpha` = 0,05?

    :math:`\sigma^2 = 250`

    :math:`n = 20 \to n-1 = 19`

    :math:`\alpha = 0.05 \to 1-\alpha = 0.95`

    :math:`\overline{x} = 1000`

    :math:`s^2 = 300`

    :math:`\chi^2_{(n-1);(1-\alpha)} = \chi^2_{19;0.95} = 30.1`

    :math:`(n-1) \times \frac{s^2}{\sigma^2} = 19 * \frac{300}{250} = 22.8`

    :underline:`Debería aceptar ya que el resultado del test es inferior al limite impuesto`


b) ¿Obtendría la misma conclusión con :math:`\alpha` = 0,10?  Comente los resultados.

    :math:`\chi^2_{(n-1);(1-\alpha)} = \chi^2_{19;0.90} = 27.2`

    :underline:`Sí, debería aceptar ya que el resultado del test es inferior al limite impuesto`
    :underline:`Al disminuir la confianza, el limite tambien disminuyó`

c) Construya  un intervalo  de confianza  para la varianza poblacional con :math:`\alpha` = 0,05.

    .. math::

        P( \frac{(n-1) \times s^2)}{\chi^2_{(n-1);(1-\alpha/2)}}
           \leq \sigma^2 \leq
           \frac{(n-1) \times s^2)}{\chi^2_{(n-1);(\alpha/2)}} ) = 1 - \alpha

    .. math::

        P( \frac{5700}{32.9} \leq \sigma^2 \leq \frac{5700}{8.9} ) = 1 - 0.5


    .. math::

        P(173.25 \leq \sigma^2 \leq 640.45) = 0.95




.. =============================================================================
.. FOOTER
.. =============================================================================

.. footer::

    Los fuentes y cálculo de tablas se encuentran en:
    http://goo.gl/A1Tq4 - ###Page###
