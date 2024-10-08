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
import Grupo

class GestionUniversitariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Universitaria")
        self.root.geometry("1200x800")
        self.root.configure(bg="white")  # Cambiar el fondo a blanco

        # Inicialización del programa académico
        self.programa_academico = ProgramaAcademico("Ingeniería", "ING123")

        # Dividir la ventana principal en dos panes
        paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        # Frame para formularios
        frame_formularios = tk.Frame(paned_window, bg="white")  # Cambiar fondo a blanco
        paned_window.add(frame_formularios)

        # Frame para la tabla
        frame_tabla = tk.Frame(paned_window)
        paned_window.add(frame_tabla)

        # -------- FORMULARIO ESTUDIANTES --------
        tk.Label(frame_formularios, text="Agregar Estudiante", bg="white", fg="black").grid(row=0, columnspan=2, pady=5)

        tk.Label(frame_formularios, text="Nombre:", bg="white", fg="black").grid(row=1, column=0)
        self.nombre_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.nombre_var).grid(row=1, column=1)

        tk.Label(frame_formularios, text="Apellido:", bg="white", fg="black").grid(row=2, column=0)
        self.apellido_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.apellido_var).grid(row=2, column=1)

        tk.Label(frame_formularios, text="Fecha de Nacimiento:", bg="white", fg="black").grid(row=3, column=0)
        self.fecha_nacimiento_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.fecha_nacimiento_var).grid(row=3, column=1)

        tk.Label(frame_formularios, text="Matrícula:", bg="white", fg="black").grid(row=4, column=0)
        self.matricula_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.matricula_var).grid(row=4, column=1)

        tk.Label(frame_formularios, text="Carrera:", bg="white", fg="black").grid(row=5, column=0)
        self.carrera_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.carrera_var).grid(row=5, column=1)

        tk.Label(frame_formularios, text="Semestre:", bg="white", fg="black").grid(row=6, column=0)
        self.semestre_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.semestre_var).grid(row=6, column=1)

        tk.Button(frame_formularios, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=7, columnspan=2, pady=5)
        tk.Button(frame_formularios, text="Eliminar Estudiante", command=self.eliminar_estudiante).grid(row=8, columnspan=2, pady=5)


        # -------- TABLA PARA ESTUDIANTES --------
        self.treeview_estudiantes = ttk.Treeview(frame_tabla, columns=("Nombre", "Apellido", "Matrícula", "Carrera/Semestre"), show="headings")
        self.treeview_estudiantes.heading("Nombre", text="Nombre")
        self.treeview_estudiantes.heading("Apellido", text="Apellido")
        self.treeview_estudiantes.heading("Matrícula", text="Matrícula")
        self.treeview_estudiantes.heading("Carrera/Semestre", text="Carrera/Semestre")
        self.treeview_estudiantes.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame_tabla, text="Lista de Estudiantes", bg="white", fg="black").pack()
        self.treeview_estudiantes.pack()

        # -------- FORMULARIO GRUPOS --------
        tk.Label(frame_formularios, text="Agregar Grupo", bg="white", fg="black").grid(row=9, columnspan=2, pady=5)

        tk.Label(frame_formularios, text="Código de Grupo:", bg="white", fg="black").grid(row=10, column=0)
        self.codigo_grupo_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.codigo_grupo_var).grid(row=10, column=1)

        tk.Label(frame_formularios, text="Asignatura:", bg="white", fg="black").grid(row=11, column=0)
        self.asignatura_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.asignatura_var).grid(row=11, column=1)

        tk.Label(frame_formularios, text="Horario:", bg="white", fg="black").grid(row=12, column=0)
        self.horario_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.horario_var).grid(row=12, column=1)

        tk.Button(frame_formularios, text="Agregar Grupo", command=self.agregar_grupo).grid(row=13, columnspan=2, pady=5)
        tk.Button(frame_formularios, text="Eliminar Grupo", command=self.eliminar_grupo).grid(row=14, columnspan=2, pady=5)

        # -------- TABLA PARA GRUPOS --------
        self.treeview_grupos = ttk.Treeview(frame_tabla, columns=("Asignatura", "Código", "Horario"), show="headings")
        self.treeview_grupos.heading("Asignatura", text="Asignatura")
        self.treeview_grupos.heading("Código", text="Código")
        self.treeview_grupos.heading("Horario", text="Horario")
        self.treeview_grupos.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame_tabla, text="Lista de Grupos", bg="white", fg="black").pack()
        self.treeview_grupos.pack()

        # -------- FORMULARIO PROFESORES --------
        tk.Label(frame_formularios, text="Agregar Profesor", bg="white", fg="black").grid(row=15, columnspan=2, pady=5)

        tk.Label(frame_formularios, text="Nombre:", bg="white", fg="black").grid(row=16, column=0)
        self.nombre_profesor_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.nombre_profesor_var).grid(row=16, column=1)

        tk.Label(frame_formularios, text="Apellido:", bg="white", fg="black").grid(row=17, column=0)
        self.apellido_profesor_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.apellido_profesor_var).grid(row=17, column=1)

        tk.Label(frame_formularios, text="Código:", bg="white", fg="black").grid(row=18, column=0)
        self.codigo_profesor_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.codigo_profesor_var).grid(row=18, column=1)

        tk.Label(frame_formularios, text="Departamento:", bg="white", fg="black").grid(row=19, column=0)
        self.departamento_profesor_var = tk.StringVar()
        tk.Entry(frame_formularios, textvariable=self.departamento_profesor_var).grid(row=19, column=1)

        tk.Button(frame_formularios, text="Agregar Profesor", command=self.agregar_profesor).grid(row=20, columnspan=2, pady=5)
        tk.Button(frame_formularios, text="Eliminar Profesor", command=self.eliminar_profesor).grid(row=21, columnspan=2, pady=5)

        # -------- TABLA PARA PROFESORES --------
        self.treeview_profesores = ttk.Treeview(frame_tabla, columns=("Nombre", "Apellido", "Código", "Departamento"), show="headings")
        self.treeview_profesores.heading("Nombre", text="Nombre")
        self.treeview_profesores.heading("Apellido", text="Apellido")
        self.treeview_profesores.heading("Código", text="Código")
        self.treeview_profesores.heading("Departamento", text="Departamento")
        self.treeview_profesores.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame_tabla, text="Lista de Profesores", bg="white", fg="black").pack()
        self.treeview_profesores.pack()

    def agregar_estudiante(self):
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        fecha_nacimiento = self.fecha_nacimiento_var.get()
        matricula = self.matricula_var.get()
        carrera = self.carrera_var.get()
        
        # Intentar convertir el semestre a entero
        try:
            semestre = int(self.semestre_var.get())
        except ValueError:
            messagebox.showerror("Error", "El semestre debe ser un número entero positivo.")
            return

        # Validar campos
        if not validar_campos_estudiante(nombre, apellido, matricula, carrera, semestre):
            messagebox.showerror("Error", "Por favor, rellene todos los campos correctamente.")
            return

        # Verificar si el estudiante ya existe
        if validar_estudiante_existente(self.programa_academico.estudiantes, matricula):
            messagebox.showerror("Error", "El estudiante ya está registrado.")
            return

        estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
        self.programa_academico.agregar_estudiante(estudiante)

        # Agregar estudiante a la tabla
        self.treeview_estudiantes.insert("", "end", values=(nombre, apellido, matricula, f"{carrera}/{semestre}"))
        self.limpiar_campos_estudiante()


    def agregar_grupo(self):
        codigo_grupo = self.codigo_grupo_var.get()
        asignatura = self.asignatura_var.get()
        horario = self.horario_var.get()

        if not validar_campos_grupo(codigo_grupo, asignatura, horario):
            return

        grupo = Grupo(codigo_grupo, asignatura, horario)
        self.programa_academico.agregar_grupo(grupo)

        # Agregar grupo a la tabla
        self.treeview_grupos.insert("", "end", values=(asignatura, codigo_grupo, horario))
        self.limpiar_campos_grupo()

    def agregar_profesor(self):
        nombre = self.nombre_profesor_var.get()
        apellido = self.apellido_profesor_var.get()
        codigo = self.codigo_profesor_var.get()
        departamento = self.departamento_profesor_var.get()

        if not validar_profesor(nombre, apellido, codigo, departamento):
            return

        profesor = Profesor(nombre, apellido, codigo, departamento)
        self.programa_academico.agregar_profesor(profesor)

        # Agregar profesor a la tabla
        self.treeview_profesores.insert("", "end", values=(nombre, apellido, codigo, departamento))
        self.limpiar_campos_profesor()

    def eliminar_estudiante(self):
        matricula = self.matricula_var.get().strip()  # Obtener la matrícula del campo y quitar espacios

        if not matricula:
            messagebox.showerror("Error", "Por favor, ingrese la matrícula del estudiante a eliminar.")
            return

        # Verificar si el estudiante existe antes de eliminar
        if not validar_eliminar_estudiante(self.programa_academico.estudiantes, matricula):
            messagebox.showerror("Error", "El estudiante no existe en el programa.")
            return

        # Llamar a la función de eliminación
        self.programa_academico.eliminar_estudiante(matricula)

        # Eliminar estudiante de la tabla
        for item in self.treeview_estudiantes.get_children():
            if self.treeview_estudiantes.item(item, "values")[2] == matricula:
                self.treeview_estudiantes.delete(item)
                break  # Salir del bucle después de eliminar

        self.limpiar_campos_estudiante()
        messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")


    def eliminar_grupo(self):
        codigo_grupo = self.codigo_grupo_var.get()

        if not validar_eliminar_grupo(codigo_grupo, self.programa_academico.grupos):
            messagebox.showerror("Error", "Grupo no encontrado o código inválido.")
            return

        self.programa_academico.eliminar_grupo(codigo_grupo)

        # Eliminar grupo de la tabla
        for item in self.treeview_grupos.get_children():
            if self.treeview_grupos.item(item, "values")[1] == codigo_grupo:
                self.treeview_grupos.delete(item)

        self.limpiar_campos_grupo()

    def eliminar_profesor(self):
        codigo = self.codigo_profesor_var.get()

        if not self.programa_academico.eliminar_profesor(codigo):
            messagebox.showerror("Error", "Profesor no encontrado o código inválido.")
            return

        # Eliminar profesor de la tabla
        for item in self.treeview_profesores.get_children():
            if self.treeview_profesores.item(item, "values")[2] == codigo:
                self.treeview_profesores.delete(item)

        self.limpiar_campos_profesor()

    def limpiar_campos_estudiante(self):
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.fecha_nacimiento_var.set("")
        self.matricula_var.set("")
        self.carrera_var.set("")
        self.semestre_var.set("")

    def limpiar_campos_grupo(self):
        self.codigo_grupo_var.set("")
        self.asignatura_var.set("")
        self.horario_var.set("")

    def limpiar_campos_profesor(self):
        self.nombre_profesor_var.set("")
        self.apellido_profesor_var.set("")
        self.codigo_profesor_var.set("")
        self.departamento_profesor_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUniversitariaApp(root)
    root.mainloop()
