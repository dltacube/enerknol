# EnerKnol Code Exercise

**[Click Here](https://enerknol.herokuapp.com/)**

## Source Code Organization
* `enerknol.py` is our main entry point if we're debugging or running locally. It gives us access to 
a debug console as well as some contextual objects (mainly database connections) when running `flask shell` after setting `FLASK_APP=enerknol.py`.
The `flask-shell-ptpython` ensures `ptpython` shell is used rather than the default python shell.

* `config.py` is used for storing environment variables and gets called later in the app package.

* `app/__init__.py` takes care of loading all of our flask modules in a global accessible context
* `search.py & models.py` the latter stores our SQL models (postgres or sqlite depending on context) while
the former handles our elasticsearches. In the future, I would write out models for the elastic indices
and glue it to the mongoDB so that changes are faithfully reflected.
* `forms.py`  here are some very simple form objects to automate some validation as well as benefit from automatic
rendering in templates.
* `routes.py` 
    - `login` very basic login view that redirects to the front page if auth'd, attempts to log in if 
    a valid form is submitted, then proceeds to populate the `login_user` objects from `flask_login` which is
    just a wrapper around flask sessions and helps us manage user state and cookies.
    - `flask_login` module here serves as a wrapper for flask sessions. The `next_page` argument
    is checked to make sure the redirect stays on our domain.
    - `register` checks if user is authenticated, if not the form validation is executed and barring any conflicts
    a new user is created. `werkzeug.security` is tapped for hashing given passwords with sha256 encryption and 8 character
    long salts.
    - `@login_required` is used for gating content to authorized users only
    - `search` validates form then searches for movies using a search term. Under the hood, the `Movies` object
    is querying our elasticsearch index first, returning matching oid's, then returning the data as it is from 
    the mongoDB database itself. Some pagination is included, but in the future I would add more details for navigating
    other pages, rather than just hitting next or previous.
    - `mark` is a jinja2 filter that simply wraps any instance of our search term in the results with `<mark>` tags
    causing the text to be highlighted.

## Installation
Create your environment
 * `virtualenv venv`
 * `. venv/bin/activate` or `source venv/bin/activate`
 * `pip install -r requirements.txt`
 * `deactivate`

## Flask implementation
`export FLASK_APP=enerknol.py`

`flask shell`

## MongoDB
`mongod --dbpath data/`

## ElasticSearch
`brew install elasticsearch`

`elasticsearch`

Data can be found in `/usr/local/var/lib/elasticsearch/`

**bulk insert of json data**

Requires data format of newline delimited JSON (NDJSON) with an action on the 
first line, and an optional source on the second.


```text
curl -XPOST localhost:9200/movies/my_doc_type/_bulk -H "Content-Type: application/x-ndjson" --data-binary @media.movies.json
{ "index" : { "_index" : "test", "_type" : "_doc", "_id" : "1" } }
{ "field1" : "value1" }
```

## Notes
* elasticsearch is missing a number of records because the free heroku plan limits the database size to about 20mb.
* [Heroku Deployment](https://enerknol.herokuapp.com/)
* `migrations` folder is excellent for changing your SQL db schema in place should you make any changes to your sqlalchemy models


## Documentations
* [elasticsearch-dsl](https://elasticsearch-dsl.readthedocs.io/)
* [elasticsearch-python](https://elasticsearch-py.readthedocs.io/en/master/)
* [mongoDB](https://docs.mongodb.com)
* [jinja2](http://jinja.pocoo.org/docs/2.10/)
* [flask-mongoengine](https://github.com/MongoEngine/flask-mongoengine)
* [mongoengine](http://docs.mongoengine.org/guide/)
* [ptpython](https://github.com/jonathanslenders/ptpython)
* [flask-shell-ptpython](https://github.com/jacquerie/flask-shell-ptpython)
* [flask](http://flask.pocoo.org/docs/0.12/)