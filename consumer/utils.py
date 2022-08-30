from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
from datetime import datetime
import json


def send_message_to_elasticsearch(message: dict, elastic_client: Elasticsearch):
    doc = {
        'text': message.get('text'),
        'timestamp': datetime.fromtimestamp(
            message.get('timestamp')),
    }
    response = elastic_client.index(index="test-index", id=1, body=doc)
    return response


def get_consumer(*topics: str):
    return KafkaConsumer(*topics,
                         value_deserializer=lambda v: json.loads(v),
                         auto_offset_reset='earliest',
                         bootstrap_servers=["kafka:29092"],
                         enable_auto_commit=True,
                         auto_commit_interval_ms=1000
                         )
