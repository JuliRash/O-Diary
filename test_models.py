from app import db , app 
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view	=	'login'

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))


class PhoneBook(db.Model):
	id		=	db.Column(db.Integer , primary_key=True)
	name 	=	db.Column(db.String(2000))
	address	=	db.Column(db.String(2000))
	fb		=	db.Column(db.String)
	phone 	=   db.Column(db.String(11))

	def __int__(self , name , address , fb , phone):
		self.name		=	name
		self.address	=	address
		self.fb			=	phone 

	def __repr__(self):
		return '<Phone : %r ' % self.phone
class Users(db.Model):
	id			=	db.Column(db.Integer , primary_key=True)
	username	=	db.Column(db.String(200))
	password	=	db.Column(db.String(200))
	email		=	db.Column(db.String(300))
	first_name	=	db.Column(db.String(300))

	def __init__(self , username , password , email , first_name):
		self.username	=	username
		self.password	=	password
		self.email		=	email
		self.first_name	=	first_name

	def is_authenticated(self):
		return True 

	def is_active(self):
		return True 

	def is_anonymous(self):
		return True 

	def get_id(self):
		return str((self.id))

	def __repr__(self):
		return '<Username : %r ' % self.username
		
