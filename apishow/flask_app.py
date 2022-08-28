from flask import Flask, abort, jsonify


app = Flask(__name__)


@app.route("/show")
def show():
	return jsonify(
		{"data": [
			{"timestamp": "2022-08-19 12: 59:35", "message": "text1"},
			{"timestamp": "2022-08-19 13: 51:35", "message": "text2"}
		]}
	)
