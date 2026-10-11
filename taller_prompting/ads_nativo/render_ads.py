# Renderiza los anuncios Meta: foto 100% Soul 3.01 + texto en HTML (Chrome headless).
# Uso: python render_ads.py [c1 c2 ...]   -> final/cN_{4x5,9x16}.png
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800'
         '&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">')

BASE = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:%(H)dpx;overflow:hidden;background:#111}
body{position:relative;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0;background:url('%(img)s') %(pos)s/cover no-repeat}
.serif{font-family:'Playfair Display',serif;font-style:italic;font-weight:700}
.abs{position:absolute}
.price{text-shadow:0 2px 12px rgba(0,0,0,.6)}
.pill{display:inline-block;border-radius:999px;padding:24px 56px;font-weight:800;font-size:46px;letter-spacing:.01em}
"""

DET = "21 · 22 · 23 OCT · 2 A 5 PM · AUDITORIO FENATRAPE"
FASE = os.environ.get("FASE", "1")
PRICE = ("$65 hasta el 5 de octubre. Luego $75 y $120. Cupos limitados." if FASE == "1" else "$75 hasta el 15 de octubre. Luego $120. Cupos limitados.")
OUTDIR = "final" if FASE == "1" else "final_fase2"


def page(fmt, img, pos, css, body):
    H = 1350 if fmt == "4x5" else 1920
    style = BASE % dict(H=H, img=img, pos=pos) + css
    return f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{FONTS}<style>{style}</style></head><body><div class='bg'></div>{body}</body></html>"


# ---------- C1: foto candid + titular editorial (emprendedores) ----------
def c1(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:{'62%' if f45 else '40%'};background:linear-gradient(180deg,rgba(247,241,232,.86),rgba(247,241,232,0))}}
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:{'38%' if f45 else '40%'};background:linear-gradient(0deg,rgba(0,0,0,.84),rgba(0,0,0,0))}}
    .eyebrow{{left:70px;top:{70 if f45 else 310}px;font-weight:800;font-size:32px;letter-spacing:.14em;color:#8f1d12;white-space:nowrap}}
    .t1{{left:66px;top:{118 if f45 else 360}px;font-size:{150 if f45 else 150}px;line-height:1;color:#15110e;white-space:nowrap}}
    .t2{{left:70px;top:{268 if f45 else 520}px;font-size:{80 if f45 else 82}px;line-height:1.02;color:#c0261a;white-space:nowrap}}
    .sub{{left:72px;{'bottom:240px' if f45 else 'top:640px'};width:{600 if f45 else 420}px;font-weight:700;font-size:44px;line-height:1.25;color:{'#fff' if f45 else '#15110e'}}}
    .cta{{left:70px;bottom:{84 if f45 else 520}px;background:#fff;color:#15110e}}
    .price{{left:455px;bottom:{84 if f45 else 524}px;color:#fff;font-weight:700;font-size:36px;line-height:1.3}}
    """
    body = f"""<div class='shade'></div><div class='shade2'></div>
    <div class='abs eyebrow'>21 · 22 · 23 OCT · FENATRAPE</div>
    <div class='abs serif t1'>Taller de IA</div>
    <div class='abs serif t2'>para emprendedores</div>
    <div class='abs sub'>Aprende a pedirle bien a la IA y úsala en tu negocio.</div>
    <div class='abs pill cta'>Regístrate</div>
    <div class='abs price'>2 A 5 PM · AUDITORIO FENATRAPE<br>{PRICE}</div>"""
    return page(fmt, img, "center top" if f45 else "center bottom", css, body)


