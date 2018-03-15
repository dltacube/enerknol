import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # eventually would be used for generating hashes
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dkfshgkjehkijugth345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELASTIC_SEARCH_URL = os.environ.get('SEARCHBOX_SSL_URL') or {'host': 'localhost', 'port': '9200'}

    mongo_uri = os.environ.get('MONGODB_SETTINGS')
    if mongo_uri:
        MONGODB_SETTINGS = {'host': mongo_uri}
    else:
        MONGODB_SETTINGS = {'db': 'media'}