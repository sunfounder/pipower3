.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

SunFounder |link_PiPower| - Protege tu dispositivo y datos
================================================================================

* |link_PiPower_3| 

Gracias por elegir nuestro |link_PiPower|.

.. note::
    Este documento está disponible en los siguientes idiomas.

        * |link_german_tutorials|
        * |link_jp_tutorials|
        * |link_en_tutorials|
        * |link_fr_tutorials|
        * |link_es_tutorials|
        * |link_it_tutorials|
    
    Haz clic en los enlaces respectivos para acceder al documento en tu idioma preferido.

.. image:: img/pipower3_picture.jpg
    :width: 400
    :align: center


PiPower 3 es una solución UPS completa, que incluye gestión de rutas de energía, carga y descarga para baterías de litio duales, protección contra inversión de polaridad, sobrecarga y descarga profunda.

Ofrece una salida robusta de 5V/3A y está configurado con HAT+ para garantizar una compatibilidad perfecta con Raspberry Pi. Además, incluye una salida USB Tipo-A y un encabezado 2x4P para salida de energía, lo que lo hace adecuado también para otras SBC, así como para plataformas Arduino y Pico, ESP32.

Un microcontrolador integrado gestiona el encendido y apagado, y a través de la comunicación I2C, puede monitorear el voltaje de entrada, el voltaje de salida, el voltaje de la batería, el nivel de batería, si hay alimentación externa conectada, el estado de carga y si la energía es suministrada por la batería o por USB.

El PiPower 3 asegura que tus proyectos mantengan la energía con una gestión avanzada de baterías y una compatibilidad versátil, convirtiéndolo en una herramienta esencial para cualquier entusiasta de la tecnología que desee mejorar su configuración de hardware.

**Características**

* **Entrada**: 5V/3A, USB Tipo-C con soporte PD
* **Salida**: 5V/3A, compatible con GPIO de Raspberry Pi, USB Tipo-A y un encabezado 2x4P 2.54
* **Potencia de carga**: 7.4V/1A
* **Especificaciones de la batería**: 7.4V 2 celdas 18650 Li-ion, conector XH2.54 3P
* Capuchón de puente predeterminado en ON, encabezado de extensión para botón externo, puente de señal de apagado
* Indicadores integrados para nivel de batería, fuente de entrada, estado de energía, inversión de polaridad y salida de energía
* Microcontrolador RISC-V de 32 bits integrado, que soporta comunicación I2C
* **Interfaces de comunicación I2C**: GPIO de Raspberry Pi, SH1.0 4P (compatible con Qwiic, STEMMA QT) y encabezado 1x4P 2.54


**Contenido**

.. toctree::
    :maxdepth: 2

    About this Kit <self>
    assembly_instructions
    quick_user_guide
    hardware_introduction
    battery
    fan
    compatible_sbc


**Aviso de Copyright**

Todos los contenidos, incluidos pero no limitados a textos, imágenes y códigos en este manual, son propiedad de la empresa SunFounder. Solo deberías utilizarlo para estudio personal, investigación, disfrute u otros fines no comerciales o sin fines de lucro, bajo las regulaciones y leyes de derechos de autor correspondientes, sin infringir los derechos legales del autor y los titulares de derechos relevantes. Para cualquier persona o entidad que utilice estos para obtener ganancias comerciales sin permiso, la empresa se reserva el derecho de tomar acciones legales.

