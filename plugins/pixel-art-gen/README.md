# Pixel Art Generator Plugin for Claude Code

Generate pixel art from text descriptions directly inside Claude Code. No external API needed — Claude designs the art itself.

```
You: "Create pixel art of a red mushroom"
Claude: *designs and renders a pixel art mushroom*
```

---

## Quick Start

**1. Add the marketplace**

```bash
/plugin marketplace add thejacedev/claude-code-skills
```

**2. Install the plugin**

```bash
/plugin install pixel-art-gen@thejacedev-skills
```

**3. Install the dependency**

```bash
pip install Pillow
```

**4. Go**

Open Claude Code and ask it to create pixel art. That's it.

---

## What It Does

This plugin adds a skill that lets Claude Code generate pixel art. When you ask for pixel art, Claude will:

1. Choose an appropriate grid size based on complexity
2. Pick a constrained color palette (4-8 colors)
3. Design the art layer by layer (silhouette, fill, details, shading)
4. Output a JSON pixel map
5. Render it to PNG using the bundled Python script
6. Display the result in your conversation

## Options

| Parameter | Values | Default |
|-----------|--------|---------|
| **Grid size** | `8x8` `10x10` `16x16` `32x32` (any NxN) | Based on subject complexity |
| **Pixel size** | Any positive integer | `32` (px per logical pixel) |
| **Grid lines** | on / off | off |
| **Background** | Any color or `transparent` | `#FFFFFF` |

## Trigger Phrases

The skill activates when you say things like:

- *"Create pixel art of..."*
- *"Make a pixel art sprite..."*
- *"Generate pixel art..."*
- *"Draw pixel art..."*
- *"8-bit style image of..."*

Or anything that implies pixel art generation.

## Project Structure

```
.claude-plugin/
  plugin.json                  # Plugin manifest
skills/
  pixel-art-gen/
    SKILL.md                   # Skill definition + instructions
    scripts/
      render_pixel_art.py      # PNG renderer (Pillow)
    references/
      pixel-art-guide.md       # Palettes, examples, JSON schema
```

## Standalone Script Usage

The bundled script also works outside Claude Code:

```bash
python3 scripts/render_pixel_art.py input.json -o output.png -p 32 -g
```

Or pipe JSON via stdin:

```bash
echo '{"width":2,"height":2,"pixels":[{"x":0,"y":0,"color":"red"},{"x":1,"y":1,"color":"blue"}]}' | python3 scripts/render_pixel_art.py - -o output.png
```

## Requirements

- Python 3.8+
- `Pillow` Python package

## License

MIT
