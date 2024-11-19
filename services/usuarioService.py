import database

def lista() -> list[any]:
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
        print(ex)
        raise Exception("Error al obtener la lista de usuarios")
    
def obtener(id: int) -> any:
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
        return usuario
    except Exception as ex:
        print(ex)
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
        print(ex)
        raise Exception("Error al cambiar el estado activo del usuario")