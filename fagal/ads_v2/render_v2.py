# Anuncios FAGAL v2: 8 lenguajes graficos distintos, poco texto, cumpliendo guias de Meta:
#  - 4:5 a 1440x1800 y 9:16 a 1440x2560 (se maqueta a 1080 y se exporta con escala 1.3333)
#  - 9:16: 14% libre arriba (270 px), 35% abajo (672 px) y 6% a los lados (65 px)
#  - poco texto en la imagen, sin botones dibujados ni interfaces imitadas (funcionalidad inexistente)
# Segmentacion desde el creativo: cada pieza nombra al perfil. Solo logo FAGAL (plano blanco o negro).
# Uso: python render_v2.py [p1..p8] [4x5|9x16]
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUT = os.path.join(HERE, "salida")
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"

GRAIN = ("<svg class='grain' xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%' height='100%' filter='url(#n)'/></svg>")

COMMON = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:@@H@@px;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased}
.in{position:absolute;inset:0;padding:@@pt@@px 84px @@pb@@px;display:flex;flex-direction:column}
.grain{position:absolute;inset:0;mix-blend-mode:overlay;opacity:@@grain@@;pointer-events:none}
.sp{flex:1}.abs{position:absolute}
.lk img{height:70px;width:auto;display:block}
.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
"""


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@@%s@@" % k, str(v))
    return s


def logo(tone):
    return f"<div class='lk'><img src='{LOGO % tone}'></div>"


def doc(fmt, fonts, css, body, grain=".04"):
    f = fmt == "4x5"
    H, pt, pb = (1350, 96, 96) if f else (1920, 270, 672)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>{T(COMMON, H=H, pt=pt, pb=pb, grain=grain)}{css}</style></head>"
            f"<body>{body}{GRAIN}</body></html>")


# ---------- p1 Foto Soul a color, pie de revista: concesionarias ----------
def p1(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#dfe2e6;font-family:'Sora',sans-serif}
    .ph{object-position:center 12%}
    .sc{position:absolute;left:0;right:0;bottom:@@sb@@px;height:@@sh@@px;background:@@bg@@}
    .tg{display:inline-block;margin-top:18px;background:#0e1116;color:#fff;font-weight:700;font-size:26px;letter-spacing:.12em;text-transform:uppercase;padding:11px 18px}
    h1{font-weight:800;font-size:@@h1@@px;line-height:1;letter-spacing:-.025em;margin-top:22px;max-width:470px;color:#0e1116}
    .gr{color:#fff;font-weight:600;font-size:34px;line-height:1.3}.gr b{font-weight:800;letter-spacing:.14em;color:#fff;border-bottom:3px solid #fff;padding-bottom:2px;margin-right:10px}
    """, sb=36 if f else 480, sh=340 if f else 460, bg=('linear-gradient(rgba(10,12,16,0),rgba(10,12,16,.82))' if f else 'linear-gradient(rgba(10,12,16,0),rgba(10,12,16,.78) 55%,rgba(10,12,16,0))'), h1=68 if f else 76)
    body = f"""<img class='ph' src='fotos/s6.png'><div class='sc'></div><div class='in'>{logo('negro')}<div><span class='tg'>Para concesionarias</span></div>
    <h1>¿Su cliente dejó de pagar la unidad?</h1><div class='sp'></div>
    <div class='gr'><b>GRATIS</b>Diagnóstico legal, 20 min</div></div>"""
    return doc(fmt, "family=Sora:wght@600;700;800", css, body)


