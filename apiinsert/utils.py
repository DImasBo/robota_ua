from kafka import KafkaProducer
import json


def get_producer():
    if getattr(get_producer, 'cache', None) is None:
        get_producer.cache = KafkaProducer(bootstrap_servers=['kafka:29092'],
                                           value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    return get_producer.cache


def sent_to_kafka(topic: str, text: str, time: int, producer: KafkaProducer):
    message = {
        "message": text,
        "timestamp": time
    }
    producer.send(topic, value=message)
    return message
