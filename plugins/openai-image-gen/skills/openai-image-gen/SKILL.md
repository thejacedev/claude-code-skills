---
name: OpenAI Image Generator
description: >
  This skill should be used when the user asks to "generate an image with OpenAI",
  "create an image using gpt-image", "make me a picture with OpenAI",
  "OpenAI image generation", "draw an image using gpt-image-1.5",
  "create artwork with OpenAI", "text to image with OpenAI", or requests
  generating or creating images via OpenAI's gpt-image-1.5 model.
  Covers text-to-image generation using the Images API
  (client.images.generate).
version: 0.1.1
---

# OpenAI Image Generator

Generate images from text prompts using OpenAI's `gpt-image-1.5` model via the Images API.

## Prerequisites

Before generating images, ensure:

1. **OPENAI_API_KEY** is set in the environment: `export OPENAI_API_KEY="sk-..."`
2. **openai** Python package is installed: `pip install openai`

If the `openai` package is missing, install it before proceeding.

## Generating Images

### Using the Bundled Script

Run the generation script located at `${CLAUDE_PLUGIN_ROOT}/skills/openai-image-gen/scripts/generate_image.py`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/openai-image-gen/scripts/generate_image.py" \
  "A sunset over a mountain range with purple clouds" \
  -o output.png \
  -s 1024x1024 \
  -q auto
```

**Arguments:**

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `prompt` | Yes | - | Text description of the image |
| `-o, --output` | No | `generated_image.png` | Output file path |
| `-s, --size` | No | `1024x1024` | Image dimensions |
| `-q, --quality` | No | `auto` | Image quality level |

### Available Sizes

- `1024x1024` - Square (default)
- `1024x1536` - Portrait
- `1536x1024` - Landscape

### Quality Options

- `auto` - Let the model decide (default)
- `low` - Faster, lower quality
- `medium` - Balanced
- `high` - Best quality, slower

### Using the API Directly

For direct API usage without the bundled script, see
`${CLAUDE_PLUGIN_ROOT}/skills/openai-image-gen/references/api-usage.md`.

## Workflow

When a user requests an image:

1. Confirm the `OPENAI_API_KEY` environment variable is set
2. Ensure the `openai` Python package is installed
3. Craft a descriptive prompt based on the user's request (add detail if the request is vague)
4. Choose an appropriate size based on the content (landscape for scenes, portrait for people, square for icons/logos)
5. Run the script with the prompt and desired parameters
6. Display the generated image to the user using the Read tool on the output file
7. Offer to regenerate with a modified prompt if the result needs adjustment

## Prompt Tips

- Be specific and descriptive for better results
- Include style references (e.g., "oil painting style", "photorealistic", "watercolor")
- Specify lighting, mood, and composition details
- Mention colors, textures, and materials explicitly

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `OPENAI_API_KEY not set` | Run `export OPENAI_API_KEY="sk-..."` |
| `openai package not installed` | Run `pip install openai` |
| No image in response | Check that the model name `gpt-image-1.5` is correct and the API key has image generation access |
| Rate limit errors | Wait and retry, or check API usage limits |
