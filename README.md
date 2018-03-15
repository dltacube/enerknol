# enerknol

## Notes on heroku deployment
`export DATABASE_URL=postgres://$(whoami)`
`heroku config:set LOG_TO_STDOUT=1`

Create your environment
 * `virtualenv venv`
 * `. venv/bin/activate` or `source venv/bin/activate`
 * `deactivate`
 
`heroku addons:create heroku-postgresql -a enerknol`

## Flask implementation
`export FLASK_APP=enerknol.py`

## MongoDB
`mongod --dbpath data/`

## ElasticSearch
`brew install elasticsearch`

**bulk insert of json data**

Requires data format of newline delimited JSON (NDJSON) with an action on the 
first line, and an optional source on the second.


```text
curl -XPOST localhost:9200/movies/my_doc_type/_bulk -H "Content-Type: application/x-ndjson" --data-binary @/Users/***REMOVED***/Desktop/media.movies.json
{ "index" : { "_index" : "test", "_type" : "_doc", "_id" : "1" } }
{ "field1" : "value1" }
```

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