from flask import Flask
from my_app.fromulario.views import login

app = Flask(__name__)
app.register_blueprint(login)