from flask import Flask
from flask_cors import CORS
from BackEnd.blueprints.configurator.configurator import conf_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(conf_bp, url_prefix='/conf')

if __name__ == "__main__":
    app.run(debug=True)