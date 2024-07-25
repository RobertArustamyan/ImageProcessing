from flask import Blueprint, request, jsonify
from BackEnd.Functions.ImageModification.ColorChanging import ImageMod
from BackEnd.Functions.ImageModification.DataProcessing import DataProcessor
conf_bp = Blueprint('conf', __name__)

@conf_bp.route('/process-image', methods=['POST'])
def process():
    try:
        data = request.get_json()
        if not data or 'image_base64' not in data or 'color_conf' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='configuration')
        return jsonify({'processed_image': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@conf_bp.route('/grayscale-image',methods=['POST'])
def grayscale():
    try:
        data = request.get_json()
        if not data or 'image_base64' not in data:
           return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='grayscale')
        return jsonify({'processed_image': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error' : str(e)}), 500


@conf_bp.route('/invert-image',methods=['POST'])
def invert():
    try:
        data = request.get_json()
        if not data or 'image_base64' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        processor = DataProcessor(image_body=data, convert_format='invert')
        return jsonify({'processed_image': processor.data_processing}), 200

    except Exception as e:
        return jsonify({'error' : str(e)}), 500