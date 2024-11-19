from database import select

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

        usuarios = select(query)
        return usuarios
    except Exception as ex:
        print(ex)
        raise Exception("Error al obtener la lista de usuarios")