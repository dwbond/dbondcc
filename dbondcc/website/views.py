from flask import render_template
from website import website
from flask.ext import gravatar

@website.route('/')
@website.route('/index')
def index():
    return render_template("index.html",
    
    )
