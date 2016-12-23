import os

class Configuration(object):
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir , 'app.sqlite')
	SQLALCHEMY_MIGRATION_REPO = os.path.join(basedir , 'db_repository')
