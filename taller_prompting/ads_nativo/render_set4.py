# Set 4: vectorial + 3 anuncios con pixel art de Soul 3.01 (sprites en pixel/). Sin fotos.
# Uso: FASE=1 python render_set4.py [a1 .. a8] [4x5|9x16]
import os, subprocess, sys, calendar

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FASE = os.environ.get("FASE", "1")
NOW = 0 if FASE == "1" else 1
OUT = os.path.join(HERE, "juego_set4", "fase1_hasta-5-oct" if FASE == "1" else "fase2_5-al-15-oct")
SPR = lambda n: "file:///" + os.path.join(HERE, "pixel", n).replace("\\", "/")

GRAIN = ("<svg class='grain' xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%' height='100%' filter='url(#n)'/></svg>")
COMMON = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:%(H)dpx;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased}
.in{position:absolute;inset:0;padding:%(pt)dpx 84px %(pb)dpx;display:flex;flex-direction:column}
.grain{position:absolute;inset:0;mix-blend-mode:overlay;opacity:%(grain)s;pointer-events:none}
.abs{position:absolute} .sp{flex:1}
.px{image-rendering:pixelated}
"""
LAD = [("1-5 OCT", "LANZAMIENTO", "$65"), ("5-15 OCT", "PREVENTA", "$75"), ("15-21 OCT", "NORMAL", "$120")]


def ladder(cls="lad"):
    h = "".join(f"<div class='li{' on' if i == NOW else ''}'><span class='d'>{d}</span><span class='n'>{n}</span><b>{p}</b></div>"
                for i, (d, n, p) in enumerate(LAD))
    return f"<div class='{cls}'>{h}</div>"


def doc(fmt, fonts, css, body, grain=".05"):
    f45 = fmt == "4x5"
    H, pt, pb = (1350, 90, 90) if f45 else (1920, 250, 340)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>{COMMON % dict(H=H, pt=pt, pb=pb, grain=grain)}{css}</style>"
            f"</head><body>{body}{GRAIN}</body></html>")


# ================= A1 PIXEL: PRESS START (arcade) =================
def a1(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:radial-gradient(90% 70% at 50% 30%,#2a2150 0%,#12101f 70%);color:#f3efff;font-family:'VT323',monospace}}
    .scan{{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.28) 0 3px,transparent 3px 7px);pointer-events:none}}
    .hud{{display:flex;justify-content:space-between;font-family:'Silkscreen';font-size:32px;color:#59e0d0;letter-spacing:.06em}}
    .t{{font-family:'Silkscreen';font-weight:700;font-size:{108 if f else 126}px;line-height:.95;color:#ff5d73;text-shadow:8px 8px 0 #5b1e6b;margin-top:{26 if f else 40}px;text-transform:uppercase}}
    .t2{{font-family:'Silkscreen';font-size:{58 if f else 70}px;color:#59e0d0;margin-top:14px;text-shadow:4px 4px 0 #0b3b44}}
    .spr{{position:absolute;right:{30 if f else 20}px;top:{120 if f else 400}px;height:{560 if f else 700}px}}
    .left{{margin-top:auto}}
    .big{{font-family:'Silkscreen';font-size:{56 if f else 62}px;line-height:1.05;color:#fff;white-space:nowrap}}
    .s{{font-size:42px;line-height:1.05;margin:8px 0 16px;color:#cfc8ee}}
    .lad .li{{display:flex;gap:10px;align-items:baseline;font-size:42px;padding:6px 12px;border:4px solid #3b3470;margin-bottom:8px;background:rgba(18,16,31,.8)}}
    .li .d{{width:210px;white-space:nowrap}} .li .n{{flex:1;color:#cfc8ee}} .li b{{font-family:'Silkscreen';font-size:40px}}
    .li.on{{background:#ff5d73;border-color:#fff;color:#fff}} .li.on .n{{color:#fff}}
    .cta{{margin-top:12px;display:block;font-family:'Silkscreen';font-weight:700;font-size:40px;background:#59e0d0;color:#0b2530;padding:20px 16px;border:4px solid #fff;text-align:center}}
    """
    body = f"""<div class='scan'></div><div class='in'><div class='hud'><span>1UP 000065</span><span>NIVEL 1 · IA</span></div>
    <div class='t'>Press<br>Start</div><div class='t2'>Taller de IA</div>
    <img class='spr px' src='{SPR('sprite_busto_laptop.png')}'>
    <div class='left'><div class='big'>21·22·23<br>OCT</div><div class='s'>2 A 5 PM · AUDITORIO FENATRAPE<br>CUPOS LIMITADOS</div>{ladder()}<div class='cta'>▶ RESERVA TU CUPO</div></div></div>"""
    return doc(fmt, "family=Silkscreen:wght@400;700&family=VT323", css, body, grain=".04")


