from elasticsearch import Elasticsearch
from flask import Flask, jsonify
from utils import get_messages

app = Flask(__name__)

TOPIC = "robota_ua"

elastic_client = Elasticsearch('http://elasticsearch:9200')


@app.route("/show")
def show():
	messages = get_messages(TOPIC, elastic_client)
	return jsonify({
		"status": "success",
		"code": 200,
		"data": messages
	})
