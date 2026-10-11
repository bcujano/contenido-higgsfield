# Portada de Facebook: base Soul 3.01 (sin texto) + logo AIUDA Academy real compuesto encima.
# Salida 1640x624 (2x de 820x312, proporcion 2.63:1). Zona segura movil: centro 640/820 = 78% del ancho.
import numpy as np
from PIL import Image, ImageFilter
LOGO = r"C:\Users\BYROND~1\AppData\Local\Temp\claude\G--Other-computers-Workstation-DELL-DELL-BYRONCUJANO-Escritorio-Eccentric-Inc-AiUDA-PROYECTOS-HIGGSFIELD\2938b23d-181c-41b8-a6af-f333f9ae61b6\images\1.png"
base = Image.open("base_soul301.png").convert("RGB")      # 2048x1152
Y0 = 70
band = base.crop((0, Y0, 2048, Y0 + 779))                 # 2048x779 = 2.63:1
logo = Image.open(LOGO).convert("RGBA")
w = 640; h = int(logo.height * w / logo.width)
logo = logo.resize((w, h), Image.LANCZOS)
a = logo.split()[3].point(lambda v: int(v * 0.96))
logo.putalpha(a.filter(ImageFilter.GaussianBlur(0.6)))
x = 1290 - w // 2; y = 150
band = band.convert("RGBA"); band.alpha_composite(logo, (x, y)); band = band.convert("RGB")
# grano leve para integrar con la foto
arr = np.asarray(band).astype(np.float32)
arr += np.random.default_rng(1).normal(0, 2.2, arr.shape[:2])[..., None]
band = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
out = band.resize((1640, 624), Image.LANCZOS)
out.save("portada_facebook_aiuda_academy_1640x624.png")
out.resize((820, 312), Image.LANCZOS).save("portada_facebook_aiuda_academy_820x312.png")
print(logo.size, out.size)
