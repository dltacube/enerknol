from flask import current_app


def query_index(query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index='media',
        doc_type='movies',
        body={'query': {
            'multi_match': {
                'query': query,
            }},
            'from': (page - 1) * per_page,
            'size': per_page
        }
    )
    ids = [res['_id'] for res in search['hits']['hits']]
    return ids, search['hits']['total']

