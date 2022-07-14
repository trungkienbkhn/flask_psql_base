from flask import Flask
from dotenv import dotenv_values

config = dotenv_values('.env')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = 'secret!'
