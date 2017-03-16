# Import flask and template operators
from flask import Flask, render_template

# Logging imports
import logging
from logging.handlers import RotatingFileHandler

# Define the WSGI application object
app = Flask(__name__)
app.debug = True

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
#Configure logging
file_handler = RotatingFileHandler('alicewebsite_error.log', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>')
def return_page(page):
    return render_template(page)         

if __name__ == "__main__":
    app.run()