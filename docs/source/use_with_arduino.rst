.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Uso con la Placa Arduino
===================================

Si estás usando el PiPower 3 para alimentar tu placa Arduino, puedes conectar la placa Arduino al puerto de salida Tipo A del PiPower 3 o usar dos cables de puente. Conecta la interfaz I2C de la placa utilizando un puente. Si no se requieren operaciones antes de apagar, conecta directamente el capuchón de puente **SDSIG** a GND. Si es necesario realizar operaciones antes del apagado, quita el capuchón de puente y conecta el cable intermedio a un puerto IO en la placa Arduino para notificar a PiPower 3 que puede apagarse de manera segura.

Proporcionamos una biblioteca que te permite monitorear los voltajes de entrada y salida, el voltaje de la batería y el porcentaje, la fuente de alimentación, el estado de carga y otros datos internos.

#. En el IDE de Arduino, abre el **Administrador de Bibliotecas**, busca ``SunFounderPowerControl``, y descárgala e instálala.

    .. image:: img/arduino_library.png

#. Después de la instalación, puedes ir a **Archivo** -> **Ejemplos** -> **SunFounderPowerControl** -> **PiPower 3**, donde encontrarás cuatro ejemplos.

    .. image:: img/arduino_examples.png

    * ``read_all``: Usa este ejemplo si necesitas leer todos los datos a la vez y procesarlos individualmente.
    * ``read_individual``: Si solo necesitas leer ciertos datos, este ejemplo proporciona instrucciones para recuperar datos individuales.
    * ``set_shutdown_percentage``: Este ejemplo enseña cómo establecer un porcentaje de batería para apagado. Esta función envía una señal de apagado al host cuando la batería no se está cargando y cae por debajo del porcentaje configurado. Después de que el host se apague, solo se apagará después de recibir una señal de apagado. Típicamente utilizado con SBCs como Raspberry Pi. Para microcontroladores, quita el capuchón de puente **SDSIG** y conecta el cable intermedio a un pin. Después de apagarse de manera segura al recibir la señal de apagado, eleva este pin para apagar el PiPower 3.
    * ``shutdown_when_request``: Este ejemplo muestra cómo manejar operaciones después de recibir una señal de apagado. Quita el capuchón de puente **SDSIG** y conecta el cable intermedio a un pin.

#. Elige uno de los ejemplos y súbelo a tu placa.

.. note::

    En placas donde los pines I2C pueden modificarse, es necesario cambiar el código en ``Wire.begin()``.

Documentación de la API de la Biblioteca Arduino:

https://github.com/sunfounder/arduino_spc?tab=readme-ov-file#api


