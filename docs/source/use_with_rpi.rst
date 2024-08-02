.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Raspberry Piでの使用
========================

``pipower3`` モジュールのダウンロードとインストール
-------------------------------------------------------

GitHubからコードをダウンロードしてインストールします：

.. code-block:: shell
    
    git clone https://github.com/sunfounder/pipower3

    cd pipower3
    sudo python3 install.py

インストール後、再起動を求められます。 ``Y`` を入力し、Enterキーを押して再起動します。再起動後、安全なシャットダウンサービスが自動的に開始されます。ボタンが2秒間押された場合やバッテリーが低下した場合、Raspberry Piはシャットダウンし、PiPower 3に電源オフを通知します。

シャットダウンパーセンテージの設定
----------------------------------

PiPower 3は、外部電源がなくなりバッテリー電圧がシャットダウンパーセンテージを下回ったときに、I2C経由でホストに「LOW BATTERY」シャットダウンリクエストを送信します。ホストはI2C経由でシャットダウンリクエスト信号を読み取り、「LOW BATTERY」が検出された場合、シャットダウンを処理できます。

シャットダウン後、 ``SDSIG`` を高く引っ張るとPiPowerの電源が切れます。これにより、PiPower 3の低バッテリーシャットダウン機能が実装されます。

.. note::

    Raspberry Pi を使用している場合、消費電力が3Aを超えると、バッテリーが長時間電力を維持できなくなります。外部電源が切断された場合にRaspberry Piにすぐにシャットダウンを通知するために、シャットダウンパーセンテージを100%に設定することをお勧めします。これにより、Raspberry Piとデータを保護できます。

シャットダウンパーセンテージを設定するには、以下のコマンドを使用します。たとえば、30%に設定します。バッテリーレベルが30%を下回ると、PiPower3はRaspberry Piをシャットダウン後に電源を切ります。

.. code-block:: shell
    
    pipower3 -sp 30 

基本設定の表示
----------------------------------------

 ``pipower3`` コマンドを使用して現在の情報を表示できます。詳細な使用方法は以下の通りです：

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

Pythonでの設定
-------------------------------

PiPower 3は ``spc`` ライブラリを使用しており、これによりPythonでデータを取得し、パラメータを設定できます。 ``spc`` ライブラリは仮想環境にインストールされているため、まず仮想環境に入る必要があります。

.. code-block:: shell

    source /opt/pipower3/venv/bin/activate

仮想環境に入るのを避けたい場合、 ``spc`` をシステムに再インストールできますが、他のライブラリとの競合の可能性があるため ``--break-system`` で確認する必要があります：

.. code-block:: shell

    sudo pip3 install --break-system git+http://github.com/sunfounder/spc.git

または、独自の仮想環境にインストールしたい場合、仮想環境に入った後にインストールコマンドを実行します：

.. code-block:: shell

    pip3 install git+http://github.com/sunfounder/spc.git

これで、以下の例を実行できます：

.. code-block:: shell

    cd ~/pipower3/examples

.. code-block:: shell

    python3 read_all.py

* ``read_all.py``: すべてのデータを一度に読み取り、それぞれを個別に処理する必要がある場合にこの例を使用します。
* ``read_individual.py``: 特定のデータのみを読み取る必要がある場合、この例は個々のデータ取得手順を提供します。
* ``set_shutdown_percentage.py``: シャットダウンバッテリーパーセンテージを設定する方法を示します。バッテリーが充電されておらず、設定されたパーセンテージを下回った場合にホストにシャットダウン信号を送信します。ホストがシャットダウンし、電源オフ信号を受信した後にのみ電源が切れます。通常、Raspberry PiのようなSBCに使用されます。マイクロコントローラーの場合、この機能を使用するには、 **SDSIG** ジャンパーキャップを取り外し、中間ワイヤーをピンに接続します。シャットダウン信号を受信して安全にシャットダウンした後、このピンを高くしてPiPower 3の電源を切ります。
* ``shutdown_when_request.py``: シャットダウン信号を受信した後の操作を処理する方法を示します。 **SDSIG** ジャンパーキャップを取り外し、中間ワイヤーをピンに接続します。

PythonライブラリAPIドキュメント:

https://github.com/sunfounder/spc?tab=readme-ov-file#api
