from flask import Flask

app = Flask(__name__)

# register blueprints into app
from website.views import views
app.register_blueprint(views, url_prefix='/')


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