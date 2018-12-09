from flask import Flask
from flask import send_file, jsonify
import json
import jwt
from time import sleep

app = Flask(__name__)

port = 4000

static_dir = './static/files'

resources_file = "./resources.json"

with open(resources_file) as f:
    resource_data = json.load(f)


@app.route("/")
def root():
    return jsonify({"message": "Hello, World!"})

@app.route("/jwt/hi")
def jwt_hi():
    return jsonify({"message": "JWT"})


@app.route("/jwt/encode/<string:data>")
def jwt_encode(data):
    return jsonify({
        "encoded": jwt.encode({'data': data}, 'secret', algorithm='HS256')
    })

@app.route("/jwt/decode/<string:data>")
def jwt_decode(data):
    return jsonify({
        "decode": jwt.decode(data, 'secret', algorithms=['HS256'])
    })


# @app.route("/resources/fast/<int:resource_id>")
# def get_resource_fast(resource_id):
#     return jsonify(resource_data[resource_id])


# @app.route("/resources/slow/<int:resource_id>")
# def get_resource_slow(resource_id):
#     sleep(0.5)
#     return jsonify(resource_data[resource_id])


# @app.route("/resources/fast/<int:resource_id>")
# def get_resource_fast(resource_id):
#     return jsonify(resource_data[resource_id])


# @app.route("/resources/cpu/<int:resource_id>")
# def get_resource_cpu(resource_id):
#     x = 0
#     for x in xrange(1, 10000):
#         x += (1 * x * x) / (x + 1)
#     return jsonify(resource_data[resource_id])


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=port)
