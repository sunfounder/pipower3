.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Schnellstartanleitung
=======================
Pinbelegung
-------------

.. image:: img/pipower3_pinout.png
  :width: 800
  :align: center

1. :ref:`power_input`: Externe Stromversorgung, kann den Raspberry Pi direkt mit Strom versorgen und gleichzeitig den Akku laden.
2. :ref:`cap_onoff`: Wählen Sie, ob das Gerät automatisch gestartet werden soll, wenn die externe Stromversorgung im ausgeschalteten Zustand angeschlossen wird.
3. :ref:`cap_sdsig`: Abschaltsignal, verbindet Pin 26 mit dem mittleren Pin über einen Jumper, der **SDSIG** mit GPIO26 auf dem Raspberry Pi verbindet. Nach der Konfiguration, wenn der Raspberry Pi heruntergefahren wird, wird GPIO26 auf High gesetzt, was PiPower 3 signalisiert, sich auszuschalten.
4. :ref:`cap_btn`: Externer Netzschalter-Jumper, verwendet für externen Netzschalter.
5. **PWR LED**: Status-LED des Ausgangs, leuchtet, wenn der Ausgang aktiviert ist.
6. **BAT LED**: Die leuchtende LED zeigt an, dass der Akku derzeit Strom liefert. Zu diesem Zeitpunkt muss der Akkustand überwacht werden, um Schäden durch Tiefentladung zu vermeiden.
7. :ref:`power_button`: Eingebauter Netzschalter zur Steuerung der Stromversorgung der Platine:

  * **Einmal drücken**: Aktiviert den Ausgang.
  * **2 Sekunden halten, bis die beiden mittleren Batterie-LEDs leuchten, dann loslassen**: Sendet eine Abschaltanforderung über i2c.
  * **Mehr als 5 Sekunden gedrückt halten**: Schaltet den Ausgang direkt aus.

8. :ref:`battery_indicators`: Zeigt den Akkustand und den Ladezustand an.
9. **I2C-Anschluss**: SH1.0 4P-Anschluss, kompatibel mit **qwIIC** und **STEMMA QT**.
10. **I2C-Pin-Header**: 1x4P 2.54-Pin-Header.
11. **Typ-A-Ausgang**: 5V-Ausgangsschnittstelle.
12. **5V/GND-Pin-Header**: 2 x 4P 2.54-Pin-Header.
13. :ref:`pin_header`: Raspberry Pi-Pin-Header, direkt verbunden mit dem Raspberry Pi.
14. :ref:`battery_connector`: XH2.54 3P-Akkustecker.
15. **Warn-LEDs**: Wenn die Batterie verpolt ist, leuchten zwei rote LEDs auf und warnen vor der Verpolung.

Betriebsschritte
------------------

1. Laden Sie das PiPower 3.

Bevor Sie Ihr PiPower 3 verwenden, laden Sie es vollständig auf. Eine vollständige Ladung verhindert Batterieprobleme und gewährleistet eine optimale Leistung.

Zum Laden verwenden Sie ein 5V/3A PD-Ladegerät, wie das offizielle 27W-Netzteil von Raspberry Pi. Dies ermöglicht es dem PiPower 3, einen maximalen Strom von 3A zu liefern.

.. image:: img/power_input.jpg
  :width: 500
  :align: center

Während des Ladevorgangs blinkt die Kontrollleuchte.

.. image:: img/battery_indicator.jpg
  :width: 500
  :align: center

* **4 LEDs leuchten**: Akku >80%
* **3 LEDs leuchten**: 60% < Akku < 80%
* **2 LEDs leuchten**: 40% < Akku < 60%
* **1 LED leuchtet**: 20% < Akku < 40%
* **Erste LED blinkt**: Akku < 20%
* **LEDs leuchten nacheinander auf**: Ladevorgang
* **Mittlere zwei LEDs blinken**: Warten auf Abschaltsignal
* **Alle LEDs aus**: Keine Stromversorgung oder im Schlafmodus

2. Ausgangsleistung an die Hauptplatine.

Wenn Sie einen Raspberry Pi verwenden, sind keine zusätzlichen Verdrahtungen erforderlich.

Für andere Hauptplatinen können Sie diese an den Typ-A-Ausgangsport des PiPower 3 anschließen oder zwei Jumper-Kabel verwenden.

.. image:: img/output_mainboard.jpg
    :width: 500
    :align: center

.. image:: img/output_mainboard_pin.jpg
    :width: 400
    :align: center

3. Drücken Sie einmal den Netzschalter, um Ihre Hauptplatine mit Strom zu versorgen.

Sie werden sehen, dass die **PWR LED** aufleuchtet und Ihre Hauptplatine Strom vom PiPower 3 erhält.

.. image:: img/pwr_led.png
    :width: 500
    :align: center

4. So schalten Sie die Stromversorgung nach dem Gebrauch aus.

  * **Halten Sie den Schalter länger als 5 Sekunden gedrückt**: Schaltet den Ausgang direkt aus.
  * **Halten Sie den Schalter 2 Sekunden gedrückt, bis die beiden mittleren Batterie-LEDs aufleuchten, und lassen Sie dann los**: Wenn Sie die :ref:`pipower_software` konfiguriert haben, sendet diese Aktion eine Abschaltanforderung über I2C für ein sicheres Herunterfahren.

.. note::

    Wenn Ihr Type-C-Stromkabel noch eingesteckt ist, zeigt die Batterieanzeige weiterhin den Ladestatus an, bis der Ladevorgang abgeschlossen ist.

.. _pipower_software:

Softwarekonfiguration
------------------------------------

Zusätzlich zur direkten Nutzung des PiPower 3 können Sie auch unsere bereitgestellte Bibliothek verwenden, um Eingangs- und Ausgangsspannungen, Strom, Batteriespannung, Prozentsatz, Stromquelle, Ladestatus und andere interne Daten wie Abschaltanforderungen zu überwachen.

Bitte wählen Sie das entsprechende Tutorial basierend auf Ihrer Hauptplatine.

.. toctree::
    :maxdepth: 2

    use_with_rpi
    use_with_pico_esp32
    use_with_arduino
