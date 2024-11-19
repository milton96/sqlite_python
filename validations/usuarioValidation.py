from pydantic import ValidationError
from models.usuarioModel import UsuarioNuevo

def nuevo_usuario(body):
    try:
        u = UsuarioNuevo(**body)

        return u.model_dump()
    except ValidationError as ve:
        detail = ve.errors()[0]
        print(detail["ctx"]["error"])
    except Exception as ex:
        print(ex)