from PIL import Image, ImageDraw
import math
def icon(size, path, pad=0.0):
    S = 4*size
    im = Image.new("RGB", (S, S), (6, 10, 18))
    d = ImageDraw.Draw(im)
    c = S/2
    def circ(r, **kw): d.ellipse([c-r, c-r, c+r, c+r], **kw)
    cy, am = (94, 231, 255), (255, 196, 107)
    sc = 1 - pad
    nodes = []
    for i in range(5):
        a = -math.pi/2 + i*2*math.pi/5
        nodes.append((c + math.cos(a)*S*0.30*sc, c + math.sin(a)*S*0.30*sc))
    for x, y in nodes:
        d.line([c, c, x, y], fill=(60, 120, 140), width=int(S*0.012))
    d.line([nodes[0], nodes[2]], fill=am, width=int(S*0.022))
    circ(S*0.12*sc, fill=(20, 70, 90), outline=cy, width=int(S*0.014))
    for x, y in nodes:
        r = S*0.055*sc
        d.ellipse([x-r, y-r, x+r, y+r], fill=(16, 27, 47), outline=cy, width=int(S*0.012))
    im.resize((size, size), Image.LANCZOS).save(path)
icon(180, "apple-touch-icon.png")
icon(192, "icon-192.png")
icon(512, "icon-512.png")
icon(512, "icon-maskable-512.png", pad=0.2)
