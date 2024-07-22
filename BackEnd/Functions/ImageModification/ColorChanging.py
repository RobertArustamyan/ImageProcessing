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
            self._pil_image = self._pil_image.convert('RGB')
            self._pixels = self._pil_image.load()
        except Exception as e:
            raise ValueError("Unable to create PIL image") from e

    def pillow_show(self):
        self._pil_image.show()

    def change_colours(self, parameters):
        width, height = self._pil_image.size
        for x in range(width):
            for y in range(height):
                r, g, b = self._pixels[x, y]
                for parameter in parameters:
                    r_start, g_start, b_start = parameter['ColorRange']['FromColor']
                    r_end, g_end, b_end = parameter['ColorRange']['ToColor']
                    if (min(r_start, r_end) <= r <= max(r_start, r_end) and
                            min(g_start, g_end) <= g <= max(g_start, g_end) and
                            min(b_start, b_end) <= b <= max(b_start, b_end)):
                        self._pil_image.putpixel((x, y), parameter['ReplaceColor'])


base64_string = "EXAMPLE IMAGE"

im = ImageMod(base64_string)
im.pillow_show()  # Image before modifications

# Example Settings
color_range = [
    {
        'ColorRange': {
            'FromColor': (0, 0, 0),
            'ToColor': (20, 20, 20)},
        'ReplaceColor': (255, 255, 255)
    },
    {
        'ColorRange': {
            'FromColor': (255, 255, 255),
            'ToColor': (200, 200, 200)},
        'ReplaceColor': (0, 0, 0)
    },

    {
        'ColorRange': {
            'FromColor': (50, 250, 50),
            'ToColor': (70, 180, 100)},
        'ReplaceColor': (0, 0, 240)
    },

]

im.change_colours(color_range)
im.pillow_show()  # Image after modifications