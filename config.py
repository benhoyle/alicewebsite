import os

class Config(object):
	DEBUG 					= 	False
	TESTING 				= 	False
	
	# Define the application directory
	BASE_DIR 				= 	os.path.abspath(os.path.dirname(__file__))
	
	# Enable protection against *Cross-site Request Forgery (CSRF)*
	CSRF_ENABLED 			= 	True
	# Use a secure, unique and absolutely secret key for signing 
	# the data
	CSRF_SESSION_KEY		=	os.environ.get('CSRF_SESSION_KEY')
	SECRET_KEY 				= 	os.environ.get('SECRET_KEY')
	
	# Path to database
	#if os.environ.get('DATABASE_URL') is None:
	#	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db') 
	#else:
	#	SQLALCHEMY_DATABASE_URI = 	os.environ.get('DATABASE_URL')
	
	# Application threads. A common general assumption is using 2 
	# per available processor cores - to handle incoming requests 
	# using one and performing background operations using the 
	# other.
	THREADS_PER_PAGE 		=	 2
	#SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	if os.environ.get('HOST'):
		HOST 		=	os.environ.get('HOST')
	else:
		HOST		=	'0.0.0.0'
	if os.environ.get('PORT'):
		PORT		=	os.environ.get('PORT')
	else:
		PORT		=	8082
	
class ProductionConfig(Config):
	DEBUG 			= 	False


class StagingConfig(Config):
	DEVELOPMENT		=	True
	DEBUG			=	True


class DevelopmentConfig(Config):
	DEVELOPMENT		=	True
	DEBUG			=	True
	USE_DEBUGGER    =   True
	

class TestingConfig(Config):
	TESTING			=	True




