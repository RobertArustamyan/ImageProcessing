from BackEnd.Functions.ImageModification.ColorChanging import ImageMod

class DataProcessor:
    def __init__(self, image_body: dict, convert_format: str):
        self._image_body = image_body
        self._convert_format = convert_format

    @property
    def data_processing(self) -> str:
        """
        Converts image depending on self._convert_format.
        :return: The base64 encoded string
        """
        image_converter = ImageMod(self._image_body['image_base64'])
        if self._convert_format == 'grayscale':
            image_converter.convert_to_grayscale()
        elif self._convert_format == 'invert':
            image_converter.invert_colors()
        else:
            image_converter.change_colors(self._image_body['color_conf'])
        return image_converter.image_data_base64
