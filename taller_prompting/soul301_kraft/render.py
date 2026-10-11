"""Rellena las plantillas HTML por foto y renderiza PNG con Chrome headless."""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# escala de la foto 1536x2048 y borde izquierdo de Byron por formato

VARIANTS = {
    "foto4": dict(PHOTO="v_9521d799.png", CUT="cut_9521d799.png", byron_left=465),
    "foto1": dict(PHOTO="v_13b11378.png", CUT="cut_13b11378.png", byron_left=488),
}

FORMATS = {
    "9x16": dict(tpl="poster_9x16.html", w=1080, h=1920, PY=400, FADEB=360,
                 NX=700, NY=318, CY=452, CW=480, PIX=826, PIY=1100, S=0.62, BX=560),
    "3x4": dict(tpl="poster_3x4.html", w=1080, h=1440, PY=298, FADEB=300,
                NX=560, NY=262, CY=356, CW=570, PIX=844, PIY=124, S=0.44, BX=646),
}


def build(name, v, fmt, f):
    S = f["S"]
    pw, ph = round(1536 * S), round(2048 * S)
    px = round(f["BX"] - v["byron_left"] * S)
    vals = dict(PX=px, PY=f["PY"], PW=pw, PH=ph, FADEB=f["FADEB"], FADEL0=round(40 * S / 0.62), FADEL1=round(330 * S / 0.62),
                NX=f["NX"], NY=f["NY"], CY=f["CY"], CW=f["CW"], PIX=f["PIX"], PIY=f["PIY"],
                PHOTO=v["PHOTO"], CUT=v["CUT"])
    html = (HERE / f["tpl"]).read_text(encoding="utf-8")
    for k, val in vals.items():
        html = html.replace("{" + k + "}", str(val))
    out_html = HERE / f"_{name}_{fmt}.html"
    out_html.write_text(html, encoding="utf-8")
    out_png = HERE / f"poster_kraft_{name}_{fmt}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={f['w']},{f['h']}", "--force-device-scale-factor=1",
                    "--virtual-time-budget=8000", f"--screenshot={out_png}",
                    out_html.as_uri()], check=True, capture_output=True)
    print(out_png.name)


if __name__ == "__main__":
    only = sys.argv[1:]
    for name, v in VARIANTS.items():
        for fmt, f in FORMATS.items():
            if not only or name in only or fmt in only:
                build(name, v, fmt, f)
