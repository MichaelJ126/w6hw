from datetime import timedelta
import os 
from dotenv import load_dotenv 


basedir = os.path.abspath(os.path.dirname(__file__))


load_dotenv(os.path.join(basedir, '.env'))


class Config():



    FLASK_APP = os.environ.get('FLASK_APP') 
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally whatever you want as long as its a string. Cool Beans'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)