from flask import Blueprint, request, jsonify
from BackEnd.Functions.ImageModification.ColorChanging import ImageMod

conf_bp = Blueprint('conf', __name__)

@conf_bp.route('/process-image', methods=['POST'])
def process():
    try:
        data = request.get_json()
        if not data or 'image_base64' not in data or 'color_conf' not in data:
            return jsonify({'error': 'Invalid data format'}), 400

        processed_data = image_data_processing(data)
        return jsonify({'processed_image': processed_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def image_data_processing(image_body):
    image_converter = ImageMod(image_body['image_base64'])
    image_converter.change_colours(image_body['color_conf'])
    return image_converter.image_data_base64


"""
DATA format example
{
    'image_base64' : 'ImageBase64' (string),
    'color_conf': [
            'ColorRange': {
                'FromColor': (0, 0, 0),
                'ToColor': (20, 20, 20)
                },
            'ReplaceColor': (255, 255, 255)
            },
            {
            'ColorRange': {
                'FromColor': (255, 255, 255),
                'ToColor': (200, 200, 200)
                },
            'ReplaceColor': (0, 0, 0)
        }
    ]
}
"""