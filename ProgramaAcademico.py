from Grupo import Grupo

class ProgramaAcademico:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.grupos = {}  # Diccionario para almacenar los grupos

    def agregar_grupo(self, numero_grupo, asignatura, profesor):
        if numero_grupo in self.grupos:
            raise ValueError(f"El grupo {numero_grupo} ya existe.")
        grupo = Grupo(numero_grupo, asignatura, profesor)
        self.grupos[numero_grupo] = grupo
        print(f"Grupo {numero_grupo} agregado al programa.")

    def eliminar_grupo(self, numero_grupo):
        if numero_grupo in self.grupos:
            del self.grupos[numero_grupo]
            print(f"Grupo {numero_grupo} eliminado del programa.")
        else:
            raise ValueError(f"El grupo {numero_grupo} no existe.")

    def obtener_grupos(self):
        return list(self.grupos.values())
