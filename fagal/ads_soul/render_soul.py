# Anuncios FAGAL con Soul Galarraga: la escena sale COMPLETA de una generacion de Soul (fotos/s1..s6.png),
# el texto va en HTML. Estilos distintos por pieza, perfil de empresa nombrado en cada creativo.
# Uso: python render_soul.py [s1..s6] [4x5|9x16]
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
.sp{flex:1}
.lk img{height:76px;width:auto;display:block}
.ph{position:absolute;display:block;object-fit:cover}
"""


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@@%s@@" % k, str(v))
    return s


def logo(tone):
    return f"<div class='lk'><img src='{LOGO % tone}'></div>"


def doc(fmt, fonts, css, body, grain=".05"):
    f = fmt == "4x5"
    H, pt, pb = (1350, 96, 96) if f else (1920, 250, 340)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>"
            f"{T(COMMON, H=H, pt=pt, pb=pb, grain=grain)}{css}</style></head><body>{body}{GRAIN}</body></html>")


# ---------- s1 Portada de revista: dueños y gerentes ----------
def s1(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#d9d7d2;font-family:'Jost',sans-serif;color:#fff}
    .ph{inset:0;width:100%;height:100%;object-position:center 22%}
    .scrim{position:absolute;left:0;right:0;bottom:0;height:@@sh@@px;background:linear-gradient(transparent,rgba(8,10,14,.86) 38%,rgba(8,10,14,.96))}
    .top{display:flex;justify-content:space-between;align-items:flex-start}
    .who{display:inline-block;margin-top:20px;background:#0c0f14;color:#fff;font-weight:600;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px}
    h1{font-family:'Bodoni Moda',serif;font-weight:800;font-size:@@h1@@px;line-height:1.02;letter-spacing:-.01em}
    h1 em{font-style:italic;font-weight:700;color:#e8d29a}
    .free{display:flex;align-items:center;gap:28px;border-top:1.5px solid #ffffff66;padding-top:22px;margin-top:22px}
    .g{font-family:'Bodoni Moda',serif;font-weight:800;font-size:104px;line-height:.8;color:#e8d29a}.fs{font-weight:500;font-size:30px;line-height:1.28}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:24px}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#d5d3cc}
    .cta{background:#fff;color:#0c0f14;font-weight:700;font-size:33px;letter-spacing:.04em;padding:22px 34px;text-transform:uppercase;white-space:nowrap}
    """, sh=620 if f else 900, h1=70 if f else 92)
    body = f"""<img class='ph' src='fotos/s1.png'><div class='scrim'></div><div class='in'>
    <div class='top'>{logo('negro')}</div><div><span class='who'>Para dueños y gerentes de empresas</span></div><div class='sp'></div>
    <h1>¿Quién revisa lo que firma <em>su empresa?</em></h1>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Bodoni+Moda:ital,wght@0,800;1,700&family=Jost:wght@500;600;700", css, body)


# ---------- s2 Tarjeta de cita: inmobiliarias ----------
def s2(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0f3d3a;font-family:'Newsreader',serif;color:#f1ece0}
    .ph{left:0;top:0;width:1080px;height:@@ph@@px;object-position:center 18%}
    .tag{position:absolute;left:84px;top:@@tt@@px;background:#0f3d3a;color:#f1ece0;font-family:'Jost',sans-serif;font-weight:600;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px}
    .pn{position:absolute;left:0;right:0;top:@@ph@@px;bottom:0;padding:34px 84px @@pb@@px;display:flex;flex-direction:column}
    .qm{font-size:120px;line-height:.5;color:#e9a77a;height:50px;margin-top:30px}
    .q{font-weight:600;font-size:@@qs@@px;line-height:1.08;margin-top:6px}
    .at{font-family:'Jost',sans-serif;font-weight:500;font-size:28px;color:#b9d2cb;margin-top:12px}
    .sp{flex:1}
    .free{display:flex;align-items:center;gap:26px;border-top:1.5px solid #f1ece055;padding-top:20px}
    .g{font-weight:700;font-size:98px;line-height:.8;color:#e9a77a}.fs{font-family:'Jost',sans-serif;font-weight:500;font-size:30px;line-height:1.28}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:24px;font-family:'Jost',sans-serif}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#b9d2cb}
    .cta{background:#e9a77a;color:#102a28;font-weight:700;font-size:33px;letter-spacing:.04em;padding:22px 32px;text-transform:uppercase;white-space:nowrap}
    .lg{position:absolute;left:84px;top:@@lt@@px}
    """, ph=640 if f else 940, tt=96 if f else 250, pb=96 if f else 340, qs=56 if f else 68, lt=96 if f else 250)
    body = f"""<img class='ph' src='fotos/s2.png'><div class='tag'>Para inmobiliarias</div>
    <div class='pn'><div>{logo('blanco')}</div><div class='qm'>“</div><div class='q'>Una cláusula vaga puede costarle la venta.</div>
    <div class='at'>Dr. Fabián Galarraga · Socio fundador, Fagal Abogados</div><div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico de los contratos que más usa su inmobiliaria. 20 min.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Newsreader:wght@600;700&family=Jost:wght@500;600;700", css, body, grain=".03")


# ---------- s3 Suizo con bloque de foto: corredores y aseguradoras ----------
def s3(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#e9e8e3;color:#101010;font-family:'Schibsted Grotesk',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:5px solid #101010}
    .who{display:inline-block;margin-top:22px;background:#101010;color:#fff;font-weight:800;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px}
    .h1{font-weight:900;font-size:@@h1@@px;line-height:.9;letter-spacing:-.035em;margin-top:24px}
    .h2{font-weight:900;font-size:@@h2@@px;line-height:.86;letter-spacing:-.04em;color:#e5321f;margin-top:4px}
    .box{position:relative;margin-top:24px;height:@@bh@@px;overflow:hidden}
    .box .ph{inset:0;width:100%;height:100%;object-position:70% @@pos@@}
    .neg{position:absolute;left:0;right:0;bottom:0;background:#e5321f;color:#fff;display:flex;justify-content:space-between;padding:14px 22px;font-weight:800;font-size:38px;letter-spacing:.08em;text-transform:uppercase}
    .sp{flex:1}
    .free{display:flex;align-items:center;gap:28px;border-top:5px solid #101010;padding-top:22px;margin-top:22px}
    .g{font-weight:900;font-size:122px;line-height:.8;letter-spacing:-.04em;color:#e5321f}.fs{font-weight:700;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:24px}
    .prf{font-weight:600;font-size:30px;line-height:1.3;color:#4a4a45}
    .cta{background:#101010;color:#fff;font-weight:800;font-size:33px;letter-spacing:.03em;padding:24px 34px;text-transform:uppercase;white-space:nowrap}
    """, h1=88 if f else 92, h2=176 if f else 190, bh=410 if f else 700, pos="30%" if f else "34%")
    body = f"""<div class='in'><div class='top'>{logo('negro')}</div><div><span class='who'>Corredores y aseguradoras</span></div>
    <div class='h1'>Siniestro negado.</div><div class='h2'>¿Y ahora?</div>
    <div class='box'><img class='ph' src='fotos/s3.png'><div class='neg'><span>Reclamo</span><span>Estado: negado</span></div></div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Revisión legal de su reclamo. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar revisión →</div></div></div>"""
    return doc(fmt, "family=Schibsted+Grotesk:wght@600;700;800;900", css, body, grain=".04")