# ================= A2 PIXEL: ficha de personaje RPG =================
def a2(fmt):
    f = fmt == "4x5"
    stat = lambda k, v: f"<div class='st'><span>{k}</span><b>{v}</b></div>"
    css = f"""
    body{{background:#1b2a2e;color:#e8f1ea;font-family:'VT323',monospace}}
    .dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 3px,transparent 3px);background-size:36px 36px}}
    .h{{font-family:'Silkscreen';font-weight:700;font-size:{70 if f else 84}px;line-height:1;color:#a8e0a0;text-shadow:6px 6px 0 #0d1a1c}}
    .card{{margin-top:{20 if f else 28}px;border:10px solid #a8e0a0;background:#223a3f;box-shadow:12px 12px 0 #0d1a1c;display:flex;gap:20px;padding:22px 24px;align-items:flex-end}}
    .card img{{height:{500 if f else 620}px;flex:none}}
    .stats{{flex:1;padding-bottom:8px}}
    .nm{{font-family:'Silkscreen';font-size:44px;color:#fff;line-height:1.05}}
    .cl{{font-size:40px;color:#a8e0a0;margin:4px 0 14px}}
    .st{{display:flex;justify-content:space-between;font-size:42px;border-top:3px dashed #3f6068;padding:6px 0;line-height:1}}
    .st b{{font-family:'Silkscreen';font-size:36px;color:#fff}}
    .mis{{margin-top:18px;border:6px solid #ff9d6b;background:#2d1f1a;padding:14px 18px;font-size:44px;line-height:1.05}}
    .mis b{{font-family:'Silkscreen';color:#ff9d6b;font-size:36px;display:block;margin-bottom:6px}}
    .lad{{margin-top:18px;display:flex;gap:10px}}
    .li{{flex:1;border:4px solid #3f6068;padding:8px;text-align:center;display:flex;flex-direction:column;font-size:36px;line-height:1}}
    .li b{{font-family:'Silkscreen';font-size:50px;margin-top:4px}} .li .n{{color:#a9c5c8}}
    .li.on{{background:#a8e0a0;color:#0d1a1c;border-color:#fff}} .li.on .n{{color:#0d1a1c}}
    .cta{{margin-top:16px;font-family:'Silkscreen';font-weight:700;font-size:40px;background:#ff9d6b;color:#1b0f0a;padding:20px;text-align:center;border:4px solid #fff}}
    """
    body = f"""<div class='dots'></div><div class='in'><div class='h'>Nuevo<br>personaje</div>
    <div class='card'><img class='px' src='{SPR('sprite_cuerpo_celular.png')}'><div class='stats'>
    <div class='nm'>BYRON<br>CUJANO</div><div class='cl'>CLASE: EMPRESARIO</div>
    {stat('IA','4 AÑOS')}{stat('EMPRESAS','30+')}{stat('SISTEMAS IA','MAX')}</div></div>
    <div class='mis'><b>MISIÓN</b>Taller de IA · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>
    {ladder()}<div class='cta'>▶ RESERVA TU CUPO</div></div>"""
    return doc(fmt, "family=Silkscreen:wght@400;700&family=VT323", css, body, grain=".04")


