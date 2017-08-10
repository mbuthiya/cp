"""
Creates the application Instance from the Flask class and instanciates all other flask extensions.
"""
from flask import Flask
from flask_bootstrap import Bootstrap

# Initializations
app = Flask(__name__)
bootstrap = Bootstrap(app)

from app import views
from app import error
