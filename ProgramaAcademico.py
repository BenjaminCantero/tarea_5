from Grupo import Grupo
from Profesor import Profesor

class ProgramaAcademico:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.grupos = {}  # Diccionario para almacenar los grupos
        self.estudiantes = []  # Lista para almacenar los estudiantes
        self.profesores = []  # Lista para almacenar los profesores

    def agregar_grupo(self, numero_grupo, asignatura, horario):
        """ Agregar un nuevo grupo al programa académico. """
        if numero_grupo in self.grupos:
            raise ValueError(f"El grupo {numero_grupo} ya existe.")
        grupo = Grupo(numero_grupo, asignatura, horario)
        self.grupos[numero_grupo] = grupo
        print(f"Grupo {numero_grupo} agregado al programa.")

    def eliminar_grupo(self, numero_grupo):
        """ Eliminar un grupo del programa académico. """
        if numero_grupo in self.grupos:
            del self.grupos[numero_grupo]
            print(f"Grupo {numero_grupo} eliminado del programa.")
        else:
            raise ValueError(f"El grupo {numero_grupo} no existe.")

    def agregar_estudiante(self, estudiante):
        """ Agregar un estudiante al programa académico. """
        if not any(e.matricula == estudiante.matricula for e in self.estudiantes):
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al programa.")
        else:
            print("El estudiante ya está registrado en el programa.")

    def eliminar_estudiante(self, matricula):
        """ Eliminar un estudiante del programa académico por su matrícula. """
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} eliminado del programa.")
                return
        raise ValueError("El estudiante no existe en el programa.")

    def agregar_profesor(self, profesor):
        """ Agregar un profesor al programa académico. """
        if not any(p.codigo == profesor.codigo for p in self.profesores):
            self.profesores.append(profesor)
            print(f"Profesor {profesor.nombre} {profesor.apellido} agregado al programa.")
        else:
            print("El profesor ya está registrado en el programa.")

    def obtener_grupos(self):
        """ Obtener la lista de grupos en el programa académico. """
        return list(self.grupos.values())

    def obtener_estudiantes(self):
        """ Obtener la lista de estudiantes en el programa académico. """
        return self.estudiantes  # Retornar la lista de estudiantes

    def obtener_profesores(self):
        """ Obtener la lista de profesores en el programa académico. """
        return self.profesores  # Retornar la lista de profesores
