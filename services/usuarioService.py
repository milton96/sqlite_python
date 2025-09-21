import database
from utils.customException import ExceptionControlada

def lista() -> list[dict[str, str | int]]:
    try:
        query = """
            SELECT
                id,
                usuario,
                nombre,
                apellido,
                edad,
                STRFTIME('%Y-%m-%dT%H:%M:%S',fecha_alta) AS fecha_alta,
                activo
            FROM
                usuarios
            ORDER BY nombre ASC;
        """

        usuarios = database.select(query)
        return usuarios
    except Exception as ex:
        raise Exception("Error al obtener la lista de usuarios")
    
def obtener(id: int) -> dict | None:
    try:
        query = """
            SELECT
                id,
                usuario,
                nombre,
                apellido,
                edad,
                STRFTIME('%Y-%m-%dT%H:%M:%S',fecha_alta) AS fecha_alta,
                activo
            FROM
                usuarios
            WHERE id = ?;
        """
        usuario = database.select(query, (id,))
        if len(usuario) == 0:
            return None
        return usuario[0]
    except Exception as ex:
        raise Exception("Error al obtener el usuario")
    
def cambiar_activo(id: int, activo: int) -> None:
    try:
        query = """
            UPDATE usuarios
            SET
                activo = ?
            WHERE id = ?;
        """
        database.update(query, (activo, id,))
    except Exception as ex:
        raise Exception("Error al cambiar el estado activo del usuario")
    
def crear(usuario: dict[str, str | int]):
    try:
        query = """
            INSERT INTO usuarios
                (usuario, password, nombre, apellido, edad, activo)
            VALUES
                (?, ?, UPPER(?), UPPER(?), ?, ?)
            RETURNING id;
        """
        data = (
            usuario.get("usuario"),
            usuario.get("password"),
            usuario.get("nombre"),
            usuario.get("apellido"),
            usuario.get("edad"),
            usuario.get("activo")
        )
        id = database.insert(query, data, "id")
        return id
    except ExceptionControlada as ec:
        raise ExceptionControlada(ec.codigo, ec.message)
    except Exception as ex:
        raise Exception("Error desconocido al crear el usuario")