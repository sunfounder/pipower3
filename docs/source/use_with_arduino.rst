.. note:: 

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux nouvelles annonces de produits et aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Utilisation avec une carte Arduino
=====================================

Si vous utilisez le PiPower 3 pour alimenter votre carte Arduino, vous pouvez connecter l'Arduino au port de sortie Type A du PiPower 3 ou utiliser deux fils de connexion. Connectez l'interface I2C de la carte à l'aide d'un cavalier. Si aucune opération n'est nécessaire avant l'extinction, connectez directement le cavalier **SDSIG** à la masse (GND). Si des opérations sont nécessaires avant l'extinction, retirez le cavalier et connectez le fil intermédiaire à un port IO de l'Arduino pour informer PiPower 3 qu'il peut s'éteindre en toute sécurité.

Nous fournissons une bibliothèque qui vous permet de surveiller les tensions d'entrée et de sortie, la tension et le pourcentage de la batterie, la source d'alimentation, l'état de la charge et d'autres données internes.

#. Dans l'IDE Arduino, ouvrez le **Gestionnaire de Bibliothèques**, recherchez ``SunFounderPowerControl``, puis téléchargez et installez-la.

    .. image:: img/arduino_library.png

#. Après l'installation, vous pouvez naviguer vers **Fichier** -> **Exemples** -> **SunFounderPowerControl** -> **PiPower 3**, où vous trouverez quatre exemples.

    .. image:: img/arduino_examples.png

    * ``read_all`` : Utilisez cet exemple si vous avez besoin de lire toutes les données en une seule fois et de les traiter individuellement.
    * ``read_individual`` : Si vous devez uniquement lire certaines données, cet exemple vous fournit des instructions pour récupérer les données individuelles.
    * ``set_shutdown_percentage`` : Cet exemple montre comment définir un pourcentage de batterie pour l'arrêt. Cette fonctionnalité envoie un signal d'arrêt à l'hôte lorsque la batterie ne se charge pas et tombe en dessous du pourcentage défini. Après l'arrêt de l'hôte, celui-ci s'éteindra uniquement après avoir reçu un signal d'extinction. Utilisé typiquement avec des SBCs comme le Raspberry Pi. Pour les microcontrôleurs, retirez le cavalier **SDSIG** et connectez le fil intermédiaire à une broche. Après un arrêt en toute sécurité suite à la réception du signal d'arrêt, tirez cette broche vers le haut pour éteindre le PiPower 3.
    * ``shutdown_when_request`` : Cet exemple montre comment gérer les opérations après avoir reçu un signal d'arrêt. Retirez le cavalier **SDSIG** et connectez le fil intermédiaire à une broche.

#. Choisissez l'un des exemples et téléchargez-le sur votre carte.

.. note::

    Sur les cartes où les broches I2C peuvent être modifiées, il est nécessaire de changer le code dans ``Wire.begin()``.

Documentation de l'API de la bibliothèque Arduino :

https://github.com/sunfounder/arduino_spc?tab=readme-ov-file#api

