from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import urandom

from src.model import aimodel
from src.image import image


app = Flask(__name__)
app.secret_key = urandom(32)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0322@localhost:3306/isa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_ECHO'] = True

app.register_blueprint(aimodel, url_prefix='/aimodel')
app.register_blueprint(image, url_prefix='/image')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')