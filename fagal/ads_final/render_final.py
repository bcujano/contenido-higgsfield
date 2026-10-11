# Tanda definitiva con fotos de Galarraga (solo 4:5, export 1440x1800). 6 lenguajes graficos distintos.
# Reglas: dolor de pyme + perfil nombrado + GRATIS gigante + credencial en el texto de Meta; sin botones ni interfaces
# imitadas; las fotos con letreros rotos se recortan o se tapan (ver FOTO_*); solo logo plano FAGAL.
# Uso: python render_final.py [a1..a6]
import os, subprocess, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"
FOT = os.path.join(HERE, "fotos")
OUT = os.path.join(HERE, "salida")


def crop(src, box, dst):
    im = Image.open(os.path.join(FOT, src)).convert("RGB"); w, h = im.size
    im.crop((int(box[0]*w), int(box[1]*h), int(box[2]*w), int(box[3]*h))).save(os.path.join(FOT, dst), quality=95)


def prep():
    crop("g12.png", (0, 0.30, 1, 1), "c12.png")
    crop("g10_clean.png", (0.31, 0.14, 1.0, 0.80), "c10.png")
    crop("g09.png", (0.06, 0.0, 0.70, 1.0), "c09.png")
    crop("g02.png", (0.0, 0.0, 0.82, 1.0), "c02.png")
    # semitono de dos tintas para g07 (cabeza y hombros; el letrero queda ilegible)
    crop("g07_clean.png", (0.31, 0.15, 0.71, 0.49), "c07.png")
    from PIL import ImageOps
    im = ImageOps.autocontrast(Image.open(os.path.join(FOT, "c07.png")).convert("L"), cutoff=2); W, H = im.size; cell = 9; S = 2
    import numpy as np
    a = np.clip((np.asarray(im).astype(float)/255), 0, 1)
    for name, ang, col in (("c07_teal.png", 0, (0, 112, 120, 255)), ("c07_pink.png", 1, (232, 52, 120, 255))):
        cv = Image.new("RGBA", (W*S, H*S), (0, 0, 0, 0)); d = ImageDraw.Draw(cv); off = 0 if ang == 0 else cell/2
        for y in range(0, H-cell, cell):
            for x in range(0, W-cell, cell):
                l = a[y:y+cell, x:x+cell].mean(); r = (1-l)**0.9*cell*(0.62 if ang == 0 else 0.46)
                if r > 0.7:
                    cx, cy = (x+cell/2+off)*S, (y+cell/2+off)*S
                    d.ellipse((cx-r*S, cy-r*S, cx+r*S, cy+r*S), fill=col)
        cv.resize((W, H), Image.LANCZOS).save(os.path.join(FOT, name))


