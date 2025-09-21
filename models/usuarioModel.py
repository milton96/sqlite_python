from typing import Optional
from pydantic import BaseModel, field_validator
from utils.common import to_sha256, validate_regex

import utils.str_regex as str_regex

class UsuarioNuevo(BaseModel):
    usuario: Optional[str]
    password: Optional[str]
    nombre: Optional[str]
    apellido: Optional[str] = None
    edad: Optional[int] = None
    activo: Optional[int] = 1

    @field_validator("usuario")
    def usuario_field(cls, v: str):
        if v is None or v.strip() == "":
            raise ValueError("El usuario es requerido")
        valido = validate_regex(v, str_regex.user)
        if not valido:
            raise ValueError("El formato del usuario no es valido")
        return v
    
    @field_validator("password")
    def password_field(cls, v: str):
        if v is None or v.strip() == "":
            raise ValueError("La contrasenia es requerida")
        valido = validate_regex(v, str_regex.password)
        if not valido:
            raise ValueError("La contrasenia debe contener al menos una mayuscula, una minuscula, un numero, un caracter especial y tener minimo 8 caracteres")
        return to_sha256(v)
    
    @field_validator("nombre")
    def nombre_field(cls, v: str):
        if v is None or v.strip() == "":
            raise ValueError("El nombre es requerido")
        valido = validate_regex(v, str_regex.name)
        if not valido:
            raise ValueError("El nombre contiene caracteres no permitidos")
        return v
    
    @field_validator("apellido")
    def apellido_field(cls, v: str):
        if v is None or v.strip() == "":
            return None
        valido = validate_regex(v, str_regex.name)
        if not valido:
            raise ValueError("El apellido contiene caracteres no permitidos")
        return v
    
    @field_validator("edad")
    def edad_field(cls, v: int):
        if v is not None and v < 18:
            raise ValueError("Debe ser mayor de edad")
        return v
    
    @field_validator("activo")
    def activo_field(cls, v: int):
        if v not in [0, 1]:
            raise ValueError("El estatus activo no es un valor valido")
        return v