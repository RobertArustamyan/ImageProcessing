import io
from PIL import Image
import base64
from io import BytesIO


class ImageMod:
    def __init__(self, base64_str: str):
        try:
            self._image_data = base64.b64decode(base64_str)
            self.pillow_image()
        except Exception as e:
            raise ValueError("Invalid image data or base64 string") from e

    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Image data must be in base64 format")
        try:
            self._image_data = base64.b64decode(value)
            self.pillow_image()
        except Exception as e:
            raise ValueError("Invalid image data or base64 string") from e

    def pillow_image(self):
        try:
            self._pil_image = Image.open(io.BytesIO(self._image_data))
        except Exception as e:
            raise ValueError("Unable to create PIL image") from e

    def pillow_show(self):
        self._pil_image.show()


base64_string = "iVBORw0KGgoAAAANSUhEUgAAACgAAAAeCAAAAAB7tgMBAAAAqklEQVR4nGPUYcALLjMwlE1YEcTAwIRfHQMDA0NTULDjdmIUcqw4LuRtRYRCBgaLtRfeEqWQgUFvBZEKGZSIVbiahbCaqheWHEfnEaFQc/+GP5qzGQkHOAQQ68ZRhbgA44QBs5qBgYHhfzERiYKBgeFvKjHJjIHhZ+ShvcQo/OJ945AWMQqbf9mrEuUZ/TXHshmIMTEqeEq6JnG+TrtcQpxChv7rRAY4yyoANSomfn2BsmYAAAAASUVORK5CYII="

im = ImageMod(base64_string)
im.pillow_show()
