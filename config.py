from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DEBUG = environ.get('DEBUG', False)
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    TESTING = environ.get('TESTING', False)
    SECRET_KEY = environ.get('SECRET_KEY', 'secret')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SENTRY_DSN = environ.get('SENTRY_DSN', False)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    CHUB_TOKEN = environ.get('CHUB_TOKEN')
    CHUB_SITE_ID = environ.get('CHUB_SITE_ID_NL')
