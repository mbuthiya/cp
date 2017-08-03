"""
Module that is executed and starts up the flask server
"""
from app import app

if __name__ == '__main__':
    app.run(debug = True)
