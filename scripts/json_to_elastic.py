import json
from time import sleep

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import AuthenticationException, RequestError

es = Elasticsearch(['***REMOVED***'], verify_certs=True)
with open('media.movies.json') as file:
    movies = []
    for line in file.readlines():
        movies.append(json.loads(line))

for movie in movies:
    movie['_id'] = movie['_id']['$oid']
    _id = movie.pop('_id')

    try:
        r = es.index(index='media', doc_type='movies', id=_id, body=movie)
    except AuthenticationException:
        sleep(5)
    except RequestError as e:
        print(e)

    print(r['result'])
    # r = put('http://localhost:9200/media/movies/' + str(_id), data=json.dumps(movie), headers={'content-type': 'application/json'})
    # print(r)
