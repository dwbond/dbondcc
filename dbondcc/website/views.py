from flask import render_template
from website import website
from flask.ext import gravatar

@website.route('/')
@website.route('/index')
def index():
    return render_template("index.html",
    
    )

# 404 error
@website.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
