#!/usr/bin/env python3
"""Prépare les sources officielles épinglées et applique le profil expérimental."""
from pathlib import Path
import hashlib,io,json,shutil,tarfile,urllib.request
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
print('Sources préparées : '+str(dest))
print('Compilation uniquement : python -m platformio run -d "'+str(dest)+'" -e mega2560')
print('Profil expérimental : aucune validation matérielle ni installation effectuée.')
