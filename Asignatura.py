class Asignatura:
    def __init__(self, nombre, codigo, creditos):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    def mostrar_informacion(self):
        return f"Asignatura: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}"
