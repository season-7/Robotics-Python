from . import main
from flask import render_template


#home route
@main.route('/')
def home():
    return render_template('index.html')
