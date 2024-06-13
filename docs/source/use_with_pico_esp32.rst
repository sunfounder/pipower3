.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Raspberry Pi PicoおよびESP32ボードでの使用
====================================================
PiPower 3を使用してRaspberry Pi PicoまたはESP32ボードに電力を供給する場合、Raspberry Pi PicoまたはESP32ボードをPiPower 3のType A出力ポートに接続するか、ジャンパーワイヤーを2本使用して接続します。

ボードのI2Cインターフェースをジャンパーで接続します。電源オフ前に操作が必要ない場合、 **SDSIG** ジャンパーキャップをGNDに直接接続します。シャットダウン前に操作が必要な場合は、ジャンパーキャップを取り外し、中間ワイヤーをRaspberry Pi PicoまたはESP32ボードのIOポートに接続します。これにより、PiPower 3がシャットダウンを完了し、電源を切ることができることを通知します。

入力および出力電圧、バッテリー電圧とパーセンテージ、電源、充電状態、およびその他の内部データを監視するためのライブラリを提供しています。

#. GitHubからライブラリをダウンロードします。以下のリンクを使用してすばやくダウンロードするか、https://github.com/sunfounder/micropython_spc を訪問してください。

    * :download:`micropython_spc <https://github.com/sunfounder/micropython_spc/archive/refs/heads/main.zip>`

#. ダウンロードして解凍した後、 ``spc`` フォルダーをRaspberry Pi PicoまたはESP32ボードにアップロードします。Thonnyを使用することをお勧めします。

    .. image:: img/micropython_upload.png
        :align: center

#. アップロードが完了したら、 ``micropython_spc-main`` フォルダーからいくつかの例を実行して効果を確認できます：

    * ``example_pipower_3_read_all.py``: すべてのデータを一度に読み取り、それぞれを個別に処理する必要がある場合にこの例を使用します。
    * ``example_pipower_3_read_individual.py``: 特定のデータのみを読み取る必要がある場合、この例は個々のデータ取得手順を提供します。
    * ``example_pipower_3_set_shutdown_percentage.py``: シャットダウンバッテリーパーセンテージを設定する方法を示します。バッテリーが充電されておらず、設定されたパーセンテージを下回った場合にホストにシャットダウン信号を送信します。ホストがシャットダウンし、電源オフ信号を受信した後にのみ電源が切れます。通常、Raspberry PiのようなSBCに使用されます。マイクロコントローラーの場合、この機能を使用するには、 **SDSIG** ジャンパーキャップを取り外し、中間ワイヤーをピンに接続します。シャットダウン信号を受信して安全にシャットダウンした後、このピンを高くしてPiPower 3の電源を切ります。
    * ``example_pipower_3_shutdown_when_request.py``: シャットダウン信号を受信した後の操作を処理する方法を示します。 **SDSIG** ジャンパーキャップを取り外し、中間ワイヤーをピンに接続します。

MicropythonライブラリAPIドキュメント:

https://github.com/sunfounder/micropython_spc?tab=readme-ov-file#api
