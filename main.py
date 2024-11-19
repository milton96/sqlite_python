from flask import Flask
from flask_restful import Api
from resources.usuarioResource import UsuariosResource

def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UsuariosResource, '/usuarios')

    app.run(debug=True)

if __name__ == "__main__":
    main()