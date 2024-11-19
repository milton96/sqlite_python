from flask import request
from flask_restful import Resource, abort


import services.usuarioService as userSrv
from validations.usuarioValidation import nuevo_usuario

class UsuariosResource(Resource):
    def get(self):
        try:
            usuarios = userSrv.lista()
            return usuarios, 200
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")

    def post(self):
        try:
            body = request.json
            u = nuevo_usuario(body)
            print(u)
            return "", 204
        except Exception as ex:
            print(ex)
            abort(400, description="Ocurrio un error inesperado")
        
class UsuarioResource(Resource):
    def get(self, id):
        try:
            usuario = userSrv.obtener(id)
            if usuario is None:
                return "", 204
            return usuario, 200
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")

    def delete(self, id):
        try:
            userSrv.cambiar_activo(id, 0)
            return "", 204
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")