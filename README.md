<p align="center">
  <img src="header.png" alt="thejacedev skills" width="100%">
</p>

# thejacedev Claude Code Skills

A collection of Claude Code plugins for image generation and creative tasks.

## Plugins

### [openai-image-gen](plugins/openai-image-gen)

Generate images from text prompts using OpenAI's `gpt-image-1.5` model.

- Requires `OPENAI_API_KEY` and the `openai` Python package
- Supports multiple sizes and quality levels
- Just ask Claude to generate an image

### [pixel-art-gen](plugins/pixel-art-gen)

Generate pixel art PNGs from text descriptions. Claude designs the art itself — no external API needed.

- Requires the `Pillow` Python package
- Supports grid sizes from 8x8 to 32x32+
- Claude picks palettes, designs in layers, and renders to PNG

## Quick Start

**1. Add the marketplace**

```bash
/plugin marketplace add thejacedev/claude-code-skills
```

**2. Install a plugin**

```bash
/plugin install openai-image-gen@thejacedev-skills
/plugin install pixel-art-gen@thejacedev-skills
```

**3. Install dependencies**

```bash
pip install openai   # for openai-image-gen
pip install Pillow   # for pixel-art-gen
```

**4. Go**

Open Claude Code and ask it to generate an image or create pixel art.

## Project Structure

```
.claude-plugin/
  marketplace.json              # Marketplace registry
plugins/
  openai-image-gen/             # OpenAI image generation plugin
    .claude-plugin/plugin.json
    skills/openai-image-gen/
      SKILL.md
      scripts/generate_image.py
      references/api-usage.md
  pixel-art-gen/                # Pixel art generation plugin
    .claude-plugin/plugin.json
    skills/pixel-art-gen/
      SKILL.md
      scripts/render_pixel_art.py
      references/pixel-art-guide.md
```

## License

MIT
