# ereknol

## Notes on heroku deployment
`export DATABASE_URL=postgres://$(whoami)`

Create your environment
 * `virtualenv venv`
 * `. venv/bin/activate` or `source venv/bin/activate`
 * `deactivate`
 
`heroku addons:create heroku-postgresql -a enerknol`

## Flask implementation
`export FLASK_APP=enerknol.py`