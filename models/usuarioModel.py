from typing import Optional
from pydantic import BaseModel, field_validator

from utils.common import to_sha256

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
        return v
    
    @field_validator("password")
    def password_field(cls, v: str):
        if v is None or v.strip() == "":
            raise ValueError("La contrasenia es requerida")
        return to_sha256(v)
    
    @field_validator("nombre")
    def nombre_field(cls, v: str):
        if v is None or v.strip() == "":
            raise ValueError("El nombre es requerido")
        return v
    
    @field_validator("apellido")
    def apellido_field(cls, v: str):
        if v is None or v.strip() == "":
            return None
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