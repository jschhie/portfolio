from flask import Blueprint, render_template, request, redirect

views = Blueprint('views', __name__)

@views.route('/', methods=["GET"])
@views.route('/home', methods=["GET"])
def home():
    return render_template('home.html')



@views.route('/about', methods=["GET"])
def about():
    return render_template('about.html')



@views.route('/projects', methods=["GET"])
def projects():
    return render_template('projects.html')

