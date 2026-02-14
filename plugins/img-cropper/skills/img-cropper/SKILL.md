---
name: Image Cropper
description: >
  This skill should be used when the user asks to "crop an image",
  "trim whitespace from an image", "remove blank space from a PNG",
  "auto-crop", "trim transparent space", "remove empty borders",
  "crop the blank area", "trim the image", or requests removing
  unused/blank/transparent/white space around image content.
version: 0.1.0
---

# Image Cropper

Auto-crop images by trimming blank or transparent space around the content.

## Prerequisites

Before cropping images, ensure:

1. **Pillow** Python package is installed: `pip install Pillow`

If Pillow is missing, install it before proceeding.

## Using the Script

Run the crop script located at `${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" \
  input.png \
  -o cropped.png
```

**Arguments:**

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `input` | Yes | - | Path to the input image |
| `-o, --output` | No | Overwrites input | Output file path |
| `-p, --padding` | No | `0` | Pixels of padding to keep around content |
| `-bg, --background` | No | Auto-detect | Background color to trim (`transparent`, hex, or CSS name) |
| `--fuzz` | No | `10` | Color tolerance 0-255 for background matching |

## How It Works

1. **Auto-detects background**: Samples the four corners of the image to determine the background color
2. **Finds content bounds**: Scans every pixel to find the tightest bounding box around non-background content
3. **Crops**: Trims the image to that bounding box, optionally with padding
4. **Reports**: Shows original size, cropped size, and percentage of space removed

## Workflow

When a user asks to crop/trim an image:

1. Confirm the image file exists and note its path
2. Run the crop script on it
3. Display the cropped result using the Read tool
4. Offer to adjust padding or fuzz tolerance if needed

## Examples

**Basic crop (auto-detect background, overwrite):**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" image.png
```

**Crop with padding and save to new file:**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" image.png -o trimmed.png -p 10
```

**Crop white background specifically:**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" image.png -bg white -o cropped.png
```

**Crop transparent space:**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" image.png -bg transparent -o cropped.png
```

**High fuzz tolerance for near-white backgrounds:**

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/img-cropper/scripts/crop_image.py" image.png --fuzz 30 -o cropped.png
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Pillow not installed` | Run `pip install Pillow` |
| Nothing cropped | Background may not match corners — try `-bg white` or `-bg transparent` explicitly |
| Too much cropped | Lower the `--fuzz` value (try `0` for exact matching) |
| Not enough cropped | Raise the `--fuzz` value (try `30` or higher) |
