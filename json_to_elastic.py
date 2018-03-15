import json

from requests import put

with open('media.movies.json') as file:
    movies = []
    for line in file.readlines():
        movies.append(json.loads(line))

for movie in movies:
    movie['_id'] = movie['_id']['$oid']
    _id = movie.pop('_id')
    r = put('http://localhost:9200/media/movies/' + str(_id), data=json.dumps(movie), headers={'content-type': 'application/json'})
    print(r)
