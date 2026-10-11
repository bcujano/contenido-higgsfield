# Tanda t5: 6 anuncios con Soul Galarraga (s01, s02, s05, s09, s11, s12), 4:5 -> 1440x1800.
# Lenguajes nuevos: afiche de cine, apuntes con marcador, sello postal, art deco, Bauhaus, tipografia vertical.
# Reglas: dolor de pyme, "Para pymes", GRATIS gigante, logo plano, sin botones ni interfaces imitadas.
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"
OUT = os.path.join(HERE, "salida")
COMMON = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}body{position:relative;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.lk img{height:70px;width:auto;display:block}"""


def logo(t):
    return f"<div class='lk'><img src='{LOGO % t}'></div>"


def doc(fonts, css, body, bg, grain=.04):
    g = ("<svg style='position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none;opacity:@@G@@' xmlns='http://www.w3.org/2000/svg'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>").replace("@@G@@", str(grain))
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?{fonts}&display=swap' rel='stylesheet'>"
            f"<style>{COMMON}{css}</style></head><body style='background:{bg}'>{body}{g}</body></html>")


# ---- b1 Afiche de cine (s01): contratos ----
def b1():
    css = """body{font-family:'Bebas Neue',sans-serif;color:#f4efe4}
    .ph{position:absolute;left:0;top:210px;width:1080px;height:1350px;object-fit:cover;filter:contrast(1.08) saturate(.8) brightness(.82)}
    .v{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 45%,rgba(0,0,0,0) 40%,rgba(0,0,0,.72) 100%),linear-gradient(#000 0,#000 21%,rgba(0,0,0,0) 38%,rgba(0,0,0,0) 55%,rgba(0,0,0,.92))}
    .eb{position:absolute;left:0;right:0;top:164px;text-align:center;font-family:'Jost',sans-serif;font-weight:500;font-size:26px;letter-spacing:.5em;color:#e8cf8d;text-transform:uppercase}
    h1{position:absolute;left:40px;right:40px;top:204px;text-align:center;font-size:112px;line-height:.9;letter-spacing:.01em;text-shadow:0 6px 30px rgba(0,0,0,.6)}
    .g{position:absolute;left:0;right:0;bottom:150px;text-align:center;font-size:330px;line-height:.8;letter-spacing:.02em;color:#e8cf8d}
    .s{position:absolute;left:0;right:0;bottom:86px;text-align:center;font-family:'Jost',sans-serif;font-weight:500;font-size:32px;letter-spacing:.22em;text-transform:uppercase}"""
    body = ("<img class='ph' src='fotos/s01.png'><div class='v'></div><div class='abs' style='left:84px;top:84px'>" + logo('blanco') + "</div>"
            "<div class='eb'>Para pymes</div><h1>Nadie revisó<br>el contrato</h1><div class='g'>GRATIS</div><div class='s'>Diagnóstico de contratos · 20 min</div>")
    return doc("family=Bebas+Neue&family=Jost:wght@500", css, body, "#000", .06)


# ---- b2 Apuntes con marcador (s02): firmar sin leer ----
def b2():
    css = """body{font-family:'Caveat',cursive;color:#1b2b4a;background-image:linear-gradient(#9fb6d633 1.5px,transparent 1.5px),linear-gradient(90deg,#9fb6d633 1.5px,transparent 1.5px);background-size:36px 36px}
    .tg{position:absolute;right:84px;top:100px;font-family:'Manrope',sans-serif;font-weight:800;font-size:24px;letter-spacing:.16em;border:2px solid #1b2b4a;padding:7px 14px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:196px;width:800px;font-weight:700;font-size:104px;line-height:.92;transform:rotate(-1.5deg)}
    h1 u{text-decoration:none;background:linear-gradient(transparent 55%,#ffe27a 55%,#ffe27a 92%,transparent 92%)}
    .card{position:absolute;left:120px;top:440px;width:600px;height:560px;background:#fff;padding:18px 18px 0;transform:rotate(2deg);box-shadow:0 26px 40px -18px #1b2b4a77}
    .card img{display:block;width:100%;height:520px;object-fit:cover;object-position:62% 30%}
    .ring{position:absolute;left:150px;top:830px;width:330px;height:150px;border:7px solid #e0352b;border-radius:50% 46% 52% 48%;transform:rotate(-8deg)}
    .note{position:absolute;left:740px;top:610px;width:320px;font-size:62px;line-height:.95;color:#e0352b;transform:rotate(5deg)}
    .arrow{position:absolute;left:480px;top:790px;transform:scaleX(-1) rotate(-20deg)}
    .g{position:absolute;left:84px;bottom:150px;font-family:'Manrope',sans-serif;font-weight:800;font-size:236px;line-height:.82;letter-spacing:-.05em;color:#e0352b}
    .s{position:absolute;left:90px;bottom:90px;font-family:'Manrope',sans-serif;font-weight:700;font-size:34px}"""
    body = ("<div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div><h1>Firmó sin leer la <u>letra pequeña</u></h1>"
            "<div class='card'><img src='fotos/s02.png'></div><div class='ring'></div><div class='note'>¡ojo con esta cláusula!</div>"
            "<svg class='arrow' width='130' height='110' viewBox='0 0 130 110'><path d='M120 8 C 80 10, 40 40, 14 92' fill='none' stroke='#e0352b' stroke-width='6' stroke-linecap='round'/>"
            "<path d='M12 62 L12 96 L44 86' fill='none' stroke='#e0352b' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'/></svg>"
            "<div class='g'>GRATIS</div><div class='s'>Revisión de contratos · 20 min</div>")
    return doc("family=Caveat:wght@700&family=Manrope:wght@700;800", css, body, "#f6f3ea", .03)


# ---- b3 Sello postal (s05): citacion ----
def b3():
    css = """body{font-family:'Special Elite',monospace;color:#1a2a52}
    .bar{position:absolute;left:0;right:0;top:0;height:30px;background:repeating-linear-gradient(135deg,#c8342b 0 36px,#f3ead7 36px 54px,#1a2a52 54px 90px,#f3ead7 90px 108px)}
    .bar.b{top:auto;bottom:0}
    .tg{position:absolute;right:84px;top:100px;font-family:'Manrope',sans-serif;font-weight:800;font-size:24px;letter-spacing:.16em;border:2px solid #1a2a52;padding:7px 14px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:190px;width:560px;font-size:80px;line-height:1;font-weight:400}
    .st{position:absolute;right:70px;top:300px;width:420px;background:#fffdf6;padding:18px;transform:rotate(3deg);box-shadow:0 14px 26px -12px #1a2a5266}
    .st img{display:block;width:100%;height:560px;object-fit:cover;object-position:50% 12%}
    .pm{position:absolute;left:290px;top:660px;width:300px;height:300px;border:7px solid #c8342b;border-radius:50%;color:#c8342b;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-14deg);opacity:.88;text-align:center;font-family:'Manrope',sans-serif;font-weight:800;font-size:44px;letter-spacing:.06em;line-height:1.05}
    .pm small{font-size:26px;letter-spacing:.16em;margin-top:6px}
    .g{position:absolute;left:84px;bottom:150px;font-family:'Manrope',sans-serif;font-weight:800;font-size:236px;line-height:.82;letter-spacing:-.05em;color:#c8342b}
    .s{position:absolute;left:90px;bottom:92px;font-weight:400;font-size:30px}"""
    body = ("<div class='bar'></div><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Llegó una citación. El plazo ya corre.</h1><div class='st'><img src='fotos/s05.png'></div><div class='pm'>CITACIÓN<small>¡URGENTE!</small></div>"
            "<div class='g'>GRATIS</div><div class='s'>Diagnóstico ante una citación · 20 min</div><div class='bar b'></div>")
    return doc("family=Special+Elite&family=Manrope:wght@800", css, body, "#f3ead7", .06)


# ---- b4 Art deco (s09): cobranza ----
def b4():
    css = """body{font-family:'Poiret One',sans-serif;color:#d9bc72}
    .fr{position:absolute;left:54px;top:54px;right:54px;bottom:54px;border:3px solid #d9bc72}
    .fr2{position:absolute;left:70px;top:70px;right:70px;bottom:70px;border:1px solid #d9bc7288}
    .tg{position:absolute;left:0;right:0;top:176px;text-align:center;font-family:'Jost',sans-serif;font-weight:500;font-size:26px;letter-spacing:.5em;text-transform:uppercase}
    h1{position:absolute;left:0;right:0;top:226px;text-align:center;font-weight:400;font-size:112px;line-height:.98;letter-spacing:.02em;color:#f3e7c4}
    .ph{position:absolute;left:310px;top:500px;width:460px;height:450px;overflow:hidden;clip-path:polygon(0 60px,60px 0,calc(100% - 60px) 0,100% 60px,100% 100%,0 100%)}
    .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 22%}
    .ray{position:absolute;left:0;right:0;top:470px;height:600px;background:repeating-conic-gradient(from 0deg at 50% 100%,#d9bc7222 0 3deg,transparent 3deg 9deg)}
    .g{position:absolute;left:0;right:0;bottom:176px;text-align:center;font-weight:400;font-size:240px;line-height:.8;letter-spacing:.04em;color:#e9d08c}
    .s{position:absolute;left:0;right:0;bottom:116px;text-align:center;font-family:'Jost',sans-serif;font-weight:500;font-size:30px;letter-spacing:.2em;text-transform:uppercase;color:#f3e7c4}"""
    body = ("<div class='ray'></div><div class='fr'></div><div class='fr2'></div><div class='abs' style='left:50%;top:92px;transform:translateX(-50%)'>" + logo('blanco') + "</div>"
            "<div class='tg'>Para pymes</div><h1>Facturas vencidas,<br>capital detenido</h1><div class='ph'><img src='fotos/s09.png'></div>"
            "<div class='g'>GRATIS</div><div class='s'>Revisión de cartera · 20 min</div>")
    return doc("family=Poiret+One&family=Jost:wght@500", css, body, "#0e1a2b", .05)


# ---- b5 Bauhaus (s11): laboral ----
def b5():
    css = """body{font-family:'Archivo Black',sans-serif;color:#111}
    .tg{position:absolute;right:84px;top:100px;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:24px;letter-spacing:.14em;border:3px solid #111;padding:6px 12px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:190px;width:540px;font-size:70px;line-height:.98;letter-spacing:-.02em}
    .circ{position:absolute;left:380px;top:390px;width:580px;height:580px;border-radius:50%;overflow:hidden;border:10px solid #111}
    .circ img{width:100%;height:100%;object-fit:cover;object-position:50% 0%;transform:scale(1.15);transform-origin:50% 8%}
    .sq{position:absolute;left:64px;top:520px;width:280px;height:250px;background:#d92b2b}
    .tri{position:absolute;left:84px;top:800px;width:0;height:0;border-left:110px solid transparent;border-right:110px solid transparent;border-bottom:190px solid #1d4fd8}
    .bl{position:absolute;right:0;top:370px;width:150px;height:90px;background:#f5c518}
    .g{position:absolute;left:84px;bottom:130px;font-size:236px;line-height:.82;letter-spacing:-.05em;color:#111}
    .s{position:absolute;left:90px;bottom:84px;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:32px}"""
    body = ("<div class='sq'></div><div class='tri'></div><div class='bl'></div><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<h1>¿Todos sus empleados tienen contrato?</h1><div class='circ'><img src='fotos/s11.png'></div><div class='g'>GRATIS</div><div class='s'>Diagnóstico laboral · 20 min</div>")
    return doc("family=Archivo+Black&family=Space+Grotesk:wght@700", css, body, "#efe9db", .05)


# ---- b6 Tipografia vertical (s12): fraude y pruebas ----
def b6():
    css = """body{font-family:'Barlow Condensed',sans-serif;color:#f1ede4}
    .ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 30%;filter:contrast(1.05) brightness(.9)}
    .v{position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,8,12,.86),rgba(6,8,12,0) 55%),linear-gradient(rgba(6,8,12,0) 50%,rgba(6,8,12,.94))}
    .vt{position:absolute;left:0;top:0;transform-origin:0 0;transform:translate(64px,1140px) rotate(-90deg);font-weight:700;font-size:250px;line-height:.8;letter-spacing:.02em;color:transparent;-webkit-text-stroke:3px #ff6a3d;white-space:nowrap}
    .tg{position:absolute;right:84px;top:100px;font-family:'Manrope',sans-serif;font-weight:800;font-size:24px;letter-spacing:.16em;border:2px solid #f1ede4;padding:7px 14px;text-transform:uppercase;font-style:normal}
    h1{position:absolute;left:690px;top:220px;width:330px;font-weight:700;font-size:70px;line-height:.95;text-transform:uppercase}
    h1 span{color:#ff6a3d}
    .g{position:absolute;left:330px;bottom:150px;font-weight:700;font-size:250px;line-height:.8;color:#ff6a3d}
    .s{position:absolute;left:336px;bottom:92px;font-family:'Manrope',sans-serif;font-weight:700;font-size:32px}"""
    body = ("<img class='ph' src='fotos/s12.png'><div class='v'></div><div class='vt'>PRUEBA</div><div class='abs' style='left:84px;top:84px'>" + logo('blanco') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Antes de denunciar, <span>asegure la prueba</span></h1><div class='g'>GRATIS</div><div class='s'>Orientación legal · 20 min</div>")
    return doc("family=Barlow+Condensed:wght@700&family=Manrope:wght@700;800", css, body, "#06080c", .05)


ADS = {"b1": b1, "b2": b2, "b3": b3, "b4": b4, "b5": b5, "b6": b6}


def render(v):
    hp = os.path.join(HERE, f"_{v}.html")
    open(hp, "w", encoding="utf-8").write(ADS[v]())
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{v}_4x5.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1.3333333", "--window-size=1080,1350",
                    "--virtual-time-budget=15000", f"--screenshot={out}", "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    for v in ([a for a in sys.argv[1:] if a in ADS] or list(ADS)):
        print(render(v))
