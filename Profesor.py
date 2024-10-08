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

    # Opcional: puedes agregar un método __str__ para facilitar la depuración
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Número de Empleado: {self.numero_empleado}, Departamento: {self.departamento}"
