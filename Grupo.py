from Asignatura import Asignatura
from Profesor import Profesor

class Grupo:
    def __init__(self, numero_grupo, asignatura, profesor):
        self.numero_grupo = numero_grupo
        self.asignatura = asignatura
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print("El estudiante ya está en el grupo")
        else:
            self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, matricula):
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                self.estudiantes.remove(estudiante)
                return
        print("El estudiante no existe en el grupo")

    def mostrar_grupo(self):
        return f"Grupo {self.numero_grupo}, Asignatura: {self.asignatura.nombre}, Profesor: {self.profesor.nombre}"
