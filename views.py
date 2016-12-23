from app import app , db
from flask import render_template , session , make_response , flash , abort , request , redirect , url_for , g
from models import *
from flask_login import login_user , logout_user , current_user , login_required


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register' , methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	new_user = Users(request.form['username'],request.form['password'],request.form['email'],request.form['first_name'])
	db.session.add(new_user)
	db.session.commit()
	return redirect(url_for('login'))

@app.route('/login' , methods=['GET','POST'])
def login():
	if request.method == 'GET':
		session.pop('users' , None)
		return render_template('login.html')
	username	=	request.form['username']
	password	=	request.form['password']
	session['username'] = request.form['username']
	registered_user = Users.query.filter_by(username=username , password=password).first()
	if registered_user is None:
		flash('username or password incorrect' , 'error')
		return redirect(url_for('login'))
	login_user(registered_user)
	return redirect(request.args.get('next') or url_for('details'))

@app.route('/details')
def details():
	return render_template('home.html')

@app.route('/logout')
def logout():
	logout_user()
	session.pop('username' , None)
	return redirect(url_for('login'))
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html') , 404
@app.route('/forms')
def forms():
	return render_template('new.html')