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
    popular_blogs = ['Boring Emoji movie','Everyone Loves Groot', 'The Mummy movie should be killed and mummified', 'Another Fast 7 movie']

    return render_template('index.html',title = "Home",popular_blogs = popular_blogs)
