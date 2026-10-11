# Juego final con las fotos aprobadas por el usuario (A2 A3 A4 A8 A10 B1 B2 B3 B4 B5 B8 B10).
# Uso: FASE=1 python render_final.py   |   FASE=2 python render_final.py
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_ads as ra
import render_ads2 as ra2

HERE = ra.HERE
FASE = ra.FASE
OUT = os.path.join(HERE, "juego_campana_final", "fase1_hasta-5-oct" if FASE == "1" else "fase2_5-al-15-oct")
FOTOS = os.path.join(HERE, "fotos_para_elegir")

# nombre: (funcion, foto 4x5, foto 9x16)
DESIGNS = {
    "01_hoja-de-ruta_chatgpt-a-web": (ra2.s1, "A4", "B5"),
    "02_creencia-rota_chatgpt-como-google": (ra2.s2, "A2", "B2"),
    "03_checklist_3-dias-3-cosas_emprendedores": (ra2.s3, "A8", "B8"),
    "04_precio-sube-cada-semana": (ra2.s4, "A10", "B10"),
    "05_nota-iphone_duenos-de-negocio": (ra.c2, "A3", "B4"),
    "06_chat-whatsapp_empresarios": (ra.c3, None, "B1"),
    "07_pregunta-directa_que-le-pedirias-a-la-ia": (ra2.s5, None, "B3"),
}


def shot(html_path, out, H):
    subprocess.run([ra.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size=1080,{H}", "--virtual-time-budget=12000", f"--screenshot={out}",
                    "file:///" + html_path.replace("\\", "/")], check=True, capture_output=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1:]
    for name, (fn, p45, p916) in DESIGNS.items():
        if only and not any(o in name for o in only):
            continue
        for fmt, photo in (("4x5", p45), ("9x16", p916)):
            if not photo:
                continue
            img = "file:///" + os.path.join(FOTOS, photo + ".png").replace("\\", "/")
            hp = os.path.join(HERE, f"_f_{name[:2]}_{fmt}.html")
            with open(hp, "w", encoding="utf-8") as f:
                f.write(fn(fmt, img))
            out = os.path.join(OUT, f"{name}_{fmt}_{photo}.png")
            shot(hp, out, 1350 if fmt == "4x5" else 1920)
            print(out)
