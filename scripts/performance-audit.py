from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
issues=[];stats={'html':0,'json':0,'js':0,'cssBytes':0,'jsBytes':0,'imageBytes':0,'pdfBytes':0}
for p in root.rglob('*.json'):
 try:json.loads(p.read_text())
 except Exception as e:issues.append(f'Invalid JSON {p.relative_to(root)}: {e}')
 stats['json']+=1
for p in root.rglob('*.html'):
 if 'partials' in p.parts:continue
 stats['html']+=1;s=p.read_text(errors='ignore')
 if '<meta name="viewport"' not in s:issues.append(f'Missing viewport: {p.relative_to(root)}')
 if 'assets/js/performance.js' not in s and p.name!='offline.html':issues.append(f'Missing performance module: {p.relative_to(root)}')
for p in root.glob('assets/js/*.js'):stats['js']+=1;stats['jsBytes']+=p.stat().st_size
for p in root.glob('assets/css/*.css'):stats['cssBytes']+=p.stat().st_size
for p in root.glob('assets/images/**/*'):
 if p.is_file():stats['imageBytes']+=p.stat().st_size
for p in root.glob('assets/docs/*.pdf'):stats['pdfBytes']+=p.stat().st_size
stats['totalAssetBytes']=stats['cssBytes']+stats['jsBytes']+stats['imageBytes']+stats['pdfBytes']
print(json.dumps({'stats':stats,'issues':issues},indent=2));sys.exit(1 if issues else 0)
