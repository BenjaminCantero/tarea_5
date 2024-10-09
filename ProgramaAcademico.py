from Grupo import Grupo
from Profesor import Profesor

class ProgramaAcademico:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []
        self.profesores = []
        self.grupos = {}
        self.asignaturas = []  # Lista de asignaturas

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

    # Método para agregar un profesor
    def agregar_profesor(self, profesor):
        """ Agregar un profesor al programa académico. """
        self.profesores.append(profesor)
        print(f"Profesor {profesor.nombre} agregado al programa.")

    # Método para eliminar un profesor
    def eliminar_profesor(self, codigo_profesor):
        for profesor in self.profesores:
            if profesor.codigo == codigo_profesor:
                self.profesores.remove(profesor)
                print(f"Profesor {profesor.nombre} eliminado del programa.")
                return True  # Retorna True si se eliminó exitosamente
        return False  # Retorna False si no se encontró el profesor
    
    def eliminar_asignatura(self, codigo_asignatura):
        """ Eliminar una asignatura del programa académico. """
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo_asignatura:  # Asumiendo que la asignatura tiene un atributo 'codigo'
                self.asignaturas.remove(asignatura)
                print(f"Asignatura {asignatura.nombre} eliminada del programa.")
                return
        raise ValueError("La asignatura no existe en el programa.")
    
    def buscar_estudiante(self, matricula):
        """ Buscar un estudiante en el programa académico por su matrícula. """
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        return None
    
    def buscar_grupo(self, codigo_grupo):
        """ Buscar un grupo en el programa académico por su código. """
        return self.grupos.get(codigo_grupo)
    
    def buscar_profesor(self, codigo_profesor):
        """ Buscar un profesor en el programa académico por su código. """
        for profesor in self.profesores:
            if profesor.codigo == codigo_profesor:
                return profesor
        return None
    
    def buscar_asignatura(self, codigo_asignatura):
        """ Buscar una asignatura en el programa académico por su código. """
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo_asignatura:
                return asignatura
        return None

    
    def agregar_asignatura(self, asignatura):
       self.asignaturas.append(asignatura)

    def obtener_asignaturas(self):
        return self.asignaturas


    def obtener_grupos(self):
        """ Obtener la lista de grupos en el programa académico. """
        return list(self.grupos.values())

    def obtener_estudiantes(self):
        """ Obtener la lista de estudiantes en el programa académico. """
        return self.estudiantes  # Retornar la lista de estudiantes

    def obtener_profesores(self):
        """ Obtener la lista de profesores en el programa académico. """
        return self.profesores  # Retornar la lista de profesores
