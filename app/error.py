from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
    '''
    Returns a custom error page for any 400 server errors encountered
    '''
    return render_template('404.html'),404
