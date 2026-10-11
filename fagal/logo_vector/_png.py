import pathlib, re, subprocess, tempfile
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
for f in sorted(pathlib.Path('.').glob('FAGAL_*_blanco.svg')) + sorted(pathlib.Path('.').glob('FAGAL_*_negro.svg')):
    s = f.read_text(encoding='utf-8'); vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    w, h = float(vb.group(1)), float(vb.group(2)); W = 2000; H = round(W * h / w)
    html = pathlib.Path(f'_t_{f.stem}.html'); html.write_text(f"<html><body style='margin:0;background:transparent'><img src='{f.name}' style='width:{W}px;height:{H}px;display:block'></body></html>", encoding='utf-8')
    out = f.with_suffix('.png').resolve()
    subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--default-background-color=00000000', f'--window-size={W},{H}', f'--screenshot={out}', html.resolve().as_uri()], capture_output=True)
    html.unlink(); print(out.name, W, H)
# vista previa
pv = """<html><body style='margin:0;display:grid;grid-template-columns:1fr 1fr;width:1600px'>
<div style='background:#0c1016;padding:40px;display:flex;flex-direction:column;gap:40px;align-items:center'>
<img src='FAGAL_logo_vertical_blanco.svg' style='height:300px'><img src='FAGAL_logo_horizontal_blanco.svg' style='height:130px'><img src='FAGAL_monograma_blanco.svg' style='height:120px'></div>
<div style='background:#f3f4f6;padding:40px;display:flex;flex-direction:column;gap:40px;align-items:center'>
<img src='FAGAL_logo_vertical_negro.svg' style='height:300px'><img src='FAGAL_logo_horizontal_negro.svg' style='height:130px'><img src='FAGAL_monograma_negro.svg' style='height:120px'></div></body></html>"""
p = pathlib.Path('_prev.html'); p.write_text(pv, encoding='utf-8')
subprocess.run([CH, '--headless=new', '--disable-gpu', '--window-size=1600,760', f'--screenshot={pathlib.Path("_prev.png").resolve()}', p.resolve().as_uri()], capture_output=True)
