import glob, os
from PIL import Image, ImageDraw
fs = sorted(glob.glob('_frames/*.jpg')); cols = 8; tw, th = 225, 300
rows = (len(fs)+cols-1)//cols
sh = Image.new('RGB', (cols*(tw+6)+6, rows*(th+6)+6), (25, 25, 25)); d = ImageDraw.Draw(sh)
for k, f in enumerate(fs):
    im = Image.open(f).convert('RGB'); im.thumbnail((tw, th)); x = 6+(k % cols)*(tw+6); y = 6+(k//cols)*(th+6)
    sh.paste(im, (x, y)); d.rectangle((x, y, x+78, y+20), fill=(0, 0, 0)); d.text((x+4, y+4), os.path.basename(f)[:-4], fill=(255, 255, 0))
sh.save('_frames_sheet.png'); print(sh.size)
