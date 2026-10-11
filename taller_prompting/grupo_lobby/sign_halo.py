# Letrero "halo lit" (letras oscuras con grosor y luz blanco-azulada trasera), como la referencia Adidas Outlet.
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

def sign_halo(base, out, cx, cy, width, depth=12, logo="logo_negro.png", glow_col=(235, 245, 255)):
    bg = Image.open(base).convert("RGBA")
    lg = Image.open(logo).convert("RGBA")
    w = width * 2
    h = round(lg.height * w / lg.width)
    big = lg.resize((w, h), Image.LANCZOS)
    a = big.getchannel("A").filter(ImageFilter.GaussianBlur(3.0))
    a = a.point(lambda v: 0 if v < 90 else (255 if v > 170 else int((v - 90) * 255 / 80)))
    big.putalpha(a)
    W, H = big.size
    pad = 220
    cv = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))
    # luz trasera: color solido, solo el alfa se difumina (evita que el color se oscurezca)
    base_mask = Image.new("L", cv.size, 0); base_mask.paste(a, (pad, pad))
    for blur, op in ((8, 1.0), (26, 0.95), (64, 0.75)):
        m = base_mask.filter(ImageFilter.GaussianBlur(blur)).point(lambda v, op=op: int(min(255, v * 3.2) * op))
        layer = Image.new("RGBA", cv.size, glow_col + (255,)); layer.putalpha(m)
        cv.alpha_composite(layer)
    # grosor oscuro hacia abajo-derecha
    side = ImageEnhance.Brightness(big).enhance(0.45)
    side.putalpha(a)
    d = depth * 2
    for i in range(d, 0, -1):
        cv.alpha_composite(side, (pad + round(i * 0.55), pad + round(i * 0.85)))
    # cara frontal: texto oscuro casi negro, remolino a color
    arr = np.array(big).astype(np.float32)
    arr[..., :3] = np.clip(arr[..., :3] * 0.92, 0, 255)
    cv.alpha_composite(Image.fromarray(arr.astype(np.uint8), "RGBA"), (pad, pad))
    cv = cv.resize((cv.width // 2, cv.height // 2), Image.LANCZOS)
    bg.alpha_composite(cv, (cx - cv.width // 2, cy - cv.height // 2))
    bg.convert("RGB").save(out, quality=95)
