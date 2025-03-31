.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Uso con Placas Raspberry Pi Pico y ESP32
====================================================

Si estás utilizando el PiPower 3 para alimentar tu placa Raspberry Pi Pico o ESP32, puedes conectar la placa Raspberry Pi Pico o ESP32 al puerto de salida Tipo A del PiPower 3 o usar dos cables de puente.

Conecta la interfaz I2C de la placa utilizando un puente. Si no se requieren operaciones antes de apagar, conecta directamente el capuchón de puente **SDSIG** a GND. Si es necesario realizar operaciones antes del apagado, retira el capuchón de puente y conecta el cable intermedio a un puerto IO en la Raspberry Pi Pico o placa ESP32. Esto se utiliza para notificar a PiPower 3 que ha completado el apagado y puede apagarse.

Proporcionamos una biblioteca que te permite monitorear los voltajes de entrada y salida, el voltaje de la batería y su porcentaje, la fuente de alimentación, el estado de carga y otros datos internos.

#. Descarga la biblioteca desde GitHub. Puedes descargarla rápidamente usando el siguiente enlace o visitar: https://github.com/sunfounder/micropython_spc.

    * :download:`micropython_spc <https://github.com/sunfounder/micropython_spc/archive/refs/heads/main.zip>`

#. Después de descargar y descomprimir, sube la carpeta ``spc`` a tu Raspberry Pi Pico o placa ESP32. Se recomienda usar Thonny para este propósito.

    .. image:: img/micropython_upload.png
        :align: center

#. Una vez subida, puedes ejecutar algunos ejemplos de la carpeta ``micropython_spc-main`` para ver los efectos:

    * ``example_pipower_3_read_all.py``: Usa este ejemplo si necesitas leer todos los datos a la vez y procesarlos individualmente.
    * ``example_pipower_3_read_individual.py``: Si solo necesitas leer ciertos datos, este ejemplo proporciona instrucciones para recuperar datos individuales.
    * ``example_pipower_3_set_shutdown_percentage.py``: Este ejemplo enseña cómo establecer un porcentaje de batería para apagado. Esto enviará una señal de apagado al host cuando la batería no se esté cargando y caiga por debajo del porcentaje configurado. El apagado solo ocurrirá después de que el host se haya apagado y haya recibido una señal de apagado. Típicamente usado con SBCs como Raspberry Pi. Para microcontroladores, retira el capuchón de puente **SDSIG** y conecta el cable intermedio a un pin. Después de apagarse de manera segura al recibir la señal de apagado, eleva este pin para apagar el PiPower 3.
    * ``example_pipower_3_shutdown_when_request.py``: Este ejemplo muestra cómo manejar operaciones después de recibir una señal de apagado. Retira el capuchón de puente **SDSIG** y conecta el cable intermedio a un pin.

Documentación de la API de la Biblioteca Micropython:

https://github.com/sunfounder/micropython_spc?tab=readme-ov-file#api
