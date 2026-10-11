"""Poster estilo referencia (Byron recortado sobre kraft claro). Renderiza con Chrome headless."""
import subprocess, sys, pathlib
HERE = pathlib.Path(__file__).parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

VARIANTS = {  # recorte, centro horizontal de Byron y borde derecho util (px en foto 1536x2048)
    "foto4": dict(CUT="cut_9521d799.png", cx=765, shoes=(585, 920),
                  clip=[(0, 0), (1280, 0), (1075, 930), (1042, 960), (1042, 1120), (1000, 1140), (1000, 2048), (570, 2048), (570, 1290), (598, 1000), (574, 990), (574, 915), (0, 915)]),  # deja fuera la lampara
    "foto1": dict(CUT="cut_13b11378.png", cx=767, shoes=(505, 860), clip=None),
}
FORMATS = {
    "3x4": dict(w=1080, h=1440, S=0.50, top=0, shoe_y=712, TTY=64, NMY=70,
                N1Y=272, P1Y=408, CEY=610, N2Y=722, ROY=162, LIY=330, LIW=300,
                HY=680, HS=260, LS=66, LGAP=12, LABEL="Años de<br>experiencia<br><span>en IA</span>",
                TY=852, PHY=846, PHH=270, IY=1166, LOY=1300, CTAY=0, EXTRA=""),
    "9x16": dict(w=1080, h=1920, S=0.62, top=110, shoe_y=1000, TTY=110, NMY=116,
                 N1Y=340, P1Y=486, CEY=712, N2Y=834, ROY=212, LIY=392, LIW=290,
                 HY=960, HS=300, LS=70, LGAP=14, LABEL="Años de<br>experiencia<br><span>en IA</span>",
                 TY=1196, PHY=1186, PHH=290, IY=1530, LOY=1772, CTAY=1652,
                 EXTRA='<div class="a cta">Reserva tu cupo <span>por WhatsApp</span></div>'),
}

def build(name, v, fmt, f):
    S = f["S"]; pw, ph = round(1536 * S), round(2048 * S)
    vals = dict(PX=round(540 - v["cx"] * S), PY=f["top"], PW=pw, PH=ph, CUT=v["CUT"],
                CLIP=("polygon(" + ",".join(f"{x/1536*100:.2f}% {y/2048*100:.2f}%" for x, y in v["clip"]) + ")") if v["clip"] else "none",
                CX=round(540 + (v["shoes"][0] - v["cx"]) * S) - 20, CTY=f["shoe_y"],
                CWW=round((v["shoes"][1] - v["shoes"][0]) * S) + 40)
    vals.update({k: val for k, val in f.items() if k.isupper()})
    vals["H"] = f["h"]
    html = (HERE / "ref_poster.html").read_text(encoding="utf-8")
    for k, val in vals.items():
        html = html.replace("{" + k + "}", str(val))
    out_html = HERE / f"_ref_{name}_{fmt}.html"; out_html.write_text(html, encoding="utf-8")
    out_png = HERE / f"poster_ref_{name}_{fmt}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={f['w']},{f['h']}", "--force-device-scale-factor=1",
                    "--virtual-time-budget=8000", f"--screenshot={out_png}", out_html.as_uri()],
                   check=True, capture_output=True)
    print(out_png.name)

if __name__ == "__main__":
    only = sys.argv[1:]
    for name, v in VARIANTS.items():
        for fmt, f in FORMATS.items():
            if not only or name in only or fmt in only:
                build(name, v, fmt, f)
