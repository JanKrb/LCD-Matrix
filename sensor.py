from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return {}

@app.route("/sensor", methods=["POST"])
def sensor_data():
    content = request.json

    # Validation
    assert type(content["temperature"]) == float
    assert type(content["humidity"]) == float

    with open('sensor_data.txt', 'w+', encoding='utf-8') as f:
        json.dump(content, f)

    return jsonify(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)