.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Verwendung mit Raspberry Pi
================================

Herunterladen und Installieren des ``pipower3`` Moduls
--------------------------------------------------------------

Laden Sie den Code von GitHub herunter und installieren Sie ihn:

.. code-block:: shell
    
    git clone https://github.com/sunfounder/pipower3

    cd pipower3
    sudo python3 install.py

Nach der Installation werden Sie aufgefordert, neu zu starten. Geben Sie ``Y`` ein und drücken Sie die Eingabetaste, um neu zu starten. Nach dem Neustart wird der sichere Abschaltdienst automatisch gestartet. Wenn der Knopf 2 Sekunden lang gedrückt wird oder der Akku schwach ist, fährt der Raspberry Pi herunter und benachrichtigt PiPower 3, sich auszuschalten.

Abschaltprozentsatz festlegen
--------------------------------

PiPower 3 sendet einen "LOW BATTERY" Abschaltbefehl über I2C an den Host, wenn keine externe Stromversorgung vorhanden ist und die Batteriespannung unter den Abschaltprozentsatz fällt. Der Host kann das Abschaltsignal über I2C lesen und bei Erkennung von "LOW BATTERY" den Shutdown-Prozess einleiten. 

Nach dem Herunterfahren wird das ``SDSIG`` hochgezogen und der PiPower wird ausgeschaltet. Dies implementiert die Niedrigbatterie-Abschaltfunktion von PiPower 3.

.. note::

    Wenn Sie den Raspberry Pi verwenden und der Stromverbrauch größer als 3A ist, kann der Akku die Stromversorgung nicht lange aufrechterhalten. Es wird empfohlen, den Abschaltprozentsatz auf 100% zu setzen, d.h., den Raspberry Pi sofort herunterzufahren, wenn die externe Stromversorgung getrennt wird, um den Raspberry Pi und die Daten zu schützen.

Sie können den Abschaltprozentsatz mit dem folgenden Befehl festlegen, z.B. auf 30%. Wenn der Akkustand unter 30% fällt, schaltet PiPower3 den Raspberry Pi nach dem Herunterfahren aus.

.. code-block:: shell
    
    pipower3 -sp 30 

Grundkonfigurationen anzeigen
----------------------------------------

Sie können den Befehl ``pipower3`` verwenden, um die aktuellen Informationen anzuzeigen. Eine detaillierte Anleitung zur Verwendung finden Sie unten:

.. code-block::

    usage: pipower3-service [-h] [-sp [SHUTDOWN_PERCENTAGE]] [-pp [POWER_OFF_PERCENTAGE]] [-so SHUTDOWN_OVERRIDE] [-iv] [-ov] [-bv] [-bp] [-bs] [-ii] [-ib] [-ic] [-ao] [-sr] [-bi]
                            [-psv] [-a]
                            [command]

    PiPower 3

    positional arguments:
    command               Befehl

    options:
    -h, --help            Zeige diese Hilfe an und beende
    -sp [SHUTDOWN_PERCENTAGE], --shutdown-percentage [SHUTDOWN_PERCENTAGE]
                            Abschaltprozentsatz festlegen, leer lassen zum Lesen
    -iv, --input-voltage  Eingangsspannung lesen
    -ov, --output-voltage
                            Ausgangsspannung lesen
    -bv, --battery-voltage
                            Batteriespannung lesen
    -bp, --battery-percentage
                            Akkustand in Prozent lesen
    -bs, --battery-source
                            Batteriequelle lesen
    -ii, --is-input-plugged_in
                            Eingangsstatus lesen
    -ic, --is-charging    Ladestatus lesen
    -do, --default-on     Standardstatus lesen
    -sr, --shutdown-request
                            Abschaltanforderung lesen
    -a, --all             Alles
    
Konfiguration mit Python
-------------------------------

PiPower 3 verwendet die Bibliothek ``spc``, die es ermöglicht, Daten abzurufen und Parameter in Python zu setzen. Die Bibliothek ``spc`` ist in einer virtuellen Umgebung installiert, daher müssen Sie zuerst die virtuelle Umgebung betreten.

.. code-block:: shell

    source /opt/pipower3/venv/bin/activate

Wenn Sie die virtuelle Umgebung nicht betreten möchten, können Sie ``spc`` erneut im System installieren, was mit ``--break-system`` bestätigt werden muss, da es zu Konflikten mit anderen Bibliotheken kommen kann:

.. code-block:: shell

    sudo pip3 install --break-system git+http://github.com/sunfounder/spc.git

Oder wenn Sie es in Ihrer eigenen virtuellen Umgebung installieren möchten, führen Sie einfach den Installationsbefehl nach dem Betreten Ihrer virtuellen Umgebung aus:

.. code-block:: shell

    pip3 install git+http://github.com/sunfounder/spc.git

Jetzt können Sie Beispiele ausführen:

.. code-block:: shell

    cd ~/pipower3/examples

.. code-block:: shell

    python3 read_all.py

* ``read_all.py``: Verwenden Sie dieses Beispiel, wenn Sie alle Daten auf einmal lesen und einzeln verarbeiten möchten.
* ``read_individual.py``: Wenn Sie nur bestimmte Daten lesen möchten, bietet dieses Beispiel Anweisungen zur individuellen Datenerfassung.
* ``set_shutdown_percentage.py``: Dieses Beispiel zeigt, wie Sie einen Abschaltprozentsatz festlegen, der ein Abschaltsignal an den Host sendet, wenn keine Ladung vorhanden ist und die Batterie unter diesen Wert fällt. Nachdem der Host heruntergefahren ist, empfängt er ein Abschaltsignal, bevor er sich ausschaltet. Typischerweise verwendet bei SBCs wie Raspberry Pi. Mikrocontroller, die diese Funktion nutzen möchten, sollten den SDSIG-Jumper entfernen und das mittlere Kabel an einen Pin anschließen. Nach Empfang des Abschaltsignals und sicherem Herunterfahren wird dieser Pin auf high gezogen, um PiPower 3 auszuschalten.
* ``shutdown_when_request``: Dieses Beispiel zeigt, wie Sie Vorgänge nach Erhalt eines Abschaltsignals handhaben. Entfernen Sie den SDSIG-Jumper und verbinden Sie das mittlere Kabel mit einem Pin.

Python-Bibliothek API-Dokumentation:

https://github.com/sunfounder/spc?tab=readme-ov-file#api
