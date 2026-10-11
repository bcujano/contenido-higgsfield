# Set 3: nueva linea grafica "datos primero" (Anton + Space Grotesk, azul electrico / naranja / negro).
# Fotos 100% Soul 3.01 (fotos_set3/<ID>_45.png y <ID>_916.png). Segmenta desde el creativo.
# Uso: FASE=1 python render_set3.py [ID ...]   (FASE=2 resalta Preventa $75)
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FASE = os.environ.get("FASE", "1")
NOW = 0 if FASE == "1" else 1
OUT = os.path.join(HERE, "juego_set3", "fase1_hasta-5-oct" if FASE == "1" else "fase2_5-al-15-oct")
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@500;600;700'
         '&display=swap" rel="stylesheet">')
BLUE, ORANGE, INK = "#2342FF", "#FF5A1F", "#0b0d12"

BASE = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:%(H)dpx;overflow:hidden;background:#000}
body{position:relative;font-family:'Space Grotesk',sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0;background:url('%(img)s') %(pos)s/cover no-repeat}
.abs{position:absolute}
.an{font-family:'Anton',sans-serif;text-transform:uppercase;letter-spacing:.005em}
.tag{display:inline-block;background:%(blue)s;color:#fff;font-weight:700;font-size:38px;letter-spacing:.06em;padding:10px 22px;text-transform:uppercase}
.chips{display:flex;gap:14px}
.chip{flex:1;border:3px solid rgba(255,255,255,.55);padding:14px 10px 12px;text-align:center;background:rgba(0,0,0,.35)}
.chip small{display:block;font-size:32px;font-weight:700;letter-spacing:.04em;line-height:1.1}
.chip b{display:block;font-family:'Anton';font-weight:400;font-size:84px;line-height:1.05}
.chip.on{background:%(orange)s;border-color:%(orange)s;color:#fff}
.cta{display:block;text-align:center;background:%(orange)s;color:#fff;font-weight:700;font-size:48px;letter-spacing:.04em;padding:24px 20px;text-transform:uppercase}
.cta.w{background:#fff;color:%(ink)s}
.sh{text-shadow:0 3px 18px rgba(0,0,0,.65)}
"""


def chips(light=False):
    items = [("LANZAMIENTO", "1-5 OCT", "$65"), ("PREVENTA", "5-15 OCT", "$75"), ("NORMAL", "15-21 OCT", "$120")]
    out = ""
    for i, (a, b, c) in enumerate(items):
        on = " on" if i == NOW else ""
        out += f"<div class='chip{on}'><small>{a}</small><small style='font-weight:500'>{b}</small><b>{c}</b></div>"
    return f"<div class='chips'>{out}</div>"


def page(fmt, img, pos, css, body):
    H = 1350 if fmt == "4x5" else 1920
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{FONTS}<style>"
            f"{BASE % dict(H=H, img=img, pos=pos, blue=BLUE, orange=ORANGE, ink=INK)}{css}</style></head>"
            f"<body><div class='bg'></div>{body}</body></html>")


def geo(fmt):
    f45 = fmt == "4x5"
    return f45, (56 if f45 else 300), (44 if f45 else 400)  # f45, top_y, bottom_y


# ---- T1: titular sobre la foto + panel azul de datos abajo ----
def t1(fmt, img, seg, hook, light=False):
    f45, top, bot = geo(fmt)
    ink = "#0b0d12" if light else "#fff"
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:46%;background:{'linear-gradient(180deg,rgba(255,255,255,.7),rgba(255,255,255,0))' if light else 'linear-gradient(180deg,rgba(0,0,0,.6),rgba(0,0,0,0))'}}}
    .t{{left:60px;right:60px;top:{top + 60}px;font-size:{112 if f45 else 120}px;line-height:.98;color:{ink}}}
    .panel{{position:absolute;left:0;right:0;bottom:{bot - 44 if f45 else bot}px;background:{BLUE};padding:30px 56px 34px}}
    .d{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:20px}}
    .d .big{{font-size:104px;line-height:1}}
    .d .sm{{text-align:right;font-weight:700;font-size:34px;line-height:1.2}}
    .cta{{margin-top:20px}}
    """
    body = f"""<div class='shade'></div>
    <div class='abs' style='left:60px;top:{top}px'><span class='tag'>{seg}</span></div>
    <div class='abs an t sh'>{hook}</div>
    <div class='panel'><div class='d'><div class='an big'>21·22·23 OCT</div><div class='sm'>2 A 5 PM<br>AUDITORIO FENATRAPE<br>CERTIFICADO INCLUIDO</div></div>
    {chips()}<div class='cta'>Reserva tu cupo · Cupos limitados</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---- T2: titular gigante arriba + banda negra con fecha y precios ----
def t2(fmt, img, seg, hook, light=False):
    f45, top, bot = geo(fmt)
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:50%;background:linear-gradient(180deg,rgba(0,0,0,.72),rgba(0,0,0,0))}}
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:44%;background:linear-gradient(0deg,rgba(0,0,0,.94) 40%,rgba(0,0,0,0))}}
    .t{{left:56px;right:40px;top:{top + 62}px;font-size:{150 if f45 else 164}px;line-height:.95}}
    .t em{{font-style:normal;color:{ORANGE}}}
    .box{{position:absolute;left:56px;right:56px;bottom:{bot}px}}
    .row{{display:flex;gap:26px;align-items:center;margin-bottom:18px}}
    .row .an{{font-size:92px;line-height:1;color:#fff}}
    .row div.s{{font-weight:700;font-size:34px;line-height:1.2}}
    """
    body = f"""<div class='shade'></div><div class='shade2'></div>
    <div class='abs' style='left:56px;top:{top}px'><span class='tag'>{seg}</span></div>
    <div class='abs an t sh'>{hook}</div>
    <div class='box'><div class='row'><div class='an'>21·22·23 OCT</div><div class='s'>2 A 5 PM · AUDITORIO FENATRAPE<br>CERTIFICADO INCLUIDO · CUPOS LIMITADOS</div></div>
    {chips()}<div class='cta' style='margin-top:18px'>Reserva tu cupo</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---- T3: entrada tipo ticket ----
def t3(fmt, img, seg, hook, light=False, side="left"):
    f45, top, bot = geo(fmt)
    w = 540 if f45 else 600
    css = f"""
    .dim{{position:absolute;inset:0;background:rgba(0,0,0,.18)}}
    .tk{{position:absolute;{side}:44px;top:{top + 20}px;width:{w}px;background:#fff;color:{INK};padding:34px 34px 30px}}
    .tk:before,.tk:after{{content:'';position:absolute;top:{'46%'};width:44px;height:44px;border-radius:50%;background:#000;opacity:.0}}
    .tt{{font-size:30px;font-weight:700;letter-spacing:.2em;color:{BLUE};margin-bottom:8px}}
    .th{{font-size:{86 if f45 else 92}px;line-height:.98;color:{INK};margin-bottom:12px}}
    .hk{{font-size:36px;font-weight:700;line-height:1.2;margin-bottom:16px}}
    .dash{{border-top:4px dashed {INK};margin:14px -34px 14px;opacity:.5}}
    .dt{{font-size:96px;line-height:1;color:{BLUE}}}
    .pl{{font-size:34px;font-weight:700;line-height:1.2;margin-top:6px}}
    .r{{display:flex;justify-content:space-between;align-items:baseline;font-size:34px;font-weight:700;padding:6px 0}}
    .r b{{font-family:'Anton';font-weight:400;font-size:56px}}
    .r.on{{background:{ORANGE};color:#fff;margin:0 -12px;padding:6px 12px}}
    .go{{display:block;text-align:center;background:{INK};color:#fff;font-weight:700;font-size:44px;padding:20px;margin-top:16px;text-transform:uppercase}}
    """
    rows = [("1-5 OCT · LANZAMIENTO", "$65"), ("5-15 OCT · PREVENTA", "$75"), ("15-21 OCT · NORMAL", "$120")]
    rh = "".join(f"<div class='r{' on' if i == NOW else ''}'><span>{a}</span><b>{b}</b></div>" for i, (a, b) in enumerate(rows))
    body = f"""<div class='dim'></div><div class='tk'>
    <div class='tt'>ENTRADA · {seg}</div><div class='an th'>Taller de IA</div><div class='hk'>{hook}</div>
    <div class='dash'></div><div class='an dt'>21·22·23 OCT</div><div class='pl'>2 A 5 PM · AUDITORIO FENATRAPE<br>CERTIFICADO INCLUIDO</div>
    <div class='dash'></div>{rh}<div class='go'>Reserva tu cupo</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---- T6: bloque inferior (cuando la cara esta arriba) ----
def t6(fmt, img, seg, hook, light=False):
    f45, top, bot = geo(fmt)
    css = f"""
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:72%;background:linear-gradient(0deg,rgba(0,0,0,.96) 55%,rgba(0,0,0,0))}}
    .box{{position:absolute;left:56px;right:56px;bottom:{bot}px}}
    .t{{font-size:{104 if f45 else 112}px;line-height:.98;margin:14px 0 18px}}
    .t em{{font-style:normal;color:{ORANGE}}}
    .row{{display:flex;gap:26px;align-items:center;margin-bottom:16px}}
    .row .an{{font-size:88px;line-height:1}}
    .row .s{{font-weight:700;font-size:34px;line-height:1.2}}
    """
    body = f"""<div class='shade2'></div><div class='box'><span class='tag'>{seg}</span><div class='an t'>{hook}</div>
    <div class='row'><div class='an'>21·22·23 OCT</div><div class='s'>2 A 5 PM · AUDITORIO FENATRAPE<br>CERTIFICADO INCLUIDO · CUPOS LIMITADOS</div></div>
    {chips()}<div class='cta' style='margin-top:16px'>Reserva tu cupo</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---- T4: precio gigante ----
def t4(fmt, img, seg, hook, light=False, right=False):
    f45, top, bot = geo(fmt)
    price, lab, until = ("$65", "LANZAMIENTO", "HASTA EL 5 DE OCTUBRE") if NOW == 0 else ("$75", "PREVENTA", "HASTA EL 15 DE OCTUBRE")
    css = f"""
    .shade{{position:absolute;left:0;right:0;top:0;height:46%;background:linear-gradient(180deg,rgba(0,0,0,.7),rgba(0,0,0,0))}}
    .shade2{{position:absolute;left:0;right:0;bottom:0;height:56%;background:linear-gradient(0deg,rgba(0,0,0,.95) 45%,rgba(0,0,0,0))}}
    .t{{left:{560 if right else 56}px;right:50px;top:{top + 62}px;font-size:{80 if right else (96 if f45 else 104)}px;line-height:1}}
    .px{{left:50px;bottom:{bot + (330 if f45 else 300)}px;font-size:{300 if f45 else 320}px;line-height:.85;color:{ORANGE}}}
    .pi{{left:{480 if f45 else 520}px;bottom:{bot + (362 if f45 else 332)}px;font-weight:700;font-size:40px;line-height:1.2}}
    .pi b{{display:block;font-family:'Anton';font-weight:400;font-size:64px;color:#fff}}
    .box{{position:absolute;left:56px;right:56px;bottom:{bot}px}}
    .bar{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:16px}}
    .bar .an{{font-size:84px;line-height:1}}
    .bar .s{{font-weight:700;font-size:32px;line-height:1.2;text-align:right}}
    .mini{{font-weight:700;font-size:32px;margin-bottom:16px;letter-spacing:.02em}}
    """
    body = f"""<div class='shade'></div><div class='shade2'></div>
    <div class='abs' style='left:{560 if right else 56}px;top:{top}px'><span class='tag' style='font-size:{30 if right else 38}px'>{seg}</span></div>
    <div class='abs an t sh'>{hook}</div>
    <div class='abs an px sh'>{price}</div>
    <div class='abs pi sh'><b>{lab}</b>{until}<br>POR PERSONA · TODO EL CURSO</div>
    <div class='box'><div class='bar'><div class='an'>21·22·23 OCT</div><div class='s'>2 A 5 PM · AUDITORIO FENATRAPE<br>CERTIFICADO INCLUIDO</div></div>
    <div class='mini'>1-5 OCT $65 · 5-15 OCT $75 · 15-21 OCT $120</div><div class='cta'>Reserva tu cupo · Cupos limitados</div></div>"""
    return page(fmt, img, "center top", css, body)


# ---- T5: calendario de 3 dias ----
def t5(fmt, img, seg, hook, light=True):
    f45, top, bot = geo(fmt)
    css = f"""
    .wash{{position:absolute;left:0;right:0;top:0;height:{'58%' if f45 else '52%'};background:linear-gradient(180deg,rgba(255,255,255,.88) 55%,rgba(255,255,255,0))}}
    .t{{left:56px;right:56px;top:{top + 62}px;font-size:{104 if f45 else 112}px;line-height:.98;color:{INK}}}
    .cal{{position:absolute;left:56px;right:56px;top:{top + (300 if f45 else 380)}px;display:flex;gap:14px}}
    .day{{flex:1;background:{INK};color:#fff;text-align:center;padding:12px 0 10px}}
    .day .an{{font-size:130px;line-height:1}}
    .day small{{display:block;font-size:34px;font-weight:700;letter-spacing:.1em}}
    .day.o{{background:{BLUE}}}
    .info{{position:absolute;left:56px;right:56px;top:{top + (560 if f45 else 640)}px;color:{INK};font-weight:700;font-size:36px;line-height:1.2}}
    .box{{position:absolute;left:56px;right:56px;bottom:{bot}px}}
    """
    body = f"""<div class='wash'></div>
    <div class='abs' style='left:56px;top:{top}px'><span class='tag'>{seg}</span></div>
    <div class='abs an t'>{hook}</div>
    <div class='cal'><div class='day'><div class='an'>21</div><small>OCT · 2 A 5 PM</small></div><div class='day o'><div class='an'>22</div><small>OCT · 2 A 5 PM</small></div><div class='day'><div class='an'>23</div><small>OCT · 2 A 5 PM</small></div></div>
    <div class='info'>AUDITORIO FENATRAPE · CERTIFICADO INCLUIDO</div>
    <div class='box'>{chips()}<div class='cta' style='margin-top:16px'>Reserva tu cupo · Cupos limitados</div></div>"""
    return page(fmt, img, "center top", css, body)


ADS = {
    "E2": (t6, "PARA EMPRENDEDORES", "Aprende IA en 3 días y úsala en tu negocio", {}),
    "E8": (t4, "NEGOCIOS SIN PÁGINA WEB", "¿Tu negocio aún no tiene web? Hazla con IA", {}),
    "F3": (t1, "PARA EMPRESARIOS", "La IA trabajando en su empresa", {}),
    "F4": (t3, "ATENCIÓN AL CLIENTE", "Agentes de IA que atienden a tus clientes", {"side": "left"}),
    "F5": (t6, "GERENTES Y DIRECTORES", "Dominen la IA hoy", {}),
    "G1": (t5, "INMOBILIARIAS", "IA para vender y atender", {}),
    "G2": (t4, "DUEÑOS DE NEGOCIO", "De ChatGPT a tu primera página web", {}),
    "G3": (t2, "NEGOCIOS LOCALES", "Tu negocio y la IA, desde el celular", {}),
    "G4": (t3, "MARKETING Y CONTENIDO", "Crea tu contenido y tus anuncios con IA", {"side": "right"}),
    "G6": (t4, "EN MOVIMIENTO", "Emprendes en movimiento. Tu IA también", {"right": True}),
    "G7": (t1, "EMPRENDES ADEMÁS DE TRABAJAR", "Aprende a usar IA en tu negocio", {}),
}


def render(pid, fmt):
    fn, seg, hook, kw = ADS[pid]
    p = os.path.join(HERE, "fotos_set3", f"{pid}_45.png")  # solo las fotos elegidas por el usuario
    if not os.path.exists(p):
        return None
    img = "file:///" + p.replace("\\", "/")
    hp = os.path.join(HERE, f"_s3_{pid}_{fmt}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(fn(fmt, img, seg, hook, **kw))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{pid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=12000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a in ADS] or list(ADS)
    fm = [a for a in sys.argv[1:] if a in ("4x5", "9x16")] or ["4x5", "9x16"]
    for pid in ids:
        for fmt in fm:
            r = render(pid, fmt)
            if r:
                print(r)
