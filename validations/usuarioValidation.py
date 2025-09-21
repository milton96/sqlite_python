from pydantic import ValidationError
from models.usuarioModel import UsuarioNuevo
from utils.common import validate_error
from utils.customException import ExceptionControlada

def nuevo_usuario(body):
    try:
        u = UsuarioNuevo(**body)

        return u.model_dump()
    except ValidationError as ve:
        validate_error(ve)
    except ExceptionControlada as ec:
        raise ExceptionControlada(ec.codigo, ec.message)
    except Exception as ex:
        print(ex)