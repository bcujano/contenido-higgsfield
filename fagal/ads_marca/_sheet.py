import sys
from PIL import Image
fmt = sys.argv[1]; ids = sys.argv[2:]
ims = [Image.open(f"salida/{i}_{fmt}.png").convert("RGB") for i in ids]
w, h = ims[0].size; s = 0.5 if fmt == "4x5" else 0.34
tw, th = int(w*s), int(h*s)
cols = 3; rows = (len(ims)+cols-1)//cols
sh = Image.new("RGB", (cols*tw+(cols+1)*10, rows*th+(rows+1)*10), (40, 40, 40))
for k, im in enumerate(ims):
    sh.paste(im.resize((tw, th), Image.LANCZOS), (10+(k % cols)*(tw+10), 10+(k//cols)*(th+10)))
sh.save(f"_sheet_{fmt}.png"); print(sh.size)
