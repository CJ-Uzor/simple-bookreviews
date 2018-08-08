import os

# define base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# key for CSF
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	# sqlalchemy .db location (for sqlite)
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
	# sqlalchemy track modifications in sqlalchemy
	SQLALCHEMY_TRACK_MODIFICATIONS = False
