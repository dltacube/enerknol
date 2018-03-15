from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login, mongo
from bson.objectid import ObjectId

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


class Movies:
    projections = ['_id', 'budget', 'homepage', 'imdb_id', 'original_title', 'overview', 'release_date', 'runtime', 'tagline', 'vote_average', 'vote_count']

    @classmethod
    def search(cls, query, page, per_page):
        ids, total = query_index(query, page, per_page)
        if total == 0:
            return {'results': None}
        oids = [ObjectId(_id) for _id in ids]
        res = mongo.db.movies.find({'_id': {'$in': oids}}, projection=cls.projections)
        print('res: {}'.format(res.count()))
        movies = [movie for movie in res]
        print('movies: {}'.format(movies))
        return movies, total


@login.user_loader
def load_user(_id):
    return User.query.get(int(_id))
