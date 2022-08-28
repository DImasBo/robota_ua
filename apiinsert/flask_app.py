from flask import Flask, abort, jsonify
import socket
from confluent_kafka import Producer

conf = {'bootstrap.servers': "localhost:9092", 'client.id': socket.gethostname()}

producer = Producer(conf)

app = Flask(__name__)


@app.route("/insert/<text>")
def insert_text(text):
    if text == 'exc':
        abort(404)
    return jsonify({'text': text})


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


producer.produce('topic', key="key", value="value", callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)
