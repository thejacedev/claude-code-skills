#!/usr/bin/env python3
"""Generate images using OpenAI's gpt-image-1.5 model via the Images API."""

import argparse
import base64
import os
import sys
from pathlib import Path


def generate_image(prompt, output_path="generated_image.png", size="1024x1024", quality="auto"):
    """Generate an image from a text prompt using OpenAI's Images API.

    Args:
        prompt: Text description of the image to generate.
        output_path: Where to save the generated image.
        size: Image dimensions. Options: 1024x1024, 1024x1536, 1536x1024.
        quality: Image quality. Options: low, medium, high, auto.

    Returns:
        Path to the saved image file.
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed. Run: pip install openai", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.", file=sys.stderr)
        print("Run: export OPENAI_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)

    client = OpenAI()

    print(f"Generating image for prompt: {prompt!r}", file=sys.stderr)
    print(f"Size: {size}, Quality: {quality}", file=sys.stderr)

    try:
        response = client.images.generate(
            model="gpt-image-1.5",
            prompt=prompt,
            size=size,
            quality=quality,
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        sys.exit(1)

    item = response.data[0]

    if hasattr(item, 'b64_json') and item.b64_json:
        image_bytes = base64.b64decode(item.b64_json)
    elif hasattr(item, 'url') and item.url:
        import urllib.request
        image_bytes = urllib.request.urlopen(item.url).read()
    else:
        print("Error: No image data in response.", file=sys.stderr)
        sys.exit(1)

    # Save the image
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_bytes(image_bytes)

    print(f"Image saved to: {output_file.resolve()}")
    return str(output_file.resolve())


def main():
    parser = argparse.ArgumentParser(description="Generate images with OpenAI gpt-image-1.5")
    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument("-o", "--output", default="generated_image.png",
                        help="Output file path (default: generated_image.png)")
    parser.add_argument("-s", "--size", default="1024x1024",
                        choices=["1024x1024", "1024x1536", "1536x1024"],
                        help="Image size (default: 1024x1024)")
    parser.add_argument("-q", "--quality", default="auto",
                        choices=["low", "medium", "high", "auto"],
                        help="Image quality (default: auto)")
    args = parser.parse_args()

    generate_image(args.prompt, args.output, args.size, args.quality)


if __name__ == "__main__":
    main()
