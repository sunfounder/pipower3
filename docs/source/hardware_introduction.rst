.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Introducción al Hardware
===========================

Tabla de Especificaciones
-----------------------------

.. list-table:: 
   :widths: 30 10 10 10 10

   * - Parámetro
     - Mín
     - Típico
     - Máx
     - Unidad
   * - Corriente de apagado de la batería
     - \-
     - \-
     - 60
     - uA
   * - Corriente en reposo de la batería
     - \-
     - 25
     - \-
     - mA
   * - Voltaje de salida DC-DC
     - 5.1957
     - 5.2855
     - 5.3766
     - V
   * - Protección por sobretemperatura DC-DC
     - \-
     - 150
     - \-
     - ℃
   * - Corriente de carga de la batería
     - \-
     - \-
     - 1
     - A
   * - Protección por sobretemperatura durante la carga
     - \-
     - 135
     - \-
     - ℃
   * - Umbral de conmutación de bajo voltaje de entrada
     - 4.54
     - 4.63
     - 4.72
     - V
   * - Corriente de balanceo
     - \-
     - 40
     - \-
     - mA
   * - Voltaje de activación del balanceo
     - \-
     - 4.1
     - \-
     - V

Diagrama de Visión General
-----------------------------

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

.. _power_button:

Botón de Encendido
----------------------

.. image:: img/power_button.jpg
  :width: 500
  :align: center

Botón de encendido integrado para controlar la energía de la placa:

* **Presión corta**: Activa la salida.
* **Mantén presionado durante 2 segundos, hasta que se iluminen los dos LEDs de batería del medio, luego suelta**: Envía una solicitud de apagado a través de I2C.
* **Sigue presionando por más de 5 segundos**: Apaga directamente la salida.

.. _battery_indicators:

Indicadores de Batería
--------------------------------

Cuatro LEDs integrados indican el nivel de la batería y el estado de carga. Ten en cuenta que, si se está cargando durante el apagado, la luz del indicador seguirá mostrando el estado de carga hasta que la carga esté completa.

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

.. _power_input:

Entrada de Alimentación
-------------------------

.. image:: img/power_input.jpg
  :width: 500
  :align: center

Si se usa en Raspberry Pi, la entrada de alimentación debe ser de una fuente USB PD que soporte 5V/3A, como la fuente de alimentación oficial de 27W de Raspberry Pi (recomendada). De lo contrario, con un consumo alto, la batería puede no cargarse o incluso agotarse hasta el punto de no poder suministrar energía.

El **LED de BAT** puede confirmar si la batería está actualmente suministrando energía externamente para asegurar la seguridad de la batería, de modo que la batería siga alimentada en caso de un corte de energía, funcionando como un UPS.

.. image:: img/bat_led.jpg
  :width: 500
  :align: center

**Ruta de Alimentación**

PiPower 3 integra una funcionalidad de ruta de alimentación, cambiando automáticamente las rutas de energía para reducir el desgaste de la batería y cambiar la alimentación sin interrupciones.

* Con alimentación externa conectada, la salida de 5V proviene directamente de los 5V externos, lo cual puede apagarse. Si las condiciones lo permiten, la alimentación externa también carga la batería (ver corriente de carga).
* Cuando la alimentación se desconecta, el sistema cambia automáticamente a la salida de paso de batería para alimentar el sistema, cambiando sin interrupciones para proteger el sistema durante un corte de energía.

**LED de BAT** puede confirmar si la batería está actualmente suministrando energía externamente.

.. image:: img/bat_led.jpg
  :width: 500
  :align: center

.. _battery_connector:

Conector de Batería
------------------------

Conector de batería XH2.54 3P.

.. image:: img/battery_connector.jpg
  :width: 500
  :align: center


Relacionado con la Carga
---------------------------

**Corriente de Carga**

La corriente máxima de carga se ajusta en función del voltaje de entrada para asegurar el suministro máximo de energía a la Raspberry Pi.

* Cuando está encendido, la corriente de carga se ajusta dinámicamente en función del voltaje de entrada. La corriente máxima de carga es de 1A; si el voltaje de entrada es inferior a 4.63V, se considera que la entrada de energía es insuficiente, y la carga se desactivará. Entre 4.63V-5.2V, el sistema ajustará automáticamente la corriente de carga para asegurar que el voltaje de entrada esté por encima de 4.63V.
* Cuando está apagado, la corriente de carga es de 1A.

**Proceso de Carga**

* Cuando el voltaje total de la batería es inferior a 3.7V, la batería se carga a 50mA.
* Cuando el voltaje total de la batería está entre 3.7V y 6V, la batería se carga a 100mA.
* Cuando el voltaje total de la batería supera los 6V, la batería se carga con la corriente máxima de carga establecida;
* Cuando el voltaje total de la batería se acerca a 8.4V, entra en modo de carga a voltaje constante.
* Después de que la batería esté completamente cargada y la entrada continúe, si el voltaje total de la batería es inferior a 8V, la carga se reiniciará;
* En modo de voltaje constante, si la corriente de carga es inferior a 200mA, se detendrá la carga después de 30 segundos, comprobando si el voltaje de la batería está por encima del voltaje de detención de carga; si es así, se detendrá la carga, si no, se continuará cargando, verificando nuevamente después de 30 segundos.

**Función de Balanceo de Carga**

