# Anuncios FAGAL "marca de abogados": formatos del Taller (carta, checklist, numero gigante, certificado,
# dos formas, pregunta, hoja de ruta, palabra gigante) con la identidad del despacho: tinta, dorado del logo y marfil.
# Reglas: JERARQUIA_Y_COPY.md (dolor > agravacion > GRATIS > CTA > credencial) + perfil nombrado en cada creativo.
# Uso: python render_marca.py [m1..m8] [4x5|9x16]
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUT = os.path.join(HERE, "salida")
LOGO = "../logo_vector/FAGAL_logo_horizontal_%s.svg"
MONO = "../logo_vector/FAGAL_monograma_%s.svg"

GRAIN = ("<svg class='grain' xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%' height='100%' filter='url(#n)'/></svg>")

COMMON = """
:root{--ink:#0c1016;--ink2:#151c27;--gold:#c9a45a;--gold2:#e6cf92;--goldd:#85651f;--ivory:#f1ece0;--paper:#f7f3ea}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:@@H@@px;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased;font-family:'Manrope',sans-serif}
.in{position:absolute;inset:0;padding:@@pt@@px 84px @@pb@@px;display:flex;flex-direction:column}
.grain{position:absolute;inset:0;mix-blend-mode:overlay;opacity:@@grain@@;pointer-events:none}
.sp{flex:1}
.lk img{height:76px;width:auto;display:block}
.who{display:inline-block;margin-top:26px;border:1.5px solid var(--acc);color:var(--acc);font-weight:700;font-size:28px;letter-spacing:.16em;text-transform:uppercase;padding:11px 20px}
.serif{font-family:'Cormorant Garamond',serif}
.free{display:flex;align-items:center;gap:28px;border-top:1.5px solid var(--line);padding-top:24px;margin-top:26px}
.free .g{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:112px;line-height:.8;letter-spacing:.02em;color:var(--acc2)}
.free .fs{font-weight:600;font-size:30px;line-height:1.3;color:var(--fg)}
.row{display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:24px}
.prf{font-weight:600;font-size:30px;line-height:1.35;color:var(--mut)}
.cta{background:linear-gradient(180deg,#d8bb78,#b8975a);color:#15110a;font-weight:800;font-size:33px;letter-spacing:.04em;padding:23px 36px;text-transform:uppercase;white-space:nowrap}
.dark{--bg:#0c1016;--fg:#ece7da;--mut:#9a9684;--line:#c9a45a66;--acc:#e6cf92;--acc2:#e6cf92}
.light{--bg:#f4efe4;--fg:#14171d;--mut:#5d5a50;--line:#14171d55;--acc:#85651f;--acc2:#85651f}
"""


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@@%s@@" % k, str(v))
    return s


def logo(tone):
    return f"<div class='lk'><img src='{LOGO % tone}'></div>"


def bottom(free_text, cta="Agendar diagnóstico"):
    return (f"<div class='free'><span class='g'>GRATIS</span><span class='fs'>{free_text}</span></div>"
            f"<div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>{cta}</div></div>")


def doc(fmt, fonts, css, body, mode="dark", grain=".05"):
    f = fmt == "4x5"
    H, pt, pb = (1350, 96, 96) if f else (1920, 250, 340)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>{T(COMMON, H=H, pt=pt, pb=pb, grain=grain)}{css}</style></head>"
            f"<body class='{mode}' style='background:var(--bg);color:var(--fg)'>{body}{GRAIN}</body></html>")


FONTS = "family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Newsreader:ital,wght@0,500;0,600;1,500&family=Manrope:wght@500;600;700;800"


