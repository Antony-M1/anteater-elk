from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['http://localhost:9200'],
    basic_auth=('elastic', 'gN6HpBz*83*Lu*pN3p-W1')
)
print(es)