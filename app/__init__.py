from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

mongo = MongoEngine(app)

app.elasticsearch = Elasticsearch([app.config['ELASTIC_SEARCH_URL'], app.config['SEARCHBOX_SSL_URL']], verify_certs=True) if app.config['ELASTIC_SEARCH_URL'] else None

# Avoids circular imports
from app import routes, models
