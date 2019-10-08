from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Vik",
        "age": 42,
        "occupation": "Network Engineer"
    }
]


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
            return "User not found", 404


api.add_resource(User, "/user/<string:name>")
app.run(debug=True)