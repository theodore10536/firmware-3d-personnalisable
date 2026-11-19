#!/usr/bin/env python3
"""Prépare les sources officielles épinglées et applique le profil expérimental."""
from pathlib import Path
import argparse,hashlib,io,json,re,shutil,tarfile,urllib.request
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--nom', help='Nom de votre machine (1 à 16 caractères ; lettres latines conseillées).')
args=parser.parse_args()
if args.nom is not None and (not 1 <= len(args.nom) <= 16 or not args.nom.isprintable()):
 parser.error('Le nom doit contenir 1 à 16 caractères imprimables, sans retour à la ligne.')
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'upstream.json').read_text())
dest=ROOT/'build'/('Marlin-'+m['tag'])
if dest.exists():
 raise SystemExit('Le dossier build existe déjà. Utilisez-le, ou renommez-le avant de préparer une autre copie.')
print('Téléchargement de Marlin '+m['tag'])
with urllib.request.urlopen(m['archive_url'],timeout=60) as r:data=r.read()
if hashlib.sha256(data).hexdigest()!=m['archive_sha256']:
 raise SystemExit('Empreinte des sources incorrecte ; préparation interrompue.')
(ROOT/'build').mkdir(exist_ok=True)
with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
 # Python >= 3.12 : filtre sécurisé, aucune extraction de lien externe.
 t.extractall(ROOT/'build',filter='data')
for name in ['Configuration.h','Configuration_adv.h']:
 shutil.copyfile(ROOT/'config'/name,dest/'Marlin'/name)
if args.nom is not None:
 config=dest/'Marlin/Configuration.h'
 content=config.read_text()
 content,count=re.subn(r'^#define CUSTOM_MACHINE_NAME[^\n]*',lambda m:'#define CUSTOM_MACHINE_NAME '+json.dumps(args.nom,ensure_ascii=False),content,flags=re.M)
 if count != 1:raise SystemExit('Définition du nom introuvable ou ambiguë.')
 config.write_text(content)
 print('Nom personnalisé : '+args.nom)
print('Sources préparées : '+str(dest))
print('Compilation uniquement : python -m platformio run -d "'+str(dest)+'" -e mega2560')
print('Profil expérimental : aucune validation matérielle ni installation effectuée.')
