from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login, mongo
from app.search import query_index


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Movies(mongo.Document):
    meta = {'strict': False}
    projections = ['_id', 'budget', 'homepage', 'imdb_id', 'original_title', 'overview', 'release_date', 'runtime', 'tagline']

    _id = mongo.ObjectIdField()
    original_title = mongo.StringField()
    overview = mongo.StringField()
    tagline = mongo.StringField()
    runtime = mongo.IntField()
    budget = mongo.IntField()
    homepage = mongo.StringField()
    release_date = mongo.DateTimeField()

    def __repr__(self):
        return '{} - id: {}: {}'.format(str(self.__class__), self._id, self.original_title)

    @classmethod
    def search(cls, query, page, per_page):
        ids, total = query_index(query, page, per_page)
        if total == 0:
            return [], 0
        movies = Movies.objects(_id__in=ids)
        return movies, total


@login.user_loader
def load_user(_id):
    return User.query.get(int(_id))
