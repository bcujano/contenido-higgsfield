# Letrero 3D realista: logo con grosor, sombra sobre el muro y halo de luz trasera. Uso: sign3d(base, out, cx, cy, ancho)
import sys
from PIL import Image, ImageFilter, ImageChops, ImageEnhance
import numpy as np

def sign3d(base, out, cx, cy, width, depth=16, lx=0.55, ly=0.85, shadow=(26, 34), halo=0.30):
    bg = Image.open(base).convert("RGBA")
    lg = Image.open("logo_blanco.png").convert("RGBA")
    S = 4
    w = width * 2
    h = round(lg.height * w / lg.width)
    big = lg.resize((w, h), Image.LANCZOS)  # 2x sobre el ancho final (supermuestreo)
    # bordes mas limpios: suaviza y endurece el alfa
    a = big.getchannel("A").filter(ImageFilter.GaussianBlur(2.2))
    a = a.point(lambda v: 0 if v < 70 else (255 if v > 190 else int((v - 70) * 255 / 120)))
    big.putalpha(a)
    W, H = big.size
    pad = 160
    canvas = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))
    # sombra proyectada sobre el muro
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    black = Image.new("RGBA", big.size, (0, 0, 0, 255)); black.putalpha(a)
    sh.alpha_composite(black, (pad + shadow[0] * 2, pad + shadow[1] * 2))
    sh = sh.filter(ImageFilter.GaussianBlur(26))
    sh.putalpha(sh.getchannel("A").point(lambda v: int(v * 0.55)))
    # halo de luz trasera
    ha = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    glow = Image.new("RGBA", big.size, (255, 226, 190, 255)); glow.putalpha(a)
    ha.alpha_composite(glow, (pad, pad))
    ha = ha.filter(ImageFilter.GaussianBlur(34))
    ha.putalpha(ha.getchannel("A").point(lambda v: int(v * halo)))
    canvas.alpha_composite(ha)
    canvas.alpha_composite(sh)
    # extrusion (cara lateral mas oscura)
    side = ImageEnhance.Brightness(big.convert("RGBA")).enhance(0.62)
    side.putalpha(a)
    d = depth * 2
    for i in range(d, 0, -1):
        canvas.alpha_composite(side, (pad + round(i * lx), pad + round(i * ly)))
    # cara frontal con leve brillo superior
    front = big.copy()
    arr = np.array(front).astype(np.float32)
    grad = np.linspace(1.04, 0.93, H)[:, None, None]
    arr[..., :3] = np.clip(arr[..., :3] * grad, 0, 255)
    front = Image.fromarray(arr.astype(np.uint8), "RGBA")
    canvas.alpha_composite(front, (pad, pad))
    # a tamano final
    fw = canvas.width // 2
    fh = canvas.height // 2
    canvas = canvas.resize((fw, fh), Image.LANCZOS)
    bg.alpha_composite(canvas, (cx - fw // 2, cy - fh // 2))
    bg.convert("RGB").save(out, quality=95)

if __name__ == "__main__":
    sign3d("M2_base.png", "M2_letrero3d.png", 900, 215, 540, depth=9, shadow=(14, 20))