COMMON = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.lk img{height:70px;width:auto;display:block}
"""


def logo(t):
    return f"<div class='lk'><img src='{LOGO % t}'></div>"


def doc(fonts, css, body, bg, grain=.04):
    g = ("<svg style='position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;pointer-events:none;opacity:@@G@@' xmlns='http://www.w3.org/2000/svg'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>").replace("@@G@@", str(grain))
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?{fonts}&display=swap' rel='stylesheet'>"
            f"<style>{COMMON}{css}</style></head><body style='background:{bg}'>{body}{g}</body></html>")


# ---- a1 Revista (g04): contratos ----
def a1():
    css = """
    body{font-family:'Jost',sans-serif;color:#fff}
    .ph{position:absolute;left:0;top:170px;width:1080px;height:1350px;object-fit:cover}
    .tf{position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(#d9d9d6 58%,rgba(217,217,214,0))}
    .sc{position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(rgba(8,10,14,0),rgba(8,10,14,.88) 55%,rgba(8,10,14,.96))}
    .tg{position:absolute;right:84px;top:98px;background:#0d1015;color:#fff;font-weight:600;font-size:26px;letter-spacing:.14em;padding:10px 18px;text-transform:uppercase}
    h1{position:absolute;left:84px;top:232px;width:900px;font-family:'Bodoni Moda',serif;font-weight:800;font-size:68px;line-height:1.02;color:#12151b}
    h1 em{font-weight:700;font-style:italic;color:#7a5a16}
    .g{position:absolute;left:84px;bottom:158px;font-family:'Bodoni Moda',serif;font-weight:800;font-size:250px;line-height:.82;letter-spacing:-.02em;color:#f1dba0}
    .s{position:absolute;left:90px;bottom:96px;font-weight:500;font-size:34px;color:#ece7da}
    """
    body = ("<img class='ph' src='fotos/g04.png'><div class='tf'></div><div class='sc'></div><div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div>"
            "<div class='tg'>Para pymes</div><h1>¿Quién revisa lo que firma <em>su pyme?</em></h1><div class='g'>GRATIS</div><div class='s'>Diagnóstico legal de sus contratos · 20 min</div>")
    return doc("family=Bodoni+Moda:ital,wght@0,800;1,700&family=Jost:wght@500;600", css, body, "#ddd", .05)


# ---- a2 Bloque de color (g12): cobranza ----
def a2():
    css = """
    body{font-family:'Epilogue',sans-serif;color:#f6ecdc}
    .top{position:absolute;left:0;right:0;top:0;height:420px;background:#5c1326}
    .ph{position:absolute;left:0;top:420px;width:1080px;height:930px;object-fit:cover;object-position:center top}
    .sc{position:absolute;left:0;right:0;bottom:0;height:430px;background:linear-gradient(rgba(36,8,16,0),rgba(36,8,16,.9) 60%)}
    .tg{display:inline-block;border:2px solid #f6ecdc;font-family:'DM Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;padding:7px 14px;margin-left:24px;vertical-align:middle;text-transform:uppercase}
    h1{position:absolute;left:84px;top:196px;right:84px;font-weight:800;font-size:78px;line-height:1.0;letter-spacing:-.03em}
    h1 span{color:#ffb4a0}
    .g{position:absolute;left:84px;bottom:130px;font-weight:800;font-size:262px;line-height:.82;letter-spacing:-.05em;color:#ffb4a0}
    .s{position:absolute;left:90px;bottom:80px;font-family:'DM Mono',monospace;font-weight:500;font-size:28px;letter-spacing:.04em}
    """
    body = ("<div class='top'></div><img class='ph' src='fotos/c12.png'><div class='sc'></div><div class='abs' style='left:84px;top:84px;display:flex;align-items:center'>" + logo('blanco') + "<span class='tg'>Para pymes</span></div>"
            "<h1>Facturas vencidas son <span>capital detenido</span></h1><div class='g'>GRATIS</div><div class='s'>Revisión de su cartera · 20 min</div>")
    return doc("family=Epilogue:wght@800&family=DM+Mono:wght@500", css, body, "#5c1326")


# ---- a3 Arco editorial (g10): socios ----
def a3():
    css = """
    body{font-family:'Fraunces',serif;color:#14301f}
    .tg{position:absolute;right:84px;top:100px;font-family:'Manrope',sans-serif;font-weight:800;font-size:24px;letter-spacing:.18em;text-transform:uppercase;border-bottom:3px solid #14301f;padding-bottom:6px}
    h1{position:absolute;left:84px;top:200px;width:900px;font-weight:700;font-size:80px;line-height:1.0;letter-spacing:-.02em}
    h1 i{font-weight:500;color:#9a4a2b}
    .arch{position:absolute;left:84px;top:410px;width:500px;height:560px;border-radius:250px 250px 0 0;overflow:hidden;box-shadow:0 30px 50px -28px #14301f88}
    .dot{position:absolute;right:84px;top:640px;width:300px;height:300px;border-radius:50%;background:#9a4a2b}
    .dt{position:absolute;right:112px;top:700px;width:244px;font-family:'Fraunces',serif;font-style:italic;font-weight:500;font-size:38px;line-height:1.15;color:#ebe3d0;text-align:center}
    .arch img{width:100%;height:100%;object-fit:cover;object-position:62% 40%}
    .g{position:absolute;left:84px;top:1000px;font-weight:900;font-size:244px;line-height:.84;letter-spacing:-.04em;color:#9a4a2b}
    .s{position:absolute;left:90px;top:1230px;font-family:'Manrope',sans-serif;font-weight:700;font-size:34px}
    """
    body = ("<div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<h1>Dos socios sin pacto escrito: <i>¿y si se separan?</i></h1><div class='arch'><img src='fotos/c10.png'></div>"
            "<div class='dot'></div><div class='dt'>Una conversación a tiempo</div><div class='g'>GRATIS</div><div class='s'>Diagnóstico societario · 20 min</div>")
    return doc("family=Fraunces:ital,wght@0,700;0,900;1,500&family=Manrope:wght@700;800", css, body, "#ebe3d0", .05)


# ---- a4 Riso semitono (g07): marca ----
def a4():
    css = """
    body{font-family:'Bowlby One',sans-serif;color:#0b2f33}
    .tg{position:absolute;right:84px;top:98px;background:#0b2f33;color:#f1ead8;font-family:'Space Mono',monospace;font-weight:700;font-size:24px;letter-spacing:.12em;padding:9px 16px;text-transform:uppercase}
    .ht{position:absolute;left:60px;top:290px;width:720px;height:740px}
    .ht img{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;mix-blend-mode:multiply}
    .reg{position:absolute;right:-40px;top:600px;z-index:6;font-family:'Bowlby One';font-size:520px;line-height:.8;color:#e83478;mix-blend-mode:multiply}
    h1{position:absolute;left:84px;top:178px;font-size:72px;line-height:.98;letter-spacing:-.01em}
    .g{position:absolute;left:84px;bottom:150px;font-size:228px;line-height:.82;color:#0b2f33;letter-spacing:-.02em}
    .s{position:absolute;left:90px;bottom:90px;font-family:'Space Mono',monospace;font-weight:700;font-size:28px}
    """
    body = ("<div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div><h1>¿Su marca es suya?</h1><div class='reg'>®</div>"
            "<div class='ht'><img src='fotos/c07_pink.png' style='left:12px;top:8px'><img src='fotos/c07_teal.png'></div>"
            "<div class='g'>GRATIS</div><div class='s'>Diagnóstico de marca · 20 min</div>")
    return doc("family=Bowlby+One&family=Space+Mono:wght@700", css, body, "#f1ead8", .08)


# ---- a5 Panel dividido (g09): laboral ----
def a5():
    css = """
    body{font-family:'Plus Jakarta Sans',sans-serif;color:#10294f}
    .ph{position:absolute;left:0;top:0;width:560px;height:1070px;object-fit:cover;object-position:center top}
    .pn{position:absolute;left:560px;top:0;right:0;height:1070px;background:#10294f;color:#fff;padding:96px 44px 0 52px}
    .tg{display:inline-block;border:2px solid #7fb2ff;color:#9cc4ff;font-weight:800;font-size:22px;letter-spacing:.14em;padding:7px 12px;text-transform:uppercase}
    h1{font-weight:800;font-size:56px;line-height:1.04;letter-spacing:-.03em;margin-top:26px}
    h1 span{color:#ffb35c}
    .ic{margin-top:34px}
    .band{position:absolute;left:0;right:0;top:1070px;bottom:0;background:#ffb35c;padding:36px 84px 0}
    .g{font-weight:800;font-size:218px;line-height:.82;letter-spacing:-.05em;color:#10294f}
    .s{font-weight:800;font-size:34px;margin-top:10px;letter-spacing:-.01em}
    """
    ic = "<svg class='ic' width='430' height='190' viewBox='0 0 430 190'>"
    orange = {2, 5, 8}
    for n in range(12):
        r, c = divmod(n, 6); x = c*72+36; y = r*92+4; col = "#ffb35c" if n in orange else "#ffffff"
        ic += f"<circle cx='{x}' cy='{y+16}' r='13' fill='{col}'/><path d='M{x-24} {y+76}v-20a24 24 0 0 1 24 -24a24 24 0 0 1 24 24v20z' fill='{col}'/>"
    ic += "</svg>"
    body = ("<img class='ph' src='fotos/c09.png'><div class='pn'><div class='tg'>Para pymes</div><h1>¿Todos sus empleados tienen <span>contrato por escrito?</span></h1>" + ic + "</div>"
            "<div class='abs' style='left:60px;top:84px'>" + logo('negro') + "</div><div class='band'><div class='g'>GRATIS</div><div class='s'>Diagnóstico laboral · 20 min</div></div>")
    return doc("family=Plus+Jakarta+Sans:wght@800", css, body, "#10294f", .03)


# ---- a6 Brutalista rojo con instantanea (g02): fraude ----
def a6():
    css = """
    body{font-family:'Anton',sans-serif;color:#0a0a0a}
    .big{position:absolute;left:60px;top:190px;right:40px;font-size:126px;line-height:.92;text-transform:uppercase;color:#0a0a0a}
    .big span{color:#fff}
    .tg{position:absolute;right:84px;top:98px;background:#0a0a0a;color:#fff;font-family:'Space Mono',monospace;font-weight:700;font-size:24px;letter-spacing:.1em;padding:9px 16px;text-transform:uppercase}
    .pol{position:absolute;left:520px;top:575px;width:420px;background:#fff;padding:16px 16px 56px;transform:rotate(3.5deg);box-shadow:0 24px 40px -14px #0008}
    .pol img{display:block;width:100%;height:340px;object-fit:cover;object-position:30% 18%}
    .pol b{position:absolute;left:0;right:0;bottom:18px;text-align:center;font-family:'Space Mono',monospace;font-size:26px}
    .g{position:absolute;left:60px;bottom:130px;font-size:270px;line-height:.8;color:#0a0a0a;letter-spacing:-.01em}
    .s{position:absolute;left:66px;bottom:80px;font-family:'Space Mono',monospace;font-weight:700;font-size:28px;color:#fff}
    """
    body = ("<div class='abs' style='left:84px;top:84px'>" + logo('negro') + "</div><div class='tg'>Para pymes</div>"
            "<div class='big'>Antes de denunciar, <span>asegure la prueba</span></div><div class='pol'><img src='fotos/c02.png'></div>"
            "<div class='g'>GRATIS</div><div class='s'>Orientación legal para su pyme · 20 min</div>")
    return doc("family=Anton&family=Space+Mono:wght@700", css, body, "#e8452c", .06)


ADS = {"a1": a1, "a2": a2, "a3": a3, "a4": a4, "a5": a5, "a6": a6}


def render(v):
    hp = os.path.join(HERE, f"_{v}.html"); open(hp, "w", encoding="utf-8").write(ADS[v]())
    os.makedirs(OUT, exist_ok=True); out = os.path.join(OUT, f"{v}_4x5.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1.3333333",
                    "--window-size=1080,1350", "--virtual-time-budget=15000", f"--screenshot={out}", "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    prep()
    for v in ([a for a in sys.argv[1:] if a in ADS] or list(ADS)):
        print(render(v))
