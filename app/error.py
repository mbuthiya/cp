from flask import render_template
from app import app

@app.errorhandler(404)
def not_found():
    '''
    Returns a custom error page for any 400 server errors encountered
    '''
    return render_template('404.html'),404

@app.errorhandler(500)
def server_error():
    '''
    Returns a custom error page for any 500 server errors encountered
    '''

    return render_template('500.html'),500
