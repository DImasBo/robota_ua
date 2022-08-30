from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
from datetime import datetime
import json


def send_message_to_elasticsearch(index_name, message: dict, elastic_client: Elasticsearch):
    doc = {
        'message': message.get('message'),
        'timestamp': datetime.fromtimestamp(
            message.get('timestamp')),
    }

    response = elastic_client.index(index=index_name, body=doc)
    elastic_client.indices.refresh(index=index_name)
    return response


def get_consumer(*topics: str):
    return KafkaConsumer(*topics,
                         value_deserializer=lambda v: json.loads(v),
                         auto_offset_reset='earliest',
                         bootstrap_servers=["kafka:29092"],
                         enable_auto_commit=True,
                         auto_commit_interval_ms=1000
                         )