# ---------- C2: nota de iPhone (dueños de negocio) ----------
def c2(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .card{{position:absolute;left:44px;right:44px;bottom:{54 if f45 else 400}px;background:rgba(28,28,30,.93);border-radius:44px;padding:44px 48px 48px;color:#fff}}
    .nav{{display:flex;justify-content:space-between;color:#0a84ff;font-size:38px;font-weight:600;margin-bottom:26px}}
    .ttl{{font-size:{64 if f45 else 68}px;font-weight:800;line-height:1.08;margin-bottom:26px;letter-spacing:-.01em}}
    .li{{font-size:40px;line-height:1.3;color:#e5e5ea;margin-bottom:12px;padding-left:46px;position:relative}}
    .li:before{{content:'';position:absolute;left:0;top:11px;width:26px;height:26px;border-radius:50%;border:3px solid #0a84ff}}
    .det{{font-size:36px;font-weight:700;color:#ffffff;margin-top:22px;line-height:1.3}}
    .pr{{font-size:36px;color:#aeaeb2;margin-top:8px;font-weight:600}}
    .btn{{display:inline-block;margin-top:26px;background:#0a84ff;color:#fff;border-radius:999px;padding:22px 54px;font-size:44px;font-weight:800}}
    """
    body = f"""<div class='card'>
    <div class='nav'><span>‹ Notas</span><span>···</span></div>
    <div class='ttl'>Taller de IA para dueños de negocio</div>
    <div class='li'>Pedirle bien las cosas a la IA</div>
    <div class='li'>Atender a tus clientes con ayuda de IA</div>
    <div class='li'>Ordenar tu negocio sin ser técnico</div>
    <div class='det'>21, 22 y 23 de octubre · Auditorio Fenatrape</div>
    <div class='pr'>{PRICE}</div>
    <div class='btn'>Regístrate</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---------- C3: chat de WhatsApp (empresarios) ----------
def c3(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .panel{{position:absolute;left:0;right:0;bottom:{0 if f45 else 384}px;background:#0b141a;padding:0 0 {40 if f45 else 36}px;border-radius:{0 if f45 else 36}px {0 if f45 else 36}px {0 if f45 else 36}px {0 if f45 else 36}px;{'margin:0 44px;left:0;right:0' if not f45 else ''}}}
    .hd{{background:#202c33;display:flex;align-items:center;gap:22px;padding:{26 if f45 else 16}px 44px}}
    .av{{width:{96 if f45 else 70}px;height:{96 if f45 else 70}px;border-radius:50%;background:#00a884;color:#fff;font-weight:800;font-size:52px;display:flex;align-items:center;justify-content:center}}
    .nm{{color:#e9edef;font-size:{50 if f45 else 44}px;font-weight:800;line-height:1.05}}
    .st{{color:#8696a0;font-size:32px;font-weight:600}}
    .ch{{padding:{30 if f45 else 18}px 44px 0}}
    .b{{max-width:86%;border-radius:26px;padding:{22 if f45 else 14}px 28px;font-size:{42 if f45 else 36}px;line-height:1.25;margin-bottom:{22 if f45 else 14}px;color:#e9edef;font-weight:500}}
    .in{{background:#202c33;border-top-left-radius:6px}}
    .out{{background:#005c4b;margin-left:auto;border-top-right-radius:6px}}
    .tm{{font-size:28px;color:#8696a0;text-align:right;margin-top:6px}}
    .btn{{margin:8px 44px 0;display:block;text-align:center;background:#25d366;color:#06281a;border-radius:999px;padding:{24 if f45 else 16}px 0;font-size:{46 if f45 else 40}px;font-weight:800}}
    .pr{{color:#8696a0;font-size:32px;text-align:center;margin-top:{16 if f45 else 10}px;font-weight:600}}
    """
    body = f"""<div class='panel'>
    <div class='hd'><div class='av'>IA</div><div><div class='nm'>Taller de IA para empresarios</div><div class='st'>en línea</div></div></div>
    <div class='ch'>
      <div class='b in'>¿Cómo le hablo a la IA para que sí me entienda?<div class='tm'>9:41</div></div>
      <div class='b out'>Eso se aprende. 21, 22 y 23 de octubre en el Auditorio Fenatrape.<div class='tm'>9:42 ✓✓</div></div>
    </div>
    <div class='btn'>Regístrate</div>
    <div class='pr'>{PRICE}</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---------- C4: portada editorial (inmobiliarias) ----------
def c4(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .box{{position:absolute;left:50px;right:50px;bottom:{50 if f45 else 410}px;background:rgba(255,255,255,.94);padding:46px 54px 50px}}
    .mast{{font-weight:800;font-size:30px;letter-spacing:.3em;color:#15110e;margin-bottom:10px}}
    .t1{{font-size:124px;line-height:1;color:#15110e;white-space:nowrap}}
    .t2{{font-size:88px;line-height:1.02;color:#a8271b;margin-bottom:16px;white-space:nowrap}}
    .sub{{font-weight:700;font-size:40px;line-height:1.28;color:#15110e;margin-bottom:20px}}
    .det{{font-weight:800;font-size:32px;letter-spacing:.08em;color:#15110e;line-height:1.4}}
    .pr{{font-weight:700;font-size:36px;color:#15110e;margin:8px 0 22px}}
    .cta{{background:#15110e;color:#fff}}
    """
    body = f"""<div class='box'><div class='mast'>BYRON CUJANO</div><div class='serif t1'>Taller de IA</div>
    <div class='serif t2'>para inmobiliarias</div><div class='sub'>Atiende, publica y da seguimiento con IA.</div>
    <div class='det'>21 · 22 · 23 OCT · 2 A 5 PM<br>AUDITORIO FENATRAPE</div><div class='pr'>{PRICE}</div>
    <div class='pill cta'>Regístrate</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---------- C5: detrás de cámaras (atención al cliente) ----------
def c5(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:{'30%' if f45 else '28%'};background:linear-gradient(180deg,rgba(0,0,0,.7),rgba(0,0,0,0))}}
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:{'38%' if f45 else '44%'};background:linear-gradient(0deg,rgba(0,0,0,.86),rgba(0,0,0,0))}}
    .t1{{left:66px;top:{70 if f45 else 300}px;font-size:{140 if f45 else 136}px;line-height:1;color:#fff}}
    .t2{{left:70px;top:{200 if f45 else 436}px;font-size:{76 if f45 else 82}px;line-height:1.02;color:#ff6a4d;white-space:nowrap}}
    .sub,.det{{text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .sub{{left:72px;bottom:{360 if f45 else 740}px;width:{600 if f45 else 860}px;font-weight:700;font-size:46px;line-height:1.25;color:#fff}}
    .det{{left:72px;bottom:{270 if f45 else 660}px;font-weight:800;font-size:32px;letter-spacing:.1em;color:#fff}}
    .cta{{left:70px;bottom:{104 if f45 else 520}px;background:#fff;color:#111}}
    .pr{{left:440px;bottom:{{PRB}}px;color:#fff;font-weight:700;font-size:36px;line-height:1.3}}
    """.replace("{PRB}", str(116 if f45 else 524))
    body = f"""<div class='shade'></div><div class='shade2'></div>
    <div class='abs serif t1'>Taller de IA</div><div class='abs serif t2'>para atención al cliente</div>
    <div class='abs sub'>Agentes de IA que atienden a tus clientes.</div>
    <div class='abs det'>{DET}</div>
    <div class='abs pill cta'>Regístrate</div><div class='abs price pr'>{PRICE}</div>"""
    return page(fmt, img, "center top", css, body)


CONCEPTS = {"c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5}


def render(cid, fmt):
    img = os.path.join(HERE, "fotos_soul", f"{cid}_{'45' if fmt == '4x5' else '916'}.png").replace("\\", "/")
    html = CONCEPTS[cid](fmt, "file:///" + img)
    hp = os.path.join(HERE, f"_{cid}_{fmt}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    os.makedirs(os.path.join(HERE, OUTDIR), exist_ok=True)
    out = os.path.join(HERE, OUTDIR, f"{cid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=12000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = sys.argv[1:] or list(CONCEPTS)
    for cid in ids:
        for fmt in ("4x5", "9x16"):
            print(render(cid, fmt))
