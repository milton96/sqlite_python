from database import test_connection, select


def main() -> None:
    test_connection()
    usuarios = select("select * from usuarios;")
    print(usuarios)

if __name__ == "__main__":
    main()