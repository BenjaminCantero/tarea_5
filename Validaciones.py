import Grupo
import ProgramaAcademico


class Grupo:
    # ...

    def agregar_estudiante(self, estudiante):
        if estudiante in self.__estudiantes:
            print("El estudiante ya está en el grupo")
        else:
            self.__estudiantes.append(estudiante)

    def eliminar_estudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.matricula == matricula:
                self.__estudiantes.remove(estudiante)
                return
        print("El estudiante no existe en el grupo")

class ProgramaAcademico:
    # ...

    def agregar_grupo(self, grupo):
        if grupo in self.__grupos:
            print("El grupo ya está en el programa académico")
        else:
            self.__grupos.append(grupo)

    def eliminar_grupo(self, numero_grupo):
        for grupo in self.__grupos:
            if grupo.numero_grupo == numero_grupo:
                self.__grupos.remove(grupo)
                return
        print("El grupo no existe en el programa académico")