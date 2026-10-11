# Anuncios FAGAL (plan de abogado de cabecera). HTML + SVG + CSS -> PNG con Chrome headless.
# Reglas: JERARQUIA_Y_COPY.md (dolor > agravacion > GRATIS > CTA > credencial), segmentacion desde el creativo
# (cada pieza nombra al perfil en una etiqueta), solo logo FAGAL, texto siempre en HTML.
# Uso: python render_fagal.py [c1 c2 c3 c4 c5 c6 e1 e2 e3] [4x5|9x16]
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUT = os.path.join(HERE, "salida")
LOGO_DIR = "../logo_vector/"

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
.lk{display:flex;align-items:center;gap:16px}
.lk img{height:84px;width:auto;display:block}
.lk b{display:block;font-family:'Tinos','Times New Roman',serif;font-weight:700;font-size:36px;letter-spacing:.06em;line-height:1}
.lk small{display:block;font-family:'Tinos','Times New Roman',serif;font-weight:700;font-size:19px;letter-spacing:.22em;line-height:1;margin-top:6px}
"""


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("@@%s@@" % k, str(v))
    return s


def logo(color):
    # logo plano oficial: blanco sobre fondos oscuros, negro sobre fondos claros
    tone = "negro" if color.lower() in ("#0f0f0f", "#1c1c1e", "#000000") else "blanco"
    return f"<div class='lk'><img src='{LOGO_DIR}FAGAL_logo_horizontal_{tone}.svg'></div>"


def doc(fmt, fonts, css, body, grain=".06"):
    f45 = fmt == "4x5"
    H, pt, pb = (1350, 96, 96) if f45 else (1920, 250, 340)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&family=Tinos:wght@700&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>"
            f"{T(COMMON, H=H, pt=pt, pb=pb, grain=grain)}{css}</style></head><body>{body}{GRAIN}</body></html>")


# ======================= C1 Inmobiliarias: la clausula (editorial de lujo) =======================
def c1(fmt):
    f = fmt == "4x5"
    css = T("""
    :root{--ink:#0c1016;--gold:#c2a15f;--gold2:#e1c88e;--txt:#e9e4d8;--mut:#9a9684}
    body{background:radial-gradient(120% 80% at 80% 0%,#1d2638 0%,#0c1016 58%);color:var(--txt);font-family:'Manrope',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:flex-start}
    .who{display:inline-block;margin-top:34px;border:1.5px solid var(--gold);color:var(--gold2);font-weight:800;font-size:28px;letter-spacing:.16em;text-transform:uppercase;padding:12px 22px;border-radius:2px}
    h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:@@h1@@px;line-height:.98;letter-spacing:-.01em;margin-top:30px;color:#f3eee2}
    h1 em{font-style:normal;color:var(--gold2)}
    .stage{position:relative;flex:1;margin-top:22px;margin-bottom:62px}
    .sheet{position:absolute;left:150px;right:-14px;top:6px;bottom:6px;background:linear-gradient(180deg,#f3eee2,#e6dfcf);border-radius:4px;transform:rotate(1.6deg);box-shadow:0 2px 0 #fff8 inset,0 30px 60px -20px #000c,0 80px 120px -40px #000a;padding:34px 50px;color:#2a2f3a;font-family:'Libre Baskerville',serif}
    .sheet:before{content:"";position:absolute;left:30px;top:0;bottom:0;width:2px;background:#c2563c33}
    .fol{display:flex;justify-content:space-between;font-family:'Manrope';font-weight:700;font-size:15px;letter-spacing:.22em;color:#8b8472;text-transform:uppercase}
    .ttl{font-weight:700;font-size:30px;margin:18px 0 4px;color:#1b2029}.cl{font-size:22px;font-weight:700;color:#7a6431;margin-bottom:14px}
    .p{font-size:24px;line-height:1.55;color:#3a3f4b}
    .hl{background:linear-gradient(transparent 52%,#e1c88e 52%,#e1c88e 92%,transparent 92%);color:#17120a;font-weight:700;padding:0 2px}
    .note{position:absolute;right:34px;bottom:-58px;background:var(--ink);border:1.5px solid var(--gold);border-radius:6px;padding:20px 22px;font-weight:800;font-size:23px;line-height:1.3;letter-spacing:.07em;color:var(--gold2);box-shadow:0 24px 50px -12px #000c;text-transform:uppercase}
    .free{display:flex;align-items:center;gap:30px;border-top:1.5px solid #c2a15f66;padding-top:26px;margin-top:34px}
    .g{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:112px;line-height:.8;letter-spacing:.02em;color:var(--gold2)}
    .fs{font-weight:600;font-size:30px;line-height:1.3}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}
    .prf{font-weight:600;font-size:30px;line-height:1.35;color:var(--mut)}
    .cta{background:linear-gradient(180deg,#d6b977,#b8975a);color:#15110a;font-weight:800;font-size:34px;letter-spacing:.04em;padding:24px 40px;border-radius:4px;text-transform:uppercase;box-shadow:0 18px 34px -12px #c2a15f66,0 1px 0 #fff6 inset;white-space:nowrap}
    """, h1=112 if f else 122)
    body = f"""<div class='in'>
    <div class='top'>{logo('#e1c88e')}</div>
    <div><span class='who'>Para inmobiliarias</span></div>
    <h1>¿Resiste su promesa de <em>compraventa?</em></h1>
    <div class='stage'><div class='sheet'>
      <div class='fol'><span>Promesa de compraventa</span><span>Folio 07</span></div>
      <div class='ttl'>CLÁUSULA SÉPTIMA</div><div class='cl'>DEL INCUMPLIMIENTO</div>
      <div class='p'>Las partes se obligan a cumplir íntegramente lo pactado en este instrumento. En caso de mora,
      <span class='hl'>el incumplimiento dará lugar a las acciones legales que correspondan</span>.</div>
      </div><div class='note'>Sin monto. Sin plazo.<br>Sin efecto.</div></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico de los contratos que más usa su inmobiliaria. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@500;600;700;800&family=Libre+Baskerville:wght@400;700", css, body)


# ======================= C2 Seguros: tipografia suiza =======================
def c2(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#e8e7e2;color:#0f0f0f;font-family:'Archivo',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:center;padding-bottom:20px;border-bottom:5px solid #0f0f0f}
    .who{display:inline-block;margin-top:26px;background:#0f0f0f;color:#fff;font-weight:800;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px}
    h1{font-weight:900;font-size:@@h1@@px;line-height:.86;letter-spacing:-.035em;margin-top:34px}h1 span{color:#e5321f}
    .tb{margin-top:40px;border-top:2px solid #0f0f0f}
    .r{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid #0f0f0f;padding:16px 0}
    .r i{font-style:normal;font-weight:600;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#5a5a55}.r b{font-weight:800;font-size:44px}
    .neg{background:#e5321f;color:#fff;margin:0 -18px;padding:16px 18px}.neg i{color:#fff}
    .free{display:flex;align-items:center;gap:30px;border-top:5px solid #0f0f0f;padding-top:24px}
    .g{font-weight:900;font-size:132px;line-height:.8;letter-spacing:-.03em;color:#e5321f}.fs{font-weight:700;font-size:32px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}
    .prf{font-weight:600;font-size:30px;line-height:1.3;color:#4a4a45}
    .cta{background:#0f0f0f;color:#fff;font-weight:800;font-size:34px;letter-spacing:.03em;padding:26px 38px;text-transform:uppercase;white-space:nowrap}.cta em{color:#ff6a55;font-style:normal}
    """, h1=162 if f else 170)
    body = f"""<div class='in'>
    <div class='top'>{logo('#0f0f0f')}</div>
    <div><span class='who'>Corredores y aseguradoras</span></div>
    <h1>Siniestro<br>negado.<br><span>¿Y ahora?</span></h1>
    <div class='tb'><div class='r'><i>Reclamo Nº</i><b>2026-0481</b></div><div class='r neg'><i>Estado</i><b>NEGADO</b></div><div class='r'><i>Siguiente paso</i><b>Estrategia legal</b></div></div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Revisión legal de su reclamo. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar revisión <em>→</em></div></div></div>"""
    return doc(fmt, "family=Archivo:wght@500;600;700;800;900", css, body, grain=".05")


# ======================= C3 Concesionarias: chat nativo =======================
def c3(fmt):
    f = fmt == "4x5"
    css = T("""
    html,body{display:flex;flex-direction:column}
    body{background:#efeae2;font-family:'Roboto',sans-serif;color:#111b21}
    .hd{background:#0b5c4d;padding:@@pt@@px 84px 22px;display:flex;align-items:center;gap:22px;color:#fff}
    .hd img{height:66px;width:auto;background:#0c1016;border-radius:50%;padding:12px;border:3px solid #c2a15f;box-sizing:content-box}
    .nm{font-weight:700;font-size:40px;line-height:1.1}.st{font-size:28px;opacity:.85;margin-top:4px}
    .chat{flex:1;padding:@@cp@@px 60px 20px;display:flex;flex-direction:column;gap:@@gap@@px}
    .day{align-self:center;background:#0c1016;color:#e1c88e;font-size:27px;font-weight:700;padding:10px 24px;border-radius:12px;letter-spacing:.12em;text-transform:uppercase}
    .b{max-width:790px;font-size:40px;line-height:1.28;padding:20px 28px 40px;border-radius:22px;position:relative;box-shadow:0 2px 2px #0002}
    .b small{position:absolute;right:20px;bottom:10px;font-size:23px;color:#667781}
    .me{align-self:flex-end;background:#d9fdd3;border-top-right-radius:6px}.you{align-self:flex-start;background:#fff;border-top-left-radius:6px}
    .pain{font-size:50px;font-weight:700;max-width:860px;line-height:1.2}
    .bot{background:#0c1016;padding:30px 84px @@pb@@px;display:flex;justify-content:space-between;align-items:center;gap:20px}
    .bt{color:#e9e4d8;font-weight:700;font-size:32px;line-height:1.2}
    .bt span{display:block;color:#e1c88e;font-family:'Cormorant Garamond',serif;font-size:96px;line-height:.85;letter-spacing:.02em}
    .cta{background:linear-gradient(180deg,#d6b977,#b8975a);color:#15110a;font-weight:800;font-size:32px;padding:22px 30px;border-radius:6px;white-space:nowrap;text-transform:uppercase;letter-spacing:.03em}
    """, pt=96 if f else 250, cp=30 if f else 60, gap=22 if f else 40, pb=96 if f else 340)
    body = """<div class='hd'><img src='../logo_vector/FAGAL_monograma_blanco.svg'><div><div class='nm'>Fagal Abogados</div><div class='st'>en línea</div></div></div>
    <div class='chat'>
      <div class='day'>Para concesionarias</div>
      <div class='b me pain'>Dr., mi cliente dejó de pagar la unidad. Van 3 cuotas.<small>10:42 ✓✓</small></div>
      <div class='b you'>Revisemos hoy la reserva de dominio. ¿Tiene el contrato a mano?<small>10:42</small></div>
      <div class='b me'>Sí. ¿Pueden venir a la concesionaria?<small>10:43 ✓✓</small></div>
      <div class='b you'>Mañana 10:00. Sin costo. Le confirmo por aquí.<small>10:43</small></div>
    </div>
    <div class='bot'><div class='bt'><span>GRATIS</span>Diagnóstico legal para concesionarias</div><div class='cta'>Escribir ahora</div></div>"""
    return doc(fmt, "family=Roboto:wght@400;500;700&family=Cormorant+Garamond:wght@700", css, body, grain=".03")


# ======================= C4 Fraude y estafa: neo-brutalista =======================
def c4(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#2336d4;color:#fff;font-family:'DM Sans',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:center}
    .who{display:inline-block;margin-top:26px;background:#ffe14d;color:#0a0a0a;font-weight:800;font-size:28px;letter-spacing:.1em;text-transform:uppercase;padding:12px 20px;border:4px solid #0a0a0a;box-shadow:6px 6px 0 #0a0a0a}
    h1{font-family:'Syne',sans-serif;font-weight:800;font-size:@@h1@@px;line-height:.98;letter-spacing:-.025em;margin-top:24px}
    h1 span{color:#ffe14d}
    .card{margin-top:28px;background:#fff;color:#0a0a0a;border:5px solid #0a0a0a;box-shadow:12px 12px 0 #0a0a0a;padding:20px 28px}
    .ct{font-family:'Syne',sans-serif;font-weight:800;font-size:36px;margin-bottom:12px}
    .it{display:flex;gap:18px;align-items:center;font-weight:700;font-size:@@it@@px;line-height:1.2;padding:@@ip@@px 0;border-top:3px solid #0a0a0a22}
    .bx{flex:none;width:38px;height:38px;border:4px solid #0a0a0a;background:#2336d4;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900}
    .warn{margin-top:22px;font-weight:700;font-size:31px;line-height:1.25;color:#ffe14d}
    .free{display:flex;align-items:center;gap:28px;border-top:4px solid #fff;padding-top:22px}
    .g{font-family:'Syne',sans-serif;font-weight:800;font-size:92px;line-height:.8;color:#ffe14d;letter-spacing:-.02em}.fs{font-weight:700;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#cfd6ff}
    .cta{background:#ffe14d;color:#0a0a0a;font-weight:800;font-size:33px;padding:22px 30px;text-transform:uppercase;letter-spacing:.03em;border:4px solid #0a0a0a;box-shadow:6px 6px 0 #0a0a0a;white-space:nowrap}
    """, h1=68 if f else 92, it=31 if f else 36, ip=8 if f else 14)
    items = ["Correos y chats originales", "Facturas y contratos firmados", "Movimientos bancarios", "Nombres de testigos", "Nada se borra ni se edita"]
    li = "".join(f"<div class='it'><span class='bx'>✓</span>{t}</div>" for t in items)
    body = f"""<div class='in'>
    <div class='top'>{logo('#ffffff')}</div>
    <div><span class='who'>Empresas · Fraude y estafa</span></div>
    <h1>Antes de denunciar, <span>asegure la prueba</span></h1>
    <div class='card'><div class='ct'>5 pruebas que debe guardar</div>{li}</div>
    <div class='warn'>Lo que no se guarda a tiempo, se pierde.</div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Orientación legal inicial. 20 min, en su empresa o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar orientación</div></div></div>"""
    return doc(fmt, "family=Syne:wght@800&family=DM+Sans:wght@500;700;800", css, body, grain=".04")


# ======================= C5 Cobro de dinero: terminal de datos =======================
def c5(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#090b0a;color:#f1ede2;font-family:'IBM Plex Mono',monospace}
    .top{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #2b2d27;padding-bottom:20px}
    .who{display:inline-block;margin-top:26px;color:#0a0a07;background:#ffb000;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase;padding:10px 18px}
    h1{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:@@h1@@px;line-height:1;letter-spacing:-.025em;margin-top:34px;color:#f5f1e6}
    h1 u{text-decoration:none;color:#ffb000}h1 i{display:inline-block;width:46px;height:92px;background:#ffb000;vertical-align:-8px;margin-left:10px}
    .cap{margin-top:34px;font-size:26px;letter-spacing:.14em;color:#8a8d80;display:flex;justify-content:space-between}
    .bars{margin-top:14px;border-top:2px solid #2b2d27}
    .br{display:flex;align-items:center;gap:22px;padding:16px 0;border-bottom:2px solid #2b2d27}
    .br .l{width:205px;font-size:32px;font-weight:600;color:#c8c5b8}.br .t{flex:1;height:36px;background:#17190f;position:relative}
    .br .t span{position:absolute;left:0;top:0;bottom:0;background:#ffb000}.br.bad .t span{background:repeating-linear-gradient(135deg,#ff4d3d 0 12px,#c0392b 12px 24px)}
    .br .v{width:190px;text-align:right;font-size:30px;font-weight:700;color:#ffb000}.br.bad .v,.br.bad .l{color:#ff6a55}
    .warn{margin-top:22px;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:34px;line-height:1.25;color:#ff6a55}
    .free{display:flex;align-items:center;gap:28px;border-top:2px solid #2b2d27;padding-top:24px}
    .g{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:112px;line-height:.8;letter-spacing:-.03em;color:#ffb000}
    .fs{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:32px;line-height:1.25;color:#e9e5d8}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}.prf{font-size:28px;line-height:1.35;color:#8a8d80}
    .cta{background:#ffb000;color:#0a0a07;font-family:'Space Grotesk',sans-serif;font-weight:800;font-size:34px;padding:26px 36px;text-transform:uppercase;letter-spacing:.03em;white-space:nowrap}
    """, h1=104 if f else 112)
    body = f"""<div class='in'>
    <div class='top'>{logo('#ffb000')}</div>
    <div><span class='who'>Empresas con cartera por cobrar</span></div>
    <h1>Facturas vencidas son <u>capital detenido</u><i></i></h1>
    <div class='cap'><span>EJEMPLO ILUSTRATIVO</span><span>% DE LA CARTERA</span></div>
    <div class='bars'>
      <div class='br'><div class='l'>0-30 días</div><div class='t'><span style='width:84%'></span></div><div class='v'>41%</div></div>
      <div class='br'><div class='l'>31-60</div><div class='t'><span style='width:52%'></span></div><div class='v'>26%</div></div>
      <div class='br'><div class='l'>61-90</div><div class='t'><span style='width:36%'></span></div><div class='v'>18%</div></div>
      <div class='br bad'><div class='l'>+90 días</div><div class='t'><span style='width:30%'></span></div><div class='v'>15%</div></div></div>
    <div class='warn'>Cada mes sin accionar, cobrar se hace más difícil.</div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Revisión de su cartera vencida. Pagarés, letras y facturas tienen camino legal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Revisar mi cartera</div></div></div>"""
    return doc(fmt, "family=IBM+Plex+Mono:wght@500;600;700&family=Space+Grotesk:wght@600;700", css, body, grain=".05")


# ======================= C6 Transporte: plano tecnico =======================
def c6(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0d4a85;color:#e6f2ff;font-family:'Barlow',sans-serif;
      background-image:linear-gradient(#ffffff14 2px,transparent 2px),linear-gradient(90deg,#ffffff14 2px,transparent 2px),linear-gradient(#ffffff09 1px,transparent 1px),linear-gradient(90deg,#ffffff09 1px,transparent 1px);
      background-size:108px 108px,108px 108px,27px 27px,27px 27px}
    .top{display:flex;justify-content:space-between;align-items:center}
    .pl{font-family:'Barlow Condensed',sans-serif;font-weight:600;font-size:26px;letter-spacing:.2em;text-align:right;color:#a9d0f5;line-height:1.5;text-transform:uppercase}
    .who{display:inline-block;margin-top:26px;border:3px solid #ffd23f;color:#ffd23f;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:34px;letter-spacing:.14em;text-transform:uppercase;padding:6px 20px}
    h1{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:@@h1@@px;line-height:.9;text-transform:uppercase;margin-top:28px;color:#fff}h1 span{color:#ffd23f}
    svg.truck{width:912px;height:340px;margin-top:34px;overflow:visible}
    .free{display:flex;align-items:center;gap:28px;border-top:3px solid #ffffff55;padding-top:22px}
    .g{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:128px;line-height:.78;color:#ffd23f;letter-spacing:.01em}
    .fs{font-weight:600;font-size:32px;line-height:1.25;color:#fff}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}.prf{font-weight:500;font-size:30px;line-height:1.3;color:#a9d0f5}
    .cta{background:#fff;color:#0d4a85;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:42px;padding:20px 38px;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}
    """, h1=160 if f else 176)

    def lab(x, y, t, ax, ay):
        return (f"<line x1='{ax}' y1='{ay}' x2='{x}' y2='{y + 10}' stroke='#ffd23f' stroke-width='3'/>"
                f"<circle cx='{ax}' cy='{ay}' r='9' fill='#0d4a85' stroke='#ffd23f' stroke-width='3'/>"
                f"<text x='{x}' y='{y}' fill='#ffd23f' font-family='Barlow Condensed' font-weight='700' font-size='38' letter-spacing='3' text-anchor='middle'>{t}</text>")
    st = "fill='none' stroke='#e6f2ff' stroke-width='4' stroke-linejoin='round' stroke-linecap='round'"
    truck = f"""<svg class='truck' viewBox='0 0 912 340'>
      <rect x='8' y='96' width='590' height='160' {st}/><path d='M8 128H598M8 224H598' {st} stroke-dasharray='2 14'/>
      <path d='M626 256V150L676 96H800Q830 96 846 128L890 184V256Z' {st}/><path d='M690 108H794Q812 108 824 134L842 170H672Z' {st}/><path d='M8 272H890' {st}/>
      <g {st}><circle cx='120' cy='272' r='34'/><circle cx='224' cy='272' r='34'/><circle cx='740' cy='272' r='34'/><circle cx='836' cy='272' r='34'/>
      <circle cx='120' cy='272' r='12'/><circle cx='224' cy='272' r='12'/><circle cx='740' cy='272' r='12'/><circle cx='836' cy='272' r='12'/></g>
      {lab(110, 36, 'SEGUROS', 110, 126)}{lab(330, 36, 'CONTRATOS', 330, 126)}{lab(560, 36, 'LABORAL', 560, 126)}{lab(760, 36, 'ACCIDENTES', 760, 136)}</svg>"""
    body = f"""<div class='in'>
    <div class='top'>{logo('#ffffff')}<div class='pl'>Plano Nº 06<br>Transporte</div></div>
    <div><span class='who'>Para empresas de transporte</span></div>
    <h1>Un accidente<br>puede parar<br><span>su flota</span></h1>
    {truck}<div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal para su flota. 20 min, en su empresa o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Barlow:wght@500;600&family=Barlow+Condensed:wght@600;700", css, body, grain=".04")


# ======================= E1 Empresas: contador si, abogado no (geometrico) =======================
def e1(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#0b3b2e;color:#f2efe4;font-family:'Work Sans',sans-serif;overflow:hidden}
    .geo{position:absolute;right:-180px;top:-180px;width:640px;height:640px;border-radius:50%;background:#134d3c}
    .geo2{position:absolute;left:-120px;bottom:@@gb@@px;width:420px;height:420px;border-radius:0 100% 0 0;background:#0f4535}
    .top{display:flex;justify-content:space-between;align-items:center;position:relative}
    .who{display:inline-block;margin-top:26px;border-bottom:5px solid #ff7a4d;color:#ffd7c6;font-weight:800;font-size:28px;letter-spacing:.14em;text-transform:uppercase;padding:0 0 8px;position:relative}
    .ti{font-family:'Big Shoulders Display',sans-serif;font-weight:700;font-size:56px;letter-spacing:.06em;text-transform:uppercase;color:#a7d1c0;margin-top:30px;position:relative}
    .rows{position:relative;margin-top:8px}
    .rw{display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid #ffffff22;padding:@@rp@@px 0}
    .rw span{font-family:'Big Shoulders Display',sans-serif;font-weight:800;font-size:@@rs@@px;line-height:.9;text-transform:uppercase;letter-spacing:.01em}
    .ck{width:96px;height:96px;border-radius:50%;background:#1d6a52;display:flex;align-items:center;justify-content:center}
    .rw.no{border-bottom:0}.rw.no span{color:#ff7a4d;font-size:@@rn@@px}
    .rw.no .ck{background:#ff7a4d;width:132px;height:132px;color:#0b3b2e;font-family:'Big Shoulders Display',sans-serif;font-weight:800;font-size:110px}
    .free{display:flex;align-items:center;gap:28px;border-top:3px solid #ffffff44;padding-top:22px;position:relative}
    .g{font-family:'Big Shoulders Display',sans-serif;font-weight:800;font-size:132px;line-height:.78;color:#ff7a4d;letter-spacing:.01em}
    .fs{font-weight:600;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px;position:relative}
    .prf{font-weight:500;font-size:30px;line-height:1.3;color:#a7d1c0}
    .cta{background:#ff7a4d;color:#0b2a21;font-weight:800;font-size:33px;padding:24px 34px;text-transform:uppercase;letter-spacing:.03em;white-space:nowrap}
    """, gb=300 if f else 330, rp=14 if f else 24, rs=124 if f else 140, rn=164 if f else 150)
    chk = "<svg width='56' height='56' viewBox='0 0 24 24' fill='none' stroke='#f2efe4' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M5 12.5l4.5 4.5L19 7.5'/></svg>"
    body = f"""<div class='geo'></div><div class='geo2'></div><div class='in'>
    <div class='top'>{logo('#f2efe4')}</div>
    <div><span class='who'>Para dueños y gerentes de empresas</span></div>
    <div class='ti'>Su empresa tiene</div>
    <div class='rows'>
      <div class='rw'><span>Contador</span><div class='ck'>{chk}</div></div>
      <div class='rw'><span>Seguro</span><div class='ck'>{chk}</div></div>
      <div class='rw'><span>Banco</span><div class='ck'>{chk}</div></div>
      <div class='rw no'><span>¿Abogado?</span><div class='ck'>?</div></div></div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Big+Shoulders+Display:wght@700;800&family=Work+Sans:wght@500;600;800", css, body, grain=".04")


# ======================= E2 Empresas medianas: nota de iPhone =======================
def e2(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:#fbfbf8;color:#1c1c1e;font-family:'Figtree',sans-serif}
    .bar{display:flex;justify-content:space-between;align-items:center;color:#c98a00;font-weight:600;font-size:34px}
    .who{font-weight:700;font-size:30px}
    .pg{margin-top:26px}
    .dt{text-align:center;color:#8e8e93;font-size:26px}
    h1{font-weight:800;font-size:@@h1@@px;line-height:1.04;letter-spacing:-.02em;margin-top:16px}
    .li{display:flex;gap:22px;align-items:flex-start;margin-top:@@gp@@px;font-size:40px;line-height:1.25;font-weight:500}
    .rg{flex:none;width:44px;height:44px;border:4px solid #c98a00;border-radius:50%;margin-top:3px}
    .hot{background:linear-gradient(transparent 55%,#ffe27a 55%,#ffe27a 95%,transparent 95%);font-weight:800}
    .big{font-size:46px}
    .sig{margin-top:30px;color:#c98a00;font-weight:700;font-size:34px}
    .free{display:flex;align-items:center;gap:28px;border-top:3px solid #1c1c1e;padding-top:22px}
    .g{font-family:'Figtree',sans-serif;font-weight:900;font-size:124px;line-height:.8;color:#1c1c1e;letter-spacing:-.03em}
    .fs{font-weight:700;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}.prf{font-weight:600;font-size:30px;line-height:1.3;color:#6a6a70}
    .cta{background:#ffcc00;color:#1c1c1e;font-weight:800;font-size:33px;padding:24px 34px;border-radius:14px;white-space:nowrap}
    """, h1=76 if f else 84, gp=26 if f else 44)
    body = f"""<div class='in'>
    <div class='bar'><span>‹ Notas</span><span class='who'>Empresas medianas</span><span>⋯</span></div>
    <div class='pg'><div class='dt'>FAGAL ABOGADOS</div>
    <h1>Lo que no tiene cubierto mi empresa</h1>
    <div class='li'><span class='rg'></span><span>Contratos con clientes revisados</span></div>
    <div class='li'><span class='rg'></span><span>Contratos laborales al día</span></div>
    <div class='li'><span class='rg'></span><span>Quién responde si me demandan</span></div>
    <div class='li big'><span class='rg'></span><span class='hot'>Qué hago si llega una citación</span></div>
    <div class='sig'>Pequeña para un departamento legal. Grande para no tener abogado.</div></div>
    <div class='sp'></div>
    <div style='margin-bottom:24px'>{logo('#1c1c1e')}</div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Figtree:wght@500;600;700;800;900", css, body, grain=".02")


# ======================= E3 Gerentes: pantalla de bloqueo =======================
def e3(fmt):
    f = fmt == "4x5"
    css = T("""
    body{background:radial-gradient(90% 60% at 20% 10%,#17414a 0%,transparent 60%),radial-gradient(80% 50% at 90% 90%,#2a2f3d 0%,transparent 60%),#0b0f14;color:#fff;font-family:'Figtree',sans-serif}
    .top{display:flex;justify-content:space-between;align-items:center}
    .who{display:inline-block;margin-top:26px;background:#ffffff1f;border:1.5px solid #ffffff55;color:#fff;font-weight:700;font-size:28px;letter-spacing:.1em;text-transform:uppercase;padding:12px 22px;border-radius:999px}
    h1{font-weight:900;font-size:@@h1@@px;line-height:1;letter-spacing:-.025em;margin-top:30px}h1 span{color:#ff8f7a}
    .nt{margin-top:30px;display:flex;flex-direction:column;gap:18px}
    .n{background:#ffffff22;border:1px solid #ffffff33;border-radius:30px;padding:24px 28px;display:flex;gap:22px;align-items:flex-start;backdrop-filter:blur(8px)}
    .ic{flex:none;width:68px;height:68px;border-radius:16px;background:#e5321f;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:40px}
    .nb{min-width:0}.nh{display:flex;justify-content:space-between;font-size:26px;color:#ffffffb0;font-weight:600;letter-spacing:.04em}
    .nt1{font-weight:800;font-size:38px;line-height:1.15;margin-top:4px}.nt2{font-weight:500;font-size:32px;line-height:1.25;margin-top:4px;color:#ffffffd9}
    .n.big .nt1{font-size:44px}
    .free{display:flex;align-items:center;gap:28px;border-top:3px solid #ffffff44;padding-top:22px}
    .g{font-weight:900;font-size:122px;line-height:.8;color:#ff8f7a;letter-spacing:-.03em}.fs{font-weight:700;font-size:31px;line-height:1.25}
    .row{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:24px}.prf{font-weight:500;font-size:30px;line-height:1.3;color:#ffffffa8}
    .cta{background:#fff;color:#0b0f14;font-weight:800;font-size:33px;padding:24px 34px;border-radius:14px;white-space:nowrap}
    """, h1=96 if f else 92)
    body = f"""<div class='in'>
    <div class='top'>{logo('#ffffff')}</div>
    <div><span class='who'>Para gerentes y dueños</span></div>
    <h1>Llegó una citación.<br><span>¿A quién llama?</span></h1>
    <div class='nt'>
      <div class='n big'><div class='ic'>!</div><div class='nb'><div class='nh'><span>CITACIÓN</span><span>ahora</span></div><div class='nt1'>Demanda contra su empresa</div><div class='nt2'>El plazo para contestar ya corre.</div></div></div>
      <div class='n'><div class='ic' style='background:#c47a00'>¶</div><div class='nb'><div class='nh'><span>LABORAL</span><span>hace 2 h</span></div><div class='nt1'>Reclamo de un exempleado</div></div></div>
      <div class='n'><div class='ic' style='background:#3a5a8c'>✎</div><div class='nb'><div class='nh'><span>CONTRATO</span><span>ayer</span></div><div class='nt1'>Firma pendiente</div><div class='nt2'>Ningún abogado lo ha revisado.</div></div></div>
    </div>
    <div class='sp'></div>
    <div class='free'><span class='g'>GRATIS</span><span class='fs'>Diagnóstico legal de su empresa. 20 min, en su oficina o en Fagal.</span></div>
    <div class='row'><div class='prf'>Convenios con gremios<br>y corporaciones</div><div class='cta'>Agendar diagnóstico</div></div></div>"""
    return doc(fmt, "family=Figtree:wght@500;600;700;800;900", css, body, grain=".04")


ADS = {"c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5, "c6": c6, "e1": e1, "e2": e2, "e3": e3}


def render(vid, fmt):
    hp = os.path.join(HERE, f"_{vid}_{fmt}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(ADS[vid](fmt))
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
