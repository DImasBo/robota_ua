from typing import List, Dict

from elasticsearch import Elasticsearch


def get_messages(topic: str, elastic_client: Elasticsearch) -> List[Dict]:
    elastic_client.indices.refresh(index=topic)
    response = elastic_client.search(index=topic, body={"query": {"match_all": {}}})

    messages = []
    for hit in response['hits']['hits']:
        messages.append(hit['_source'])
    return messages
