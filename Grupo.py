from Asignatura import Asignatura
from Profesor import Profesor
class Grupo:
    def __init__(self, numero_grupo, asignatura, horario, profesor=None):
        self.numero_grupo = numero_grupo
        self.asignatura = asignatura
        self.horario = horario  # Añadir horario aquí
        self.profesor = profesor  # Almacena un objeto de la clase Profesor
        self.__estudiantes = []  # Lista de estudiantes en el grupo


    def agregar_estudiante(self, estudiante):
        if estudiante in self.__estudiantes:
            print("El estudiante ya está en el grupo")
        else:
            self.__estudiantes.append(estudiante)

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} eliminado del grupo.")
                return
        print("El estudiante no existe en el grupo.")

    def asignar_profesor(self, profesor):
        self.profesor = profesor
        print(f"Profesor {profesor.nombre} asignado al grupo {self.numero_grupo}.")