# ================= A3 PIXEL: mapa de misión =================
def a3(fmt):
    f = fmt == "4x5"
    node = lambda n, t, x: f"<div class='nd' style='margin-left:{x}px'><div class='nb'>{n}</div><div class='nt'>{t}</div></div>"
    css = f"""
    body{{background:linear-gradient(180deg,#7ec8f0 0%,#bfe6fb 60%,#d9f2d0 60%);color:#10263a;font-family:'VT323',monospace}}
    .cl{{position:absolute;background:#fff;box-shadow:0 0 0 6px #fff;{'display:none' if not f else ''}}}
    .gr{{position:absolute;left:0;right:0;bottom:0;height:{34 if f else 28}%;background:#5fbf5a;border-top:10px solid #3d8f3a}}
    .h{{font-family:'Silkscreen';font-weight:700;font-size:{74 if f else 90}px;line-height:1;color:#10263a;text-shadow:5px 5px 0 #fff}}
    .path{{margin-top:{22 if f else 40}px;position:relative}}
    .nd{{display:flex;align-items:center;gap:16px;margin-bottom:{16 if f else 26}px}}
    .nb{{font-family:'Silkscreen';font-weight:700;font-size:38px;background:#ff5d73;color:#fff;border:6px solid #10263a;padding:14px 12px;min-width:136px;text-align:center;box-shadow:6px 6px 0 #10263a}}
    .nt{{font-size:{44 if f else 48}px;line-height:1;background:#fff;border:6px solid #10263a;padding:10px 14px;box-shadow:6px 6px 0 #10263a;max-width:{430 if f else 440}px}}
    .spr{{position:absolute;right:{40 if f else 20}px;top:{240 if f else 520}px;height:{520 if f else 620}px}}
    .box{{margin-top:auto;background:#10263a;color:#fff;padding:20px 22px;border:6px solid #fff;box-shadow:8px 8px 0 rgba(16,38,58,.4)}}
    .info{{font-size:44px;line-height:1.05;margin-bottom:12px}}
    .lad{{display:flex;gap:10px}}
    .li{{flex:1;border:4px solid #5b7a94;padding:8px;text-align:center;display:flex;flex-direction:column;font-size:36px;line-height:1}}
    .li b{{font-family:'Silkscreen';font-size:48px;margin-top:4px}} .li .n{{color:#a8c4d8}}
    .li.on{{background:#ff5d73;border-color:#fff}} .li.on .n{{color:#fff}}
    .cta{{margin-top:14px;font-family:'Silkscreen';font-weight:700;font-size:40px;background:#5fbf5a;color:#06210a;padding:18px;text-align:center;border:4px solid #fff}}
    """
    body = f"""<div class='cl' style='right:60px;top:{40 if f else 270}px;width:150px;height:46px'></div><div class='cl' style='right:200px;top:{120 if f else 350}px;width:120px;height:40px'></div><div class='gr'></div>
    <div class='in'><div class='h'>Tu negocio<br>sube de nivel</div>
    <div class='path'>{node('DÍA 1','ChatGPT sin miedo',0)}{node('DÍA 2','Contenido y anuncios',30)}{node('DÍA 3','Tu primera página web',60)}</div>
    <img class='spr px' src='{SPR('sprite_cuerpo_celular.png')}'>
    <div class='box'><div class='info'>Taller de IA · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>▶ RESERVA TU CUPO</div></div></div>"""
    return doc(fmt, "family=Silkscreen:wght@400;700&family=VT323", css, body, grain=".03")


