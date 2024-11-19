import sqlite3

def __connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect("sample_database.db")
        return conn
    except Exception as ex:
        print(ex)
        raise Exception("No se pudo conectar a la base de datos")
    
def __dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
    
def test_connection() -> None:
    try:
        with __connection() as conn:
            print("Conexion exitosa")
    except Exception as ex:
        print(ex)

def select(query: str, params: tuple = ()) -> list[any]:
    try:
        data = []
        with __connection() as conn:
            conn.row_factory = __dict_factory
            cur = conn.cursor()
            cur.execute(query, params)
            data = [d for d in cur.fetchall()]
            cur.close()

        return data
    except sqlite3.ProgrammingError as pe:
        print(pe)
        raise Exception("Error al obtener datos, es probable que las condiciones no se cumplan completamente")
    except Exception as ex:
        print(ex)
        raise Exception("Error al obtener datos")
    
def insert(query: str, params: tuple, last_id: str = None) -> int | str | None:
    try:
        id = None
        with __connection() as conn:
            conn.row_factory = __dict_factory
            cur = conn.cursor()
            cur.execute(query, params)
            
            if last_id is not None:
                id = cur.fetchone()[last_id]

            cur.close()

        return id
    except sqlite3.ProgrammingError as pe:
        print(pe)
        raise Exception("Error al insertar los datos")
    except Exception as ex:
        print(ex)
        raise Exception("Ocurrio un error desconocido al insertar los datos")

def update(query: str, params: tuple, updated_row: bool = False) -> dict | None:
    try:
        updated = None
        with __connection() as conn:
            conn.row_factory = __dict_factory
            cur = conn.cursor()
            cur.execute(query, params)

            if updated_row:
                updated = cur.fetchone()

            cur.close()

        return updated
    except sqlite3.ProgrammingError as pe:
        print(pe)
        raise Exception("Error al actualizar los datos")
    except Exception as ex:
        print(ex)
        raise Exception("Ocurrio un error desconocido al actualizar los datos")