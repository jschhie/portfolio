from flask import Blueprint, render_template, request, redirect
import json

def load_data_from_json(filepath):
  try:
    with open(filepath, 'r') as f:
      # Convert JSON into Python list/dict
      data = json.load(f)
      return data
  except FileNotFoundError:
    return []
  except json.JSONDecodeError:
    return []

views = Blueprint('views', __name__)

@views.route('/', methods=["GET"])
@views.route('/home', methods=["GET"])
def home():
  return render_template('home.html')



@views.route('/about', methods=["GET"])
def about():
  all_skills_data = load_data_from_json('website/static/aboutSkills.json')
  all_lang_data = all_skills_data["languages"]
  all_frameworks_data = all_skills_data["frameworks"]
  all_data_skills = all_skills_data["dataSkills"]
  all_tools_data = all_skills_data["tools"]
  return render_template(
                          'about.html', 
                          all_lang_data=all_lang_data, 
                          all_frameworks_data=all_frameworks_data, 
                          all_data_skills=all_data_skills, 
                          all_tools_data=all_tools_data
                        )



@views.route('/projects', methods=["GET"])
def projects():
  return render_template('projects.html')

