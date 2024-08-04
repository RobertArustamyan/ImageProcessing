from flask import Blueprint, request, jsonify
from BackEnd.Functions.ImageModification.ColorChanging import ImageMod
from BackEnd.Functions.ImageModification.DataProcessing import DataProcessor

conf_bp = Blueprint('conf', __name__)

@conf_bp.route('/process-image', methods=['POST'])
def process():
    """

    Endpoint to process an image with a specified color configuration.

    Expects a JSON payload with 'image_base64' and 'color_conf' fields.
    Processes the image based on the provided color configuration and returns the processed image.

    :return: JSON response with the processed image or error message.
    """
    try:
        data = request.get_json()
        if not data or 'Image' not in data or 'ColorConfigs' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='configuration')
        return jsonify({'ProcessedImage': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@conf_bp.route('/grayscale-image',methods=['POST'])
def grayscale():
    """

    Endpoint to convert an image to grayscale.

    Expects a JSON payload with 'image_base64' field.
    Converts the image to grayscale and returns the processed image.

    :return: JSON response with the processed image or error message.
    """
    try:
        data = request.get_json()
        if not data or 'Image' not in data:
           return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='grayscale')
        return jsonify({'ProcessedImage': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error' : str(e)}), 500


@conf_bp.route('/invert-image',methods=['POST'])
def invert():
    """
    Endpoint to invert the colors of an image.

    Expects a JSON payload with 'image_base64' field.
    Inverts the colors of the image and returns the processed image.

    :return: JSON response with the processed image or error message.
    """
    try:
        data = request.get_json()
        if not data or 'Image' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='invert')
        return jsonify({'ProcessedImage': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error' : str(e)}), 500