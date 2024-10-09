
def validar_campos_estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
    # Validar que todos los campos estén llenos
    if not nombre or not apellido or not fecha_nacimiento or not matricula or not carrera or not semestre:
        return False
    return True

def validar_estudiante_existente(programa_academico, matricula):
    # Obtener la lista de estudiantes del programa académico
    estudiantes = programa_academico.obtener_estudiantes()  # Método para obtener estudiantes
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return True  # El estudiante ya existe
    return False  # El estudiante no existe


def validar_campos_grupo(numero_grupo, asignatura, horario):
    if not numero_grupo or not asignatura or not horario:
        return False
    return True

def validar_profesor(nombre, apellido, fecha_nacimiento, codigo, departamento):
    if not nombre or not apellido or not fecha_nacimiento or not codigo or not departamento:
        return False
    # Aquí puedes agregar más validaciones si lo necesitas
    return True

def validar_eliminar_estudiante(programa_academico, matricula):
    estudiantes = programa_academico.obtener_estudiantes()  # Obtén la lista de estudiantes
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return True
    return False


def validar_eliminar_grupo(codigo_grupo, programa_academico):
    # Obtener la lista de grupos del programa académico
    grupos = programa_academico.obtener_grupos()
    return any(grupo.numero_grupo == codigo_grupo for grupo in grupos)



