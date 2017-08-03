"""
Creates the application Instance from the Flask class and instanciates all other flask extensions.
"""
from flask import Flask
app = Flask(__name__)
from app import views
