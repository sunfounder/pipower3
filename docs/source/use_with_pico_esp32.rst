.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Verwendung mit Raspberry Pi Pico und ESP32 Boards
====================================================
Wenn Sie den PiPower 3 verwenden, um Ihr Raspberry Pi Pico oder ESP32 Board mit Strom zu versorgen, können Sie das Raspberry Pi Pico oder ESP32 Board an den Typ-A-Ausgangsport des PiPower 3 anschließen oder zwei Jumper-Kabel verwenden.

Verbinden Sie die I2C-Schnittstelle des Boards mit einem Jumper. Wenn keine Operation vor dem Ausschalten erforderlich ist, verbinden Sie den **SDSIG**-Jumper direkt mit GND. Wenn vor dem Herunterfahren Operationen notwendig sind, entfernen Sie den Jumper und verbinden das mittlere Kabel mit einem IO-Port am Raspberry Pi Pico oder ESP32 Board. Dies wird verwendet, um PiPower 3 mitzuteilen, dass es den Shutdown abgeschlossen hat und ausgeschaltet werden kann.

Wir stellen eine Bibliothek bereit, die es Ihnen ermöglicht, Eingangs- und Ausgangsspannungen, Batteriespannung und -prozent, Stromquelle, Ladestatus und andere interne Daten zu überwachen.

#. Laden Sie die Bibliothek von GitHub herunter. Sie können sie schnell über den untenstehenden Link herunterladen oder besuchen Sie: https://github.com/sunfounder/micropython_spc.

    * :download:`micropython_spc <https://github.com/sunfounder/micropython_spc/archive/refs/heads/main.zip>`

#. Nach dem Herunterladen und Entpacken laden Sie den ``spc``-Ordner auf Ihr Raspberry Pi Pico oder ESP32 Board hoch. Thonny wird für diesen Zweck empfohlen.

    .. image:: img/micropython_upload.png
        :align: center

#. Sobald der Upload abgeschlossen ist, können Sie einige Beispiele aus dem Ordner ``micropython_spc-main`` ausführen, um die Effekte zu sehen:

    * ``example_pipower_3_read_all.py``: Verwenden Sie dieses Beispiel, wenn Sie alle Daten auf einmal lesen und einzeln verarbeiten müssen.
    * ``example_pipower_3_read_individual.py``: Wenn Sie nur bestimmte Daten lesen müssen, bietet dieses Beispiel Anleitungen zur individuellen Datenabfrage.
    * ``example_pipower_3_set_shutdown_percentage.py``: Dieses Beispiel zeigt, wie Sie einen Abschaltprozentsatz für die Batterie einstellen. Dies sendet ein Abschaltsignal an den Host, wenn die Batterie nicht geladen wird und unter den eingestellten Prozentsatz fällt. Es wird erst abgeschaltet, nachdem der Host heruntergefahren ist und ein Ausschalt-Signal empfangen hat. Typischerweise wird dies mit SBCs wie dem Raspberry Pi verwendet. Für Mikrocontroller entfernen Sie den **SDSIG**-Jumper und verbinden das mittlere Kabel mit einem Pin. Nachdem der Mikrocontroller das Abschaltsignal erhalten und sicher heruntergefahren wurde, ziehen Sie diesen Pin auf High, um PiPower 3 auszuschalten.
    * ``example_pipower_3_shutdown_when_request.py``: Dieses Beispiel zeigt, wie Sie Vorgänge nach Erhalt eines Abschaltsignals behandeln. Entfernen Sie den **SDSIG**-Jumper und verbinden Sie das mittlere Kabel mit einem Pin.

Micropython-Bibliothek API-Dokumentation:

https://github.com/sunfounder/micropython_spc?tab=readme-ov-file#api
