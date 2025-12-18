# __init__.py
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me'  # для будущих форм/flash

from . import routes  # регистрируем маршруты