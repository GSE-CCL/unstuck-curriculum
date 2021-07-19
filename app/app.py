"""Getting Unstuck application

This module implements a Flask application that represents the Getting Unstuck curriculum site.

"""
from flask import Flask, request, render_template, redirect, url_for
import content

app = Flask(__name__)

#uncomment to enable logging to stdout under gunicorn
#import logging, sys
#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.DEBUG)

@app.context_processor
def add_context():
    """Executed before every route handler to provide a dictionary of common content passed to all templates. """

    user_agent = request.headers.get('User-Agent')
    
    return { 
        "unstuck_modules" : content.unstuck_modules,
    }

#An extra route with an ".html" suffix is provided for all handlers. This is for backwards compatibility 
#with the previous static site. This could be handled by Apache mod-rewrite, but seems easy to hanldle here. 

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modules/<name>.html')
@app.route('/modules/<name>')
def modules(name):
    if name in content.unstuck_modules:
        return render_template('module.html', unstuck_module_name=name, **content.unstuck_modules[name])
    else:
        return redirect(url_for('page_not_found'))

@app.route('/faq.html')
@app.route('/faq')
def faq():
    return render_template('faq.html', unstuck_faq=content.unstuck_faq)

@app.route('/strategies.html')
@app.route('/strategies')
def strategies():
    return render_template('strategies.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
