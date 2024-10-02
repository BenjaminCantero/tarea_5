import Persona

class ClaseProfesor(Persona):
    def __init__(self, numero_empleado, departamento):
        self.__numero_empleado = numero_empleado
        self.__departamento = departamento

    def enseñar(self, materia):
        print(f"El profesor está enseñando {materia}.")

    def presentarse(self):
        super().presentarse()  
        print(f"Número de empleado: {self.numero_empleado}")
        print(f"Departamento: {self.departamento}")

    @property
    def numero_empleado(self):
        return self.__numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, value):
        self.__numero_empleado = value

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, value):
        self.__departamento = value