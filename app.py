from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
app.secret_key = '\xad\x16\xb8L\xd2\xfc\xc7\x9e\xb3\xef'
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view	=	'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))