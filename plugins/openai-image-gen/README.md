# OpenAI Image Gen Plugin for Claude Code

Generate images from text prompts directly inside Claude Code using OpenAI's `gpt-image-1.5` model.

```
You: "Generate an image of a cyberpunk city at sunset"
Claude: *generates and displays the image*
```

No copy-pasting API code. No leaving your terminal. Just ask.

---

## Quick Start

**1. Add the marketplace**

```bash
/plugin marketplace add thejacedev/claude-code-skills
```

**2. Install the plugin**

```bash
/plugin install openai-image-gen@thejacedev-skills
```

**3. Set your API key**

```bash
export OPENAI_API_KEY="sk-..."
```

**4. Install the dependency**

```bash
pip install openai
```

**5. Go**

Open Claude Code and ask it to generate an image. That's it.

---

## What It Does

This plugin adds a skill that lets Claude Code generate images via the OpenAI Images API. When you ask for an image, Claude will:

1. Build a detailed prompt from your request
2. Call `gpt-image-1.5` via `client.images.generate()`
3. Save the result as a PNG
4. Display it right in your conversation

## Options

| Parameter | Values | Default |
|-----------|--------|---------|
| **Size** | `1024x1024` `1024x1536` `1536x1024` | `1024x1024` |
| **Quality** | `low` `medium` `high` `auto` | `auto` |

## Trigger Phrases

The skill activates when you say things like:

- *"Generate an image of..."*
- *"Create artwork with OpenAI..."*
- *"Make me a picture of..."*
- *"Text to image..."*
- *"Draw an image of..."*

Or anything that implies OpenAI image generation.

## Project Structure

```
.claude-plugin/
  plugin.json                  # Plugin manifest
  marketplace.json             # Marketplace registry
skills/
  openai-image-gen/
    SKILL.md                   # Skill definition + instructions
    scripts/
      generate_image.py        # Image generation script
    references/
      api-usage.md             # Direct API usage docs
```

## Standalone Script Usage

The bundled script also works outside Claude Code:

```bash
python3 scripts/generate_image.py "a mountain lake at dawn" -o lake.png -s 1536x1024 -q high
```

## Requirements

- Python 3.8+
- `openai` Python package
- OpenAI API key with image generation access

## License

MIT
