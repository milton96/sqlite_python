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