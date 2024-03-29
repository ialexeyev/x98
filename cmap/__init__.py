from flask import Flask


# Application definition
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'kisyr79dnns0146xbas231frv98'

  from .views import views

  app.register_blueprint(views, url_prefix='/')

  return app
