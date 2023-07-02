from flask import Flask, request, make_response
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)


@app.route("/imageplaceholder")
def generate_image_placeholder():
    width = int(request.args.get("width", 400))
    height = int(request.args.get("height", 200))
    text = f"{width} x {height}"

    # Create a blank white image
    image = Image.new("RGB", (width, height), "#e4e4e4")
    draw = ImageDraw.Draw(image)

    # Add optional text to the image
    if text:
        # Determine the font size based on the image dimensions
        font_size = min(width, height) // 5
        font = ImageFont.truetype("arial.ttf", font_size)

        # Calculate the text bounding box
        text_bbox = draw.textbbox((0, 0), text, font=font)

        # Calculate the text position at the center of the image
        text_position = ((width - text_bbox[2]) // 2, (height - text_bbox[3]) // 2)

        # Draw the text on the image
        draw.text(text_position, text, font=font, fill="black")

    # Save the image to a BytesIO buffer
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    # Create a response with the image data
    response = make_response(buffer.getvalue())
    response.headers["Content-Type"] = "image/png"

    return response


if __name__ == "__main__":
    app.run()
