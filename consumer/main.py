from utils import get_consumer, send_message_to_elasticsearch

TOPIC = "robota_ua"


def main():
    consumer = get_consumer(TOPIC)
    for record in consumer:
        send_message_to_elasticsearch(record.value)
