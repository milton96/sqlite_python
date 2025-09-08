class ExceptionControlada(Exception):
    def __init__(self, codigo=400, message="Ocurrio un error"):
        self.codigo = codigo
        self.message = message
        super().__init__(self.message)