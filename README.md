# THÉO20m

Firmware gratuit et open source en français, sous forme de prototype personnel, pour une Geeetech A20M modifiée à une extrudeuse logique. Basé sur **Marlin 2.1.2.10**, sous GPL-3.0-or-later.

**Version 0.1.0-alpha.1 — expérimentale, non validée sur machine.** Ce projet reconstruit une configuration ; il ne reproduit pas à l'identique le firmware personnalisé Mad20M Build 502. La réussite de compilation ne prouve pas la compatibilité matérielle. Aucun firmware de ce projet n'a été installé sur l'imprimante.

## Ce que prépare ce profil

- Nom affiché personnalisable, **THÉO20m** par défaut ; menus Marlin en français, avec accents.
- Une extrudeuse logique et un moteur d'extrusion dans ce prototype ; mélange bicolore désactivé. Le nombre physique de moteurs reste à confirmer.
- USB à 250000 bauds ; processeur ATmega2560.
- Nivellement **UBL manuel**, réglage fin Z, Linear Advance, pause avancée et reprise après coupure.
- Calibration des pas, limites de vitesse, accélérations, PID et préchauffages reportées depuis le relevé de la machine.
- Stockage EEPROM disponible, sans initialisation automatique ni réinitialisation usine ajoutée.

Les traductions sont celles fournies par Marlin : les commandes G-code et les identifiants techniques gardent leurs noms standard. La présence de fonctions dans ce profil ne garantit pas la conservation de toutes les fonctions du firmware antérieur.

## Choisir le nom de sa machine

Chacun choisit librement le nom affiché. **THÉO20m est le nom par défaut**, pas une obligation. À l’étape de préparation, ajouter l’option `--nom` :

```sh
.venv/bin/python scripts/preparer.py --nom "Ma machine"
```

Utiliser 1 à 16 caractères imprimables ; les lettres latines sont conseillées pour cet écran. Le changement s’applique aux sources préparées avant compilation. Les empreintes et le rapport fournis concernent le profil par défaut ; un nom personnalisé produit un autre binaire. Le nom du dépôt GitHub reste THEO20m.

## Compiler

Prérequis : Linux, Python **3.12 ou plus**, accès Internet. Les outils et bibliothèques AVR sont téléchargés par PlatformIO.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/preparer.py
PLATFORMIO_CORE_DIR="$PWD/.pio-core" .venv/bin/python -m platformio run -d build/Marlin-2.1.2.10 -e mega2560
```

Le script vérifie l'empreinte SHA256 de l'archive officielle avant extraction. Il copie les deux configurations de ce dépôt dans les sources Marlin et n'accède à aucun port série. La commande de compilation ne flashe pas l'imprimante.

La sortie de compilation est `build/Marlin-2.1.2.10/.pio/build/mega2560/firmware.hex`. Elle reste expérimentale et n'est pas distribuée comme un firmware prêt à installer.

## Vérification réalisée

Compilation `mega2560` réussie : 209290 octets de flash sur 253952 et 7069 octets de RAM statique sur 8192. Le nom UTF-8 THÉO20m et un message français sont présents dans le binaire. Les fichiers de configuration publiés sont identiques à ceux compilés. Voir [le rapport](docs/COMPILATION.json). La marge de RAM restante doit être validée en fonctionnement ; aucun test sur machine ni transfert de maillage n’a été réalisé.

## Avant installation

Consulter [la validation matérielle et la migration](docs/VALIDATION.md). La carte GT2560 V3 A20, ses broches, les pilotes, les sondes thermiques, les sens de déplacement, le moteur d'extrusion et les limites géométriques doivent être confirmés. Ils ne sont pas identifiables avec certitude à partir du seul nom A20M ou de la signature ATmega2560.

Ne pas importer une EEPROM du firmware de 2021 directement dans ce nouveau Marlin : son format et celui des maillages peuvent différer. Les sauvegardes originales sont conservées localement chez le propriétaire et ne sont pas publiées ici.

## Sources et licence

- [Marlin 2.1.2.10](https://github.com/MarlinFirmware/Marlin/releases/tag/2.1.2.10).
- [Configuration officielle Geeetech A20M correspondante](https://github.com/MarlinFirmware/Configurations/tree/release-2.1.2.10/config/examples/Geeetech/A20M).
- [Marlin, documentation des langues](https://marlinfw.org/docs/settings/interface.html).

Les configurations dérivent du projet Marlin. Les modifications et scripts de ce dépôt sont distribués sous **GPL-3.0-or-later** ; voir [LICENSE](LICENSE). Le code source complet de la base et son empreinte sont référencés dans `upstream.json` ; les configurations modifiées sont intégralement fournies dans `config/`.

## Télécharger et partager gratuitement

Le projet est disponible publiquement sur [GitHub](https://github.com/theodore10536/THEO20m). Le bouton **Code → Download ZIP** permet de télécharger les sources gratuitement. Vous pouvez les utiliser, les modifier et les redistribuer selon la licence GPL-3.0-or-later, en conservant les mentions de licence et en fournissant les sources requises.

Les autres plateformes peuvent partager le lien de ce dépôt. Ne pas présenter ce prototype comme un firmware validé pour toutes les A20M. Le référencement par les moteurs de recherche dépend de leurs robots et n’est pas garanti.
