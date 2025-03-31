.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Guía Rápida de Usuario
========================

Pinout
------------

.. image:: img/pipower3_pinout.png
  :width: 800
  :align: center

1. :ref:`power_input`: Entrada de alimentación externa, puede alimentar directamente la Raspberry Pi mientras carga la batería.
2. :ref:`cap_onoff`: Selecciona si debe iniciarse automáticamente cuando se conecta la entrada de alimentación externa durante el estado de apagado.
3. :ref:`cap_sdsig`: Señal de apagado, conectar el pin 26 al pin central con un capuchón de puente conecta **SDSIG** al GPIO26 de la Raspberry Pi. Una vez configurado, si la Raspberry Pi se apaga, GPIO26 se eleva, indicando que PiPower 3 debe apagarse.
4. :ref:`cap_btn`: Puente para botón de encendido externo, utilizado para el botón de encendido externo.
5. **LED de PWR**: LED de estado de salida, se ilumina cuando la salida está activada.
6. **LED de BAT**: El LED iluminado indica que la batería está suministrando energía. En este momento, debes monitorear el nivel de la batería para evitar daños por sobre-descarga.
7. :ref:`power_button`: Botón de encendido integrado para controlar la energía de la placa:

  * **Presión corta**: Activa la salida.
  * **Mantén presionado durante 2 segundos, hasta que se iluminen los dos LEDs de batería del medio, luego suelta**: Envía una solicitud de apagado a través de I2C.
  * **Sigue presionando por más de 5 segundos**: Apaga directamente la salida.

8. :ref:`battery_indicators`: Indica el nivel de batería y el estado de carga.
9. **Conector I2C**: Terminal SH1.0 4P, compatible con **qwIIC** y **STEMMA QT**.
10. **Pines I2C**: 1x4P encabezados de 2.54 pines.
11. **Salida Tipo A**: Interfaz de salida de 5V.
12. **Pines 5V/GND**: 2 x 4P encabezados de 2.54 pines.
13. :ref:`pin_header`: Encabezados de pines para Raspberry Pi, se conecta directamente a la Raspberry Pi.
14. :ref:`battery_connector`: Conector de batería XH2.54 3P.
15. **LEDs de advertencia**: Si la batería está invertida, se iluminan dos LEDs rojos, advirtiendo sobre la inversión de la batería.

Pasos de Operación
----------------------

1. Carga el PiPower 3.

Antes de usar tu PiPower 3, cárgalo completamente. Una carga completa previene problemas con la batería y asegura un rendimiento óptimo.

Para cargarlo, usa un cargador PD 5V/3A, como la fuente de alimentación oficial de 27W de Raspberry Pi. Esto permite que el PiPower 3 entregue una corriente máxima de 3A.

.. image:: img/power_input.jpg
  :width: 500
  :align: center

Verás que el indicador de carga parpadea durante el proceso de carga.

.. image:: img/battery_indicator.jpg
  :width: 500
  :align: center

* **4 LEDs iluminados**: Batería >80%
* **3 LEDs iluminados**: 60%< Batería <80%
* **2 LEDs iluminados**: 40%< Batería <60%
* **1 LED iluminado**: 20%< Batería <40%
* **Primer LED parpadeando**: Batería <20%
* **LEDs iluminándose en ciclo**: Cargando
* **Dos LEDs centrales parpadeando**: Esperando la señal de apagado
* **Todos los LEDs apagados**: Sin alimentación o en modo de reposo

2. Suministra energía a la placa principal.

Si estás usando una Raspberry Pi, no es necesario realizar conexiones adicionales.

Para otras placas principales, puedes conectarlas al puerto de salida Tipo A del PiPower 3 o usar dos cables de puente.

.. image:: img/output_mainboard.jpg
    :width: 500
    :align: center

.. image:: img/output_mainboard_pin.jpg
    :width: 400
    :align: center

3. Presiona el botón de encendido una vez para alimentar tu placa principal.

Verás que el **LED de PWR** se ilumina, y tu placa principal recibirá energía del PiPower 3.

.. image:: img/pwr_led.png
    :width: 500
    :align: center


4. Para apagar la energía después de usarla.

  * **Sigue presionando por más de 5 segundos**: Apaga directamente la salida.
  * **Mantén presionado durante 2 segundos, hasta que se iluminen los dos LEDs de batería del medio, luego suelta**: Si has configurado el :ref:`pipower_software`, esta acción enviará una solicitud de apagado a través de I2C para un apagado seguro.

.. note::

    Cuando el cable de alimentación Tipo C aún esté conectado, el indicador de batería continuará mostrando el estado de carga hasta que la carga se complete.

.. _pipower_software:

Configuración del Software
------------------------------------

Además de usar PiPower 3 directamente, también puedes utilizar nuestra biblioteca proporcionada para monitorear los voltajes de entrada y salida, corriente, voltaje de la batería, porcentaje, fuente de alimentación, estado de carga y otros datos internos, como las solicitudes de apagado.

Por favor, elige el tutorial correspondiente según tu placa principal.

.. toctree::
    :maxdepth: 2

    use_with_rpi
    use_with_pico_esp32
    use_with_arduino

    
