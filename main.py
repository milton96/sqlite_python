from flask import Flask
from flask_restful import Api
from resources.usuarioResource import UsuariosResource, UsuarioResource

def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UsuariosResource, '/usuarios')
    api.add_resource(UsuarioResource, '/usuarios/<int:id>')

    app.run(debug=True)

if __name__ == "__main__":
    main()