# Ads 100% vectoriales (sin fotos): HTML + SVG + CSS renderizado con Chrome headless.
# Reglas: ../diseno_vectorial_reglas.md (ui-ux-pro-max, impeccable, taste-skill, canvas-design, Andromeda).
# Uso: FASE=1 python render_vector.py [v1 .. v8] [4x5|9x16]
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FASE = os.environ.get("FASE", "1")
NOW = 0 if FASE == "1" else 1
OUT = os.path.join(HERE, "juego_vectorial", "fase1_hasta-5-oct" if FASE == "1" else "fase2_5-al-15-oct")

GRAIN = ("<svg class='grain' xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%' height='100%' filter='url(#n)'/></svg>")

COMMON = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:%(H)dpx;overflow:hidden}
body{position:relative;-webkit-font-smoothing:antialiased}
.in{position:absolute;inset:0;padding:%(pt)dpx 84px %(pb)dpx;display:flex;flex-direction:column}
.grain{position:absolute;inset:0;mix-blend-mode:overlay;opacity:%(grain)s;pointer-events:none}
.abs{position:absolute}
"""

LAD = [("1-5 OCT", "LANZAMIENTO", "$65"), ("5-15 OCT", "PREVENTA", "$75"), ("15-21 OCT", "NORMAL", "$120")]


def ladder(cls="lad"):
    h = ""
    for i, (d, n, p) in enumerate(LAD):
        h += f"<div class='li{' on' if i == NOW else ''}'><span class='d'>{d}</span><span class='n'>{n}</span><b>{p}</b></div>"
    return f"<div class='{cls}'>{h}</div>"


def doc(fmt, fonts, css, body, grain=".07"):
    f45 = fmt == "4x5"
    H, pt, pb = (1350, 96, 96) if f45 else (1920, 250, 340)
    link = f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
    return (f"<!doctype html><html lang='es'><head><meta charset='utf-8'>{link}<style>"
            f"{COMMON % dict(H=H, pt=pt, pb=pb, grain=grain)}{css}</style></head><body>{body}{GRAIN}</body></html>")


# ============ V1 cartel brutalista: PROMPT gigante ============
def v1(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#0f1318;color:#eceee8;font-family:'Work Sans',sans-serif}}
    .tag{{font-weight:700;font-size:32px;letter-spacing:.14em;color:#c3ea66}}
    .giant{{font-family:'Anton';font-size:{300 if f else 300}px;line-height:.9;letter-spacing:-.01em;margin:{34 if f else 90}px 0 0 -8px;white-space:nowrap}} .bar{{height:14px;width:220px;background:#c3ea66;margin:8px 0 18px}}
    .sub{{font-family:'Anton';font-size:{64 if f else 76}px;color:#c3ea66;line-height:1.05;margin-top:22px;text-transform:uppercase}}
    .sp{{flex:1}}
    .row{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:22px}}
    .big{{font-family:'Anton';font-size:84px;line-height:1}}
    .s{{font-weight:600;font-size:34px;line-height:1.25;text-align:right}}
    .lad{{border-top:2px solid #3a4250;margin-bottom:22px}}
    .li{{display:flex;gap:18px;align-items:baseline;font-size:36px;font-weight:600;padding:10px 0;border-bottom:2px solid #3a4250}}
    .li .d{{width:200px}} .li .n{{flex:1;color:#9aa3b2;font-weight:500}} .li b{{font-family:'Anton';font-weight:400;font-size:52px}}
    .li.on{{color:#c3ea66}} .li.on .n{{color:#c3ea66}}
    .cta{{background:#c3ea66;color:#0f1318;text-align:center;font-weight:700;font-size:48px;padding:24px;letter-spacing:.04em;text-transform:uppercase}}
    """
    body = f"""<div class='in'><div class='tag'>TALLER DE IA · PARA EMPRENDEDORES</div>
    <div class='giant'>PROMPT</div><div class='bar'></div><div class='sub'>Aprende a pedirle bien<br>a la IA</div><div class='sp'></div>
    <div class='row'><div class='big'>21·22·23 OCT</div><div class='s'>2 A 5 PM · CUPOS LIMITADOS<br>AUDITORIO FENATRAPE</div></div>
    {ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Anton&family=Work+Sans:wght@500;600;700", css, body)


# ============ V2 numero gigante: 9 HORAS ============
def v2(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:radial-gradient(120% 80% at 10% 0%,#2a4dff 0%,#1a35c9 55%,#10228a 100%);color:#f2efe8;font-family:'Inter Tight',sans-serif}}
    .blob{{position:absolute;right:-180px;top:{300 if f else 520}px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,#5b7bff 0%,rgba(91,123,255,0) 70%);filter:blur(30px)}}
    .top{{font-weight:700;font-size:34px;letter-spacing:.1em}}
    .num{{font-family:'Bricolage Grotesque';font-weight:800;font-size:{760 if f else 860}px;line-height:.78;letter-spacing:-.05em;margin:{20 if f else 30}px 0 0 -18px}}
    .side{{position:absolute;left:{540 if f else 600}px;top:{270 if f else 440}px;right:60px}}
    .side .h{{font-family:'Bricolage Grotesque';font-weight:800;font-size:{118 if f else 130}px;line-height:.95;letter-spacing:-.03em}}
    .side .p{{font-size:{46 if f else 50}px;font-weight:600;line-height:1.15;margin-top:16px}}
    .sp{{flex:1}}
    .card{{background:#f2efe8;color:#10228a;border-radius:28px;padding:24px 30px;margin-bottom:20px}}
    .card .a{{font-weight:800;font-size:46px;letter-spacing:-.01em}} .card .b{{font-weight:600;font-size:34px;margin-top:4px}}
    .lad{{display:flex;gap:12px;margin-bottom:20px}}
    .li{{flex:1;border:3px solid rgba(242,239,232,.5);border-radius:22px;padding:14px 12px;text-align:center;display:flex;flex-direction:column}}
    .li .d{{font-weight:600;font-size:32px}} .li .n{{font-weight:500;font-size:30px;opacity:.85}}
    .li b{{font-family:'Bricolage Grotesque';font-weight:800;font-size:70px;line-height:1.05}}
    .li.on{{background:#ff6b4a;border-color:#ff6b4a;color:#fff}}
    .cta{{background:#ff6b4a;color:#fff;border-radius:999px;text-align:center;font-weight:800;font-size:48px;padding:24px}}
    """
    body = f"""<div class='blob'></div><div class='in'><div class='top'>TALLER DE IA · 3 DÍAS</div>
    <div class='num'>9</div><div class='side'><div class='h'>HORAS</div><div class='p'>para usar la IA en tu negocio</div></div><div class='sp'></div>
    <div class='card'><div class='a'>21·22·23 OCT · 2 A 5 PM</div><div class='b'>Auditorio Fenatrape · Certificado incluido</div></div>
    {ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Bricolage+Grotesque:wght@800&family=Inter+Tight:wght@500;600;700;800", css, body)


# ============ V3 checklist tipo app de notas ============
def v3(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:radial-gradient(90% 60% at 80% 0%,#1d5a4a 0%,#0f2a24 60%,#0a1d19 100%);color:#eef3ee;font-family:'Manrope',sans-serif}}
    .hd{{font-family:'Fraunces',serif;font-weight:600;font-size:{82 if f else 96}px;line-height:1;letter-spacing:-.02em;margin-bottom:{26 if f else 34}px}}
    .hd i{{color:#7be0b4;font-style:italic}}
    .card{{background:#f3f6f1;color:#10261f;border-radius:36px;padding:{30 if f else 38}px 40px;box-shadow:0 30px 60px rgba(0,0,0,.35),0 2px 0 rgba(255,255,255,.4) inset}}
    .bar{{display:flex;align-items:center;gap:12px;margin-bottom:{18 if f else 26}px;font-weight:700;font-size:32px;color:#4f6b61}}
    .dot{{width:18px;height:18px;border-radius:50%;background:#c9d6cf}}
    .it{{display:flex;align-items:center;gap:22px;font-weight:700;font-size:{44 if f else 50}px;padding:{12 if f else 18}px 0;border-bottom:2px solid #dbe4de;line-height:1.1}}
    .it:last-child{{border:0}}
    .ck{{flex:none;width:54px;height:54px;border-radius:16px;background:#0f6b4f;display:flex;align-items:center;justify-content:center}}
    .sp{{flex:1}}
    .info{{font-weight:700;font-size:36px;margin:{18 if f else 24}px 0 16px;line-height:1.25}}
    .lad{{display:flex;gap:12px;margin-bottom:18px}}
    .li{{flex:1;border:3px solid #3f7d68;border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column;color:#dff5ea}}
    .li .d{{font-weight:700;font-size:32px}} .li .n{{font-size:30px;font-weight:600;opacity:.85}} .li b{{font-size:62px;font-weight:800;line-height:1.05}}
    .li.on{{background:#7be0b4;border-color:#7be0b4;color:#0b2a20}}
    .cta{{background:#ff7a59;color:#fff;border-radius:22px;text-align:center;font-weight:800;font-size:48px;padding:24px}}
    """
    chk = "<svg width='32' height='32' viewBox='0 0 24 24' fill='none' stroke='#fff' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'><path d='M5 12.5l4.5 4.5L19 7.5'/></svg>"
    items = "".join(f"<div class='it'><div class='ck'>{chk}</div>{t}</div>" for t in
                    ["Responder a tus clientes", "Crear tus anuncios y contenido", "Hacer tu primera página web", "Ordenar tu negocio sin ser técnico"])
    body = f"""<div class='in'><div class='hd'>Lo que vas a poder <i>hacer</i> con IA</div>
    <div class='card'><div class='bar'><span class='dot'></span><span class='dot'></span><span class='dot'></span>&nbsp; Taller de IA para dueños de negocio</div>{items}</div><div class='sp'></div>
    <div class='info'>21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Fraunces:ital,wght@0,600;1,600&family=Manrope:wght@600;700;800", css, body)


# ============ V4 sin IA vs con IA ============
def v4(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#0e1116;color:#eef0f3;font-family:'IBM Plex Sans',sans-serif}}
    .hd{{font-family:'Space Grotesk';font-weight:700;font-size:{96 if f else 108}px;line-height:.98;letter-spacing:-.03em;margin-bottom:{28 if f else 36}px}}
    .cols{{display:flex;gap:18px}}
    .c{{flex:1;border-radius:26px;padding:{26 if f else 32}px 24px}}
    .c h3{{font-family:'Space Grotesk';font-size:56px;font-weight:700;margin-bottom:14px;letter-spacing:-.02em}}
    .c p{{font-size:{36 if f else 40}px;font-weight:500;line-height:1.2;padding:{12 if f else 16}px 0;border-top:2px solid rgba(255,255,255,.18)}}
    .no{{border:3px solid #ff6a5c;color:#ffd9d4}} .no h3{{color:#ff6a5c}}
    .si{{background:#6fe3b5;color:#0b2a20}} .si h3{{color:#0b2a20}} .si p{{border-color:rgba(11,42,32,.25)}}
    .sp{{flex:1}}
    .info{{font-weight:600;font-size:36px;line-height:1.25;margin-bottom:16px}}
    .lad{{display:flex;gap:12px;margin-bottom:18px}}
    .li{{flex:1;border:3px solid #3a424f;border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column}}
    .li .d{{font-weight:600;font-size:32px}} .li .n{{font-size:30px;color:#9aa3b2}} .li b{{font-family:'Space Grotesk';font-size:62px;line-height:1.05}}
    .li.on{{background:#6fe3b5;border-color:#6fe3b5;color:#0b2a20}} .li.on .n{{color:#0b2a20}}
    .cta{{background:#6fe3b5;color:#0b2a20;border-radius:16px;text-align:center;font-family:'Space Grotesk';font-weight:700;font-size:50px;padding:22px}}
    """
    body = f"""<div class='in'><div class='hd'>Dos formas de llevar tu negocio</div>
    <div class='cols'><div class='c no'><h3>Sin IA</h3><p>Respondes cliente por cliente</p><p>Publicas cuando te acuerdas</p><p>La página web sigue pendiente</p></div>
    <div class='c si'><h3>Con IA</h3><p>Un agente atiende contigo</p><p>Contenido listo para publicar</p><p>Tu primera web, hecha en el taller</p></div></div><div class='sp'></div>
    <div class='info'>Taller de IA · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Space+Grotesk:wght@700&family=IBM+Plex+Sans:wght@500;600;700", css, body)


# ============ V5 ticket de evento ============
def v5(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#0d1a31;color:#101c33;font-family:'Figtree',sans-serif}}
    .lines{{position:absolute;inset:0;background:repeating-linear-gradient(135deg,rgba(255,255,255,.035) 0 2px,transparent 2px 26px)}}
    .tk{{position:relative;background:#eeeee8;border-radius:26px;padding:{34 if f else 44}px 44px;box-shadow:0 40px 70px rgba(0,0,0,.45);flex:1;display:flex;flex-direction:column}}
    .tk:before,.tk:after{{content:'';position:absolute;left:-28px;width:56px;height:56px;border-radius:50%;background:#0d1a31;top:var(--cut)}}
    .tk:after{{left:auto;right:-28px}}
    .eb{{font-weight:800;font-size:32px;letter-spacing:.2em;color:#a8302a}}
    .t{{font-family:'Instrument Serif',serif;font-size:{118 if f else 136}px;line-height:.95;margin:10px 0 14px;letter-spacing:-.02em}}
    .t i{{color:#a8302a}}
    .dt{{font-weight:800;font-size:{84 if f else 90}px;line-height:1;letter-spacing:-.02em}}
    .pl{{font-weight:600;font-size:36px;line-height:1.25;margin-top:8px}}
    .perf{{border-top:4px dashed #101c33;opacity:.35;margin:{22 if f else 30}px 0}}
    .lad .li{{display:flex;gap:16px;align-items:baseline;font-size:38px;font-weight:700;padding:8px 14px;border-radius:12px}}
    .li .d{{width:190px}} .li .n{{flex:1;font-weight:600;opacity:.75}} .li b{{font-family:'Instrument Serif';font-weight:400;font-size:64px;line-height:1}}
    .li.on{{background:#a8302a;color:#fff}} .li.on .n{{opacity:1}}
    .bars{{margin-top:auto;height:70px;background:repeating-linear-gradient(90deg,#101c33 0 4px,transparent 4px 9px,#101c33 9px 11px,transparent 11px 18px,#101c33 18px 24px,transparent 24px 28px);opacity:.85}}
    .stamp{{position:absolute;right:50px;bottom:{150 if f else 190}px;transform:rotate(-10deg);border:6px solid #c0382e;color:#c0382e;font-weight:900;font-size:46px;padding:10px 22px;letter-spacing:.08em;border-radius:10px;background:rgba(238,238,232,.9)}}
    .cta{{margin-top:24px;background:#c0382e;color:#fff;text-align:center;border-radius:14px;font-weight:800;font-size:50px;padding:24px}}
    """
    body = f"""<div class='lines'></div><div class='in'><div class='tk' style='--cut:{58 if f else 62}%'>
    <div class='eb'>ENTRADA · PARA EMPRENDEDORES</div><div class='t'>Taller de <i>IA</i></div>
    <div class='dt'>21·22·23 OCT</div><div class='pl'>2 A 5 PM · AUDITORIO FENATRAPE · CERTIFICADO INCLUIDO</div>
    <div class='perf'></div>{ladder()}<div class='bars'></div><div class='stamp'>CUPOS LIMITADOS</div></div><div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Instrument+Serif:ital@0;1&family=Figtree:wght@600;700;800;900", css, body, grain=".05")


# ============ V6 diagrama de flujo: sin saber programar ============
def v6(fmt):
    f = fmt == "4x5"
    icon = lambda p: f"<svg width='84' height='84' viewBox='0 0 24 24' fill='none' stroke='#fff' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'>{p}</svg>"
    bulb = icon("<path d='M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z'/>")
    chat = icon("<path d='M4 5h16v11H9l-5 4V5z'/><path d='M8 9h8M8 12h5'/>")
    ok = icon("<circle cx='12' cy='12' r='9'/><path d='M8 12.5l3 3 5-6'/>")
    css = f"""
    body{{background:radial-gradient(70% 50% at 15% 10%,#2b8f95 0%,rgba(43,143,149,0) 60%),radial-gradient(80% 60% at 90% 70%,#2147a8 0%,rgba(33,71,168,0) 65%),#0a2236;color:#f1f6f8;font-family:'IBM Plex Sans',sans-serif}}
    .hd{{font-family:'Space Grotesk';font-weight:700;font-size:{128 if f else 150}px;line-height:.92;letter-spacing:-.035em}}
    .hd i{{font-style:normal;color:#8ff0d6}}
    .flow{{display:flex;flex-direction:{'row' if f else 'column'};align-items:center;gap:{14 if f else 8}px;margin:{34 if f else 24}px 0}}
    .nd{{flex:1;width:100%;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.28);border-radius:28px;padding:{44 if f else 24}px 18px;text-align:center;backdrop-filter:blur(6px)}}
    .nd b{{display:block;font-family:'Space Grotesk';font-size:{44 if f else 52}px;margin-top:6px;letter-spacing:.02em}}
    .ar{{font-size:60px;color:#8ff0d6;font-weight:700;line-height:1}}
    .sp{{flex:1}}
    .info{{font-weight:600;font-size:36px;line-height:1.25;margin-bottom:16px}}
    .lad{{display:flex;gap:12px;margin-bottom:18px}}
    .li{{flex:1;border:3px solid rgba(255,255,255,.4);border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column}}
    .li .d{{font-weight:600;font-size:32px}} .li .n{{font-size:30px;opacity:.8}} .li b{{font-family:'Space Grotesk';font-size:62px;line-height:1.05}}
    .li.on{{background:#8ff0d6;border-color:#8ff0d6;color:#06303a}}
    .cta{{background:#fff;color:#0a2236;border-radius:999px;text-align:center;font-family:'Space Grotesk';font-weight:700;font-size:50px;padding:22px}}
    """
    flow = f"<div class='flow'><div class='nd'>{bulb}<b>IDEA</b></div><div class='ar'>{'→' if f else '↓'}</div><div class='nd'>{chat}<b>PROMPT</b></div><div class='ar'>{'→' if f else '↓'}</div><div class='nd'>{ok}<b>RESULTADO</b></div></div>"
    body = f"""<div class='in'><div class='hd'>Sin saber<br><i>programar</i></div>{flow}<div class='sp'></div>
    <div class='info'>Taller de IA para tu negocio<br>21·22·23 OCT · 2 A 5 PM · Auditorio Fenatrape</div>{ladder()}<div class='cta'>Reserva tu cupo · Cupos limitados</div></div>"""
    return doc(fmt, "family=Space+Grotesk:wght@700&family=IBM+Plex+Sans:wght@500;600", css, body, grain=".09")


# ============ V7 quiz provocador ============
def v7(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#e0552d;color:#fff;font-family:'Work Sans',sans-serif}}
    .shape{{position:absolute;right:-220px;bottom:{250 if f else 420}px;width:620px;height:620px;border-radius:50%;background:#0f1d33;opacity:.14}}
    .eb{{font-weight:700;font-size:34px;letter-spacing:.14em;color:#0f1d33}}
    .q{{font-family:'Bricolage Grotesque';font-weight:800;font-size:{112 if f else 138}px;line-height:.95;letter-spacing:-.04em;margin:{20 if f else 28}px 0 {26 if f else 40}px}}
    .ans{{display:flex;flex-direction:column;gap:14px}}
    .a{{background:#0f1d33;color:#fff;border-radius:20px;padding:{22 if f else 28}px 30px;font-weight:700;font-size:{44 if f else 50}px;display:flex;justify-content:space-between;align-items:center}}
    .a span{{opacity:.6;font-weight:600;font-size:34px}}
    .sp{{flex:1}}
    .take{{font-family:'Bricolage Grotesque';font-weight:800;font-size:{62 if f else 70}px;line-height:1;margin:18px 0 12px}}
    .info{{font-weight:600;font-size:36px;line-height:1.25;margin-bottom:16px}}
    .lad{{display:flex;gap:12px;margin-bottom:18px}}
    .li{{flex:1;border:3px solid rgba(255,255,255,.7);border-radius:20px;padding:12px;text-align:center;display:flex;flex-direction:column}}
    .li .d{{font-weight:700;font-size:32px}} .li .n{{font-size:30px;opacity:.9}} .li b{{font-family:'Bricolage Grotesque';font-weight:800;font-size:64px;line-height:1.05}}
    .li.on{{background:#0f1d33;border-color:#0f1d33}}
    .cta{{background:#fff;color:#0f1d33;border-radius:999px;text-align:center;font-weight:800;font-size:50px;padding:22px}}
    """
    body = f"""<div class='shape'></div><div class='in'><div class='eb'>PREGUNTA PARA DUEÑOS DE NEGOCIO</div>
    <div class='q'>¿Tu negocio responde WhatsApp a las 11 pm?</div>
    <div class='ans'><div class='a'>Sí, respondo yo <span>A</span></div><div class='a'>No, se pierde la venta <span>B</span></div></div><div class='sp'></div>
    <div class='take'>Aprende a automatizarlo</div><div class='info'>Taller de IA · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Bricolage+Grotesque:wght@800&family=Work+Sans:wght@500;600;700;800", css, body, grain=".08")


# ============ V8 carta del fundador ============
def v8(fmt):
    f = fmt == "4x5"
    css = f"""
    body{{background:#dcdfd6;color:#17261f;font-family:'Manrope',sans-serif}}
    .paper{{position:absolute;left:54px;right:54px;top:{54 if f else 190}px;bottom:{54 if f else 280}px;background:#f1f2ec;box-shadow:0 30px 60px rgba(23,38,31,.22)}}
    .in{{padding-left:{120 if f else 130}px;padding-right:{120 if f else 130}px}}
    .eb{{font-weight:800;font-size:30px;letter-spacing:.2em;color:#9a2f27}}
    .l{{font-family:'Fraunces',serif;font-weight:500;font-size:{62 if f else 66}px;line-height:1.14;margin-top:26px;letter-spacing:-.01em}}
    .l b{{font-weight:700;background:linear-gradient(transparent 62%,rgba(154,47,39,.22) 62%)}}
    .sig{{font-family:'Fraunces',serif;font-style:italic;font-size:76px;margin-top:30px;color:#17261f}}
    .role{{font-weight:700;font-size:32px;color:#4b5f55;margin-top:2px}}
    .sp{{flex:1}}
    .info{{font-weight:700;font-size:36px;line-height:1.25;margin-bottom:14px}}
    .lad{{margin-bottom:16px;border-top:2px solid #17261f}}
    .li{{display:flex;gap:16px;align-items:baseline;font-size:36px;font-weight:700;padding:8px 0;border-bottom:2px solid rgba(23,38,31,.25)}}
    .li .d{{width:190px}} .li .n{{flex:1;font-weight:600;opacity:.7}} .li b{{font-family:'Fraunces';font-size:50px;font-weight:600}}
    .li.on{{color:#9a2f27}} .li.on .n{{opacity:1}}
    .cta{{background:#17261f;color:#f1f2ec;text-align:center;font-weight:800;font-size:46px;padding:22px}}
    """
    body = f"""<div class='paper'></div><div class='in'><div class='eb'>DE UN EMPRESARIO A OTRO</div>
    <div class='l'>Hola, soy Byron. Llevo <b>4 años</b> usando IA en empresas y ayudé a <b>más de 30</b>. En 3 días te enseño a usarla en la tuya.</div>
    <div class='sig'>Byron Cujano</div><div class='role'>Fundador CEO de AIUDA</div><div class='sp'></div>
    <div class='info'>Taller de IA · 21·22·23 OCT · 2 A 5 PM<br>Auditorio Fenatrape · Cupos limitados</div>{ladder()}<div class='cta'>Reserva tu cupo</div></div>"""
    return doc(fmt, "family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@600;700;800", css, body, grain=".06")


ADS = {"v1": v1, "v2": v2, "v3": v3, "v4": v4, "v5": v5, "v6": v6, "v7": v7, "v8": v8}


def render(vid, fmt):
    hp = os.path.join(HERE, f"_v_{vid}_{fmt}.html")
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
