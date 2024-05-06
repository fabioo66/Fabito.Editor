from PIL import Image
from rembg import remove
import io
import json


def process_image(image_uploaded):
    """Process the uploaded image by removing its background using the rembg library."""
    image = Image.open(image_uploaded)
    processed_image = remove_background(image)
    return processed_image


def remove_background(image):
    """Remove the background from the given image using the rembg library."""
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    proccesed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(proccesed_image_bytes))


def compress_image(uploaded_image, quality=50, max_size=(1024, 1024)):
    """
    Compress the uploaded image to reduce file size.
    """
    img = Image.open(uploaded_image)
    img.thumbnail(max_size)
    
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='JPEG', optimize=True, quality=quality)
    
    img_byte_array.seek(0)
    compressed_img = Image.open(img_byte_array)
    
    return compressed_img


def load_lottieflie(filepath: str):
    """This function creates the animation"""
    with open(filepath, "r") as f:
        return json.load(f)