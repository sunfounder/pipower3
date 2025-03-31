.. note:: 

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Accede antes que nadie a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Uso con Raspberry Pi
========================

Descargar e Instalar el Módulo ``pipower3``
----------------------------------------------------

Descarga el código desde GitHub e instálalo:

.. code-block:: shell
    
    git clone https://github.com/sunfounder/pipower3

    cd pipower3
    sudo python3 install.py

Después de la instalación, se te pedirá reiniciar. Ingresa ``Y`` y presiona Enter para reiniciar. Tras reiniciar, el servicio de apagado seguro comenzará automáticamente. Si se presiona el botón durante 2 segundos o si la batería está baja, la Raspberry Pi se apagará y notificará a PiPower 3 para que apague la alimentación.

Configurar el Porcentaje de Apagado
------------------------------------

PiPower 3 envía una solicitud de apagado "BAJA BATERÍA" a través de I2C al host cuando no hay alimentación externa y el voltaje de la batería cae por debajo del porcentaje de apagado. El host puede leer la señal de solicitud de apagado a través de I2C, y si se detecta "BAJA BATERÍA", puede procesar el apagado.

Después de apagarse, elevar el ``SDSIG`` apagará el PiPower. Esto implementa la función de apagado por baja batería de PiPower 3.

.. note::

    Si usas una Raspberry Pi, si la potencia utilizada es mayor a 3A, la batería no podrá mantener la alimentación durante mucho tiempo. Se recomienda configurar el porcentaje de apagado a 100%, es decir, notificar a la Raspberry Pi para que se apague inmediatamente cuando se desconecte la alimentación externa, para proteger la Raspberry Pi y los datos.

Puedes configurar el porcentaje de apagado usando el comando, por ejemplo, configurándolo al 30%. Cuando el nivel de la batería esté por debajo del 30%, PiPower3 apagará la Raspberry Pi después de que esta se apague.

.. code-block:: shell
    
    pipower3 -sp 30 

Ver las Configuraciones Básicas
----------------------------------------

Puedes usar el comando ``pipower3`` para ver la información actual, el tutorial de uso detallado es el siguiente:

.. code-block::

    usage: pipower3-service [-h] [-sp [SHUTDOWN_PERCENTAGE]] [-pp [POWER_OFF_PERCENTAGE]] [-so SHUTDOWN_OVERRIDE] [-iv] [-ov] [-bv] [-bp] [-bs] [-ii] [-ib] [-ic] [-ao] [-sr] [-bi]
                            [-psv] [-a]
                            [command]

    PiPower 3

    positional arguments:
    command               Command

    options:
    -h, --help            show this help message and exit
    -sp [SHUTDOWN_PERCENTAGE], --shutdown-percentage [SHUTDOWN_PERCENTAGE]
                            Set shutdown percentage, leave empty to read
    -iv, --input-voltage  Read input voltage
    -ov, --output-voltage
                            Read output voltage
    -bv, --battery-voltage
                            Read battery voltage
    -bp, --battery-percentage
                            Read battery percentage
    -bs, --battery-source
                            Read battery source
    -ii, --is-input-plugged_in
                            Read is input plugged in
    -ic, --is-charging    Read is charging
    -do, --default-on     Read default on
    -sr, --shutdown-request
                            Read shutdown request
    -a, --all             All

Configurar con Python
-------------------------------

PiPower 3 usa la biblioteca ``spc``, que te permite obtener datos y establecer parámetros en Python. La biblioteca ``spc`` se instala en un entorno virtual, por lo que primero necesitas ingresar al entorno virtual.

.. code-block:: shell

    source /opt/pipower3/venv/bin/activate

Si no deseas ingresar al entorno virtual, puedes reinstalar ``spc`` en el sistema, lo cual debe ser confirmado con ``--break-system`` debido a posibles conflictos con otras bibliotecas:

.. code-block:: shell

    sudo pip3 install --break-system git+http://github.com/sunfounder/spc.git

O si prefieres instalarla en tu propio entorno virtual, simplemente ejecuta el comando de instalación después de ingresar a tu entorno virtual:

.. code-block:: shell

    pip3 install git+http://github.com/sunfounder/spc.git

Ahora puedes ejecutar ejemplos:

.. code-block:: shell

    cd ~/pipower3/examples

.. code-block:: shell

    python3 read_all.py

* ``read_all.py``: Usa este ejemplo si necesitas leer todos los datos a la vez y procesarlos individualmente.
* ``read_individual.py``: Si solo necesitas leer ciertos datos, este ejemplo proporciona instrucciones para recuperar datos individuales.
* ``set_shutdown_percentage.py``: Este ejemplo enseña cómo establecer un porcentaje de batería para apagado, el cual envía una señal de apagado al host cuando no hay carga y la batería cae por debajo de este valor. Después de que el host se apague, recibe una señal de apagado antes de apagarse completamente. Típicamente utilizado con SBCs como Raspberry Pi. Los microcontroladores que necesiten usar esta función deben retirar el capuchón del puente SDSIG y conectar el cable intermedio a un pin. Después de recibir la señal de apagado y apagarse de manera segura, eleva este pin para apagar PiPower 3.
* ``shutdown_when_request``: Este ejemplo muestra cómo manejar las operaciones después de recibir una señal de apagado. Retira el capuchón del puente SDSIG y conecta el cable intermedio a un pin.

Documentación de la API de la Biblioteca Python:

https://github.com/sunfounder/spc?tab=readme-ov-file#api

