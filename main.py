from flask import Flask
from flask_restful import Resource, Api

class HelloWolrd(Resource):
    def get(self):
        return {'hello': 'world!'}

def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(HelloWolrd, '/')

    app.run(debug=True)

if __name__ == "__main__":
    main()