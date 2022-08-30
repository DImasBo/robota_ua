from utils import get_consumer, send_message_to_elasticsearch
from elasticsearch import Elasticsearch


TOPIC = "robota_ua"

elastic_client = Elasticsearch('http://elasticsearch:9200')


def main():
    consumer = get_consumer(TOPIC)
    for record in consumer:
        send_message_to_elasticsearch(TOPIC, record.value, elastic_client)


if __name__ == '__main__':
    main()

