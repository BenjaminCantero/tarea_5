class Persona:
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento

    def presentarse(self):
        print(f"Hola, soy {self.__nombre} {self.__apellido}, nacido el {self.__fecha_de_nacimiento}.")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, value):
        self.__fecha_de_nacimiento = value