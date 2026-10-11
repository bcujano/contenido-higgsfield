import re, pathlib, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

SRC = pathlib.Path('FAGAL_FG_logo_vector.svg').read_text(encoding='utf-8')
MONO_D = re.search(r'<path[^>]*\sd="([^"]+)"', SRC).group(1)
VBW, VBH = 1975.108, 1238.135
font = TTFont(r'C:\Windows\Fonts\timesbd.ttf'); gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font['head'].unitsPerEm

def text_path(txt, size, x, y, tracking=0.0):
    """Devuelve (d, ancho) con el texto convertido a curvas. y = linea base."""
    s = size / upm; pen = SVGPathPen(gs); cx = x
    for ch in txt:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[g].draw(tp)
        cx += gs[g].width * s + tracking * size
    return pen.getCommands(), cx - x - tracking * size

def width(txt, size, tracking=0.0):
    s = size / upm
    return sum(gs[cmap[ord(c)]].width * s for c in txt) + tracking * size * (len(txt) - 1)

def svg(w, h, body, color, name):
    out = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}">'
           f'<g fill="{color}">{body}</g></svg>')
    pathlib.Path(name).write_text(out, encoding='utf-8')

mono = f'<path d="{MONO_D}"/>'
for tone, color in (('blanco', '#FFFFFF'), ('negro', '#000000')):
    # monograma solo
    svg(VBW, VBH, mono, color, f'FAGAL_monograma_{tone}.svg')
    # vertical: monograma arriba, FAGAL y ABOGADOS centrados (mismo tamano de letra)
    size = 560; trk = 0.02
    wF = width('FAGAL', size, trk); wA = width('ABOGADOS', size, trk)
    W = max(VBW, wA) + 0; ox = (W - VBW) / 2
    y1 = VBH + 120 + size * 0.66; y2 = y1 + size * 0.66 + 70
    dF, _ = text_path('FAGAL', size, (W - wF) / 2, y1, trk); dA, _ = text_path('ABOGADOS', size, (W - wA) / 2, y2, trk)
    H = y2 + 30
    svg(W, H, f'<g transform="translate({ox:.1f},0)">{mono}</g><path d="{dF}"/><path d="{dA}"/>', color, f'FAGAL_logo_vertical_{tone}.svg')
    # horizontal: monograma a la izquierda, texto a la derecha
    size = 470; trk = 0.03
    gx = VBW + 150; cap = size * 0.66
    block = cap * 2 + 90; top = (VBH - block) / 2
    dF, wf = text_path('FAGAL', size, gx, top + cap, trk); dA, wa = text_path('ABOGADOS', size, gx, top + cap * 2 + 90, trk)
    W = gx + max(wf, wa) + 10
    svg(W, VBH, f'{mono}<path d="{dF}"/><path d="{dA}"/>', color, f'FAGAL_logo_horizontal_{tone}.svg')
print('ok')
