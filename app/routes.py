from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from jinja2 import Markup, escape
from werkzeug.urls import url_parse
from app.models import User, Movies
from . import app, db
from .forms import LoginForm, RegistrationForm, SearchForm
import re


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid user or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/search')
@login_required
def search():
    form = SearchForm()
    if not form.validate():
        return render_template('search.html', form=form)

    query = request.args.get('q')
    page = request.args.get('page', 1, int)
    per_page = request.args.get('per_page', 5, int)

    movies, total = Movies.search(query, page, per_page)
    next_url = url_for('search', page=page + 1, q=query) if page * per_page < total else None
    prev_url = url_for('search', page=page - 1, q=query) if page > 1 else None
    return render_template('results.html', movies=movies, next_url=next_url, prev_url=prev_url)

def mark(value):
    # fetch the search term
    q = request.args.get('q')
    regx = re.compile(r"("+ q + ")", flags=re.IGNORECASE)
    esc_val = escape(value)
    # replace search term w/ mark tags
    result = re.sub(regx, r'<mark>\1</mark>', str(esc_val))
    # Make sure the html tags are not escaped
    return Markup(result)
# register the filter w/ the jinja environment
app.jinja_env.filters['mark'] = mark