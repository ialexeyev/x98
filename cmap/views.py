from flask import Blueprint, render_template

views = Blueprint('views', __name__)
appName = 'CMAP'

@views.route('/', methods=['GET', 'POST'])
def home():
  return (render_template('index.html', header = appName))
