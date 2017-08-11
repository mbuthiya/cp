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
    # popular blog list
    popular_blogs = ['Boring Emoji movie','Everyone Loves Groot', 'The Mummy movie should be killed and mummified', 'Another Fast 7 movie']
    # Scandal blog list
    scandal_blogs = ['Did Jk Rowling do it?', 'The Oj Simpson Story','Mother of dragons fryer of eggs']

    return render_template('index.html',title = "Home",popular_blogs = popular_blogs,scandal_blogs = scandal_blogs)


@app.route('/movies')
def movies():
    '''
    View function that returns movie blogs
    '''
    title ='movies'
    return render_template('movies.html', title=title)



@app.route('/shows')
def shows():
    '''
    View function that returns tvshow blogs
    '''
    title ='shows'
    return render_template('shows.html', title=title)



@app.route('/news')
def news():
    '''
    View function that returns news blogs
    '''

    title ='news'
    return render_template('news.html', title =title)


@app.route('/login')
def login():
    '''
    View function that returns a login form
    '''
    title = 'login'
    return render_template('login.html', title =title)


@app.route('/signup')
def signup():
    '''
    View function that returns a signup form
    '''
    title ='signup'
    return render_template('signup.html', title =title)
