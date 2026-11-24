"""Draw the news-image-20261124 front page (1024x1024 PNG) with PIL.

Written fresh for Tuesday 24 November 2026's news. Flat vector style:
a masthead with the date, one hero story (Russian jets near Ulleung
Island), a 2x2 grid of four more stories, and an "also today" ticker.
Layout differs from earlier days on purpose: the hero's text sits on
the left with its illustration on the right, and each grid card's icon
box sits on the right. No photos, no screenshots, no copied artwork.
Run:  python3 draw.py  ->  entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
NAVY2 = (28, 46, 84)
GOLD = (252, 163, 17)
RED = (193, 18, 31)
INK = (25, 25, 25)
GREY = (70, 70, 70)
CARD = (255, 255, 255)
BORDER = (200, 196, 186)
SEA = (24, 68, 110)
SKY = (214, 231, 240)
GREEN = (82, 183, 136)
TEAL = (0, 90, 140)

FONT_DIR = "/home/hatch/workspace/custom-skills/video-animasi-ringan/fonts/"
XB = FONT_DIR + "Montserrat-ExtraBold.ttf"
B = FONT_DIR + "Montserrat-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, f, color, leading=None):
    if leading is None:
        leading = int(f.size * 1.25)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=color)
        y += leading
    return y


def fit_lines(d, text, f, max_w, max_lines):
    """Wrap text; shrink the font until it fits max_lines (min 60% size)."""
    size = f.size
    while size > int(f.size * 0.6):
        lines = wrap(d, text, f, max_w)
        if len(lines) <= max_lines:
            return lines, f
        size -= 2
        f = font(f.path, size)
    return wrap(d, text, f, max_w)[:max_lines], f


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((W // 2, 26), "THE WORLD TODAY", font=font(XB, 62), fill=(255, 255, 255), anchor="ma")
d.text((W // 2, 100), "TUESDAY  24  NOVEMBER  2026", font=font(B, 30), fill=GOLD, anchor="ma")
d.rectangle([0, 148, W, 156], fill=RED)

# ---------- hero: Russian jets near Ulleung Island ----------
hx0, hy0, hx1, hy1 = 28, 168, 996, 470
d.rectangle([hx0, hy0, hx1, hy1], fill=CARD, outline=BORDER, width=2)
# illustration panel, right side: sea, island, radar rings, jets, alert
ax0, ay0, ax1, ay1 = 648, hy0 + 2, hx1 - 2, hy1 - 2
d.rectangle([ax0, ay0, ax1, ay1], fill=SKY)
d.rectangle([ax0, ay1 - 108, ax1, ay1], fill=SEA)
# radar rings centred on the island
icx, icy = 822, ay1 - 108
for r, wd in ((118, 2), (84, 2), (50, 2)):
    d.ellipse([icx - r, icy - r, icx + r, icy + r], outline=(255, 255, 255), width=wd)
# island: green hill rising out of the sea
d.polygon([(icx - 110, ay1 - 108), (icx - 52, ay1 - 196), (icx + 8, ay1 - 150),
           (icx + 62, ay1 - 188), (icx + 118, ay1 - 108)], fill=GREEN)
d.polygon([(icx - 52, ay1 - 196), (icx - 34, ay1 - 168), (icx - 62, ay1 - 158)],
          fill=(255, 255, 255))
# two jet silhouettes, top right
for jx, jy, s in ((700, 236, 1.0), (760, 206, 0.8)):
    d.polygon([(jx, jy), (jx + 58 * s, jy - 12 * s), (jx + 74 * s, jy - 4 * s),
               (jx + 58 * s, jy + 6 * s), (jx + 16 * s, jy + 10 * s)], fill=NAVY)
    d.polygon([(jx + 58 * s, jy - 12 * s), (jx + 70 * s, jy - 22 * s),
               (jx + 66 * s, jy - 2 * s)], fill=NAVY)
# red alert triangle with "!" over the island
tx, ty = 700, 300
d.polygon([(tx, ty - 42), (tx + 44, ty + 30), (tx - 44, ty + 30)],
          fill=RED, outline=(255, 255, 255), width=3)
d.text((tx, ty - 4), "!", font=font(XB, 44), fill=(255, 255, 255), anchor="mm")
# hero text, left side
tx0 = 52
d.text((tx0, hy0 + 22), "KOREA  ·  ULLEUNG ISLAND", font=font(B, 21), fill=RED)
d.text((tx0, hy0 + 56), "RUSSIAN JETS SPARK", font=font(XB, 52), fill=NAVY)
d.text((tx0, hy0 + 114), "AIR-RAID ALERT", font=font(XB, 52), fill=NAVY)
deck = ("Several Russian warplanes enter the air-defence zone; islanders "
        "are told to take shelter as Seoul scrambles jets.")
lines, _ = fit_lines(d, deck, font(B, 23), 620 - tx0 - 24, 4)
text_block(d, tx0, hy0 + 192, lines, font(B, 23), GREY, leading=30)

# ---------- 2x2 grid (icon box on the right of each card) ----------
cards = [
    # (kicker, headline, deck, accent, icon)
    ("IRAN  ·  TEHRAN", "Tehran demands $290bn from US",
     "Courts award damages over decades of US actions; Iran vows to "
     "break the naval blockade.",
     RED, "scales"),
    ("INDONESIA  ·  BANTEN", "26 dead named, 28 still missing",
     "Bodies identified after the candy factory fire; the search goes "
     "on at the Cikande plant.",
     (200, 90, 0), "flame"),
    ("NVIDIA  ·  SILICON VALLEY", "Huang back at Nvidia; shares soar",
     "Board reinstates its CEO after Trump pressure; the US blacklists "
     "Megaspeed the same day.",
     (0, 110, 60), "chip"),
    ("MEXICO  ·  MEXICO CITY", "El Chapo Isidro to be tried at home",
     "Mexico refuses the US extradition request for the captured cartel "
     "boss.",
     (0, 80, 160), "court"),
]
gx, gy = 28, 486
cw, chh, gap = 476, 186, 16
for i, (kicker, head, deck, accent, icon) in enumerate(cards):
    x0 = gx + (i % 2) * (cw + gap)
    y0 = gy + (i // 2) * (chh + gap)
    x1, y1 = x0 + cw, y0 + chh
    d.rectangle([x0, y0, x1, y1], fill=CARD, outline=BORDER, width=2)
    d.rectangle([x0, y0, x1, y0 + 6], fill=accent)
    # icon box, right side
    ix0, iy0, ix1, iy1 = x1 - 128, y0 + 22, x1 - 14, y0 + chh - 14
    d.rectangle([ix0, iy0, ix1, iy1], fill=(238, 238, 234))
    icx, icy = (ix0 + ix1) // 2, (iy0 + iy1) // 2
    if icon == "scales":
        # balance scales: beam, two pans, centre post
        d.rectangle([icx - 3, icy - 44, icx + 3, icy + 34], fill=(60, 60, 60))
        d.line([(icx - 44, icy - 40), (icx + 44, icy - 40)], fill=(60, 60, 60), width=5)
        d.polygon([(icx - 44, icy - 40), (icx - 58, icy - 6), (icx - 30, icy - 6)],
                  outline=(60, 60, 60))
        d.polygon([(icx + 44, icy - 40), (icx + 58, icy - 6), (icx + 30, icy - 6)],
                  outline=(60, 60, 60))
        d.ellipse([icx - 56, icy - 12, icx - 32, icy + 2], fill=GOLD)
        d.ellipse([icx + 32, icy - 12, icx + 56, icy + 2], fill=GOLD)
        d.rectangle([icx - 26, iy1 - 12, icx + 26, iy1 - 8], fill=(60, 60, 60))
    elif icon == "flame":
        # flame shape
        d.polygon([(icx, icy - 52), (icx + 26, icy - 18), (icx + 40, icy + 6),
                   (icx + 30, icy + 40), (icx - 6, icy + 52), (icx - 34, icy + 38),
                   (icx - 40, icy + 2), (icx - 22, icy - 26)], fill=(255, 120, 40))
        d.polygon([(icx, icy - 6), (icx + 16, icy + 14), (icx + 10, icy + 34),
                   (icx - 12, icy + 34), (icx - 16, icy + 12)], fill=GOLD)
    elif icon == "chip":
        # microchip with pins
        d.rectangle([icx - 34, icy - 34, icx + 34, icy + 34], fill=NAVY2)
        d.rectangle([icx - 18, icy - 18, icx + 18, icy + 18], fill=GOLD)
        for px in (-22, 0, 22):
            d.rectangle([icx + px - 3, icy - 46, icx + px + 3, icy - 34], fill=NAVY)
            d.rectangle([icx + px - 3, icy + 34, icx + px + 3, icy + 46], fill=NAVY)
        for py in (-22, 0, 22):
            d.rectangle([icx - 46, icy + py - 3, icx - 34, icy + py + 3], fill=NAVY)
            d.rectangle([icx + 34, icy + py - 3, icx + 46, icy + py + 3], fill=NAVY)
    else:  # court: columns under a pediment
        d.polygon([(icx - 48, icy - 34), (icx, icy - 52), (icx + 48, icy - 34)],
                  fill=(200, 200, 195), outline=NAVY, width=2)
        d.rectangle([icx - 44, icy - 28, icx + 44, icy - 20], fill=(200, 200, 195))
        for cxp in (-36, -13, 10, 33):
            d.rectangle([icx + cxp, icy - 16, icx + cxp + 8, iy1 - 16], fill=(160, 160, 155))
        d.rectangle([icx - 48, iy1 - 16, icx + 48, iy1 - 8], fill=(200, 200, 195))
    # card text, left side
    tx = x0 + 16
    tw = ix0 - tx - 12
    d.text((tx, y0 + 20), kicker, font=font(B, 16), fill=accent)
    hlines, _ = fit_lines(d, head, font(XB, 25), tw, 2)
    y = text_block(d, tx, y0 + 46, hlines, font(XB, 25), NAVY, leading=30)
    dlines, _ = fit_lines(d, deck, font(B, 17), tw, 3)
    text_block(d, tx, y + 4, dlines, font(B, 17), GREY, leading=22)

# ---------- ticker ----------
ty0, ty1 = 890, 996
d.rectangle([0, ty0, W, ty1], fill=NAVY)
d.text((28, ty0 + 14), "ALSO TODAY", font=font(XB, 22), fill=GOLD)
tick = ("Colombia: 23 hurt as car bomb hits the Meta governor's office  ·  "
        "UN chief calls for global AI rules within a year  ·  "
        "Final Spain polls put PP+Vox ahead for the 29 Nov vote")
tlines, _ = fit_lines(d, tick, font(B, 21), W - 56, 3)
text_block(d, 28, ty0 + 44, tlines, font(B, 21), (255, 255, 255), leading=27)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