# ---------- s4 Cartel duotono: transporte ----------
def s4(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0a1f44;font-family:'Barlow',sans-serif;color:#fff}
    .duo{position:absolute;left:0;top:@@off@@px;width:1080px;height:@@dh@@px;background:#ff6a1a;overflow:hidden}
    .duo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;filter:grayscale(1) contrast(1.15) brightness(1.05);mix-blend-mode:multiply}
    .duo:after{content:"";position:absolute;inset:0;background:#0a1f44;mix-blend-mode:lighten}
    .fade{position:absolute;left:0;right:0;top:@@off@@px;height:260px;background:linear-gradient(#0a1f44,rgba(10,31,68,0))}
    .scrim{position:absolute;left:0;right:0;bottom:0;height:@@sh@@px;background:linear-gradient(rgba(10,31,68,0),rgba(10,31,68,.95) 45%)}
    .top{display:flex;justify-content:space-between;align-items:flex-start}
    .who{display:inline-block;margin-top:16px;border:3px solid #ff6a1a;color:#ff9a5c;font-family:'Anton',sans-serif;font-size:32px;letter-spacing:.12em;text-transform:uppercase;padding:6px 18px}
    h1{font-family:'Anton',sans-serif;font-weight:400;font-size:@@h1@@px;line-height:.98;text-transform:uppercase;margin-top:18px}h1 span{color:#ff8a3d}
    .free{display:flex;align-items:center;gap:26px;border-top:3px solid #ffffff55;padding-top:20px}
    .g{font-family:'Anton',sans-serif;font-size:118px;line-height:.78;color:#ff8a3d}.fs{font-weight:600;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:24px}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#b7c6e2}
    .cta{background:#ff6a1a;color:#0a1f44;font-family:'Anton',sans-serif;font-size:38px;letter-spacing:.05em;padding:18px 34px;text-transform:uppercase;white-space:nowrap}
    """, off=300 if f else 470, dh=1050 if f else 1450, sh=430 if f else 560, h1=110 if f else 124)
    body = f"""<div class='duo'><img src='fotos/s4.png'></div><div class='fade'></div><div class='scrim'></div><div class='in'>
    <div class='top'>{logo('blanco')}</div><div><span class='who'>Para empresas de transporte</span></div>
    <h1>Un accidente puede parar <span>su flota</span></h1><div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal para su flota. 20 min, en su empresa o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Anton&family=Barlow:wght@500;600", css, body, grain=".05")


# ---------- s5 Cartel de cine negro: cartera por cobrar ----------
def s5(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#050505;font-family:'Jost',sans-serif;color:#f2eee4}
    .ph{left:0;top:@@off@@px;width:1080px;height:@@ph@@px;object-position:center top;-webkit-mask-image:linear-gradient(transparent,#000 22%);mask-image:linear-gradient(transparent,#000 22%)}
    .scrim{position:absolute;left:0;right:0;bottom:0;height:@@sh@@px;background:linear-gradient(rgba(5,5,5,0),rgba(5,5,5,.94) 50%)}
    .top{display:flex;justify-content:space-between;align-items:flex-start}
    .who{display:inline-block;margin-top:18px;border:1.5px solid #c9c4b6;color:#f2eee4;font-weight:500;font-size:28px;letter-spacing:.3em;text-transform:uppercase;padding:10px 20px}
    h1{font-family:'DM Serif Display',serif;font-weight:400;font-size:@@h1@@px;line-height:1;text-transform:uppercase;letter-spacing:.04em;margin-top:26px;text-align:center}
    .sub{text-align:center;font-weight:500;font-size:34px;letter-spacing:.06em;color:#d9d4c6;margin-top:14px}
    .free{display:flex;align-items:center;gap:26px;border-top:1.5px solid #f2eee466;padding-top:20px}
    .g{font-family:'DM Serif Display',serif;font-size:104px;line-height:.8;letter-spacing:.03em;color:#e8c27a}.fs{font-weight:500;font-size:30px;line-height:1.28}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:24px}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#a9a597}
    .cta{background:#f2eee4;color:#050505;font-weight:600;font-size:32px;letter-spacing:.14em;padding:22px 32px;text-transform:uppercase;white-space:nowrap}
    """, off=250 if f else 330, ph=1440 if f else 1600, sh=400 if f else 560, h1=84 if f else 96)
    body = f"""<img class='ph' src='fotos/s5.png'><div class='scrim'></div><div class='in'>
    <div class='top'>{logo('blanco')}</div><div><span class='who'>Empresas con cartera por cobrar</span></div>
    <h1>Capital<br>detenido</h1><div class='sub'>Cada mes sin accionar, cobrar se hace más difícil.</div><div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Revisión de su cartera vencida. Pagarés, letras y facturas tienen camino legal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Revisar mi cartera</div></div></div>"""
    return doc(fmt, "family=DM+Serif+Display&family=Jost:wght@500;600", css, body, grain=".07")


# ---------- s6 Anuncio retail con banda diagonal: concesionarias ----------
def s6(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#e7e9ec;font-family:'Rubik',sans-serif;color:#0d0d0d}
    .ph{inset:0;width:100%;height:100%;object-position:center 15%}
    .band{position:absolute;left:-60px;right:-60px;bottom:@@bb@@px;height:@@bh@@px;background:#d71f2a;transform:skewY(-5deg);box-shadow:0 -14px 40px #0004}
    .top{display:flex;justify-content:space-between;align-items:flex-start}
    .who{display:inline-block;margin-top:18px;background:#0d0d0d;color:#fff;font-weight:800;font-size:28px;letter-spacing:.12em;text-transform:uppercase;padding:12px 22px;font-style:italic}
    h1{font-weight:900;font-style:italic;font-size:@@h1@@px;line-height:.96;letter-spacing:-.02em;margin-top:22px;max-width:560px;text-shadow:0 2px 0 #fff8}
    .sub{font-weight:600;font-size:32px;line-height:1.25;margin-top:18px;max-width:560px;background:#ffffffd9;display:inline-block;padding:6px 10px}
    .free{display:flex;align-items:center;gap:26px;color:#fff;position:relative}
    .g{font-weight:900;font-style:italic;font-size:112px;line-height:.8;color:#fff;letter-spacing:-.02em}.fs{font-weight:600;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:24px;position:relative}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#ffe3e5}
    .cta{background:#0d0d0d;color:#fff;font-weight:800;font-style:italic;font-size:33px;padding:22px 32px;text-transform:uppercase;white-space:nowrap}
    """, bb=-10 if f else -10, bh=380 if f else 560, h1=82 if f else 88)
    body = f"""<img class='ph' src='fotos/s6.png'><div class='band'></div><div class='in'>
    <div class='top'>{logo('negro')}</div><div><span class='who'>Para concesionarias</span></div>
    <h1>¿Cliente que dejó de pagar la unidad?</h1><div><span class='sub'>Reserva de dominio y cobro, antes de que sea pérdida.</span></div><div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal para concesionarias. 20 min, en su local o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Rubik:ital,wght@1,800;1,900&family=Rubik:wght@500;600", css, body, grain=".03")


ADS = {"s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5, "s6": s6}


def render(vid, fmt):
    hp = os.path.join(HERE, f"_{vid}_{fmt}.html")
    open(hp, "w", encoding="utf-8").write(ADS[vid](fmt))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{vid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=15000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a in ADS] or list(ADS)
    fm = [a for a in sys.argv[1:] if a in ("4x5", "9x16")] or ["4x5", "9x16"]
    for v in ids:
        for fmt in fm:
            print(render(v, fmt))
