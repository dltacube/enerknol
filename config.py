import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dkfshgkjehkijugth345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELASTIC_SEARCH_URL = os.environ.get('ELASTIC_SEARCH_URL') or {'host': 'localhost', 'port': '9200'}
    MONGODB_SETTINGS = os.environ.get('MONGODB_SETTINGS') or {'db': 'media'}