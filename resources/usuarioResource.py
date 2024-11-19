from flask_restful import Resource, abort

import services.usuarioService as userSrv

class UsuariosResource(Resource):
    def get(self):
        try:
            usuarios = userSrv.lista()
            return usuarios, 200
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")
        
class UsuarioResource(Resource):
    def get(self, id):
        try:
            usuario = userSrv.obtener(id)
            return usuario or {}, 200
        except Exception as ex:
            abort(400, description="Ocurrio un error inesperado")