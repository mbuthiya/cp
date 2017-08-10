from flask import render_template
from app import app

@app.errorhandler(404)
def not_found(e):
    '''
    Returns a custom error page for any 400 server errors encountered
    '''
    title = 'page not found'
    return render_template('404.html',title=title),404

@app.errorhandler(500)
def server_error(e):
    '''
    Returns a custom error page for any 500 server errors encountered
    '''
    title = 'Server error'
    return render_template('500.html',title=title),500
