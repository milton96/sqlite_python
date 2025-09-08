from hashlib import sha256

from pydantic import ValidationError

from utils.customException import ExceptionControlada

def to_sha256(string: str) -> str:
    hash_string = sha256(string.encode()).hexdigest()
    return hash_string

def validate_error(ve: ValidationError):
    detail = ve.errors()[0]
    ctx = detail.get("ctx")
    if (ctx is not None):
        error = ctx.get("error")
        raise ExceptionControlada(400, error.__str__())
    
    raise ExceptionControlada(500, "Ocurrio un error desconocido en las validaciones")
