# Validation et migration de Firmware 3D personnalisable

## Valeurs établies par lecture USB

| Élément | Valeur relevée |
|---|---|
| Processeur | ATmega2560, signature 0x1e9801 |
| Vitesse USB Marlin | 250000 bauds |
| Extrudeuses logiques | 1 |
| Pas/mm X, Y, Z, E | 80.40, 80.80, 398.00, 420.00 |
| Vitesses maximales X, Y, Z, E | 300, 300, 5, 50 mm/s |
| Accélérations maximales X, Y, Z, E | 3000, 3000, 200, 3000 mm/s² |
| Accélérations impression, rétraction, déplacement | 4000, 250, 4000 mm/s² |
| Junction deviation | 0.01 mm |
| PID buse P, I, D | 15.20, 1.28, 45.14 |
| PID plateau P, I, D | 42.96, 8.32, 147.80 |
| Préchauffage PLA buse/plateau | 200 / 60 °C |
| Préchauffage ABS buse/plateau | 240 / 100 °C |
| UBL | actif, emplacement 1, fondu à 10 mm |
| Linear Advance K | 0 |
| Détection de filament | fonction disponible, désactivée, distance 2 mm |
| Chargement / déchargement | 200 / 500 mm |
| Reprise après coupure | activée |
| Sonde Z déclarée par M115 | absente |

Ces valeurs sont des réglages existants, pas une validation de leur adéquation mécanique. Les autres paramètres avancés de mouvement (M205 B/S/T), les limites géométriques et les fonctions spécifiques à l'ancien firmware restent à comparer avant migration.

## Hypothèses du prototype, à confirmer avant flash

| Élément | Choix du prototype | Statut |
|---|---|---|
| Carte et broches | BOARD_GT2560_V3_A20 | exemple officiel A20M, révision physique inconnue |
| Pilotes moteurs | A4988 | exemple officiel, non vérifié physiquement |
| Sondes thermiques | type Marlin 1 pour buse et plateau | exemple officiel, non vérifié |
| Sens des moteurs et fins de course | configuration officielle A20M | non vérifié sur cette machine modifiée |
| Moteurs d'extrusion | un seul, pas de mélange | cohérent avec le prototype demandé, à confirmer physiquement |
| Surface / hauteur | 255 × 255 × 250 mm | exemple officiel, non mesuré |
| Écran | contrôleur graphique 12864 de l'exemple officiel | modèle exact et rendu du É à vérifier |
| UBL | 5 × 5, X 5–250, Y 5–240 | reconstruction partielle ; sortie du relevé original incomplète |
| Reprise après coupure | entrée 69, active bas | exemple officiel, câblage non vérifié |

L'EEPROM d'origine entière est sauvegardée. Aucun maillage n'a encore été converti ou injecté dans Firmware 3D personnalisable. Ne pas considérer l'activation d'UBL à la compilation comme une restauration du calibrage.

## Ordre de vérification sur la machine

1. Confirmer les références et le câblage ; adapter les configurations et recompiler.
2. Vérifier les sauvegardes de la flash et de l'EEPROM et la méthode de restauration adaptée au bootloader, avant toute écriture.
3. Documenter le format du maillage original, ses coordonnées et ses 25 hauteurs si la grille 5 × 5 est confirmée. Conserver aussi les autres emplacements sauvegardés ; ne pas les écraser.
4. Préparer une migration explicite des réglages et des maillages, sans M502. Vérifier la compatibilité EEPROM ; une nouvelle version peut démarrer avec ses valeurs de compilation si le format ancien est refusé.
5. Après un flash validé : vérifier l'identification USB, les températures ambiantes sans chauffe et le rendu des menus avant tout mouvement.
6. Vérifier séparément fins de course, sens de déplacement, courses et arrêt. Puis contrôler la chauffe, le plateau et le ventilateur sous surveillance, et enfin l'extrusion à température adaptée.
7. Comparer les réglages relevés et les hauteurs de maillage avant/après, puis réaliser une impression contrôlée avant de qualifier cette version de compatible.

Les étapes sur machine n'ont pas encore été réalisées. Aucun script de ce dépôt ne flashe, ne chauffe, ne déplace les axes ni ne réinitialise l'EEPROM.
