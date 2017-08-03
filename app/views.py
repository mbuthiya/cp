"""
Defines all the routes in the application and creates view functions that handle request from routes
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """
    Handler for the index route.
    """
    return render_template('index.html')
