import tkinter as tk
from tkinter import messagebox, ttk
from ProgramaAcademico import ProgramaAcademico
from Asignatura import Asignatura
from Estudiante import Estudiante

class GestionUniversitariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Universitaria")
        self.root.geometry("1000x600")

        # Inicialización del programa académico
        self.programa_academico = ProgramaAcademico("Ingeniería", "ING123")

        # Variables de entrada para estudiantes y grupos
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.matricula_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        self.semestre_var = tk.IntVar()
        self.numero_grupo_var = tk.StringVar()
        self.asignatura_var = tk.StringVar()

        # Crear un PanedWindow para dividir la interfaz
        paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        # Sección izquierda: Agregar estudiantes y grupos
        frame_left = tk.Frame(paned_window, width=400, padx=10, pady=10)
        paned_window.add(frame_left)

        # Sección derecha: Mostrar estudiantes y grupos en Treeviews
        frame_right = tk.Frame(paned_window, width=600, padx=10, pady=10)
        paned_window.add(frame_right)

        # --- Frame para Estudiantes ---
        frame_estudiantes = tk.LabelFrame(frame_left, text="Agregar Estudiante", padx=10, pady=10)
        frame_estudiantes.pack(fill="both", expand=True, pady=10)

        # Campos de entrada para estudiantes
        tk.Label(frame_estudiantes, text="Nombre:").grid(row=0, column=0)
        tk.Entry(frame_estudiantes, textvariable=self.nombre_var).grid(row=0, column=1)
        tk.Label(frame_estudiantes, text="Apellido:").grid(row=1, column=0)
        tk.Entry(frame_estudiantes, textvariable=self.apellido_var).grid(row=1, column=1)
        tk.Label(frame_estudiantes, text="Matrícula:").grid(row=2, column=0)
        tk.Entry(frame_estudiantes, textvariable=self.matricula_var).grid(row=2, column=1)
        tk.Label(frame_estudiantes, text="Carrera:").grid(row=3, column=0)
        tk.Entry(frame_estudiantes, textvariable=self.carrera_var).grid(row=3, column=1)
        tk.Label(frame_estudiantes, text="Semestre:").grid(row=4, column=0)
        tk.Entry(frame_estudiantes, textvariable=self.semestre_var).grid(row=4, column=1)

        # Botón para agregar estudiantes
        tk.Button(frame_estudiantes, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=5, columnspan=2, pady=5)

        # --- Frame para Grupos ---
        frame_grupos = tk.LabelFrame(frame_left, text="Agregar Grupo", padx=10, pady=10)
        frame_grupos.pack(fill="both", expand=True, pady=10)

        # Campos de entrada para grupos
        tk.Label(frame_grupos, text="Número de Grupo:").grid(row=0, column=0)
        tk.Entry(frame_grupos, textvariable=self.numero_grupo_var).grid(row=0, column=1)
        tk.Label(frame_grupos, text="Asignatura:").grid(row=1, column=0)
        tk.Entry(frame_grupos, textvariable=self.asignatura_var).grid(row=1, column=1)

        # Botón para agregar grupos
        tk.Button(frame_grupos, text="Agregar Grupo", command=self.agregar_grupo).grid(row=2, columnspan=2, pady=5)

        # --- Treeview para mostrar estudiantes ---
        self.tree_estudiantes = ttk.Treeview(frame_right, columns=("Nombre", "Apellido", "Matrícula"), show="headings")
        self.tree_estudiantes.heading("Nombre", text="Nombre")
        self.tree_estudiantes.heading("Apellido", text="Apellido")
        self.tree_estudiantes.heading("Matrícula", text="Matrícula")
        self.tree_estudiantes.pack(fill=tk.BOTH, expand=True, pady=10)

        # --- Treeview para mostrar grupos ---
        self.tree_grupos = ttk.Treeview(frame_right, columns=("Número de Grupo", "Asignatura"), show="headings")
        self.tree_grupos.heading("Número de Grupo", text="Número de Grupo")
        self.tree_grupos.heading("Asignatura", text="Asignatura")
        self.tree_grupos.pack(fill=tk.BOTH, expand=True, pady=10)

    def agregar_estudiante(self):
        # Lógica para agregar un estudiante
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        matricula = self.matricula_var.get()
        carrera = self.carrera_var.get()
        semestre = self.semestre_var.get()

        # Validación de entradas
        if not nombre or not apellido or not matricula or not carrera or semestre <= 0:
            messagebox.showerror("Error", "Complete todos los campos correctamente.")
            return

        # Agregar estudiante al Treeview
        self.tree_estudiantes.insert("", "end", values=(nombre, apellido, matricula))
        # Limpiar campos de entrada
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.matricula_var.set("")
        self.carrera_var.set("")
        self.semestre_var.set(0)

    def agregar_grupo(self):
        # Lógica para agregar un grupo
        numero_grupo = self.numero_grupo_var.get()
        asignatura_nombre = self.asignatura_var.get()

        # Validación de entradas
        if not numero_grupo or not asignatura_nombre:
            messagebox.showerror("Error", "Complete todos los campos del grupo.")
            return

        # Crear asignatura y agregar grupo al Treeview
        asignatura = Asignatura(asignatura_nombre, "ASIG123", 3)
        self.tree_grupos.insert("", "end", values=(numero_grupo, asignatura_nombre))
        # Limpiar campos de entrada
        self.numero_grupo_var.set("")
        self.asignatura_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUniversitariaApp(root)
    root.mainloop()
