from flask import current_app
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch


def query_index(q, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    s = Search(using=current_app.elasticsearch, index="media")
    start = (page - 1) * per_page
    end = page * per_page
    result = s.query(MultiMatch(query=q))[start: end].execute()

    ids = [res['_id'] for res in result['hits']['hits']]
    return ids, result['hits']['total']
