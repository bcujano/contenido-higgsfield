# Tanda v3 FAGAL: solo vectorial y texto, enfocada en PYMES (sin nicho), 8 dolores legales comunes.
# Maestro 9:16. El bloque central de cada pieza se escala y centra en la zona segura de cada formato:
#   9:16 (1440x2560): libre 14% arriba, 35% abajo, 6% lados | 4:5 (1440x1800) | 1:1 (1440x1440)
# Reglas Meta: poco texto, sin botones ni interfaces imitadas, GRATIS grande. Solo logo FAGAL plano.
# Uso: python render_v3.py [v1..v8] [9x16|4x5|1x1]
import math, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUT = os.path.join(HERE, "salida")
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"

# (alto del lienzo, margen superior seguro, margen inferior seguro)
FORMATS = {"9x16": (1920, 270, 672), "4x5": (1350, 96, 96), "1x1": (1080, 84, 84)}

COMMON = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:@@H@@px;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased}
.safe{position:absolute;left:84px;right:84px;top:@@ST@@px;bottom:@@SB@@px;display:flex;align-items:center;justify-content:center}
.fit{width:912px;flex:none;transform-origin:center center}
.hd{display:flex;justify-content:space-between;align-items:center}
.lk img{height:72px;width:auto;display:block}
"""

FIT_JS = """<script>document.fonts.ready.then(function(){var s=document.querySelector('.safe'),f=document.querySelector('.fit');
var k=Math.min(1.12,s.clientHeight/f.offsetHeight,s.clientWidth/f.offsetWidth);f.style.transform='scale('+k+')';});</script>"""


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@@%s@@" % k, str(v))
    return s


def logo(tone):
    return f"<div class='lk'><img src='{LOGO % tone}'></div>"


def doc(fmt, fonts, css, body, bg, grain=0.04):
    H, st, sb = FORMATS[fmt]
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    g = ("<svg style='position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none;opacity:@@G@@' xmlns='http://www.w3.org/2000/svg'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>").replace('@@G@@', str(grain))
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>{T(COMMON, H=H, ST=st, SB=sb)}{css}</style></head>"
            f"<body style='background:{bg}'><div class='safe'><div class='fit'>{body}</div></div>{g}{FIT_JS}</body></html>")


# ---------- v1 Contrato censurado: contratos sin revisar ----------
def v1(fmt):
    css = """
    body{font-family:'Courier Prime',monospace;color:#111}
    .tg{background:#111;color:#fff;font-family:'Courier Prime';font-weight:700;font-size:26px;letter-spacing:.14em;padding:8px 14px}
    h1{font-family:'Special Elite',monospace;font-weight:400;font-size:78px;line-height:1.02;margin-top:26px}
    .paper{margin-top:24px;background:#fff;box-shadow:0 24px 50px -24px #0006;padding:26px 32px;font-size:30px;line-height:1.55}
    .rd{display:inline-block;background:#0a0a0a;height:.92em;vertical-align:-.12em}
    .hl{background:#ffe14d;font-weight:700;padding:0 4px}
    .bar{margin-top:24px;background:#0a0a0a;color:#fff;padding:16px 32px 22px}
    .bar b{display:block;font-family:'Special Elite',monospace;font-weight:400;font-size:250px;line-height:.95;letter-spacing:-.02em}
    .bar span{display:block;font-weight:700;font-size:30px;line-height:1.3;margin-top:2px}
    """
    body = f"""<div class='hd'>{logo('negro')}<div class='tg'>PARA PYMES</div></div>
    <h1>¿Qué dice la letra pequeña?</h1>
    <div class='paper'>ART. 4 Plazo: <span class='rd' style='width:210px'></span> meses.<br>
    ART. 7 Mora: <span class='rd' style='width:360px'></span><br>
    ART. 9 <span class='rd' style='width:520px'></span><br>
    ART. 12 <span class='hl'>Renovación automática.</span><br>
    ART. 15 <span class='rd' style='width:440px'></span></div>
    <div class='bar'><b>GRATIS</b><span>Diagnóstico legal de sus contratos · 20 min</span></div>"""
    return doc(fmt, "family=Special+Elite&family=Courier+Prime:wght@400;700", css, body, "#e9e8e3", 0.05)


# ---------- v2 Anillos de antiguedad: cobranza ----------
def v2(fmt):
    css = """
    body{font-family:'Outfit',sans-serif;color:#f4eee2}
    .tg{border:2px solid #ff7a59;color:#ff9b80;font-weight:700;font-size:26px;letter-spacing:.16em;padding:7px 14px}
    h1{font-weight:800;font-size:84px;line-height:1;letter-spacing:-.02em;margin-top:24px}
    .cap{font-weight:500;font-size:26px;letter-spacing:.1em;color:#8fc4c0;text-align:center;margin-top:6px;text-transform:uppercase}
    .gr{display:block;margin-top:22px}
    .gr b{display:block;font-weight:800;font-size:250px;line-height:.86;color:#ff7a59;letter-spacing:-.02em}
    .gr span{display:block;margin-top:8px;font-weight:600;font-size:36px;line-height:1.2}
    svg{display:block;margin:10px auto 0}
    """
    cx = cy = 210; rings = [(190, 300, "#f4eee2", "0-30"), (148, 235, "#9fd6d2", "31-60"), (106, 165, "#f2b8a6", "61-90"), (64, 95, "#ff7a59", "+90")]
    s = f"<svg width='380' height='380' viewBox='0 0 420 420'>"
    for r, ang, col, lab in rings:
        c = 2 * math.pi * r
        s += f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='#ffffff14' stroke-width='30'/>"
        s += f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{col}' stroke-width='30' stroke-dasharray='{c*ang/360:.1f} {c:.1f}' transform='rotate(-90 {cx} {cy})'/>"
        s += f"<text x='{cx-10}' y='{cy-r+8}' text-anchor='end' font-family='Outfit' font-weight='700' font-size='22' fill='#0c3b40'>{lab}</text>"
    s += "</svg>"
    body = f"""<div class='hd'>{logo('blanco')}<div class='tg'>PARA PYMES</div></div>
    <h1>Cada mes, cobrar cuesta más.</h1>{s}<div class='cap'>Días de vencimiento · ejemplo ilustrativo</div>
    <div class='gr'><b>GRATIS</b><span>Revisión de su cartera · 20 min</span></div>"""
    return doc(fmt, "family=Outfit:wght@500;600;700;800", css, body, "#0c3b40")


# ---------- v3 Isotipos: contratos laborales ----------
def v3(fmt):
    css = """
    body{font-family:'Red Hat Display',sans-serif;color:#14284b}
    .tg{background:#14284b;color:#fff;font-weight:900;font-size:26px;letter-spacing:.14em;padding:8px 14px}
    h1{font-weight:900;font-size:66px;line-height:1.03;letter-spacing:-.02em;margin-top:24px}
    h1 span{color:#f08a24}
    .lg{display:flex;gap:34px;margin-top:6px;font-weight:700;font-size:26px;align-items:center}
    .lg i{display:inline-block;width:22px;height:22px;border-radius:50%;margin-right:10px;vertical-align:-3px}
    .gr{display:block;margin-top:22px}
    .gr b{display:block;font-weight:900;font-size:250px;line-height:.86;color:#f08a24;letter-spacing:-.03em}
    .gr span{display:block;margin-top:8px;font-weight:800;font-size:36px;line-height:1.2}
    svg{display:block;margin-top:18px}
    """
    orange = {2, 7, 8, 13, 16}
    s = "<svg width='912' height='312' viewBox='0 0 912 312'>"
    for n in range(18):
        r, c = divmod(n, 6); x = c * 152 + 76; y = r * 104 + 4
        col = "#f08a24" if n in orange else "#14284b"
        s += (f"<circle cx='{x}' cy='{y+19}' r='17' fill='{col}'/><path d='M{x-30} {y+96}v-26a30 30 0 0 1 30 -30a30 30 0 0 1 30 30v26z' fill='{col}'/>")
    s += "</svg>"
    body = f"""<div class='hd'>{logo('negro')}<div class='tg'>PARA PYMES</div></div>
    <h1>¿Todos sus empleados tienen <span>contrato por escrito?</span></h1>{s}
    <div class='lg'><span><i style='background:#14284b'></i>Con contrato</span><span><i style='background:#f08a24'></i>Sin contrato</span></div>
    <div class='gr'><b>GRATIS</b><span>Diagnóstico laboral · 20 min</span></div>"""
    return doc(fmt, "family=Red+Hat+Display:wght@700;800;900", css, body, "#f7f8fa", 0.02)


# ---------- v4 Reloj ferroviario: citacion y plazos ----------
def v4(fmt):
    css = """
    body{font-family:'Hanken Grotesk',sans-serif;color:#0a0a0a}
    .tg{background:#0a0a0a;color:#f6c915;font-weight:900;font-size:26px;letter-spacing:.14em;padding:8px 14px}
    h1{font-weight:900;font-size:100px;line-height:.92;letter-spacing:-.04em;margin-top:22px}
    svg{display:block;margin:20px auto 0}
    .gr{display:block;margin-top:18px}
    .gr b{display:block;font-weight:900;font-size:280px;line-height:.84;letter-spacing:-.05em;display:block}
    .gr span{display:block;margin-top:8px;font-weight:800;font-size:36px;line-height:1.2}
    """
    cx = cy = 210; s = "<svg width='360' height='360' viewBox='0 0 420 420'>"
    s += f"<circle cx='{cx}' cy='{cy}' r='204' fill='#0a0a0a'/><circle cx='{cx}' cy='{cy}' r='190' fill='#ffffff'/>"
    for i in range(60):
        a = i * 6; thick = i % 5 == 0
        w, l = (10, 34) if thick else (3, 14)
        s += f"<rect x='{cx-w/2}' y='{cy-186}' width='{w}' height='{l}' fill='#0a0a0a' transform='rotate({a} {cx} {cy})'/>"
    s += f"<rect x='{cx-9}' y='{cy-108}' width='18' height='120' rx='3' fill='#0a0a0a' transform='rotate(304 {cx} {cy})'/>"
    s += f"<rect x='{cx-7}' y='{cy-158}' width='14' height='170' rx='3' fill='#0a0a0a' transform='rotate(48 {cx} {cy})'/>"
    s += f"<g transform='rotate(216 {cx} {cy})'><rect x='{cx-3}' y='{cy-170}' width='6' height='222' fill='#e1261c'/><circle cx='{cx}' cy='{cy-130}' r='17' fill='#e1261c'/></g>"
    s += f"<circle cx='{cx}' cy='{cy}' r='9' fill='#e1261c'/></svg>"
    body = f"""<div class='hd'>{logo('negro')}<div class='tg'>PARA PYMES</div></div>
    <h1>El plazo<br>ya corre.</h1>{s}
    <div class='gr'><b>GRATIS</b><span>Diagnóstico ante una citación · 20 min</span></div>"""
    return doc(fmt, "family=Hanken+Grotesk:wght@500;800;900", css, body, "#f6c915", 0.03)


# ---------- v5 Venn en blanco y negro: socios ----------
def v5(fmt):
    css = """
    body{font-family:'Unbounded',sans-serif;color:#fff}
    .tg{border:2px solid #fff;font-weight:600;font-size:22px;letter-spacing:.14em;padding:8px 14px}
    h1{font-weight:800;font-size:60px;line-height:1.08;letter-spacing:-.02em;margin-top:26px}
    svg{display:block;margin:16px 0 0}
    .gr{display:block;margin-top:16px}
    .gr b{display:block;font-weight:800;font-size:200px;line-height:.88;letter-spacing:-.04em}
    .gr span{display:block;margin-top:8px;font-family:'Manrope',sans-serif;font-weight:700;font-size:36px;line-height:1.2}
    """
    s = ("<svg width='912' height='430' viewBox='0 0 912 430'><defs><clipPath id='c1'><circle cx='330' cy='215' r='205'/></clipPath></defs>"
         "<circle cx='330' cy='215' r='205' fill='none' stroke='#fff' stroke-width='4'/><circle cx='582' cy='215' r='205' fill='none' stroke='#fff' stroke-width='4'/>"
         "<circle cx='582' cy='215' r='205' fill='#fff' clip-path='url(#c1)'/>"
         "<text x='215' y='222' text-anchor='middle' font-family='Unbounded' font-weight='600' font-size='30' fill='#fff'>SOCIO A</text>"
         "<text x='697' y='222' text-anchor='middle' font-family='Unbounded' font-weight='600' font-size='30' fill='#fff'>SOCIO B</text>"
         "<text x='456' y='205' text-anchor='middle' font-family='Manrope' font-weight='800' font-size='30' fill='#0a0a0a'>¿Y si se</text>"
         "<text x='456' y='244' text-anchor='middle' font-family='Manrope' font-weight='800' font-size='30' fill='#0a0a0a'>separan?</text></svg>")
    body = f"""<div class='hd'>{logo('blanco')}<div class='tg'>PARA PYMES</div></div>
    <h1>Socios sin pacto por escrito</h1>{s}
    <div class='gr'><b>GRATIS</b><span>Diagnóstico societario · 20 min</span></div>"""
    return doc(fmt, "family=Unbounded:wght@600;800&family=Manrope:wght@700;800", css, body, "#0a0a0a", 0.05)


# ---------- v6 Marca registrada gigante: propiedad intelectual ----------
def v6(fmt):
    css = """
    body{font-family:'Manrope',sans-serif;color:#f1efe6}
    .tg{border:2px solid #d9c27a;color:#d9c27a;font-weight:800;font-size:26px;letter-spacing:.16em;padding:7px 14px}
    .art{position:relative;height:500px;margin-top:10px;overflow:hidden}
    .art svg{position:absolute;left:0;top:0}
    .art h1{position:absolute;left:0;bottom:6px;font-family:'Playfair Display',serif;font-style:italic;font-weight:900;font-size:108px;line-height:.95;letter-spacing:-.02em}
    .sub{font-weight:600;font-size:36px;line-height:1.25;margin-top:16px;color:#cfe3d8}
    .gr{display:block;margin-top:16px}
    .gr b{display:block;font-family:'Playfair Display',serif;font-weight:900;font-size:236px;line-height:.86;color:#d9c27a}
    .gr span{display:block;margin-top:8px;font-weight:700;font-size:36px;line-height:1.2}
    """
    body = f"""<div class='hd'>{logo('blanco')}<div class='tg'>PARA PYMES</div></div>
    <div class='art'><svg width='912' height='500' viewBox='0 0 912 500'><text x='456' y='470' text-anchor='middle' font-family='Playfair Display' font-weight='900' font-size='600' fill='#17684d'>®</text></svg>
    <h1>¿Su marca<br>es suya?</h1></div>
    <div class='sub'>Si no la registra, cualquiera puede hacerlo.</div>
    <div class='gr'><b>GRATIS</b><span>Diagnóstico de marca · 20 min</span></div>"""
    return doc(fmt, "family=Playfair+Display:ital,wght@0,900;1,900&family=Manrope:wght@600;700;800", css, body, "#0d4a38", 0.04)


# ---------- v7 Marcadores de evidencia: fraude y pruebas ----------
def v7(fmt):
    css = """
    body{font-family:'Oswald',sans-serif;color:#f3f1ea}
    .tg{background:#ffb020;color:#16171a;font-weight:700;font-size:26px;letter-spacing:.16em;padding:7px 14px}
    h1{font-weight:700;font-size:80px;line-height:1;text-transform:uppercase;margin-top:22px;letter-spacing:.005em}
    h1 span{color:#ffb020}
    svg{display:block;margin-top:14px}
    .gr{display:block;margin-top:12px}
    .gr b{display:block;font-weight:700;font-size:280px;line-height:.86;color:#ffb020}
    .gr span{font-family:'Roboto Mono',monospace;font-weight:500;font-size:28px;line-height:1.3;margin-top:34px}
    """
    s = "<svg width='912' height='360' viewBox='0 0 912 360'><rect width='912' height='360' fill='#303338'/>"
    for i in range(-6, 19):
        s += f"<line x1='{456 + (i-6)*30}' y1='70' x2='{456 + (i-6)*130}' y2='360' stroke='#ffffff1c' stroke-width='2'/>"
    for k in range(1, 7):
        y = 70 + (k / 6) ** 1.8 * 290
        s += f"<line x1='0' y1='{y:.0f}' x2='912' y2='{y:.0f}' stroke='#ffffff1c' stroke-width='2'/>"
    marks = [(120, 250, 1.0, 1), (290, 190, 0.8, 2), (480, 270, 1.15, 3), (660, 205, 0.85, 4), (800, 285, 1.05, 5)]
    for x, y, sc, n in marks:
        w = 74 * sc; h = 92 * sc
        s += f"<ellipse cx='{x}' cy='{y+4}' rx='{w*0.7:.0f}' ry='{10*sc:.0f}' fill='#00000066'/>"
        s += (f"<polygon points='{x-w/2:.0f},{y} {x+w/2:.0f},{y} {x+w*0.28:.0f},{y-h:.0f} {x-w*0.28:.0f},{y-h:.0f}' fill='#ffb020'/>"
              f"<polygon points='{x-w/2:.0f},{y} {x+w/2:.0f},{y} {x+w*0.5:.0f},{y+8*sc:.0f} {x-w*0.5:.0f},{y+8*sc:.0f}' fill='#c97d00'/>"
              f"<text x='{x}' y='{y-h*0.28:.0f}' text-anchor='middle' font-family='Oswald' font-weight='700' font-size='{44*sc:.0f}' fill='#16171a'>{n}</text>")
    s += "</svg>"
    body = f"""<div class='hd'>{logo('blanco')}<div class='tg'>PARA PYMES</div></div>
    <h1>Antes de denunciar, <span>asegure la prueba</span></h1>{s}
    <div class='gr'><b>GRATIS</b><span>Orientación legal · 20 min</span></div>"""
    return doc(fmt, "family=Oswald:wght@500;700&family=Roboto+Mono:wght@500", css, body, "#1c1e22", 0.05)


# ---------- v8 Ticket de caja: el costo de no tener abogado ----------
def v8(fmt):
    css = """
    body{font-family:'Lexend',sans-serif;color:#0b1d3a}
    .tg{border:2px solid #0b1d3a;font-weight:700;font-size:24px;letter-spacing:.14em;padding:7px 14px}
    h1{font-weight:800;font-size:68px;line-height:1.04;letter-spacing:-.03em;margin-top:22px}
    .rc{position:relative;width:660px;height:@@RH@@px;margin:22px auto 0;background:#fffdf6;font-family:'Inconsolata',monospace;color:#111;padding:36px 38px;filter:drop-shadow(0 22px 24px #0b1d3a44)}
    .rt{text-align:center;font-weight:700;font-size:32px;letter-spacing:.06em}
    .dl{border-top:3px dashed #111;margin:16px 0}
    .r{display:flex;justify-content:space-between;font-size:32px;line-height:1.5}
    .r.t{font-weight:700}
    .g{text-align:center;font-family:'Lexend',sans-serif;font-weight:800;font-size:158px;line-height:.9;letter-spacing:-.04em}
    .gs{text-align:center;font-weight:700;font-size:30px;margin-top:6px}
    """
    RH = 640
    pts = []
    for x in range(0, 661, 20):
        pts.append(f"{x}px {0 if (x//20)%2 == 0 else 12}px")
    pts.append(f"660px {RH-12}px")
    for x in range(660, -1, -20):
        pts.append(f"{x}px {RH if (x//20)%2 == 0 else RH-12}px")
    clip = "polygon(" + ",".join(pts) + ")"
    css = T(css, RH=RH) + f".rc{{clip-path:{clip};filter:none}}"
    body = f"""<div class='hd'>{logo('negro')}<div class='tg'>PARA PYMES</div></div>
    <h1>¿Cuánto cuesta no tener abogado?</h1>
    <div class='rc'><div class='rt'>TICKET DE RIESGOS</div><div class='dl'></div>
    <div class='r'><span>Contrato sin revisar</span><span>$ ?</span></div>
    <div class='r'><span>Cartera incobrable</span><span>$ ?</span></div>
    <div class='r'><span>Demanda laboral</span><span>$ ?</span></div>
    <div class='r t'><span>TOTAL</span><span>$ ???</span></div><div class='dl'></div>
    <div class='g'>GRATIS</div><div class='gs'>Diagnóstico legal · 20 min</div></div>"""
    return doc(fmt, "family=Lexend:wght@700;800&family=Inconsolata:wght@500;700", css, body, "#cfe0ff", 0.03)


ADS = {"v1": v1, "v2": v2, "v3": v3, "v4": v4, "v5": v5, "v6": v6, "v7": v7, "v8": v8}


def render(vid, fmt, scale="1.3333333"):
    hp = os.path.join(HERE, f"_{vid}_{fmt}.html")
    open(hp, "w", encoding="utf-8").write(ADS[vid](fmt))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{vid}_{fmt}.png")
    H = FORMATS[fmt][0]
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={scale}",
                    f"--window-size=1080,{H}", "--virtual-time-budget=15000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a in ADS] or list(ADS)
    fm = [a for a in sys.argv[1:] if a in FORMATS] or list(FORMATS)
    for v in ids:
        for fmt in fm:
            print(render(v, fmt))
