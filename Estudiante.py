from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        self._grupo = None  # Grupo asignado al estudiante
        self._profesor = None  # Profesor asignado al estudiante
        self._grupos = []  # Lista de grupos asignados al estudiante
        self._asignaturas_estudiadas = []  # Lista de asignaturas estudiadas

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

    @property
    def grupo(self):
        return self._grupo

    @grupo.setter
    def grupo(self, value):
        self._grupo = value

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, value):
        self._profesor = value

    @property
    def grupos(self):
        return self._grupos

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

    @property
    def asignaturas_estudiadas(self):
        return self._asignaturas_estudiadas

    @asignaturas_estudiadas.setter
    def asignaturas_estudiadas(self, value):
        self._asignaturas_estudiadas = value

    def estudiar_asignatura(self, asignatura):
        """ Agregar una asignatura al historial académico del estudiante. """
        if asignatura not in self.asignaturas_estudiadas:
            self.asignaturas_estudiadas.append(asignatura)
        else:
            print("El estudiante ya ha estudiado esta asignatura.")