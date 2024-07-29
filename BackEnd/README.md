# Image Processing API

This project provides an API to process images by replacing colors within specified ranges with new colors, converting images to grayscale, and inverting image colors.

## Usage 

API Base URL: `https://industrial-reta-robertarustamyan-58b2564f.koyeb.app/image`

### Endpoints
- **Color Replacement** `/process-image` 
  - Replace colors within specified ranges with new colors.
- **Grayscale** `/grayscale-image` 
  - Convert the image to grayscale.
- **Invert** `/invert-image` 
  - Invert the colors of the image.


API Swagger [Documentation](https://app.swaggerhub.com/apis-docs/ROBERTARUSTAMYAN2/ImageProcessingAPI/1.0.0)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RobertArustamyan/ImageProcessing.git
    cd BackEnd 
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Test the project locally:
   ```shell
   python app.py
   python Tester.py
   ```

