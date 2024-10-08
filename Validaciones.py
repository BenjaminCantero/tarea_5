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


def validar_profesor(nombre, apellido, numero_empleado, departamento):
    """Valida que los campos del profesor no estén vacíos."""
    if not nombre or not apellido or not numero_empleado or not departamento:
        return False
    return True

def validar_eliminar_estudiante(estudiantes, matricula):
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return True  # El estudiante existe y se puede eliminar
    return False  # El estudiante no existe


def validar_eliminar_grupo(grupos, numero_grupo):
    """Valida que un grupo con el número proporcionado existe para poder eliminarlo."""
    if numero_grupo in grupos:
        return True  # El grupo existe y se puede eliminar
    return False  # El grupo no existe
