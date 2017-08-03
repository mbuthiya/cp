"""
Defines all the routes in the application and creates view functions that handle request from routes
"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    """
    Handler for the index route.
    """
    return '<h1> Hello World </h1>'