# ---------- p2 Bodegon fotografico, serif de contraste: dueños y gerentes ----------
def p2(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0b0807;color:#f3ead9;font-family:'Manrope',sans-serif}
    .ph{object-position:@@op@@ center}
    .tg{display:inline-block;margin-top:18px;color:#d9b66a;font-weight:700;font-size:26px;letter-spacing:.2em;text-transform:uppercase;border-bottom:2px solid #d9b66a;padding-bottom:6px}
    h1{font-family:'Gloock',serif;font-weight:400;font-size:@@h1@@px;line-height:1.03;margin-top:22px;max-width:900px}
    .gr{margin-top:22px;font-weight:600;font-size:32px;color:#e9dfca}.gr b{font-weight:800;letter-spacing:.16em;color:#d9b66a;margin-right:10px}
    """, op="72%" if not f else "50%", h1=82 if f else 88)
    body = f"""<img class='ph' src='fotos/bodegon.png'><div class='in'>{logo('blanco')}<div><span class='tg'>Para dueños y gerentes de empresas</span></div>
    <h1>¿Quién revisa lo que firma su empresa?</h1><div class='gr'><b>GRATIS</b>Diagnóstico legal, 20 min</div></div>"""
    return doc(fmt, "family=Gloock&family=Manrope:wght@600;700;800", css, body, grain=".05")


# ---------- p3 Foto aerea, capitales espaciadas: transporte ----------
def p3(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0a1630;color:#fff;font-family:'Syncopate',sans-serif}
    .ph{object-position:center 30%}
    .tg{display:inline-block;margin-top:20px;font-weight:700;font-size:20px;letter-spacing:.3em;text-transform:uppercase;color:#9fc0ff}
    h1{font-weight:700;font-size:@@h1@@px;line-height:1.12;letter-spacing:.04em;text-transform:uppercase;margin-top:22px;max-width:940px}
    .gr{font-family:'Manrope',sans-serif;font-weight:600;font-size:32px;color:#dbe6ff}.gr b{font-weight:800;letter-spacing:.16em;color:#ffb066;margin-right:10px}
    .sc{position:absolute;left:0;right:0;top:0;height:@@th@@px;background:linear-gradient(rgba(6,12,30,.78),rgba(6,12,30,0))}
    .sc2{position:absolute;left:0;right:0;bottom:@@s2b@@px;height:420px;background:linear-gradient(rgba(6,12,30,0),rgba(6,12,30,.82) 55%,rgba(6,12,30,0))}
    """, h1=50 if f else 54, th=620 if f else 800, s2b=0 if f else 530)
    body = f"""<img class='ph' src='fotos/aerea.png'><div class='sc'></div><div class='sc2'></div><div class='in'>{logo('blanco')}<div><span class='tg'>Para empresas de transporte</span></div>
    <h1>Un accidente puede parar su flota</h1><div class='sp'></div><div class='gr'><b>GRATIS</b>Diagnóstico legal, 20 min</div></div>"""
    return doc(fmt, "family=Syncopate:wght@700&family=Manrope:wght@600;800", css, body, grain=".05")


# ---------- p4 Ilustracion editorial en verde: inmobiliarias ----------
def p4(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#c9d7c2;font-family:'Manrope',sans-serif}
    .ph{object-position:center @@op@@}
    .tg{display:inline-block;margin-top:18px;background:#173d2e;color:#e9f0e4;font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;padding:11px 18px}
    h1{font-family:'Young Serif',serif;font-weight:400;font-size:@@h1@@px;line-height:1.04;color:#14301f;margin-top:22px;max-width:880px}
    .gr{color:@@gc@@;font-weight:700;font-size:32px}.gr b{font-weight:800;letter-spacing:.16em;margin-right:10px;border-bottom:3px solid @@gc@@}
    """, op="60%" if f else "75%", gc=("#eaf0e4" if f else "#14301f"), h1=66 if f else 84)
    body = f"""<img class='ph' src='fotos/ilustracion.png'><div class='in'>{logo('negro')}<div><span class='tg'>Para inmobiliarias</span></div>
    <h1>¿Resiste su promesa de compraventa?</h1><div class='sp'></div><div class='gr'><b>GRATIS</b>Diagnóstico de contratos, 20 min</div></div>"""
    return doc(fmt, "family=Young+Serif&family=Manrope:wght@600;700;800", css, body, grain=".03")


# ---------- p5 Tipografico suizo monocromo: corredores y aseguradoras ----------
def p5(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#f6f6f3;color:#0a0a0a;font-family:'Bricolage Grotesque',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:4px solid #0a0a0a;padding-bottom:18px}
    .tg{font-weight:700;font-size:26px;letter-spacing:.1em;text-transform:uppercase;text-align:right;line-height:1.3}
    h1{font-weight:800;font-size:@@h1@@px;line-height:.84;letter-spacing:-.05em;margin-top:@@hm@@px}
    h2{font-weight:300;font-size:@@h2@@px;line-height:.9;letter-spacing:-.04em;margin-top:10px}
    .gr{display:flex;justify-content:space-between;align-items:baseline;border-top:4px solid #0a0a0a;padding-top:16px;font-weight:600;font-size:32px}.gr b{font-weight:800;letter-spacing:.14em}
    """, h1=262 if f else 258, h2=190 if f else 186, hm=40 if f else 50)
    body = f"""<div class='in'><div class='top'>{logo('negro')}<div class='tg'>Corredores y<br>aseguradoras</div></div>
    <h1>Siniestro negado.</h1><h2>¿Y ahora?</h2><div class='sp'></div>
    <div class='gr'><span><b>GRATIS</b> · Revisión legal de su reclamo</span><span>20 min</span></div></div>"""
    return doc(fmt, "family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,600;12..96,800", css, body, grain=".03")


# ---------- p6 Collage de semitono sobre papel: empresas medianas ----------
def p6(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#ece5d6;font-family:'Space Mono',monospace;color:#10132b}
    .circ{position:absolute;right:-120px;top:@@ct@@px;width:760px;height:760px;border-radius:50%;background:#e8452c}
    .ht{position:absolute;right:-60px;top:@@pt2@@px;width:@@hw@@px;height:@@hh@@px;object-fit:contain;mix-blend-mode:multiply}
    .tg{display:inline-block;margin-top:18px;background:#10132b;color:#ece5d6;font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;padding:10px 16px}
    .big{align-self:flex-start;font-family:'Abril Fatface',serif;font-size:@@bs@@px;line-height:.86;color:#10132b;margin-top:@@bm@@px;letter-spacing:-.01em}
    .strip{display:inline-block;align-self:flex-start;background:#10132b;color:#ece5d6;font-family:'Abril Fatface',serif;font-size:56px;padding:6px 20px;transform:rotate(-2deg);margin-top:10px}
    .sub{font-size:28px;line-height:1.35;margin-top:18px;max-width:520px;font-weight:700}
    .badge{position:absolute;left:@@bl@@px;bottom:@@bb@@px;width:210px;height:210px;border-radius:50%;background:#10132b;color:#ece5d6;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-8deg);font-weight:700;font-size:22px;letter-spacing:.1em;line-height:1.3}
    .badge b{font-family:'Abril Fatface',serif;font-size:50px;letter-spacing:.02em;line-height:1}
    """, ct=380 if f else 560, pt2=170 if f else 360, hw=760 if f else 820, hh=1010 if f else 1093, bs=330 if f else 340, bm=22 if f else 30, bl=84, bb=96 if f else 700)
    body = f"""<div class='circ'></div><img class='ht' src='fotos/s2_halftone.png'><div class='in'>{logo('negro')}<div><span class='tg'>Para empresas medianas</span></div>
    <div class='big'>20</div><div class='strip'>MINUTOS</div><div class='sub'>para conocer los riesgos legales de su empresa</div></div>
    <div class='badge'><b>GRATIS</b>diagnóstico<br>legal</div>"""
    return doc(fmt, "family=Abril+Fatface&family=Space+Mono:wght@400;700", css, body, grain=".07")


# ---------- p7 Infografia clara de datos: cartera por cobrar ----------
def p7(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#edf1f5;color:#0c2340;font-family:'Public Sans',sans-serif}
    .tg{display:inline-block;margin-top:18px;border:2px solid #0c2340;font-weight:700;font-size:25px;letter-spacing:.1em;text-transform:uppercase;padding:9px 16px}
    h1{font-weight:800;font-size:@@h1@@px;line-height:1.02;letter-spacing:-.03em;margin-top:22px}
    h1 span{color:#e26a1b}
    .ch{margin-top:@@cm@@px}
    .cap{font-weight:600;font-size:22px;letter-spacing:.12em;color:#5b7088;text-transform:uppercase;margin-bottom:10px}
    .gr{font-weight:600;font-size:32px}.gr b{font-weight:800;letter-spacing:.14em;color:#e26a1b;margin-right:10px}
    """, h1=78 if f else 88, cm=26 if f else 44)
    ch = 470 if f else 400
    bars = [("0-30", 0.92), ("31-60", 0.64), ("61-90", 0.42), ("+90", 0.30)]
    bw, gap = 190, 50
    svg = f"<svg width='912' height='{ch+60}' viewBox='0 0 912 {ch+60}'>"
    for i, (lab, v) in enumerate(bars):
        x = i * (bw + gap) + 11; h = int(v * ch); y = ch - h
        fill = "#e26a1b" if lab == "+90" else "#0c2340"
        svg += f"<rect x='{x}' y='{y}' width='{bw}' height='{h}' fill='{fill}'/>"
        if lab == "+90":
            svg += f"<path d='M{x} {y+40}l{bw} -40M{x} {y+90}l{bw} -90M{x} {y+140}l{bw} -140' stroke='#edf1f5' stroke-width='3' opacity='.55'/>"
        svg += f"<text x='{x+bw/2}' y='{ch+44}' text-anchor='middle' font-family='Public Sans' font-weight='700' font-size='30' fill='#0c2340'>{lab} días</text>"
    svg += f"<line x1='0' y1='{ch}' x2='912' y2='{ch}' stroke='#0c2340' stroke-width='3'/></svg>"
    body = f"""<div class='in'>{logo('negro')}<div><span class='tg'>Empresas con cartera por cobrar</span></div>
    <h1>Facturas vencidas son <span>capital detenido</span></h1>
    <div class='ch'><div class='cap'>Cartera por antigüedad · ejemplo ilustrativo</div>{svg}</div><div class='sp'></div>
    <div class='gr'><b>GRATIS</b>Revisión de su cartera, 20 min</div></div>"""
    return doc(fmt, "family=Public+Sans:wght@500;600;700;800", css, body, grain=".02")


# ---------- p8 Aviso de periodico (edicto): gerentes y dueños ----------
def p8(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#d9d5c8;color:#111;font-family:'Libre Baskerville',serif}
    .mast{text-align:center;border-top:6px double #111;border-bottom:3px solid #111;padding:14px 0 10px}
    .mast .m1{font-family:'UnifrakturCook',serif;font-weight:700;font-size:@@ms@@px;line-height:1}
    .mast .m2{font-family:'Manrope',sans-serif;font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase;margin-top:8px}
    .tg{text-align:center;font-family:'Manrope',sans-serif;font-weight:800;font-size:26px;letter-spacing:.18em;text-transform:uppercase;margin-top:18px}
    h1{font-family:'Old Standard TT',serif;font-weight:700;font-size:@@h1@@px;line-height:1;text-align:center;text-transform:uppercase;margin-top:@@hm@@px;letter-spacing:-.01em}
    h1 em{font-style:italic;font-weight:400}
    .rule{height:3px;background:#111;margin:26px 0}
    .box{border:4px double #111;padding:22px 26px;text-align:center}
    .box b{display:block;font-family:'Old Standard TT',serif;font-size:@@bs@@px;letter-spacing:.04em}
    .box span{font-family:'Manrope',sans-serif;font-weight:700;font-size:28px;letter-spacing:.06em;text-transform:uppercase}
    .ft{display:flex;justify-content:space-between;align-items:center;margin-top:22px}
    """, ms=100 if f else 100, h1=100 if f else 96, hm=36 if f else 40, bs=88 if f else 84)
    body = f"""<div class='in'><div class='mast'><div class='m1'>Aviso a las empresas</div><div class='m2'>Fagal Abogados · Edición para gerentes</div></div>
    <div class='tg'>Para gerentes y dueños de empresas</div>
    <h1>Si le llega una citación, <em>el plazo ya corre</em></h1><div class='rule'></div>
    <div class='box'><b>GRATIS</b><span>Diagnóstico legal de su empresa · 20 min</span></div><div class='sp'></div>
    <div class='ft'>{logo('negro')}</div></div>"""
    return doc(fmt, "family=UnifrakturCook:wght@700&family=Old+Standard+TT:ital,wght@0,700;1,400&family=Libre+Baskerville&family=Manrope:wght@700;800", css, body, grain=".09")


ADS = {"p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5, "p6": p6, "p7": p7, "p8": p8}


def render(vid, fmt):
    hp = os.path.join(HERE, f"_{vid}_{fmt}.html")
    open(hp, "w", encoding="utf-8").write(ADS[vid](fmt))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{vid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1.3333333",
                    f"--window-size=1080,{H}", "--virtual-time-budget=15000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a in ADS] or list(ADS)
    fm = [a for a in sys.argv[1:] if a in ("4x5", "9x16")] or ["4x5", "9x16"]
    for v in ids:
        for fmt in fm:
            print(render(v, fmt))
