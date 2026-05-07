from pathlib import Path
import base64
import zipfile

root = Path(__file__).resolve().parent
parts = sorted(root.glob('mitaller_android_final.zip.b64.part*'))
if not parts:
    raise SystemExit('No encuentro archivos .part')

encoded = ''.join(p.read_text().strip() for p in parts)
zip_path = root / 'mitaller_android_final_2026_05_07.zip'
zip_path.write_bytes(base64.b64decode(encoded))

with zipfile.ZipFile(zip_path, 'r') as zf:
    bad = zf.testzip()
    if bad:
        raise SystemExit(f'ZIP corrupto en: {bad}')
    zf.extractall(root / 'MitallerAndroid')

print(f'OK: creado {zip_path.name}')
print('Proyecto extraído en ./MitallerAndroid')
