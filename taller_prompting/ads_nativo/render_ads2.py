# Ronda 2: estilos nuevos con hooks y escala de precios. Fotos 100% Soul 3.01 (fotos_soul/), texto en HTML.
# Uso: python render_ads2.py [s1 s2 ...]  -> final2/sN_{4x5,9x16}.png
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900'
         '&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">')
BASE = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:%(H)dpx;overflow:hidden;background:#111}
body{position:relative;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0;background:url('%(img)s') %(pos)s/cover no-repeat}
.abs{position:absolute}
.serif{font-family:'Playfair Display',serif;font-weight:700}
.pill{display:inline-block;border-radius:999px;padding:24px 56px;font-weight:800;font-size:46px}
.lad .r{display:flex;justify-content:space-between;align-items:baseline;font-size:34px;font-weight:700;padding:9px 0;border-bottom:2px solid rgba(128,128,128,.35)}
.lad .r b{font-size:44px;font-weight:900}
.lad .now b{color:#d6281c}
"""
FASE = os.environ.get("FASE", "1")
NOW = 0 if FASE == "1" else 1
LAD_ROWS = [("1 al 5 OCT · LANZAMIENTO", "$65", NOW == 0), ("5 al 15 OCT · PREVENTA", "$75", NOW == 1), ("15 al 21 OCT · NORMAL", "$120", False)]
OUTDIR = "final2" if FASE == "1" else "final2_fase2"
FOOT = "21 · 22 · 23 OCT · 2 A 5 PM · AUDITORIO FENATRAPE · CUPOS LIMITADOS"


def ladder(color="#111", accent="#d6281c", now_label="AHORA", short=False):
    labels = {"$65": "1-5 OCT · Lanzamiento", "$75": "5-15 OCT · Preventa", "$120": "15-21 OCT · Normal"}
    rows = "".join(f"<div class='r{' now' if n else ''}'><span>{labels[p] if short else t}{' ← ' + now_label if (n and now_label) else ''}</span><b>{p}</b></div>"
                   for t, p, n in LAD_ROWS)
    return f"<div class='lad' style='color:{color}'>{rows}</div><style>.lad .now b{{color:{accent}}}</style>"


def page(fmt, img, pos, css, body):
    H = 1350 if fmt == "4x5" else 1920
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{FONTS}<style>{BASE % dict(H=H, img=img, pos=pos)}{css}</style>"
            f"</head><body><div class='bg'></div>{body}</body></html>")


# S1 hoja de ruta (foto c3: sala de juntas, caminando)
def s1(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .card{{position:absolute;left:0;right:0;bottom:{0 if f45 else 384}px;background:#f4efe6;color:#15110e;padding:{34 if f45 else 46}px 60px {36 if f45 else 46}px}}
    .eb{{font-weight:800;font-size:30px;letter-spacing:.16em;color:#a8271b;margin-bottom:12px}}
    .h{{font-size:{58 if f45 else 74}px;line-height:1.08;margin-bottom:{16 if f45 else 22}px}}
    .st{{display:flex;gap:14px;margin-bottom:{16 if f45 else 24}px}}
    .st div{{flex:1;background:#fff;border-radius:18px;padding:16px 18px;font-size:32px;font-weight:700;line-height:1.2}}
    .st1{{font-size:32px;font-weight:700;margin-bottom:14px;color:#222}} .st1 b{{color:#a8271b;letter-spacing:.06em}}
    .st span{{display:block;font-size:30px;letter-spacing:.1em;color:#a8271b;font-weight:800;margin-bottom:4px}}
    .cta{{background:#15110e;color:#fff;margin-top:16px;padding:20px 52px}}
    .ft{{font-size:30px;font-weight:700;margin-top:12px;letter-spacing:.02em;color:#444}}
    """
    body = f"""<div class='card'><div class='eb'>TALLER DE IA PARA TU NEGOCIO</div>
    <div class='serif h'>Desde usar ChatGPT hasta tu primera página web</div>
    {"<div class='st1'><b>DÍA 1</b> ChatGPT · <b>DÍA 2</b> Anuncios · <b>DÍA 3</b> Tu web</div>" if f45 else "<div class='st'><div><span>DÍA 1</span>ChatGPT sin miedo</div><div><span>DÍA 2</span>Contenido y anuncios</div><div><span>DÍA 3</span>Tu página web</div></div>"}
    {ladder(now_label='')}<div class='pill cta'>Regístrate</div><div class='ft'>21·22·23 OCT · AUDITORIO FENATRAPE · CUPOS LIMITADOS</div></div>"""
    return page(fmt, img, "center top", css, body)


# S2 creencia rota (foto c1: oficina, ríe)
def s2(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .shade{{position:absolute;left:0;right:0;bottom:0;height:{'52%' if f45 else '50%'};background:linear-gradient(0deg,rgba(0,0,0,.9) 0%,rgba(0,0,0,.78) 55%,rgba(0,0,0,0))}}
    .h{{left:66px;top:{64 if f45 else 300}px;width:{760 if f45 else 760}px;font-size:{74 if f45 else 84}px;line-height:1.06;color:#15110e}}
    .h em{{color:#c0261a}}
    .sub{{background:rgba(255,255,255,.88);padding:10px 16px;left:60px;top:{330 if f45 else 640}px;width:{380 if f45 else 440}px;font-weight:700;font-size:40px;line-height:1.25;color:#15110e}}
    .box{{position:absolute;left:60px;right:60px;bottom:{50 if f45 else 400}px;color:#fff}}
    .cta{{background:#fff;color:#15110e;margin-top:20px}}
    """
    body = f"""<div class='shade'></div>
    <div class='abs serif h'>¿Todavía le escribes a <em>ChatGPT</em> como a Google?</div>
    <div class='abs sub'>Aprende a pedirle bien y úsalo en tu negocio.</div>
    <div class='box'>{ladder('#fff','#ff6a4d')}<div class='pill cta'>Regístrate</div>
    <div style='font-size:30px;font-weight:700;margin-top:14px;opacity:.9'>21 · 22 · 23 OCT · AUDITORIO FENATRAPE · CUPOS LIMITADOS</div></div>"""
    return page(fmt, img, "center top" if f45 else "center top", css, body)


# S3 tarjeta de temario con checklist (foto c4: departamento, traje)
def s3(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .card{{position:absolute;{'left:40px;top:70px;width:610px' if f45 else 'left:50px;right:50px;bottom:400px'};background:rgba(255,255,255,.95);padding:44px 46px 46px;color:#15110e}}
    .eb{{font-weight:800;font-size:30px;letter-spacing:.16em;color:#a8271b;margin-bottom:12px}}
    .h{{font-size:{56 if f45 else 66}px;line-height:1.08;margin-bottom:20px}}
    .ck{{display:flex;gap:16px;align-items:flex-start;font-size:{36 if f45 else 38}px;font-weight:700;line-height:1.2;margin-bottom:14px}}
    .ck i{{flex:none;width:36px;height:36px;border:4px solid #15110e;border-radius:8px;margin-top:2px;position:relative}}
    .ck i:after{{content:'✓';position:absolute;left:3px;top:-12px;font-size:40px;color:#c0261a;font-style:normal;font-weight:900}}
    .cta{{background:#15110e;color:#fff;margin-top:22px}}
    .lad{{margin-top:18px}} .lad .r{{font-size:{31 if f45 else 34}px}} .lad .r b{{font-size:{40 if f45 else 44}px}}
    """
    body = f"""<div class='card'><div class='eb'>TALLER DE IA PARA EMPRENDEDORES</div>
    <div class='serif h'>3 días, 3 cosas que tu negocio ya puede automatizar</div>
    <div class='ck'><i></i><span>Atender clientes con ayuda de IA</span></div>
    <div class='ck'><i></i><span>Crear tu contenido y tus anuncios</span></div>
    <div class='ck'><i></i><span>Hacer tu primera página web</span></div>
    {ladder(now_label='', short=f45)}<div class='pill cta'>Regístrate</div>
    <div style='font-size:30px;font-weight:700;margin-top:14px;color:#444'>AUDITORIO FENATRAPE · CUPOS LIMITADOS</div></div>"""
    return page(fmt, img, "center top", css, body)


# S4 escalera de precios (foto c5: auditorio, diadema)
def s4(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:{'30%' if f45 else '26%'};background:linear-gradient(180deg,rgba(0,0,0,.78),rgba(0,0,0,0))}}
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:{'46%' if f45 else '44%'};background:linear-gradient(0deg,rgba(0,0,0,.9) 0%,rgba(0,0,0,.7) 60%,rgba(0,0,0,0))}}
    .h{{left:66px;right:66px;top:{64 if f45 else 300}px;font-weight:900;font-size:{80 if f45 else 92}px;line-height:1;color:#fff;letter-spacing:-.01em}}
    .h em{{font-style:normal;color:#ff5a3d}}
    .sub{{left:70px;top:{250 if f45 else 520}px;font-weight:700;font-size:38px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .bars{{position:absolute;left:50px;right:50px;bottom:{200 if f45 else 545}px;display:flex;gap:16px;align-items:flex-end}}
    .bar{{flex:1;border-radius:20px 20px 0 0;padding:22px 20px;color:#fff;text-align:center}}
    .bar b{{display:block;font-size:84px;font-weight:900;line-height:1}}
    .bar span{{display:block;font-size:32px;font-weight:700;margin-top:6px;line-height:1.15}}
    .b1{{height:215px;background:{'#d6281c' if NOW==0 else '#2b2b2b;border:3px solid #555'}}} .b2{{height:280px;background:{'#d6281c' if NOW==1 else '#2b2b2b;border:3px solid #555'}}} .b3{{height:350px;background:#2b2b2b;border:3px solid #555}}
    .cta{{left:70px;bottom:{44 if f45 else 410}px;background:#fff;color:#111}}
    .ft{{left:430px;bottom:{50 if f45 else 416}px;color:#fff;font-weight:700;font-size:30px;line-height:1.3;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    """
    body = f"""<div class='shade'></div><div class='shade2'></div>
    <div class='abs h'>El precio del taller <em>sube cada semana</em></div>
    <div class='abs sub'>Taller de IA para tu negocio</div>
    <div class='bars'><div class='bar b1'><b>$65</b><span>1 al 5 OCT<br>LANZAMIENTO</span></div>
    <div class='bar b2'><b>$75</b><span>5 al 15 OCT<br>PREVENTA</span></div>
    <div class='bar b3'><b>$120</b><span>15 al 21 OCT<br>NORMAL</span></div></div>
    <div class='abs pill cta'>Regístrate</div><div class='abs ft'>21 · 22 · 23 OCT<br>AUDITORIO FENATRAPE · CUPOS LIMITADOS</div>"""
    return page(fmt, img, "center top", css, body)


# S5 pregunta directa con ejemplos (foto c2: cafetería, celular)
def s5(fmt, img):
    f45 = fmt == "4x5"
    css = f"""
    .shade{{position:absolute;left:0;right:0;bottom:0;height:{'72%' if f45 else '62%'};background:linear-gradient(0deg,rgba(0,0,0,.94) 0%,rgba(0,0,0,.9) 62%,rgba(0,0,0,0))}}
    .box{{position:absolute;left:60px;right:60px;bottom:{44 if f45 else 400}px;color:#fff}}
    .eb{{display:inline-block;background:#d6281c;color:#fff;font-weight:800;font-size:30px;letter-spacing:.12em;padding:8px 18px;margin-bottom:16px}}
    .h{{font-size:{74 if f45 else 70}px;line-height:1.06;margin-bottom:{20 if f45 else 14}px}}
    .pills{{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:22px}}
    .pills span{{border:3px solid #fff;border-radius:999px;padding:10px 26px;font-size:34px;font-weight:700}}
    .cta{{background:#fff;color:#111;margin-top:20px}}
    """
    body = f"""<div class='shade'></div><div class='box'><div class='eb'>TALLER DE IA PARA DUEÑOS DE NEGOCIO</div>
    <div class='serif h'>¿Qué le pedirías a la IA para tu negocio?</div>
    {'' if not f45 else "<div class='pills'><span>Responder clientes</span><span>Crear anuncios</span><span>Tu página web</span></div>"}
    {ladder('#fff','#ff6a4d')}<div class='pill cta'>Regístrate</div>
    <div style='font-size:30px;font-weight:700;margin-top:14px;opacity:.92'>21 · 22 · 23 OCT · AUDITORIO FENATRAPE · CUPOS LIMITADOS</div></div>"""
    return page(fmt, img, "center top", css, body)


STYLES = {"s1": (s1, "c3"), "s2": (s2, "c1"), "s3": (s3, "c4"), "s4": (s4, "c5"), "s5": (s5, "c2")}


def render(sid, fmt):
    fn, photo = STYLES[sid]
    img = os.path.join(HERE, "fotos_soul", f"{photo}_{'45' if fmt == '4x5' else '916'}.png").replace("\\", "/")
    hp = os.path.join(HERE, f"_{sid}_{fmt}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(fn(fmt, "file:///" + img))
    os.makedirs(os.path.join(HERE, OUTDIR), exist_ok=True)
    out = os.path.join(HERE, OUTDIR, f"{sid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=12000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    for sid in (sys.argv[1:] or list(STYLES)):
        for fmt in ("4x5", "9x16"):
            print(render(sid, fmt))
