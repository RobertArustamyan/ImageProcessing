import io
from PIL import Image
import base64
from io import BytesIO


class ImageMod:
    def __init__(self, img_base64_str: str) -> None:
        self._pil_image = None
        self._pixels = None
        self._image_data = None
        self._load_image_from_base64(img_base64_str)

    def _load_image_from_base64(self, base64_str: str) -> None:
        """
        Load an image from a base64 encoded string and convert it to RGB format.
        :param base64_str: Base64 encoded string representing image data
        :raises:
            ValueError: If base64 string is invalid
        """
        try:
            self._image_data = base64.b64decode(base64_str)
            self._pil_image = Image.open(io.BytesIO(self._image_data))
            self._pil_image = self._pil_image.convert('RGB')
            self._pixels = self._pil_image.load()
        except (base64.binascii.Error, IOError, ValueError) as e:
            raise ValueError("Invalid image data or base64 string") from e

    def pillow_show(self) -> None:
        """
        Displays the image that is in self._pil_image
        """
        self._pil_image.show()

    def change_colours(self, parameters: list[dict]):
        """
        Change the image color depending on provided parameters.
        :param parameters: List of dictionaries where each dictionary contains:
            - 'ColorRange': A dictionary with 'FromColor' and 'ToColor' specifying the color range to match.
            - 'ReplaceColor': The color to replace the matched colors with.
        """
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
    base64_string = "ImageBase64Format"

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

    image_converter.change_colours(color_range)
    image_converter.pillow_show()  # Image after modifications

    print(image_converter.image_data_base64)  # Prints Modified image in base64
