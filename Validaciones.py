def validar_campos_estudiante(nombre, apellido, matricula, carrera, semestre):
    if not nombre or not apellido or not matricula or not carrera or semestre <= 0:
        return False
    return True


def validar_estudiante_existente(estudiantes, matricula):
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return True  # El estudiante ya existe
    return False  # El estudiante no existe


def validar_campos_grupo(numero_grupo, asignatura):
    if not numero_grupo or not asignatura:
        return False
    return True


def validar_profesor(nombre, apellido, fecha_nacimiento, codigo, departamento):
    if not nombre or not apellido or not fecha_nacimiento or not codigo or not departamento:
        return False
    # Aquí puedes agregar más validaciones si lo necesitas
    return True




def validar_eliminar_estudiante(estudiantes, matricula):
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return True  # El estudiante existe y se puede eliminar
    return False  # El estudiante no existe


def validar_eliminar_grupo(codigo_grupo, grupos):
    return codigo_grupo in grupos

