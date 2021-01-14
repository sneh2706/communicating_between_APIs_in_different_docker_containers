import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class calling_obj(Resouce):
    def get(self):
        r = requests.get('')
        return r.status_code


api.add_resource(calling_obj, '/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
