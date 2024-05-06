from PIL import Image
from rembg import remove
import io
import json


def process_image(image_uploaded):
    """
    Process the uploaded image by removing its background using the rembg library.
    """
    image = Image.open(image_uploaded)
    processed_image = remove_background(image)
    return processed_image


def remove_background(image):
    """
    Remove the background from the given image using the rembg library.
    """
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    proccesed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(proccesed_image_bytes))


def compress_image(uploaded_image):
    """
    Compress the uploaded image to reduce file size.
    """
    picture = Image.open(uploaded_image)
    picture.save("compressed_image.jpg", optimize=True, quality=60)
    return picture


def load_lottieflie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)