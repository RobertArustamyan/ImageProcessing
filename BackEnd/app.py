from flask import Flask
from blueprints.configurator.configurator import conf_bp

app = Flask(__name__)
app.register_blueprint(conf_bp)

if __name__ == "__main__":
    app.run(debug=True)
