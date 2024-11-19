from database import test_connection, select


def main() -> None:
    try:
        test_connection()
        usuarios = select("select * from usuarios where usuario = ?;", ('a',))
        print(usuarios)
        lista_usuarios = select("select * from usuarios;")
        print(lista_usuarios)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()