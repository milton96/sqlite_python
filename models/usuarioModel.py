from pydantic import BaseModel, field_validator

class UsuarioNuevo(BaseModel):
    usuario: str | None = None
    password: str | None = None
    nombre: str
    apellido: str | None = None
    edad: int | None = None
    activo: int = 1

    @field_validator("usuario")
    def usuario_field(cls, v):
        print(v)
        return v
    
    @field_validator("password")
    def password_field(cls, v):
        print(v)
        return v
    
    @field_validator("nombre")
    def nombre_field(cls, v):
        print(v)
        return v
    
    @field_validator("apellido")
    def apellido_field(cls, v):
        print(v)
        return v
    
    @field_validator("edad")
    def edad_field(cls, v: int):
        if v < 18:
            raise ValueError("Debe ser mayor de edad")
        return v
    
    @field_validator("activo")
    def activo_field(cls, v: int):
        if v not in [0, 1]:
            raise ValueError("El estatus activo no es un valor valido")
        return v