# Image Cropper Plugin for Claude Code

Auto-crop images by removing blank or transparent space around content.

```
You: "Crop the whitespace from screenshot.png"
Claude: *trims blank space and shows the result*
```

---

## Quick Start

**1. Add the marketplace**

```bash
/plugin marketplace add thejacedev/claude-code-skills
```

**2. Install the plugin**

```bash
/plugin install img-cropper@thejacedev-skills
```

**3. Install the dependency**

```bash
pip install Pillow
```

**4. Go**

Open Claude Code and ask it to crop or trim an image. That's it.

---

## What It Does

This plugin adds a skill that lets Claude Code auto-crop images. When you ask to trim an image, Claude will:

1. Auto-detect the background color from the image corners
2. Find the tightest bounding box around the actual content
3. Crop the image and save it
4. Show you the result with before/after dimensions

## Options

| Parameter | Values | Default |
|-----------|--------|---------|
| **Padding** | Any positive integer (px) | `0` |
| **Background** | `transparent`, hex, CSS color name | Auto-detect |
| **Fuzz** | `0`-`255` tolerance | `10` |

## Trigger Phrases

The skill activates when you say things like:

- *"Crop the whitespace from..."*
- *"Trim this image..."*
- *"Remove blank space from..."*
- *"Auto-crop this PNG..."*
- *"Remove the transparent border..."*

## Standalone Script Usage

```bash
python3 scripts/crop_image.py input.png -o cropped.png -p 5 --fuzz 10
```

## Requirements

- Python 3.8+
- `Pillow` Python package

## License

MIT
