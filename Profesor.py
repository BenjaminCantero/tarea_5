from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, codigo, departamento):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._codigo = codigo
        self._departamento = departamento
        self._asignaturas = []  # Lista de asignaturas asignadas al profesor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value

    @property
    def asignaturas(self):
        return self._asignaturas

    def asignar_asignatura(self, asignatura):
        """ Agregar una asignatura a la lista de asignaturas asignadas al profesor. """
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
        else:
            print("El profesor ya tiene asignada esta asignatura.")

    # Opcional: puedes agregar un método __str__ para facilitar la depuración
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Código: {self.codigo}, Departamento: {self.departamento}"