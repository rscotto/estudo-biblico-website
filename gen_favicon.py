"""
Generates favicon.ico for estudo-biblico-website.
Design: "EB" monogram. Uses ImageFont to render real text, falling back
to a clean geometric approach if no suitable serif font is found.
Colors: navy #2c2416, gold #FFA400, gold-dim border #cc8500.
Sizes: 256, 64, 48, 32, 16.
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys, glob

NAVY   = (44,  36,  22,  255)
GOLD   = (255, 164,   0, 255)
GOLD2  = (204, 133,   0, 255)
TRANSP = (0,   0,    0,   0)

# ── locate a serif font on Windows ──────────────────────────────────────────
SERIF_CANDIDATES = [
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\georgiai.ttf",
    r"C:\Windows\Fonts\times.ttf",
    r"C:\Windows\Fonts\timesnr.ttf",
    r"C:\Windows\Fonts\cambria.ttc",
    r"C:\Windows\Fonts\palatino.ttf",
    r"C:\Windows\Fonts\palatab.ttf",   # Palatino Bold
    r"C:\Windows\Fonts\bkant.ttf",     # Book Antiqua
    r"C:\Windows\Fonts\BKANT.TTF",
]

def find_font():
    for p in SERIF_CANDIDATES:
        if os.path.exists(p):
            return p
    # last resort: any .ttf in Windows Fonts
    hits = glob.glob(r"C:\Windows\Fonts\*.ttf")
    return hits[0] if hits else None


def make_frame(size):
    img  = Image.new("RGBA", (size, size), TRANSP)
    draw = ImageDraw.Draw(img)

    # rounded-square background
    r = max(4, size // 7)
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=r, fill=NAVY)

    # thin gold border
    bw = max(1, size // 52)
    draw.rounded_rectangle(
        [bw, bw, size-1-bw, size-1-bw],
        radius=max(2, r-bw),
        outline=GOLD2,
        width=bw,
    )

    # render "EB" text
    font_path = find_font()
    rendered  = False

    if font_path and size >= 32:
        try:
            # try loading at a large point size then scale
            pt = int(size * 0.58)
            font = ImageFont.truetype(font_path, pt)

            # measure combined text
            text = "EB"
            bbox = font.getbbox(text)
            tw   = bbox[2] - bbox[0]
            th   = bbox[3] - bbox[1]

            # centre in canvas with slight upward nudge
            tx = (size - tw) // 2 - bbox[0]
            ty = (size - th) // 2 - bbox[1] - round(size * 0.03)

            # subtle shadow / depth
            shadow_offset = max(1, size // 64)
            draw.text((tx + shadow_offset, ty + shadow_offset), text,
                      font=font, fill=GOLD2)
            draw.text((tx, ty), text, font=font, fill=GOLD)
            rendered = True
        except Exception as e:
            print(f"  font render failed ({e}), using geometric fallback")

    if not rendered:
        # geometric fallback for very small sizes or missing font
        _draw_eb_geometric(draw, size, GOLD)

    return img


def _draw_eb_geometric(draw, S, color):
    """Simple block-letter EB for small sizes or font fallback."""
    top = round(S * 0.18)
    bot = round(S * 0.82)
    sw  = max(1, round(S * 0.07))

    # E  (left half: x 0.09 .. 0.46)
    ex0 = round(S * 0.09)
    ex1 = round(S * 0.46)
    mid = (top + bot) // 2 - sw // 2
    draw.rectangle([ex0,      top,       ex0 + sw, bot       ], fill=color)
    draw.rectangle([ex0,      top,       ex1,      top + sw  ], fill=color)
    draw.rectangle([ex0,      mid,       round(S*0.42), mid+sw], fill=color)
    draw.rectangle([ex0,      bot - sw,  ex1,      bot       ], fill=color)

    # B  (right half: x 0.54 .. 0.91)
    bx0 = round(S * 0.54)
    bx1 = round(S * 0.91)
    draw.rectangle([bx0,      top,       bx0 + sw, bot       ], fill=color)
    draw.rectangle([bx0,      top,       bx1,      top + sw  ], fill=color)
    draw.rectangle([bx0,      mid,       round(bx1*0.96), mid+sw], fill=color)
    draw.rectangle([bx0,      bot - sw,  bx1,      bot       ], fill=color)
    # upper bump
    draw.arc([bx0 + sw, top + sw, bx1, mid], start=270, end=90,
             fill=color, width=sw)
    # lower bump (slightly wider)
    bx1b = bx1 + round(S * 0.03)
    draw.arc([bx0 + sw, mid, bx1b, bot - sw], start=270, end=90,
             fill=color, width=sw)


def make_ico(out_path):
    sizes  = [256, 64, 48, 32, 16]
    frames = []
    for s in sizes:
        print(f"  rendering {s}x{s} ...")
        frames.append(make_frame(s))

    frames[0].save(
        out_path,
        format="ICO",
        sizes=[(s, s) for s in sizes],
        append_images=frames[1:],
    )
    print(f"Saved: {out_path}  ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    ico  = os.path.join(base, "astro-site", "public", "favicon.ico")
    prev = os.path.join(base, "favicon_preview.png")

    font_path = find_font()
    print(f"Font: {font_path or 'none found — using geometric fallback'}")

    make_ico(ico)

    preview = make_frame(512)
    preview.save(prev, "PNG")
    print(f"Preview: {prev}")
