from kafka import KafkaConsumer
import json


def send_message_to_elasticsearch(message: dict):
    pass


def get_consumer(*topics: str):
    return KafkaConsumer(*topics,
                         value_deserializer=lambda v: json.loads(v),
                         auto_offset_reset='earliest',
                         bootstrap_servers=["kafka:29092"],
                         enable_auto_commit=True,
                         auto_commit_interval_ms=1000
                         )
