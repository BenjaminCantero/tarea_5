import tkinter as tk
from tkinter import ttk, messagebox
from Validaciones import (
    validar_campos_estudiante,
    validar_estudiante_existente,
    validar_campos_grupo,
    validar_profesor,
    validar_eliminar_estudiante,
    validar_eliminar_grupo,
)
from Estudiante import Estudiante
from Profesor import Profesor
from ProgramaAcademico import ProgramaAcademico
from Grupo import Grupo
from Asignatura import Asignatura

class GestionUniversitariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Universitaria")
        self.root.geometry("800x600")

        # Inicialización del programa académico
        self.programa_academico = ProgramaAcademico("Ingeniería", "ING123")

        # Crear pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de Estudiantes
        self.tab_estudiantes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_estudiantes, text="Estudiantes")
        self.setup_estudiantes_tab()

        # Pestaña de Profesores
        self.tab_profesores = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_profesores, text="Profesores")
        self.setup_profesores_tab()

        # Pestaña de Grupos
        self.tab_grupos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_grupos, text="Grupos")
        self.setup_grupos_tab()

        # Pestaña de Asignaturas
        self.tab_asignaturas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_asignaturas, text="Asignaturas")
        self.setup_asignaturas_tab()

        self.tab_inscripcion = ttk.Frame(self.notebook)
        self.tab_estudiar = ttk.Frame(self.notebook)
        self.tab_ensenar = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_inscripcion, text="Inscripción")
        self.notebook.add(self.tab_estudiar, text="Estudiar")
        self.notebook.add(self.tab_ensenar, text="Enseñar")

        self.setup_inscripcion_tab()
        self.setup_estudiar_tab()
        self.setup_ensenar_tab()

    def setup_estudiantes_tab(self):
        form_frame = ttk.LabelFrame(self.tab_estudiantes, text="Agregar Estudiante")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.nombre_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Apellido:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.apellido_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.apellido_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Fecha de Nacimiento:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.fecha_nacimiento_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.fecha_nacimiento_var).grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Matrícula:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.matricula_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.matricula_var).grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Carrera:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.carrera_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.carrera_var).grid(row=4, column=1, padx=5, pady=2)

        # Add Semester Field
        ttk.Label(form_frame, text="Semestre:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=2)
        self.semestre_var = tk.StringVar()  # Define the variable for the semester
        ttk.Entry(form_frame, textvariable=self.semestre_var).grid(row=5, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=6, column=0, pady=5)
        ttk.Button(form_frame, text="Eliminar Estudiante", command=self.eliminar_estudiante).grid(row=6, column=1, pady=5)
        ttk.Button(form_frame, text="Limpiar", command=self.limpiar_estudiante).grid(row=6, column=2, pady=5)

        # Lista de estudiantes
        list_frame = ttk.Frame(self.tab_estudiantes)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_estudiantes = ttk.Treeview(list_frame, columns=("Nombre", "Apellido", "Matrícula", "Carrera"), show="headings")
        self.treeview_estudiantes.heading("Nombre", text="Nombre")
        self.treeview_estudiantes.heading("Apellido", text="Apellido")
        self.treeview_estudiantes.heading("Matrícula", text="Matrícula")
        self.treeview_estudiantes.heading("Carrera", text="Carrera")
        self.treeview_estudiantes.pack(fill=tk.BOTH, expand=True)

    def setup_profesores_tab(self):
        form_frame = ttk.LabelFrame(self.tab_profesores, text="Agregar Profesor")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.nombre_profesor_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_profesor_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Apellido:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.apellido_profesor_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.apellido_profesor_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Fecha de Nacimiento:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.fecha_nacimiento_profesor_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.fecha_nacimiento_profesor_var).grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Número de Empleado:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_profesor_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_profesor_var).grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Departamento:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.departamento_profesor_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.departamento_profesor_var).grid(row=4, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Agregar Profesor", command=self.agregar_profesor).grid(row=5, column=0, pady=5)
        ttk.Button(form_frame, text="Eliminar Profesor", command=self.eliminar_profesor).grid(row=5, column=1, pady=5)
        ttk.Button(form_frame, text="Limpiar", command=self.limpiar_profesor).grid(row=5, column=2, pady=5)

        # Lista de profesores
        list_frame = ttk.Frame(self.tab_profesores)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_profesores = ttk.Treeview(list_frame, columns=("Nombre", "Apellido", "Código", "Departamento"), show="headings")
        self.treeview_profesores.heading("Nombre", text="Nombre")
        self.treeview_profesores.heading("Apellido", text="Apellido")
        self.treeview_profesores.heading("Código", text="Código")
        self.treeview_profesores.heading("Departamento", text="Departamento")
        self.treeview_profesores.pack(fill=tk.BOTH, expand=True)

    def setup_grupos_tab(self):
        form_frame = ttk.LabelFrame(self.tab_grupos, text="Gestión de Grupos")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Número de Grupo:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_grupo_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_grupo_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Asignatura:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.asignatura_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.asignatura_var).grid(row=1, column=1, padx=5, pady=2)

        # Agregar el campo para el horario
        ttk.Label(form_frame, text="Horario:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.horario_var = tk.StringVar()  # Asegúrate de definir la variable aquí
        ttk.Entry(form_frame, textvariable=self.horario_var).grid(row=2, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Agregar Grupo", command=self.agregar_grupo).grid(row=3, column=0, pady=5)
        ttk.Button(form_frame, text="Eliminar Grupo", command=self.eliminar_grupo).grid(row=3, column=1, pady=5)
        ttk.Button(form_frame, text="Limpiar", command=self.limpiar_grupo).grid(row=3, column=2, pady=5)

        # Lista de grupos
        list_frame = ttk.Frame(self.tab_grupos)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_grupos = ttk.Treeview(list_frame, columns=("Código", "Asignatura", "Horario"), show="headings")
        self.treeview_grupos.heading("Código", text="Código")
        self.treeview_grupos.heading("Asignatura", text="Asignatura")
        self.treeview_grupos.heading("Horario", text="Horario")  # Asegúrate de agregar la columna de horario
        self.treeview_grupos.pack(fill=tk.BOTH, expand=True)

    def setup_asignaturas_tab(self):
        form_frame = ttk.LabelFrame(self.tab_asignaturas, text="Agregar Asignatura")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.nombre_asignatura_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_asignatura_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Código:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_asignatura_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_asignatura_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Créditos:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.creditos_asignatura_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.creditos_asignatura_var).grid(row=2, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Agregar Asignatura", command=self.agregar_asignatura).grid(row=3, column=0, pady=5)
        ttk.Button(form_frame, text="Eliminar Asignatura", command=self.eliminar_asignatura).grid(row=3, column=1, pady=5)
        ttk.Button(form_frame, text="Limpiar", command=self.limpiar_asignatura).grid(row=3, column=2, pady=5)

        # Lista de asignaturas
        list_frame = ttk.Frame(self.tab_asignaturas)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_asignaturas = ttk.Treeview(list_frame, columns=("Nombre", "Código", "Créditos"), show="headings")
        self.treeview_asignaturas.heading("Nombre", text="Nombre")
        self.treeview_asignaturas.heading("Código", text="Código")
        self.treeview_asignaturas.heading("Créditos", text="Créditos")
        self.treeview_asignaturas.pack(fill=tk.BOTH, expand=True)

        
    def setup_inscripcion_tab(self):
        form_frame = ttk.LabelFrame(self.tab_inscripcion, text="Inscripción a Grupo")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Matrícula del Estudiante:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.matricula_inscripcion_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.matricula_inscripcion_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Código del Grupo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_grupo_inscripcion_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_grupo_inscripcion_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Inscribir", command=self.inscribir_estudiante).grid(row=2, column=0, columnspan=2, pady=5)

        # Lista de inscripciones
        list_frame = ttk.Frame(self.tab_inscripcion)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_inscripciones = ttk.Treeview(list_frame, columns=("Estudiante", "Grupo", "Asignatura"), show="headings")
        self.treeview_inscripciones.heading("Estudiante", text="Estudiante")
        self.treeview_inscripciones.heading("Grupo", text="Grupo")
        self.treeview_inscripciones.heading("Asignatura", text="Asignatura")
        self.treeview_inscripciones.pack(fill=tk.BOTH, expand=True)

    def setup_estudiar_tab(self):
        form_frame = ttk.LabelFrame(self.tab_estudiar, text="Estudiar Asignatura")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Matrícula del Estudiante:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.matricula_estudiar_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.matricula_estudiar_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Código de la Asignatura:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_asignatura_estudiar_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_asignatura_estudiar_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Estudiar", command=self.estudiar_asignatura).grid(row=2, column=0, columnspan=2, pady=5)

        # Lista de estudios
        list_frame = ttk.Frame(self.tab_estudiar)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_estudios = ttk.Treeview(list_frame, columns=("Estudiante", "Asignatura", "Estado"), show="headings")
        self.treeview_estudios.heading("Estudiante", text="Estudiante")
        self.treeview_estudios.heading("Asignatura", text="Asignatura")
        self.treeview_estudios.heading("Estado", text="Estado")
        self.treeview_estudios.pack(fill=tk.BOTH, expand=True)

    def setup_ensenar_tab(self):
        form_frame = ttk.LabelFrame(self.tab_ensenar, text="Enseñar Asignatura")
        form_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(form_frame, text="Código del Profesor:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_profesor_ensenar_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_profesor_ensenar_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Código de la Asignatura:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.codigo_asignatura_ensenar_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_asignatura_ensenar_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Button(form_frame, text="Asignar", command=self.asignar_profesor).grid(row=2, column=0, columnspan=2, pady=5)

        # Lista de asignaciones
        list_frame = ttk.Frame(self.tab_ensenar)
        list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.treeview_asignaciones = ttk.Treeview(list_frame, columns=("Profesor", "Asignatura"), show="headings")
        self.treeview_asignaciones.heading("Profesor", text="Profesor")
        self.treeview_asignaciones.heading("Asignatura", text="Asignatura")
        self.treeview_asignaciones.pack(fill=tk.BOTH, expand=True)

    def inscribir_estudiante(self):
        matricula = self.matricula_inscripcion_var.get()
        codigo_grupo = self.codigo_grupo_inscripcion_var.get()

        estudiante = self.programa_academico.buscar_estudiante(matricula)
        grupo = self.programa_academico.buscar_grupo(codigo_grupo)

        if estudiante and grupo:
            grupo.agregar_estudiante(estudiante)
            self.treeview_inscripciones.insert("", tk.END, values=(estudiante.nombre, grupo.codigo, grupo.asignatura))
            messagebox.showinfo("Éxito", "Estudiante inscrito correctamente.")
        else:
            messagebox.showerror("Error", "Estudiante o grupo no encontrado.")

    def estudiar_asignatura(self):
        matricula = self.matricula_estudiar_var.get()
        codigo_asignatura = self.codigo_asignatura_estudiar_var.get()

        estudiante = self.programa_academico.buscar_estudiante(matricula)
        asignatura = self.programa_academico.buscar_asignatura(codigo_asignatura)

        if estudiante and asignatura:
            estudiante.estudiar_asignatura(asignatura)
            self.treeview_estudios.insert("", tk.END, values=(estudiante.nombre, asignatura.nombre, "En progreso"))
            messagebox.showinfo("Éxito", "Estudiante ha comenzado a estudiar la asignatura.")
        else:
            messagebox.showerror("Error", "Estudiante o asignatura no encontrada.")

    def asignar_profesor(self):
        codigo_profesor = self.codigo_profesor_ensenar_var.get()
        codigo_asignatura = self.codigo_asignatura_ensenar_var.get()

        profesor = self.programa_academico.buscar_profesor(codigo_profesor)
        asignatura = self.programa_academico.buscar_asignatura(codigo_asignatura)

        if profesor and asignatura:
            profesor.asignar_asignatura(asignatura)
            self.treeview_asignaciones.insert("", tk.END, values=(profesor.nombre, asignatura.nombre))
            messagebox.showinfo("Éxito", "Profesor asignado a la asignatura correctamente.")
        else:
            messagebox.showerror("Error", "Profesor o asignatura no encontrada.")

    # Métodos para limpiar los campos de cada pestaña
    def limpiar_estudiante(self):
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.fecha_nacimiento_var.set("")
        self.matricula_var.set("")
        self.carrera_var.set("")
        self.semestre_var.set("")  # Limpiar semestre

    def limpiar_profesor(self):
        self.nombre_profesor_var.set("")
        self.apellido_profesor_var.set("")
        self.fecha_nacimiento_profesor_var.set("")
        self.codigo_profesor_var.set("")
        self.departamento_profesor_var.set("")

    def limpiar_grupo(self):
        self.codigo_grupo_var.set("")
        self.asignatura_var.set("")
        self.horario_var.set("")

    def limpiar_asignatura(self):
        self.nombre_asignatura_var.set("")
        self.codigo_asignatura_var.set("")
        self.creditos_asignatura_var.set("")

    def agregar_estudiante(self):
        try:
            nombre = self.nombre_var.get()
            apellido = self.apellido_var.get()
            fecha_nacimiento = self.fecha_nacimiento_var.get()
            matricula = self.matricula_var.get()
            carrera = self.carrera_var.get()
            semestre = self.semestre_var.get()  # Get the semester value

            if validar_campos_estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
                nuevo_estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
                if not validar_estudiante_existente(self.programa_academico, matricula):
                    self.programa_academico.agregar_estudiante(nuevo_estudiante)
                    self.treeview_estudiantes.insert("", tk.END, values=(nombre, apellido, matricula, carrera))
                    messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
                else:
                    messagebox.showerror("Error", "El estudiante ya existe.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el estudiante: {str(e)}")

    def eliminar_estudiante(self):
        try:
            selected_item = self.treeview_estudiantes.selection()
            if selected_item:  # Verifica si hay una selección
                estudiante_info = self.treeview_estudiantes.item(selected_item, "values")
                matricula = estudiante_info[2]

                if validar_eliminar_estudiante(self.programa_academico, matricula):
                    self.programa_academico.eliminar_estudiante(matricula)
                    self.treeview_estudiantes.delete(selected_item)
                    messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el estudiante.")
            else:
                messagebox.showerror("Error", "Seleccione un estudiante para eliminar.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el estudiante: {str(e)}")

    def agregar_profesor(self):
        try:
            nombre = self.nombre_profesor_var.get()
            apellido = self.apellido_profesor_var.get()
            fecha_nacimiento = self.fecha_nacimiento_profesor_var.get()
            codigo = self.codigo_profesor_var.get()
            departamento = self.departamento_profesor_var.get()

            if validar_profesor(nombre, apellido, fecha_nacimiento, codigo, departamento):
                nuevo_profesor = Profesor(nombre, apellido, fecha_nacimiento, codigo, departamento)
                self.programa_academico.agregar_profesor(nuevo_profesor)
                self.treeview_profesores.insert("", tk.END, values=(nombre, apellido, codigo, departamento))
                messagebox.showinfo("Éxito", "Profesor agregado correctamente.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el profesor: {str(e)}")

    def eliminar_profesor(self):
        try:
            selected_item = self.treeview_profesores.selection()
            if selected_item:
                profesor_info = self.treeview_profesores.item(selected_item, "values")
                codigo = profesor_info[2]
                self.programa_academico.eliminar_profesor(codigo)
                self.treeview_profesores.delete(selected_item)
                messagebox.showinfo("Éxito", "Profesor eliminado correctamente.")
            else:
                messagebox.showerror("Error", "Seleccione un profesor para eliminar.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el profesor: {str(e)}")

    def agregar_grupo(self):
        try:
            codigo = self.codigo_grupo_var.get()  # Obtener el número de grupo
            asignatura = self.asignatura_var.get()  # Obtener la asignatura
            horario = self.horario_var.get()  # Obtener el horario

            # Validar todos los campos necesarios, incluyendo horario
            if validar_campos_grupo(codigo, asignatura, horario):  # Validar con todos los parámetros
                self.programa_academico.agregar_grupo(codigo, asignatura, horario)  # Llamar al método con todos los argumentos
                self.treeview_grupos.insert("", tk.END, values=(codigo, asignatura, horario))
                messagebox.showinfo("Éxito", "Grupo agregado correctamente.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el grupo: {str(e)}")

    def eliminar_grupo(self):
        try:
            selected_item = self.treeview_grupos.selection()
            if selected_item:
                grupo_info = self.treeview_grupos.item(selected_item, "values")
                codigo = grupo_info[0]

                # Verifica si el grupo puede ser eliminado
                if validar_eliminar_grupo(codigo, self.programa_academico):
                    self.programa_academico.eliminar_grupo(codigo)
                    self.treeview_grupos.delete(selected_item)
                    messagebox.showinfo("Éxito", "Grupo eliminado correctamente.")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el grupo.")
            else:
                messagebox.showerror("Error", "Seleccione un grupo para eliminar.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el grupo: {str(e)}")


    def agregar_asignatura(self):
        try:
            nombre = self.nombre_asignatura_var.get()
            codigo = self.codigo_asignatura_var.get()
            creditos = self.creditos_asignatura_var.get()

            if nombre and codigo and creditos:
                nueva_asignatura = Asignatura(nombre, codigo, creditos)
                self.programa_academico.agregar_asignatura(nueva_asignatura)
                self.treeview_asignaturas.insert("", tk.END, values=(nombre, codigo, creditos))
                messagebox.showinfo("Éxito", "Asignatura agregada correctamente.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar la asignatura: {str(e)}")

    def eliminar_asignatura(self):
        try:
            # Supongamos que tienes un treeview para seleccionar asignaturas
            selected_item = self.treeview_asignaturas.selection()
            if selected_item:
                asignatura_info = self.treeview_asignaturas.item(selected_item, "values")
                codigo_asignatura = asignatura_info[1]  # Asumiendo que el código está en el segundo índice

                self.programa_academico.eliminar_asignatura(codigo_asignatura)
                self.treeview_asignaturas.delete(selected_item)
                messagebox.showinfo("Éxito", "Asignatura eliminada correctamente.")
            else:
                messagebox.showerror("Error", "Seleccione una asignatura para eliminar.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar la asignatura: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUniversitariaApp(root)
    root.mainloop()
