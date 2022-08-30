import time

from flask import Flask, abort, jsonify
import re
from utils import get_producer, sent_to_kafka

app = Flask(__name__)

TOPIC = "robota_ua"
REGULAR_VALID_TEXT = '^[a-zA-Z]{1,20}$'

producer = get_producer()


@app.route("/insert/<text>")
def insert_text(text):
    if not re.match(REGULAR_VALID_TEXT, text):
        abort(400, 'text is not valid')

    time_now = int(time.time())
    message = sent_to_kafka(TOPIC, text, time_now, producer)
    return jsonify({
        "status": "success",
        "code": 200,
        "message": message
    })
