from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from elasticsearch import Elasticsearch
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

mongo = MongoEngine(app)

app.elasticsearch = Elasticsearch([app.config['ELASTIC_SEARCH_URL']], verify_certs=True) if app.config['ELASTIC_SEARCH_URL'] else None
bootstrap = Bootstrap(app)

# Avoids circular imports
from app import routes, models
