#!/usr/bin/env python3
"""Auto-crop images by removing blank/transparent space around content.

Usage:
    python3 crop_image.py <input> [-o output.png] [-p padding] [-bg BGCOLOR] [--fuzz FUZZ]
"""

import argparse
import sys

try:
    from PIL import Image, ImageColor
except ImportError:
    print("Error: Pillow is not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def parse_color(color_str):
    """Parse a color string into an RGBA tuple."""
    if color_str.lower() == "transparent":
        return (0, 0, 0, 0)
    try:
        rgba = ImageColor.getrgb(color_str)
        if len(rgba) == 3:
            return rgba + (255,)
        return rgba
    except (ValueError, AttributeError):
        raise ValueError(f"Unrecognized color: {color_str!r}")


def colors_match(c1, c2, fuzz):
    """Check if two RGBA colors match within a fuzz tolerance (0-255)."""
    # If both pixels are fully transparent, they match regardless of RGB
    if len(c1) >= 4 and len(c2) >= 4 and c1[3] == 0 and c2[3] == 0:
        return True
    # If background is transparent, any pixel with alpha=0 matches
    if len(c2) >= 4 and c2[3] == 0 and len(c1) >= 4 and c1[3] <= fuzz:
        return True
    return all(abs(a - b) <= fuzz for a, b in zip(c1, c2))


def find_content_bbox(img, bg_color, fuzz):
    """Find the bounding box of non-background content.

    Returns (left, top, right, bottom) or None if the image is entirely background.
    """
    pixels = img.load()
    w, h = img.size

    top = None
    bottom = None
    left = w
    right = 0

    for y in range(h):
        row_has_content = False
        for x in range(w):
            px = pixels[x, y]
            if not colors_match(px, bg_color, fuzz):
                row_has_content = True
                if x < left:
                    left = x
                if x > right:
                    right = x
        if row_has_content:
            if top is None:
                top = y
            bottom = y

    if top is None:
        return None

    return (left, top, right + 1, bottom + 1)


def auto_detect_background(img):
    """Detect background color by checking the four corners."""
    pixels = img.load()
    w, h = img.size

    corners = [
        pixels[0, 0],
        pixels[w - 1, 0],
        pixels[0, h - 1],
        pixels[w - 1, h - 1],
    ]

    # If image has alpha and corners are transparent, background is transparent
    if img.mode == "RGBA":
        transparent_corners = sum(1 for c in corners if c[3] == 0)
        if transparent_corners >= 3:
            return (0, 0, 0, 0)

    # Otherwise use the most common corner color
    from collections import Counter
    most_common = Counter(corners).most_common(1)[0][0]
    return most_common


def crop_image(img, bg_color=None, padding=0, fuzz=0):
    """Crop blank/transparent space from an image.

    Args:
        img: PIL Image.
        bg_color: Background color to trim as RGBA tuple. Auto-detected if None.
        padding: Pixels of padding to keep around content.
        fuzz: Color matching tolerance (0-255).

    Returns:
        Cropped PIL Image.
    """
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    if bg_color is None:
        bg_color = auto_detect_background(img)

    bbox = find_content_bbox(img, bg_color, fuzz)

    if bbox is None:
        print("Warning: Image appears to be entirely background. Returning original.", file=sys.stderr)
        return img

    left, top, right, bottom = bbox

    # Apply padding
    w, h = img.size
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(w, right + padding)
    bottom = min(h, bottom + padding)

    cropped = img.crop((left, top, right, bottom))

    original_pixels = w * h
    cropped_pixels = cropped.size[0] * cropped.size[1]
    removed_pct = (1 - cropped_pixels / original_pixels) * 100

    print(f"Original: {w}x{h}", file=sys.stderr)
    print(f"Cropped:  {cropped.size[0]}x{cropped.size[1]}", file=sys.stderr)
    print(f"Removed:  {removed_pct:.1f}% of blank space", file=sys.stderr)

    return cropped


def main():
    parser = argparse.ArgumentParser(
        description="Auto-crop blank/transparent space from images."
    )
    parser.add_argument(
        "input",
        help="Path to input image file",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output file path (default: overwrites input)",
    )
    parser.add_argument(
        "-p", "--padding",
        type=int,
        default=0,
        help="Pixels of padding to keep around content (default: 0)",
    )
    parser.add_argument(
        "-bg", "--background",
        default=None,
        help="Background color to trim (default: auto-detect from corners). "
             "Use 'transparent', hex (#RRGGBB), or CSS color name.",
    )
    parser.add_argument(
        "--fuzz",
        type=int,
        default=10,
        help="Color matching tolerance 0-255 (default: 10). "
             "Higher values treat near-background colors as background too.",
    )

    args = parser.parse_args()

    img = Image.open(args.input)

    bg_color = None
    if args.background:
        bg_color = parse_color(args.background)

    cropped = crop_image(img, bg_color=bg_color, padding=args.padding, fuzz=args.fuzz)

    output_path = args.output or args.input
    cropped.save(output_path, "PNG")
    print(f"Saved {output_path} ({cropped.size[0]}x{cropped.size[1]}px)")


if __name__ == "__main__":
    main()
