.. note:: 

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux nouvelles annonces de produits et aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Utilisation avec les cartes Raspberry Pi Pico et ESP32
=========================================================

Si vous utilisez le PiPower 3 pour alimenter votre Raspberry Pi Pico ou carte ESP32, vous pouvez connecter la carte Raspberry Pi Pico ou ESP32 au port de sortie Type A du PiPower 3 ou utiliser deux fils de connexion.

Connectez l'interface I2C de la carte à l'aide d'un cavalier. Si aucune opération n'est nécessaire avant l'extinction, connectez directement le cavalier **SDSIG** à la masse (GND). Si des opérations sont nécessaires avant l'extinction, retirez le cavalier et connectez le fil intermédiaire à un port IO de la carte Raspberry Pi Pico ou ESP32. Cela sert à informer PiPower 3 qu'il a bien effectué l'extinction et peut s'éteindre.

Nous fournissons une bibliothèque qui vous permet de surveiller les tensions d'entrée et de sortie, la tension de la batterie et son pourcentage, la source d'alimentation, l'état de la charge, et d'autres données internes.

#. Téléchargez la bibliothèque depuis GitHub. Vous pouvez la télécharger rapidement en utilisant le lien ci-dessous ou visiter : https://github.com/sunfounder/micropython_spc.

    * :download:`micropython_spc <https://github.com/sunfounder/micropython_spc/archive/refs/heads/main.zip>`

#. Après avoir téléchargé et extrait le fichier, téléchargez le dossier ``spc`` sur votre Raspberry Pi Pico ou carte ESP32. Thonny est recommandé pour cette opération.

    .. image:: img/micropython_upload.png
        :align: center

#. Une fois le téléchargement effectué, vous pouvez exécuter quelques exemples depuis le dossier ``micropython_spc-main`` pour voir les effets :

    * ``example_pipower_3_read_all.py`` : Utilisez cet exemple si vous avez besoin de lire toutes les données à la fois et de les traiter individuellement.
    * ``example_pipower_3_read_individual.py`` : Si vous devez uniquement lire certaines données, cet exemple fournit des instructions pour récupérer les données individuellement.
    * ``example_pipower_3_set_shutdown_percentage.py`` : Cet exemple montre comment définir un pourcentage de batterie pour l'arrêt. Cela enverra un signal d'arrêt à l'hôte lorsque la batterie n'est pas en charge et descend en dessous du pourcentage défini. Elle s'éteindra uniquement après que l'hôte se soit arrêté et ait reçu un signal d'extinction. Utilisé typiquement avec des SBC comme le Raspberry Pi. Pour les microcontrôleurs, retirez le cavalier **SDSIG** et connectez le fil intermédiaire à une broche. Après un arrêt en toute sécurité après avoir reçu le signal d'arrêt, tirez cette broche vers le haut pour éteindre PiPower 3.
    * ``example_pipower_3_shutdown_when_request.py`` : Cet exemple montre comment gérer les opérations après avoir reçu un signal d'arrêt. Retirez le cavalier **SDSIG** et connectez le fil intermédiaire à une broche.

Documentation de l'API de la bibliothèque Micropython :

https://github.com/sunfounder/micropython_spc?tab=readme-ov-file#api