Durante la carga, el chip de carga monitorea constantemente el voltaje de las dos celdas de la batería. Cuando el voltaje de cualquier celda alcanza el voltaje de activación de balanceo de 4.1V, se activa el MOS interno correspondiente, reduciendo la corriente de carga para esa celda.

Condiciones de apagado del balanceo:

#. Ambos voltajes de las celdas de la batería están por encima del voltaje de activación de balanceo de 4.1V;
#. Se sale del estado de carga normal (por ejemplo, protección NTC, sobrevoltaje de entrada, batería completamente cargada);

**Protección de Temperatura**

* Cuando la temperatura interna del chip de carga supera los 135 grados, la carga se detendrá forzosamente;
* Cuando la temperatura interna del chip DC-DC supera los 150 grados, se apagará el DC-DC;

Comunicación I2C con el MCU
-------------------------------

.. image:: img/i2c_pins.jpg
  :width: 500
  :align: center

Dirección I2C: 0x5a

El MCU integrado recoge diversas señales de la placa y las almacena en registros, los cuales pueden ser accedidos a través de I2C.

* :download:`Register Table </_static/pdf/Register Table.pdf>`

Tabla de registros configurados:

.. image:: img/set_register.png
    :width: 700
    :align: center

.. _cap_onoff:

Encendido/Apagado Predeterminado
------------------------------------

.. image:: img/btn_sdsig_off_on.jpg
  :width: 500
  :align: center

Este puente **ON/OFF** se utiliza para seleccionar: si la salida se activa de forma predeterminada cuando se conecta la alimentación USB después del apagado.

* Si el capuchón del puente está a la izquierda, conectado a OFF, entonces insertar alimentación USB después del apagado no activará la salida.
* Si el capuchón del puente está a la derecha, conectado a ON, entonces insertar alimentación USB después del apagado activará la salida.

Esta función se utiliza típicamente para dispositivos que necesitan estar encendidos de manera predeterminada, como servidores privados: cuando hay un corte de energía, PiPower 3 indica a la Raspberry Pi que se apague. Al esperar el próximo suministro de energía, PiPower 3 activa automáticamente la salida, encendiendo la Raspberry Pi, eliminando la necesidad de operación manual.

Esta función también puede usarse como una función remota de encendido/apagado. Conecta la entrada a un enchufe inteligente o interruptor inteligente. Configura el porcentaje de apagado al 100%. Cuando se necesita apagar remotamente, controla directamente el enchufe inteligente para cortar la energía, PiPower 3 detecta el corte de energía, notifica a la Raspberry Pi para apagarse y luego corta la energía. Cuando se necesita encender remotamente, enciende directamente el interruptor inteligente, PiPower detecta la energía, se enciende de manera predeterminada y puede iniciar la Raspberry Pi, logrando el control remoto del encendido y apagado.

.. _cap_btn:

BTN
---------

.. image:: img/btn_sdsig_off_on.jpg
  :width: 500
  :align: center

Este puente **BTN** es para un botón de encendido externo. Si necesitas instalar PiPower 3 dentro de una carcasa, es posible que no puedas presionar el botón de encendido integrado. En este caso, necesitas un botón externo para encender y apagar la energía. Conecta un interruptor autorecuperante al puente, que puede ser un interruptor táctil o un botón metálico vintage. Después de conectarlo, puedes presionar el botón externo de la misma manera que el botón integrado.

.. _cap_sdsig:

SDSIG
------------

La señal de apagado **SDSIG** involucra tres pines: pin 26, un pin central y un pin GND del lado derecho.

* Si conectas el pin 26 al pin central usando un capuchón de puente, SDSIG se conectará al GPIO26 de la Raspberry Pi. Después de la configuración, si la Raspberry Pi se apaga, el pin GPIO26 se elevará, indicando que SDSIG está en alto, señalizando a PiPower 3 que se apague.
* Si esta función no es necesaria, como en el caso de una computadora de placa única como Arduino o Raspberry Pi Pico, el capuchón del puente debe conectarse a GND.

.. image:: img/btn_sdsig_off_on.jpg
  :width: 500
  :align: center

**SDSIG** es el pin de señal de apagado. Elevar este pin indica que el dispositivo principal está apagado y necesita apagarse. Bajarlo indica que el dispositivo principal está encendido. Si esta función no es necesaria, como con una computadora de placa única como Arduino o Raspberry Pi Pico, el capuchón del puente debe conectarse a GND. Si usas una Raspberry Pi, conecta el capuchón del puente al pin 26, instala el software ``pipower3`` en la Raspberry Pi, y cuando la Raspberry Pi se apague, elevará este pin, señalizando a PiPower 3 que se apague.

.. _pin_header:

Encabezados de Pines para RPi
-------------------------------

Los encabezados de pines para Raspberry Pi se conectan directamente a la Raspberry Pi, incluyendo I2C y alimentación, ver diagrama de pines de Raspberry Pi. Los encabezados se pueden usar para apilar HATs, pero ten en cuenta que I2C y el pin 26 están conectados.

.. image:: img/40pin_header.jpg
  :width: 500
  :align: center

.. list-table:: 
   :widths: 15 15
   :header-rows: 1

   * - Raspberry Pi
     - MCU en la placa
   * - SDA
     - SDA
   * - SCL
     - SCL
   * - GPIO26
     - APAGADO
   * - ID_SD
     - ID_EEPROM SDA
   * - ID_SC
     - ID_EEPROM SCL
  
