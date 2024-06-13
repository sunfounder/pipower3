.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Verwendung mit dem Arduino-Board
===================================

Wenn Sie den PiPower 3 verwenden, um Ihr Arduino-Board mit Strom zu versorgen, können Sie das Arduino-Board an den Typ-A-Ausgangsport des PiPower 3 anschließen oder zwei Jumper-Kabel verwenden. Verbinden Sie die I2C-Schnittstelle des Boards mit einem Jumper. Wenn keine Operation vor dem Ausschalten erforderlich ist, verbinden Sie den **SDSIG**-Jumper direkt mit GND. Wenn vor dem Herunterfahren Operationen notwendig sind, entfernen Sie den Jumper und verbinden Sie das mittlere Kabel mit einem IO-Port am Arduino, um PiPower 3 mitzuteilen, dass es sicher ausgeschaltet werden kann.

Wir stellen eine Bibliothek bereit, die es Ihnen ermöglicht, Eingangs- und Ausgangsspannungen, Batteriespannung und -prozent, Stromquelle, Ladestatus und andere interne Daten zu überwachen.

#. Öffnen Sie im Arduino IDE den **Bibliotheksverwalter**, suchen Sie nach ``SunFounderPowerControl`` und laden Sie diese herunter und installieren Sie sie.

    .. image:: img/arduino_library.png

#. Nach der Installation können Sie zu **Datei** -> **Beispiele** -> **SunFounderPowerControl** -> **PiPower 3** navigieren, wo Sie vier Beispiele finden.

    .. image:: img/arduino_examples.png

    * ``read_all``: Verwenden Sie dieses Beispiel, wenn Sie alle Daten auf einmal lesen und einzeln verarbeiten müssen.
    * ``read_individual``: Wenn Sie nur bestimmte Daten lesen müssen, bietet dieses Beispiel Anleitungen zur individuellen Datenabfrage.
    * ``set_shutdown_percentage``: Dieses Beispiel zeigt, wie Sie einen Abschaltprozentsatz für die Batterie einstellen. Diese Funktion sendet ein Abschaltsignal an den Host, wenn die Batterie nicht geladen wird und unter den eingestellten Prozentsatz fällt. Nachdem der Host heruntergefahren ist, wird er nur nach Erhalt eines Ausschaltsignals ausgeschaltet. Typischerweise wird dies mit SBCs wie dem Raspberry Pi verwendet. Für Mikrocontroller entfernen Sie den **SDSIG**-Jumper und verbinden das mittlere Kabel mit einem Pin. Nachdem der Mikrocontroller das Abschaltsignal erhalten und sicher heruntergefahren wurde, ziehen Sie diesen Pin auf High, um PiPower 3 auszuschalten.
    * ``shutdown_when_request``: Dieses Beispiel zeigt, wie Sie Vorgänge nach Erhalt eines Abschaltsignals behandeln. Entfernen Sie den **SDSIG**-Jumper und verbinden Sie das mittlere Kabel mit einem Pin.

#. Wählen Sie eines der Beispiele aus und laden Sie es auf Ihr Board hoch.

.. note::

    Bei Boards, bei denen die I2C-Pins geändert werden können, ist es notwendig, den Code in ``Wire.begin()`` zu ändern.

Arduino-Bibliothek API-Dokumentation:

https://github.com/sunfounder/arduino_spc?tab=readme-ov-file#api
