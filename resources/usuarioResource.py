from flask import Response, request
from flask_restful import Resource, abort


import services.usuarioService as userSrv
from utils.common import get_body
from utils.customException import ExceptionControlada
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
            body = get_body(request)
            if body is None or len(body.keys()) == 0:
                raise ExceptionControlada(400, "No se recibio informacion")

            body["activo"] = 1
            u = nuevo_usuario(body)
            return u, 201
        except ExceptionControlada as ec:
            abort(ec.codigo, description=ec.message)
        except Exception as ex:
            abort(500, description="Ocurrio un error inesperado")
        
class UsuarioResource(Resource):
    def get(self, id):
        try:
            usuario = userSrv.obtener(id)
            if usuario is None:
                return Response(status=404)
            return usuario, 200
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")

    def delete(self, id):
        try:
            userSrv.cambiar_activo(id, 0)
            return Response(status=204)
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")