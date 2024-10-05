from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        self.grupos = []  # Lista de grupos a los que pertenece

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, value):
        self._carrera = value

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, value):
        self._semestre = value

    def agregar_grupo(self, grupo):
        if grupo not in self.grupos:
            self.grupos.append(grupo)

    def eliminar_grupo(self, grupo):
        if grupo in self.grupos:
            self.grupos.remove(grupo)


