class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, matricula, carrera, semestre):
        super().__init__(nombre, apellido)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre

    def estudiar(self, materia, horas):
        return f"Estudié {materia} durante {horas} horas"

    def presentarse(self):
        return f"{super().presentarse()} y soy estudiante de {self.__carrera} en el semestre {self.__semestre}"

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self, semestre):
        self.__semestre = semestre