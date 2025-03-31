.. note:: 

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux nouvelles annonces de produits et aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Utilisation avec Raspberry Pi
================================

Téléchargement et installation du module ``pipower3``
-------------------------------------------------------

Téléchargez le code depuis GitHub et installez-le :

.. code-block:: shell
    
    git clone https://github.com/sunfounder/pipower3

    cd pipower3
    sudo python3 install.py

Après l'installation, vous serez invité à redémarrer. Entrez ``Y`` et appuyez sur Entrée pour redémarrer. Après le redémarrage, le service de mise hors tension sécurisé démarrera automatiquement. Si le bouton est maintenu enfoncé pendant 2 secondes ou si la batterie est faible, le Raspberry Pi s'éteindra et informera PiPower 3 de se couper.

Définir le pourcentage d'arrêt
----------------------------------

PiPower 3 envoie une demande d'arrêt "LOW BATTERY" via I2C à l'hôte lorsqu'il n'y a pas d'alimentation externe et que la tension de la batterie descend en dessous du pourcentage d'arrêt. L'hôte peut lire le signal de demande d'arrêt via I2C, et si "LOW BATTERY" est détecté, il peut procéder à l'arrêt.

Après l'arrêt, tirer le ``SDSIG`` vers le haut éteindra PiPower. Cela met en œuvre la fonctionnalité d'arrêt en cas de faible batterie du PiPower 3.

.. note::

    Si vous utilisez un Raspberry Pi, si la puissance utilisée est supérieure à 3A, la batterie ne pourra pas fournir de l'énergie longtemps. Il est recommandé de définir le pourcentage d'arrêt à 100%, c'est-à-dire informer immédiatement le Raspberry Pi de s'éteindre lorsque l'alimentation externe est déconnectée, afin de protéger le Raspberry Pi et les données.

Vous pouvez définir le pourcentage d'arrêt en utilisant la commande, par exemple, définissez-le à 30%. Lorsque le niveau de la batterie est inférieur à 30%, PiPower3 éteindra le Raspberry Pi après qu'il se soit éteint.

.. code-block:: shell
    
    pipower3 -sp 30 

Voir les configurations de base
----------------------------------------

Vous pouvez utiliser la commande ``pipower3`` pour voir les informations actuelles, le tutoriel d'utilisation détaillé est le suivant :

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

Configurer avec Python
--------------------------

PiPower 3 utilise la bibliothèque ``spc``, qui permet de récupérer des données et de définir des paramètres en Python. La bibliothèque ``spc`` est installée dans un environnement virtuel, vous devez donc d'abord entrer dans l'environnement virtuel.

.. code-block:: shell

    source /opt/pipower3/venv/bin/activate

Si vous ne souhaitez pas entrer dans l'environnement virtuel, vous pouvez réinstaller ``spc`` sur le système, ce qui nécessite l'option ``--break-system`` en raison des conflits possibles avec d'autres bibliothèques :

.. code-block:: shell

    sudo pip3 install --break-system git+http://github.com/sunfounder/spc.git

Ou, si vous voulez l'installer dans votre propre environnement virtuel, exécutez simplement la commande d'installation après être entré dans votre environnement virtuel :

.. code-block:: shell

    pip3 install git+http://github.com/sunfounder/spc.git

Vous pouvez maintenant exécuter des exemples :

.. code-block:: shell

    cd ~/pipower3/examples

.. code-block:: shell

    python3 read_all.py

* ``read_all.py`` : Utilisez cet exemple si vous avez besoin de lire toutes les données à la fois et de les traiter individuellement.
* ``read_individual.py`` : Si vous devez uniquement lire certaines données, cet exemple fournit des instructions pour récupérer les données individuellement.
* ``set_shutdown_percentage.py`` : Cet exemple montre comment définir un pourcentage de batterie pour l'arrêt, ce qui enverra un signal d'arrêt à l'hôte lorsqu'il n'y a pas de charge et que la batterie descend sous cette valeur. Après l'arrêt de l'hôte, il recevra un signal d'extinction avant de s'éteindre. Utilisé typiquement avec des SBC comme le Raspberry Pi. Les microcontrôleurs souhaitant utiliser cette fonctionnalité doivent retirer le cavalier SDSIG et connecter le fil intermédiaire à une broche. Après avoir reçu le signal d'arrêt et s'être éteint en toute sécurité, tirez cette broche vers le haut pour éteindre PiPower 3.
* ``shutdown_when_request`` : Cet exemple montre comment gérer les opérations après avoir reçu un signal d'arrêt. Retirez le cavalier SDSIG et connectez le fil intermédiaire à une broche.

Documentation de l'API de la bibliothèque Python :

https://github.com/sunfounder/spc?tab=readme-ov-file#api

