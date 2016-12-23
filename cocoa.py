#cocoa models 

from app import db 

class Disease(db.Model):
	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(300))
	category_id = db.Column(db.Integer , db.ForeignKey('category'))
	category   = db.relationship('Category' , backref=db.backref('diseases' , lazy='dynamic'))
	symptoms   = db.Column(db.Text)
	solutions	=	db.column(db.Text)
	info 	=	db.Column(db.String(300))

	def __init__(self , name , category , symptoms , solutions , info):
		self.name = name
		self.category =category
		self.symptoms = symptoms
		self.solutions = solutions
		self.info = info 
	def __repr__(self):
		return '<Name : %r ' % self.name
