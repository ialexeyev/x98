from flask import Blueprint, render_template
from .models import applicationHeaders
from .models import get_current_time

views = Blueprint('views', __name__)
appName = 'CMAP'

@views.route('/', methods=['GET', 'POST'])
def home():
  return (render_template('index.html', headers = applicationHeaders, time = get_current_time()))