# ---------- m1 Carta: de un abogado a un empresario ----------
def m1(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(110% 70% at 85% 0%,#1c2432 0%,#0c1016 60%)!important}
    .card{margin-top:30px;background:var(--paper);color:#15181f;padding:@@pp@@px 54px;box-shadow:0 50px 90px -30px #000c,0 0 0 1px #c9a45a55;position:relative}
    .card:before{content:"";position:absolute;inset:14px;border:1px solid #c9a45a88;pointer-events:none}
    .eb{font-weight:800;font-size:26px;letter-spacing:.24em;text-transform:uppercase;color:#85651f}
    .lt{font-family:'Newsreader',serif;font-weight:500;font-size:@@ls@@px;line-height:1.28;margin-top:18px;color:#1a1d24}
    .lt b{font-weight:600;background:linear-gradient(transparent 58%,#e6cf9299 58%,#e6cf9299 94%,transparent 94%)}
    .sg{margin-top:20px;font-family:'Cormorant Garamond',serif;font-weight:700;font-style:italic;font-size:56px;color:#14171d}
    .sg small{display:block;font-family:'Manrope';font-style:normal;font-weight:600;font-size:24px;letter-spacing:.06em;color:#5d5a50;margin-top:2px}
    """, pp=48 if f else 64, ls=43 if f else 50)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para dueños y gerentes de empresas</span></div>
    <div class='card'><div class='eb'>De un abogado a un empresario</div>
    <div class='lt'><b>Una empresa sin abogado fijo llama tarde:</b> cuando el contrato ya se firmó, la cartera ya venció o la citación ya llegó. Hagamos lo contrario. Revisemos su empresa en 20 minutos, sin costo.</div>
    <div class='sg'>Fabián Galarraga<small>Socio fundador, Fagal Abogados</small></div></div>
    <div class='sp'></div>{bottom('Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m2 Checklist educativo: inmobiliarias ----------
def m2(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(100% 60% at 20% 0%,#16263a 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:28px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .card{margin-top:30px;background:var(--paper);color:#15181f;padding:@@pp@@px 40px;box-shadow:0 40px 80px -30px #000c;border-top:6px solid var(--gold)}
    .ct{font-weight:800;font-size:24px;letter-spacing:.2em;text-transform:uppercase;color:#85651f;margin-bottom:6px}
    .it{display:flex;gap:22px;align-items:center;font-family:'Newsreader',serif;font-weight:500;font-size:@@is@@px;line-height:1.2;padding:@@ip@@px 0;border-top:1px solid #14171d22}
    .it:first-of-type{border-top:0}
    .bx{flex:none;width:40px;height:40px;border:3px solid #85651f}
    .hot{font-weight:600;background:linear-gradient(transparent 60%,#e6cf9299 60%)}
    """, h1=76 if f else 90, pp=22 if f else 34, is_=0, **{}) if False else T("""
    body{background:radial-gradient(100% 60% at 20% 0%,#16263a 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:28px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .card{margin-top:30px;background:var(--paper);color:#15181f;padding:@@pp@@px 40px;box-shadow:0 40px 80px -30px #000c;border-top:6px solid var(--gold)}
    .ct{font-weight:800;font-size:24px;letter-spacing:.2em;text-transform:uppercase;color:#85651f;margin-bottom:6px}
    .it{display:flex;gap:22px;align-items:center;font-family:'Newsreader',serif;font-weight:500;font-size:@@is@@px;line-height:1.2;padding:@@ip@@px 0;border-top:1px solid #14171d22}
    .it:first-of-type{border-top:0}
    .bx{flex:none;width:40px;height:40px;border:3px solid #85651f}
    .hot{font-weight:600;background:linear-gradient(transparent 60%,#e6cf9299 60%)}
    """, h1=76 if f else 90, pp=22 if f else 34, is_=0) if False else T("""
    body{background:radial-gradient(100% 60% at 20% 0%,#16263a 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:28px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .card{margin-top:30px;background:var(--paper);color:#15181f;padding:@@pp@@px 40px;box-shadow:0 40px 80px -30px #000c;border-top:6px solid var(--gold)}
    .ct{font-weight:800;font-size:24px;letter-spacing:.2em;text-transform:uppercase;color:#85651f;margin-bottom:6px}
    .it{display:flex;gap:22px;align-items:center;font-family:'Newsreader',serif;font-weight:500;font-size:@@isz@@px;line-height:1.2;padding:@@ip@@px 0;border-top:1px solid #14171d22}
    .it:first-of-type{border-top:0}
    .bx{flex:none;width:40px;height:40px;border:3px solid #85651f}
    .hot{font-weight:600;background:linear-gradient(transparent 60%,#e6cf9299 60%)}
    """, h1=78 if f else 100, pp=20 if f else 40, isz=39 if f else 48, ip=14 if f else 28)
    items = ["Plazo y condiciones de entrega", "Multas por incumplimiento", "Arras y devolución de valores", "Gravámenes y saneamiento", "<span class='hot'>Resolución del contrato</span>"]
    li = "".join(f"<div class='it'><span class='bx'></span><span>{t}</span></div>" for t in items)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para inmobiliarias</span></div>
    <h1>5 cláusulas que su inmobiliaria debe <em>revisar antes de firmar</em></h1>
    <div class='card'><div class='ct'>Lista de revisión de contratos</div>{li}</div>
    <div class='sp'></div>{bottom('Diagnóstico de los contratos que más usa su inmobiliaria. 20 min.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m3 Numero gigante: 20 minutos (empresas medianas) ----------
def m3(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(90% 55% at 80% 15%,#222d3e 0%,#0c1016 65%)!important}
    .q{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:@@qs@@px;line-height:1.05;margin-top:26px;color:#f3eee2}
    .num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@ns@@px;line-height:.82;letter-spacing:-.03em;background:linear-gradient(180deg,#f0dba2 0%,#c9a45a 48%,#8f6c25 100%);-webkit-background-clip:text;background-clip:text;color:transparent;margin-top:@@nm@@px}
    .un{display:flex;align-items:baseline;gap:26px;margin-top:6px}.un b{font-weight:800;font-size:64px;letter-spacing:.3em;color:#ece7da}.un span{font-weight:500;font-size:38px;color:#b8b3a2;line-height:1.3}
    """, qs=80 if f else 96, ns=500 if f else 640, nm=0 if f else 30)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para empresas medianas</span></div>
    <div class='q'>¿Sabe qué riesgos legales tiene su empresa?</div>
    <div class='num'>20</div><div class='un'><b>MINUTOS</b><span>para saberlo,<br>con un abogado.</span></div>
    <div class='sp'></div>{bottom('Diagnóstico legal de su empresa, en su oficina o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m4 Certificado de diagnostico: transporte ----------
def m4(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(110% 70% at 15% 0%,#1b2a3e 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:26px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .cert{margin-top:@@cm@@px;background:var(--paper);color:#14171d;padding:@@cp@@px 44px;position:relative;box-shadow:0 50px 90px -30px #000c;text-align:center}
    .cert:before{content:"";position:absolute;inset:12px;border:3px double #a98a45;pointer-events:none}
    .cert img{height:96px;width:auto;opacity:.92}
    .cs{font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase;color:#85651f;margin-top:14px}
    .ctt{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@ct@@px;line-height:1;margin-top:10px}
    .cl{font-family:'Newsreader',serif;font-style:italic;font-size:40px;color:#4a4638;margin-top:14px}
    .seal{position:absolute;right:30px;top:26px;width:100px;height:100px;border-radius:50%;border:3px solid #a98a45;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;letter-spacing:.18em;color:#85651f;text-align:center;line-height:1.4;transform:rotate(-12deg)}
    """, h1=96 if f else 112, cm=34 if f else 64, cp=44 if f else 70, ct=68 if f else 78)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para empresas de transporte</span></div>
    <h1>Un accidente puede <em>parar toda su flota</em></h1>
    <div class='cert'><img src='{MONO % 'negro'}'><div class='cs'>Fagal Abogados · Cortesía</div><div class='ctt'>Diagnóstico legal para su flota</div>
    <div class='cl'>Seguros, contratos, laboral y accidentes</div><div class='seal'>SIN<br>COSTO</div></div>
    <div class='sp'></div>{bottom('Diagnóstico legal para su flota. 20 min, en su empresa o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m5 Dos formas: concesionarias ----------
def m5(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(100% 60% at 80% 0%,#1d2a3a 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:26px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .cols{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:@@cm@@px}
    .c{padding:32px 26px;display:flex;flex-direction:column;gap:@@gp@@px}
    .c1{border:1.5px solid #ffffff33;color:#b9b5a6}.c2{border:1.5px solid var(--gold);background:linear-gradient(180deg,#1b2433,#121923);color:#f3eee2}
    .ch{font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase}.c1 .ch{color:#9a9684}.c2 .ch{color:var(--gold2)}
    .i{font-family:'Newsreader',serif;font-weight:500;font-size:@@is@@px;line-height:1.22;padding-left:46px;position:relative}
    .i:before{position:absolute;left:0;top:0;font-family:'Manrope';font-weight:800;font-size:32px}
    .c1 .i:before{content:"✕";color:#a9674f}.c2 .i:before{content:"✓";color:var(--gold2)}
    """, h1=74 if f else 88, cm=26 if f else 44, gp=16 if f else 28, is_=0) if False else T("""
    body{background:radial-gradient(100% 60% at 80% 0%,#1d2a3a 0%,#0c1016 62%)!important}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:26px;color:#f3eee2}h1 em{color:var(--gold2);font-style:italic}
    .cols{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:@@cm@@px}
    .c{padding:26px 24px;display:flex;flex-direction:column;gap:@@gp@@px}
    .c1{border:1.5px solid #ffffff33;color:#b9b5a6}.c2{border:1.5px solid var(--gold);background:linear-gradient(180deg,#1b2433,#121923);color:#f3eee2}
    .ch{font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase}.c1 .ch{color:#9a9684}.c2 .ch{color:var(--gold2)}
    .i{font-family:'Newsreader',serif;font-weight:500;font-size:@@isz@@px;line-height:1.22;padding-left:46px;position:relative}
    .i:before{position:absolute;left:0;top:0;font-family:'Manrope';font-weight:800;font-size:32px}
    .c1 .i:before{content:"✕";color:#a9674f}.c2 .i:before{content:"✓";color:var(--gold2)}
    """, h1=86 if f else 100, cm=30 if f else 50, gp=24 if f else 40, isz=35 if f else 40)
    a = ["Busca abogado cuando el problema ya llegó", "Revisa el contrato después de firmarlo", "Cobra tarde, con documentos incompletos"]
    b = ["Un abogado que ya conoce su concesionaria", "Revisa antes de que usted firme", "Actúa a tiempo en la cobranza"]
    ca = "".join(f"<div class='i'>{t}</div>" for t in a); cb = "".join(f"<div class='i'>{t}</div>" for t in b)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para concesionarias</span></div>
    <h1>Dos formas de manejar lo legal en una <em>concesionaria</em></h1>
    <div class='cols'><div class='c c1'><div class='ch'>Sin abogado fijo</div>{ca}</div><div class='c c2'><div class='ch'>Con abogado de cabecera</div>{cb}</div></div>
    <div class='sp'></div>{bottom('Diagnóstico legal para concesionarias. 20 min, en su local o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m6 Pregunta A/B/C: gerentes y duenos ----------
def m6(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(100% 60% at 15% 0%,#212b3a 0%,#0c1016 62%)!important}
    .eb{margin-top:26px;font-weight:800;font-size:26px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold2)}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:14px;color:#f3eee2}
    .ops{display:flex;flex-direction:column;gap:@@og@@px;margin-top:@@om@@px}
    .o{display:flex;align-items:center;gap:22px;border:1.5px solid #ffffff3a;padding:@@op@@px 26px;font-family:'Newsreader',serif;font-weight:500;font-size:@@os@@px;line-height:1.2;color:#d9d4c6}
    .o i{flex:none;font-style:normal;font-family:'Manrope';font-weight:800;font-size:28px;width:54px;height:54px;border:1.5px solid #ffffff55;display:flex;align-items:center;justify-content:center;color:#b9b5a6}
    .o.k{border-color:var(--gold);background:#c9a45a1f;color:#f6efdc}.o.k i{background:var(--gold);border-color:var(--gold);color:#15110a}
    """, h1=84 if f else 100, og=14 if f else 24, om=30 if f else 50, op=20 if f else 30, os_=0) if False else T("""
    body{background:radial-gradient(100% 60% at 15% 0%,#212b3a 0%,#0c1016 62%)!important}
    .eb{margin-top:26px;font-weight:800;font-size:26px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold2)}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:14px;color:#f3eee2}
    .ops{display:flex;flex-direction:column;gap:@@og@@px;margin-top:@@om@@px}
    .o{display:flex;align-items:center;gap:22px;border:1.5px solid #ffffff3a;padding:@@op@@px 26px;font-family:'Newsreader',serif;font-weight:500;font-size:@@osz@@px;line-height:1.2;color:#d9d4c6}
    .o i{flex:none;font-style:normal;font-family:'Manrope';font-weight:800;font-size:28px;width:54px;height:54px;border:1.5px solid #ffffff55;display:flex;align-items:center;justify-content:center;color:#b9b5a6}
    .o.k{border-color:var(--gold);background:#c9a45a1f;color:#f6efdc}.o.k i{background:var(--gold);border-color:var(--gold);color:#15110a}
    """, h1=100 if f else 116, og=18 if f else 30, om=34 if f else 56, op=26 if f else 38, osz=42 if f else 46)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Para gerentes y dueños</span></div>
    <div class='eb'>Una pregunta para su empresa</div>
    <h1>¿Quién revisa lo que firma su empresa?</h1>
    <div class='ops'><div class='o'><i>A</i>El gerente, entre reuniones</div><div class='o'><i>B</i>Nadie, hasta que hay un problema</div><div class='o k'><i>C</i>Un abogado que ya la conoce</div></div>
    <div class='sp'></div>{bottom('Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body)


# ---------- m7 Hoja de ruta (fondo claro): duenos de empresas ----------
def m7(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#f1ece0!important}
    .who{color:#85651f;border-color:#85651f}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:1;margin-top:26px;color:#12151b}h1 em{color:#85651f;font-style:italic}
    .st{display:flex;flex-direction:column;margin-top:@@sm@@px}
    .s{display:flex;gap:26px;align-items:flex-start;padding:@@sp@@px 0;border-top:1.5px solid #14171d33}
    .n{flex:none;font-family:'Cormorant Garamond',serif;font-weight:700;font-size:112px;line-height:.8;color:#a98a45;width:84px}
    .t{font-weight:800;font-size:44px;line-height:1.1;color:#12151b}.d{font-family:'Newsreader',serif;font-size:34px;line-height:1.25;color:#44413a;margin-top:6px}
    .tg{display:inline-block;background:#12151b;color:#e6cf92;font-weight:800;font-size:22px;letter-spacing:.2em;text-transform:uppercase;padding:5px 12px;margin-left:12px;vertical-align:middle}
    """, h1=82 if f else 104, sm=20 if f else 50, sp=20 if f else 46)
    body = f"""<div class='in'>{logo('negro')}<div><span class='who'>Para dueños de empresas</span></div>
    <h1>Un abogado que ya conoce su empresa <em>antes del problema</em></h1>
    <div class='st'>
      <div class='s'><div class='n'>1</div><div><div class='t'>Diagnóstico <span class='tg'>Gratis</span></div><div class='d'>20 minutos para conocer su empresa y sus riesgos.</div></div></div>
      <div class='s'><div class='n'>2</div><div><div class='t'>Propuesta a su medida</div><div class='d'>Usted decide qué necesita, sin compromiso.</div></div></div>
      <div class='s'><div class='n'>3</div><div><div class='t'>Abogado de cabecera</div><div class='d'>Mes a mes, para revisar antes de que firme.</div></div></div></div>
    <div class='sp'></div>{bottom('Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.')}</div>"""
    return doc(fmt, FONTS, css, body, mode="light", grain=".04")


# ---------- m8 Palabra gigante: cartera por cobrar ----------
def m8(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(100% 60% at 70% 20%,#1f2836 0%,#0b0e13 66%)!important}
    .w{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;font-size:@@ws@@px;line-height:.86;letter-spacing:-.03em;color:#f3eee2;margin-top:@@wm@@px;white-space:nowrap}.w i{color:var(--gold);font-style:normal}
    .l{width:160px;height:5px;background:var(--gold);margin:22px 0}
    .sb{font-family:'Newsreader',serif;font-weight:500;font-size:46px;line-height:1.2;color:#e1dccc;max-width:800px}
    .sb b{font-weight:600;color:var(--gold2)}
    """, ws=330 if f else 300, wm=24 if f else 60)
    body = f"""<div class='in'>{logo('blanco')}<div><span class='who'>Empresas con cartera por cobrar</span></div>
    <div class='w'>Vencida<i>.</i></div><div class='l'></div>
    <div class='sb'>Una factura impaga no se cobra sola. <b>Cada mes sin accionar,</b> cobrar se hace más difícil.</div>
    <div class='sp'></div>{bottom('Revisión de su cartera vencida. Pagarés, letras y facturas tienen camino legal.', 'Revisar mi cartera')}</div>"""
    return doc(fmt, FONTS, css, body, grain=".06")


ADS = {"m1": m1, "m2": m2, "m3": m3, "m4": m4, "m5": m5, "m6": m6, "m7": m7, "m8": m8}


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
