from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        self._grupo = None  # Grupo asignado al estudiante
        self._profesor = None  # Profesor asignado al estudiante

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

    def asignar_grupo(self, grupo):
        self.grupo = grupo  # Asigna el grupo al estudiante

    def asignar_profesor(self, profesor):
        self.profesor = profesor  # Asigna el profesor al estudiante