# ================= A4 VECTOR: terminal =================
def a4(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#0b0e13;color:#e6edf5;font-family:'IBM Plex Mono',monospace}}
    .glow{{position:absolute;left:-200px;top:-200px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(125,211,252,.25),rgba(125,211,252,0) 70%)}}
    .win{{background:#111722;border:2px solid #263042;border-radius:22px;box-shadow:0 30px 60px rgba(0,0,0,.5);overflow:hidden}}
    .bar{{display:flex;gap:10px;padding:18px 24px;background:#171f2e;align-items:center;font-size:30px;color:#8896ab}}
    .dt{{width:18px;height:18px;border-radius:50%}}
    .tx{{padding:{26 if f else 34}px 30px {30 if f else 38}px;font-size:{42 if f else 46}px;line-height:1.3}}
    .pr{{color:#7dd3fc}} .ok{{color:#86efac}} .mu{{color:#8896ab}}
    .cur{{display:inline-block;width:24px;height:46px;background:#7dd3fc;vertical-align:-8px}}
    .hd{{font-family:'Bricolage Grotesque';font-weight:800;font-size:{104 if f else 120}px;line-height:.95;letter-spacing:-.035em;margin:{26 if f else 36}px 0 8px;color:#fff}}
    .hd i{{font-style:normal;color:#7dd3fc}}
    .info{{font-size:34px;line-height:1.3;color:#c9d4e3;margin-bottom:14px}}
    .lad{{display:flex;gap:12px;margin-bottom:16px}}
    .li{{flex:1;border:2px solid #2a3446;border-radius:16px;padding:12px;text-align:center;display:flex;flex-direction:column;font-size:32px}}
    .li .n{{font-size:30px;color:#8896ab}} .li b{{font-family:'Bricolage Grotesque';font-weight:800;font-size:60px;line-height:1.05}}
    .li.on{{background:#7dd3fc;border-color:#7dd3fc;color:#06202e}} .li.on .n{{color:#06202e}}
    .cta{{background:#fff;color:#0b0e13;border-radius:14px;text-align:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:50px;padding:22px}}
    """
    body = f"""<div class='glow'></div><div class='in'><div class='win'><div class='bar'><span class='dt' style='background:#ff6b6b'></span><span class='dt' style='background:#f5c451'></span><span class='dt' style='background:#4ade80'></span>&nbsp; ia — taller</div>
    <div class='tx'><span class='pr'>&gt;</span> hazme una página web<br>&nbsp;&nbsp;para mi negocio<br><span class='mu'>…la IA no sabe qué quieres</span><br><br>
    <span class='pr'>&gt;</span> <span class='ok'>pide bien, responde bien</span><span class='cur'></span></div></div>
    <div class='hd'>Pedir bien a la IA <i>se aprende</i></div><div class='sp'></div>
    <div class='info'>Taller de IA para tu negocio · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=IBM+Plex+Mono:wght@500;600&family=Bricolage+Grotesque:wght@800", css, body, grain=".06")


# ================= A5 VECTOR: calendario =================
def a5(fmt):
    f = fmt == "4x5"
    cal = calendar.Calendar(firstweekday=0)  # lunes
    days = ["L", "M", "X", "J", "V", "S", "D"]
    head = "".join(f"<div class='hd2'>{d}</div>" for d in days)
    cells = ""
    for d in cal.itermonthdays(2026, 10):
        if d == 0:
            cells += "<div class='c'></div>"
        else:
            cells += f"<div class='c{' on' if d in (21, 22, 23) else ''}'>{d}</div>"
    css = f"""
    body{{background:#f3f1ec;color:#1a1a1d;font-family:'Archivo',sans-serif}}
    .tag{{font-weight:800;font-size:32px;letter-spacing:.16em;color:#d9381e}}
    .t{{font-family:'Archivo Black';font-size:{108 if f else 124}px;line-height:.95;letter-spacing:-.03em;margin:12px 0 {18 if f else 30}px}}
    .t i{{font-style:normal;color:#d9381e}}
    .grid{{display:grid;grid-template-columns:repeat(7,1fr);gap:{8 if f else 12}px}}
    .hd2{{font-weight:800;font-size:30px;text-align:center;color:#8a8a90}}
    .c{{font-weight:700;font-size:{40 if f else 46}px;text-align:center;padding:{8 if f else 12}px 0;color:#a5a5ab}}
    .c.on{{background:#d9381e;color:#fff;border-radius:50%;font-weight:900;font-size:{50 if f else 56}px}}
    .m{{font-weight:800;font-size:34px;letter-spacing:.12em;margin:{14 if f else 22}px 0 8px}}
    .info{{font-weight:700;font-size:38px;line-height:1.2;margin:{16 if f else 24}px 0 14px}}
    .lad{{display:flex;gap:12px;margin-bottom:16px}}
    .li{{flex:1;border:3px solid #1a1a1d;border-radius:16px;padding:12px;text-align:center;display:flex;flex-direction:column;font-weight:700;font-size:32px}}
    .li .n{{font-size:30px;font-weight:600;opacity:.7}} .li b{{font-family:'Archivo Black';font-weight:400;font-size:58px;line-height:1.05}}
    .li.on{{background:#1a1a1d;color:#fff}}
    .cta{{background:#d9381e;color:#fff;text-align:center;font-family:'Archivo Black';font-size:46px;padding:22px;border-radius:16px}}
    """
    body = f"""<div class='in'><div class='tag'>TALLER DE IA · PARA EMPRENDEDORES</div><div class='t'>Marca estas<br><i>3 fechas</i></div>
    <div class='m'>OCTUBRE 2026</div><div class='grid'>{head}{cells}</div><div class='sp'></div>
    <div class='info'>2 A 5 PM · Auditorio Fenatrape<br>Certificado incluido · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Archivo+Black&family=Archivo:wght@600;700;800", css, body, grain=".05")


# ================= A6 VECTOR: recibo =================
def a6(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#d5d9df;color:#15171c;font-family:'IBM Plex Mono',monospace}}
    .rc{{position:relative;background:#fbfbf9;padding:{34 if f else 44}px 40px;box-shadow:0 30px 60px rgba(21,23,28,.25);flex:1;display:flex;flex-direction:column;
      -webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 18px) no-repeat,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/36px 18px repeat-x}}
    .c{{text-align:center;font-weight:600;font-size:34px;letter-spacing:.14em}}
    .tt{{text-align:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:{84 if f else 96}px;line-height:.95;letter-spacing:-.03em;margin:10px 0 14px}}
    .ln{{display:flex;font-size:{38 if f else 42}px;font-weight:500;line-height:1.5}}
    .ln span:first-child{{flex:none}} .ln .dots{{flex:1;border-bottom:4px dotted #9a9ca3;margin:0 10px 12px}}
    .hr{{border-top:4px dashed #15171c;margin:{16 if f else 22}px 0;opacity:.55}}
    .lad .li{{display:flex;justify-content:space-between;font-size:{38 if f else 42}px;font-weight:600;padding:6px 10px;line-height:1.35}}
    .li .d,.li .n{{display:inline}} .li .d{{margin-right:14px}} .li b{{font-weight:700}}
    .li.on{{background:#15171c;color:#fff}}
    .tot{{display:flex;justify-content:space-between;font-family:'Bricolage Grotesque';font-weight:800;font-size:{74 if f else 84}px;margin-top:6px}}
    .bars{{margin-top:auto;height:60px;background:repeating-linear-gradient(90deg,#15171c 0 4px,transparent 4px 9px,#15171c 9px 11px,transparent 11px 18px,#15171c 18px 24px,transparent 24px 28px)}}
    .stamp{{position:absolute;right:36px;bottom:{34 if f else 60}px;transform:rotate(-7deg);background:rgba(251,251,249,.92);border:6px solid #c8321f;color:#c8321f;font-weight:700;font-size:44px;padding:8px 20px;letter-spacing:.06em;border-radius:8px}}
    .cta{{margin-top:22px;background:#15171c;color:#fff;text-align:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:50px;padding:24px;border-radius:12px}}
    """
    body = f"""<div class='in'><div class='rc'><div class='c'>RECIBO DE TU CUPO</div><div class='tt'>Taller de IA</div><div class='hr'></div>
    <div class='ln'><span>3 DÍAS</span><span class='dots'></span><span>9 HORAS</span></div>
    <div class='ln'><span>FECHA</span><span class='dots'></span><span>21·22·23 OCT</span></div>
    <div class='ln'><span>HORARIO</span><span class='dots'></span><span>2 A 5 PM</span></div>
    <div class='ln'><span>LUGAR</span><span class='dots'></span><span>AUDITORIO FENATRAPE</span></div>
    <div class='ln'><span>CERTIFICADO</span><span class='dots'></span><span>INCLUIDO</span></div><div class='hr'></div>
    {ladder()}<div class='hr'></div><div class='tot'><span>TOTAL HOY</span><span>{LAD[NOW][2]}</span></div><div class='bars'></div><div class='stamp'>CUPOS LIMITADOS</div></div>
    <div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=IBM+Plex+Mono:wght@500;600;700&family=Bricolage+Grotesque:wght@800", css, body, grain=".05")


# ================= A7 VECTOR: hilo / publicacion =================
def a7(fmt):
    f = fmt == "4x5"
    ck = "<svg width='30' height='30' viewBox='0 0 24 24'><circle cx='12' cy='12' r='11' fill='#1d6bff'/><path d='M7 12.5l3.2 3.2L17 9' stroke='#fff' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"
    items = "".join(f"<div class='it'><b>{i + 1}</b>{t}</div>" for i, t in enumerate(
        ["Responder a tus clientes", "Escribir tus anuncios", "Crear tu contenido", "Ordenar tus ventas", "Hacer tu primera página web"]))
    css = f"""
    body{{background:linear-gradient(160deg,#d6e6ff 0%,#aac8ff 100%);color:#0e1a33;font-family:'Plus Jakarta Sans',sans-serif}}
    .card{{background:#fff;border-radius:44px;padding:{34 if f else 44}px 40px;box-shadow:0 40px 80px rgba(30,70,160,.28)}}
    .hd{{display:flex;align-items:center;gap:18px;margin-bottom:{18 if f else 26}px}}
    .av{{width:84px;height:84px;border-radius:50%;background:#1d6bff;color:#fff;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center}}
    .nm{{font-weight:800;font-size:38px;display:flex;align-items:center;gap:8px}} .hn{{font-weight:600;font-size:30px;color:#6b7a99}}
    .q{{font-weight:800;font-size:{64 if f else 74}px;line-height:1.04;letter-spacing:-.025em;margin-bottom:{16 if f else 26}px}}
    .it{{display:flex;gap:20px;align-items:center;font-weight:700;font-size:{42 if f else 46}px;padding:{10 if f else 14}px 0;border-top:2px solid #e6ecf7}}
    .it b{{flex:none;width:56px;height:56px;border-radius:50%;background:#e8f0ff;color:#1d6bff;display:flex;align-items:center;justify-content:center;font-size:34px}}
    .ft{{font-weight:800;font-size:40px;margin-top:14px;color:#1d6bff}}
    .sp{{flex:1}}
    .info{{font-weight:700;font-size:36px;line-height:1.25;margin-bottom:14px}}
    .lad{{display:flex;gap:12px;margin-bottom:16px}}
    .li{{flex:1;background:rgba(255,255,255,.65);border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column;font-weight:700;font-size:32px}}
    .li .n{{font-size:30px;font-weight:600;color:#4a5b80}} .li b{{font-weight:800;font-size:60px;line-height:1.05}}
    .li.on{{background:#1d6bff;color:#fff}} .li.on .n{{color:#dbe7ff}}
    .cta{{background:#0e1a33;color:#fff;text-align:center;font-weight:800;font-size:48px;padding:24px;border-radius:999px}}
    """
    body = f"""<div class='in'><div class='card'><div class='hd'><div class='av'>IA</div><div><div class='nm'>Taller de IA {ck}</div><div class='hn'>para dueños de negocio</div></div></div>
    <div class='q'>5 cosas que le puedes pedir a la IA para tu negocio</div>{items}<div class='ft'>En 3 días practicas las 5.</div></div><div class='sp'></div>
    <div class='info'>21·22·23 OCT · 2 A 5 PM · Auditorio Fenatrape<br>Cupos limitados · Certificado incluido</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Plus+Jakarta+Sans:wght@600;700;800", css, body, grain=".04")


# ================= A8 VECTOR: bento =================
def a8(fmt):
    f = fmt == "4x5"
    ic = lambda p, c="#fff": f"<svg width='76' height='76' viewBox='0 0 24 24' fill='none' stroke='{c}' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'>{p}</svg>"
    chat = ic("<path d='M4 5h16v11H9l-5 4V5z'/><path d='M8 9h8M8 12h5'/>", "#0f2a1f")
    mega = ic("<path d='M3 11v3h3l7 4V7L6 11H3z'/><path d='M16 9a4 4 0 0 1 0 6'/>", "#2a1b05")
    web = ic("<rect x='3' y='4' width='18' height='16' rx='2'/><path d='M3 9h18M7 6.5h.01M10 6.5h.01'/>", "#fff")
    cert = ic("<circle cx='12' cy='9' r='5'/><path d='M9 13.5L7.5 21 12 18.5 16.5 21 15 13.5'/>", "#fff")
    css = f"""
    body{{background:#efece6;color:#14141a;font-family:'DM Sans',sans-serif}}
    .g{{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1;grid-auto-rows:1fr}}
    .t{{border-radius:34px;padding:26px 28px;display:flex;flex-direction:column;justify-content:space-between}}
    .t h4{{font-family:'Unbounded';font-weight:800;font-size:{40 if f else 46}px;line-height:1.05;letter-spacing:-.02em}}
    .t p{{font-weight:700;font-size:34px;line-height:1.15}}
    .big{{grid-column:span 2;background:#14141a;color:#efece6}}
    .big h3{{font-family:'Unbounded';font-weight:800;font-size:{86 if f else 100}px;line-height:.95;letter-spacing:-.04em}}
    .big h3 i{{font-style:normal;color:#ff6a3d}}
    .cb{{background:#2b4bff;color:#fff}} .tm{{background:#ff6a3d;color:#fff}} .mt{{background:#9be8c0}} .sd{{background:#f2c98f}} .ik{{background:#14141a;color:#efece6}}
    .info{{font-weight:700;font-size:36px;line-height:1.25;margin:16px 0 12px}}
    .lad{{display:flex;gap:12px;margin-bottom:14px}}
    .li{{flex:1;border:3px solid #14141a;border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column;font-weight:700;font-size:32px}}
    .li .n{{font-size:30px;font-weight:600;opacity:.7}} .li b{{font-family:'Unbounded';font-weight:800;font-size:50px;line-height:1.1}}
    .li.on{{background:#2b4bff;color:#fff;border-color:#2b4bff}}
    .cta{{background:#14141a;color:#fff;text-align:center;font-family:'Unbounded';font-weight:800;font-size:40px;padding:26px;border-radius:999px}}
    """
    body = f"""<div class='in'><div class='g'>
    <div class='t big'><p style='color:#b8b6ae'>TALLER PARA EMPRENDEDORES</p><h3>Aprende <i>IA</i><br>en 3 días</h3></div>
    <div class='t cb'><div>{web}</div><h4>3 días<br>9 horas</h4></div>
    <div class='t tm'><div>{cert}</div><h4>Certificado incluido</h4></div>
    <div class='t mt'><div>{chat}</div><h4>Atiende a tus clientes</h4></div>
    <div class='t sd'><div>{mega}</div><h4>Crea tus anuncios</h4></div></div>
    <div class='info'>21·22·23 OCT · 2 A 5 PM · Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Unbounded:wght@800&family=DM+Sans:wght@600;700", css, body, grain=".05")


ADS = {"a1": a1, "a2": a2, "a3": a3, "a4": a4, "a5": a5, "a6": a6, "a7": a7, "a8": a8}


def render(aid, fmt):
    hp = os.path.join(HERE, f"_s4_{aid}_{fmt}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(ADS[aid](fmt))
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"{aid}_{fmt}.png")
    H = 1350 if fmt == "4x5" else 1920
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=15000", f"--screenshot={out}",
                    "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    return out


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a in ADS] or list(ADS)
    fm = [a for a in sys.argv[1:] if a in ("4x5", "9x16")] or ["4x5", "9x16"]
    for a in ids:
        for fmt in fm:
            print(render(a, fmt))
