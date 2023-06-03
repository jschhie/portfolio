from flask import Flask, Blueprint, render_template, request, redirect


app = Flask(__name__)

#### HOME ####
@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def home():
    return render_template('home.html')


#### ABOUT ####
@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


#### PROJECTS ####
@app.route('/projects', methods=["GET"])
def projects():
    return render_template('projects.html')

"""
Previously (__init__.py):

from flask import Flask

def create_app():
    app = Flask(__name__)

    # register blueprints into app
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app
"""