from hashlib import sha256
import re
from flask import Request, json
from pydantic import ValidationError
from utils.customException import ExceptionControlada

def to_sha256(string: str) -> str:
    hash_string = sha256(string.encode()).hexdigest()
    return hash_string

def get_body(request: Request) -> dict | None:
    data = request.get_data()
    if len(data) > 0:
        return json.loads(data)
    return None

def validate_error(ve: ValidationError):
    try:
        detail = ve.errors()[0]
        ctx = detail.get("ctx")
        msg = detail.get("msg")
        if (ctx is not None):
            error = ctx.get("error")
            raise ExceptionControlada(400, error.__str__())
        elif msg is not None:
            raise ExceptionControlada(400, msg)
        else:
            raise ExceptionControlada(500, "Ocurrio una validacion desconocida en las validaciones")
    except ExceptionControlada as ec:
        raise ExceptionControlada(ec.codigo, ec.message)
    except Exception as ex:
        raise ExceptionControlada(500, "Ocurrio un error desconocido en las validaciones")

def validate_regex(value: str, regex: re.Pattern[str] | str) -> bool:
    try:
        match = re.match(regex, value)
        return True if match is not None else False
    except Exception as ex:
        return False