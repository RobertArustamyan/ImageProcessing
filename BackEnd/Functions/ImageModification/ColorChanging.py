import io
from PIL import Image
import base64
import binascii
from io import BytesIO


class ImageMod:
    def __init__(self, img_base64_str: str) -> None:
        self._initial_image_data = None
        self._initial_pil_image = None
        self._load_initial_image_from_base64(img_base64_str)
        self._pil_image = None
        self._pixels = None
        self._load_default_image()

    def _load_initial_image_from_base64(self, base64_str: str) -> None:
        """
        Load an image from a base64 encoded string and convert it to RGB format.
        :param base64_str: Base64 encoded string representing image data
        :raises:
            ValueError: If base64 string is invalid
        """
        try:
            self._initial_image_data = base64.b64decode(base64_str)
            self._initial_pil_image = Image.open(io.BytesIO(self._initial_image_data))
            self._initial_pil_image = self._initial_pil_image.convert('RGB')
        except (binascii.Error, IOError, ValueError) as e:
            raise ValueError("Invalid image data or base64 string") from e

    def _load_default_image(self):
        self._pil_image = self._initial_pil_image.copy()
        self._pixels = self._pil_image.load()

    def pillow_show(self) -> None:
        """
        Displays the image that is in self._pil_image
        """
        self._pil_image.show()

    def change_colors(self, parameters: list[dict]) -> None:
        """
        Change the image color depending on provided parameters.
        :param parameters: List of dictionaries where each dictionary contains:
            - 'ColorRange': A dictionary with 'FromColor' and 'ToColor' specifying the color range to match.
            - 'ReplaceColor': The color to replace the matched colors with.
        """
        self._load_default_image()
        width, height = self._pil_image.size
        for x in range(width):
            for y in range(height):
                r, g, b = self._pixels[x, y]
                for parameter in parameters:
                    r_start = parameter['ColorRange']['FromColor']['r']
                    g_start = parameter['ColorRange']['FromColor']['g']
                    b_start = parameter['ColorRange']['FromColor']['b']

                    r_end = parameter['ColorRange']['ToColor']['r']
                    g_end = parameter['ColorRange']['ToColor']['g']
                    b_end = parameter['ColorRange']['ToColor']['b']

                    replace_colors = (parameter['ReplaceColor']['r'],parameter['ReplaceColor']['g'],parameter['ReplaceColor']['b'],)
                    if (min(r_start, r_end) <= r <= max(r_start, r_end) and
                            min(g_start, g_end) <= g <= max(g_start, g_end) and
                            min(b_start, b_end) <= b <= max(b_start, b_end)):
                        self._pil_image.putpixel((x, y), tuple(replace_colors))

    def convert_to_grayscale(self) -> None:
        """
        Convert the image to grayscale.
        """
        self._load_default_image()
        self._pil_image = self._pil_image.convert('L')
        self._pixels = self._pil_image.load()

    def invert_colors(self) -> None:
        """
        Invert the colors of the image.
        """
        self._load_default_image()
        width, height = self._pil_image.size
        for x in range(width):
            for y in range(height):
                r, g, b = self._pixels[x, y]
                self._pil_image.putpixel((x, y), (255 - r, 255 - g, 255 - b))

    @property
    def image_data_base64(self) -> str:
        """
        Get the image data as a base64 encoded string.
        :return: The base64 encoded string.
        """
        buffered = BytesIO()
        self._pil_image.save(buffered, format='PNG')
        return base64.b64encode(buffered.getvalue()).decode('utf-8')


if __name__ == '__main__':
    base64_string = "Test Image"
    image_converter = ImageMod(base64_string)
    image_converter.pillow_show()  # Image before modifications

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

    image_converter.change_colors(color_range)  # Changes image colors according to parameters
    image_converter.pillow_show()

    image_converter.convert_to_grayscale()  # Makes image gray
    image_converter.pillow_show()

    image_converter.    invert_colors()  # Inverts image colors
    image_converter.pillow_show()
