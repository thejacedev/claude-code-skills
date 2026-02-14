# Direct API Usage

For more control over image generation, call the OpenAI Images API directly
instead of using the bundled script.

## Basic Generation

```python
from openai import OpenAI
import base64

client = OpenAI()  # Uses OPENAI_API_KEY env var

response = client.images.generate(
    model="gpt-image-1.5",
    prompt="A sunset over a mountain range with purple clouds",
    size="1024x1024",
    quality="auto",
)

# Save the image (response may contain b64_json or url)
item = response.data[0]
if item.b64_json:
    with open("output.png", "wb") as f:
        f.write(base64.b64decode(item.b64_json))
elif item.url:
    import urllib.request
    urllib.request.urlretrieve(item.url, "output.png")
```

## Parameters Reference

### `size`

| Value | Aspect | Use Case |
|-------|--------|----------|
| `1024x1024` | Square | Icons, logos, profile pictures |
| `1024x1536` | Portrait | Character art, phone wallpapers |
| `1536x1024` | Landscape | Scenes, banners, desktop wallpapers |

### `quality`

| Value | Description |
|-------|-------------|
| `auto` | Model decides optimal quality |
| `low` | Fastest generation, lower detail |
| `medium` | Balanced speed and quality |
| `high` | Maximum detail, slowest |

## Error Handling

Wrap API calls in try/except for production use:

```python
from openai import OpenAI, APIError

client = OpenAI()

try:
    response = client.images.generate(
        model="gpt-image-1.5",
        prompt="Your prompt here",
        size="1024x1024",
    )
except APIError as e:
    print(f"API error: {e.message}")
```

## Cost Awareness

Image generation calls incur costs. The cost depends on the image size and
quality settings. Refer to the OpenAI pricing page for current rates.
