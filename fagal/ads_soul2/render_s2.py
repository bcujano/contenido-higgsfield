# Serie S rehecha (ads_soul2): 6 lenguajes de la serie S, ahora con fotos con barba (tanda4) y reglas de Meta.
# Solo 4:5 -> 1440x1800. Poco texto, GRATIS gigante, "Para pymes" en cada pieza, sin botones ni interfaces imitadas.
import os, subprocess, sys
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"
FOT = os.path.join(HERE, "fotos")
OUT = os.path.join(HERE, "salida")
COMMON = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}body{position:relative;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.lk img{height:70px;width:auto;display:block}
.ph{position:absolute;display:block;object-fit:cover}"""


def prep():
    # s07: duotono azul noche -> naranja (neutraliza el pañuelo amarillo y el color del saco)
    im = ImageOps.autocontrast(Image.open(os.path.join(FOT, "s07.png")).convert("L"), cutoff=1)
    ImageOps.colorize(im, black=(10, 24, 56), white=(255, 138, 61), mid=(120, 70, 90)).save(os.path.join(FOT, "s07_duo.png"))
    # s03: blanco y negro de alto contraste (neutraliza la corbata café)
    g = ImageOps.autocontrast(Image.open(os.path.join(FOT, "s03.png")).convert("L"), cutoff=1)
    g.point(lambda v: min(255, int(((v/255.0 - .5)*1.18 + .5)*255))).convert("RGB").save(os.path.join(FOT, "s03_bn.png"))


def logo(t):
    return f"<div class='lk'><img src='{LOGO % t}'></div>"


def doc(fonts, css, body, bg, grain=.04):
    g = ("<svg style='position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none;opacity:@@G@@' xmlns='http://www.w3.org/2000/svg'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>").replace("@@G@@", str(grain))
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?{fonts}&display=swap' rel='stylesheet'>"
            f"<style>{COMMON}{css}</style></head><body style='background:{bg}'>{body}{g}</body></html>")


# ---- c1 Revista (s04): reclamo laboral ----
def c1():
    css = """body{font-family:'Jost',sans-serif;color:#fff}
    .ph{inset:0;width:100%;height:100%;object-position:62% 50%}
    .sc{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,13,18,.78),rgba(10,13,18,0) 62%),linear-gradient(rgba(10,13,18,0) 50%,rgba(10,13,18,.9))}
    .tg{position:absolute;left:84px;top:178px;background:#fff;color:#0d1015;font-weight:600;font-size:26px;letter-spacing:.14em;padding:9px 16px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:244px;width:370px;font-family:'Bodoni Moda',serif;font-weight:800;font-size:62px;line-height:1.04}
    h1 em{font-weight:700;font-style:italic;color:#f1dba0}
    .g{position:absolute;left:84px;bottom:150px;font-family:'Bodoni Moda',serif;font-weight:800;font-size:214px;line-height:.82;letter-spacing:-.02em;color:#f1dba0}
    .s{position:absolute;left:90px;bottom:92px;font-weight:500;font-size:34px}"""
    body = ("<img class='ph' src='fotos/s04.png'><div class='sc'></div><div class='abs' style='left:84px;top:84px'>" + logo('blanco') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Un reclamo laboral puede <em>frenar su pyme</em></h1><div class='g'>GRATIS</div><div class='s'>Diagnóstico laboral · 20 min</div>")
    return doc("family=Bodoni+Moda:ital,wght@0,800;1,700&family=Jost:wght@500;600", css, body, "#111", .05)


# ---- c2 Tarjeta de cita (s06): contrato vago ----
def c2():
    css = """body{font-family:'Newsreader',serif;color:#f1ece0}
    .ph{left:0;top:0;width:1080px;height:760px;object-position:50% 14%}
    .pn{position:absolute;left:0;right:0;top:760px;bottom:0;background:#0f3d3a;padding:34px 84px 0}
    .qm{font-size:110px;line-height:.5;color:#e9a77a;height:44px}
    .q{font-weight:600;font-size:54px;line-height:1.06}
    .at{font-family:'Jost',sans-serif;font-weight:500;font-size:26px;color:#b9d2cb;margin-top:12px}
    .tg{position:absolute;left:84px;top:178px;background:#0f3d3a;color:#f1ece0;font-family:'Jost',sans-serif;font-weight:600;font-size:26px;letter-spacing:.14em;padding:9px 16px;text-transform:uppercase}
    .g{position:absolute;left:84px;bottom:130px;font-weight:700;font-size:190px;line-height:.82;color:#e9a77a}
    .s{position:absolute;left:90px;bottom:80px;font-family:'Jost',sans-serif;font-weight:600;font-size:32px}"""
    body = ("<img class='ph' src='fotos/s06.png'><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<div class='pn'><div class='qm'>“</div><div class='q'>Un contrato vago puede costarle un cliente.</div><div class='at'>Dr. Fabián Galarraga · Fagal Abogados</div></div>"
            "<div class='g'>GRATIS</div><div class='s'>Diagnóstico de contratos · 20 min</div>")
    return doc("family=Newsreader:wght@600;700&family=Jost:wght@500;600", css, body, "#0f3d3a", .03)


# ---- c3 Suizo con foto (s10): siniestro negado ----
def c3():
    css = """body{font-family:'Schibsted Grotesk',sans-serif;color:#101010}
    .top{display:flex;justify-content:space-between;align-items:center;padding-bottom:16px;border-bottom:5px solid #101010}
    .tg{background:#101010;color:#fff;font-weight:800;font-size:24px;letter-spacing:.14em;padding:9px 14px;text-transform:uppercase}
    .h1{position:absolute;left:84px;top:190px;font-weight:900;font-size:112px;line-height:.95;letter-spacing:-.04em;white-space:nowrap}
    .h2{position:absolute;left:84px;top:300px;font-weight:900;font-size:112px;line-height:.95;letter-spacing:-.04em;color:#e5321f}
    .bx{position:absolute;left:84px;top:470px;width:912px;height:430px;overflow:hidden}
    .bx img{width:100%;height:100%;object-fit:cover;object-position:50% 8%}
    .g{position:absolute;left:84px;bottom:150px;font-weight:900;font-size:238px;line-height:.82;letter-spacing:-.05em;color:#e5321f}
    .s{position:absolute;left:90px;bottom:90px;font-weight:700;font-size:34px}"""
    body = ("<div class='abs' style='left:84px;right:84px;top:84px'><div class='top'>" + logo('negro') + "<div class='tg'>Para pymes</div></div></div>"
            "<div class='h1'>Siniestro negado.</div><div class='h2'>¿Y ahora?</div><div class='bx'><img src='fotos/s10.png'></div>"
            "<div class='g'>GRATIS</div><div class='s'>Revisión legal de su reclamo · 20 min</div>")
    return doc("family=Schibsted+Grotesk:wght@700;900", css, body, "#e9e8e3", .04)


# ---- c4 Cartel duotono (s07): accidente y operacion ----
def c4():
    css = """body{font-family:'Anton',sans-serif;color:#fff}
    .ph{right:0;top:230px;width:500px;height:700px;object-position:50% 12%}
    .tg{position:absolute;left:84px;top:170px;border:3px solid #ff8a3d;color:#ffb27a;font-family:'Barlow',sans-serif;font-weight:600;font-size:26px;letter-spacing:.12em;padding:6px 14px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:250px;width:470px;font-size:76px;line-height:1;text-transform:uppercase}
    h1 span{color:#ff8a3d}
    .g{position:absolute;left:70px;bottom:130px;font-size:270px;line-height:.78;color:#ff8a3d}
    .s{position:absolute;left:76px;bottom:80px;font-family:'Barlow',sans-serif;font-weight:600;font-size:32px}"""
    body = ("<img class='ph' src='fotos/s07_duo.png'><div class='abs' style='left:84px;top:84px'>" + logo('blanco') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Un accidente puede <span>parar su operación</span></h1><div class='g'>GRATIS</div><div class='s'>Diagnóstico legal · 20 min</div>")
    return doc("family=Anton&family=Barlow:wght@600", css, body, "#0a1838", .05)


# ---- c5 Cine negro B/N (s03): cartera ----
def c5():
    css = """body{font-family:'Jost',sans-serif;color:#f2eee4}
    .ph{left:0;top:0;width:1080px;height:1000px;object-position:50% 0%}
    .sc{position:absolute;left:0;right:0;top:560px;height:440px;background:linear-gradient(rgba(5,5,5,0),rgba(5,5,5,.95))}
    .tg{position:absolute;right:84px;top:100px;border:1.5px solid #111;color:#111;font-weight:500;font-size:24px;letter-spacing:.3em;padding:8px 16px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:790px;font-family:'DM Serif Display',serif;font-weight:400;font-size:112px;line-height:.95;text-transform:uppercase;letter-spacing:.03em}
    .g{position:absolute;left:84px;bottom:110px;font-family:'DM Serif Display',serif;font-size:236px;line-height:.8;letter-spacing:.03em;color:#e8c27a}
    .s{position:absolute;left:90px;bottom:56px;font-weight:500;font-size:30px;letter-spacing:.12em;text-transform:uppercase}"""
    body = ("<img class='ph' src='fotos/s03_bn.png'><div class='sc'></div><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Capital detenido</h1><div class='g'>GRATIS</div><div class='s'>Revisión de cartera · 20 min</div>")
    return doc("family=DM+Serif+Display&family=Jost:wght@500", css, body, "#050505", .07)


# ---- c6 Retail con banda diagonal (s01): cliente moroso ----
def c6():
    css = """body{font-family:'Rubik',sans-serif;color:#0d0d0d}
    .ph{inset:0;width:100%;height:100%;object-position:50% 30%}
    .band{position:absolute;left:-60px;right:-60px;bottom:-40px;height:470px;background:#d71f2a;transform:skewY(-5deg);box-shadow:0 -14px 40px #0004}
    .tg{position:absolute;right:84px;top:100px;background:#0d0d0d;color:#fff;font-weight:800;font-size:24px;letter-spacing:.12em;padding:9px 14px;text-transform:uppercase;font-style:italic}
    h1{position:absolute;left:84px;top:196px;width:330px;font-weight:900;font-style:italic;font-size:58px;line-height:.96;letter-spacing:-.02em;text-shadow:0 2px 0 #fff9}
    .g{position:absolute;left:84px;bottom:130px;font-weight:900;font-style:italic;font-size:226px;line-height:.8;color:#fff;letter-spacing:-.03em}
    .s{position:absolute;left:90px;bottom:80px;font-weight:600;font-size:32px;color:#fff}"""
    body = ("<img class='ph' src='fotos/s01.png'><div class='band'></div><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<h1>¿Un cliente dejó de pagar?</h1><div class='g'>GRATIS</div><div class='s'>Diagnóstico de cobranza · 20 min</div>")
    return doc("family=Rubik:ital,wght@1,800;1,900&family=Rubik:wght@600", css, body, "#e7e9ec", .03)


ADS = {"c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5, "c6": c6}


def render(v):
    hp = os.path.join(HERE, f"_{v}.html")
    open(hp, "w", encoding="utf-8").write(ADS[v]())
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{v}_4x5.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1.3333333", "--window-size=1080,1350",
                    "--virtual-time-budget=15000", f"--screenshot={out}", "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    prep()
    for v in ([a for a in sys.argv[1:] if a in ADS] or list(ADS)):
        print(render(v))
