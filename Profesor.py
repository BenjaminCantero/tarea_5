from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, value):
        self._numero_empleado = value

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value

    def presentarse(self):
        return f"{super().presentarse()} y soy profesor del departamento de {self.departamento}"
