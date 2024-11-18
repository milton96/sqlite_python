import sqlite3

def __connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect("sample_database.db")
        return conn
    except Exception as ex:
        raise Exception("No se pudo conectar a la base de datos")
    
def test_connection() -> None:
    try:
        with __connection() as conn:
            print("Conexion exitosa")
    except Exception as ex:
        print(ex)