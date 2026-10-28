import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team M: IoT Sensor Analytics", stack="flask")

@app.route("/api/ingest", methods=["POST"])
def ep_0(**kwargs):
    # TODO: Body: {device, value, ts}
    return jsonify(error="Not implemented", todo="Body: {device, value, ts}"), 501

@app.route("/api/series", methods=["GET"])
def ep_1(**kwargs):
    # TODO: Aggregated series by interval
    return jsonify(error="Not implemented", todo="Aggregated series by interval"), 501

@app.route("/api/stream", methods=["GET"])
def ep_2(**kwargs):
    # TODO: SSE live feed
    return jsonify(error="Not implemented", todo="SSE live feed"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
