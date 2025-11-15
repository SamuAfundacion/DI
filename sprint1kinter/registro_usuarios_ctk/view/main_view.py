import customtkinter as ctk
import tkinter as tk

class UsuarioView:
    def __init__(self, master, controller=None):
        self.master = master
        self.controller = controller

        self.frame = ctk.CTkFrame(master)
        self.frame.pack(padx=20, pady=20, expand=True, fill="both")

        # ===== MENÚ SUPERIOR =====
        self.menubar = tk.Menu(master)
        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menu_archivo.add_command(label="Guardar Lista")
        self.menu_archivo.add_command(label="Cargar Lista")
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menubar.add_cascade(label="Ayuda")
        master.config(menu=self.menubar)

        # ===== BARRA DE OPCIONES =====
        self.frame_opciones = ctk.CTkFrame(self.frame)
        self.frame_opciones.pack(fill="x", pady=(0, 10))

        # Buscar
        ctk.CTkLabel(self.frame_opciones, text="Buscar:").pack(side="left", padx=(5, 2), pady=5)
        self.texto_busqueda = ctk.StringVar()
        self.busqueda = ctk.CTkEntry(self.frame_opciones, textvariable=self.texto_busqueda, width=200)
        self.busqueda.pack(side="left", padx=(0, 10))

        self.texto_busqueda.trace_add("write", self._on_busqueda)

        # Género (ComboBox)
        ctk.CTkLabel(self.frame_opciones, text="Género:").pack(side="left", padx=(5, 2))

        self.genero_filtro_var = tk.StringVar(value="todos")
        self.combo_genero = ctk.CTkComboBox(
            self.frame_opciones,
            values=["todos", "M", "F", "Otro"],
            width=100,
            variable=self.genero_filtro_var
        )
        self.combo_genero.pack(side="left", padx=(0, 10))
        self.genero_filtro_var.trace_add("write", self._on_filtro_genero)

        # Botones
        self.boton_eliminar = ctk.CTkButton(self.frame_opciones, text="Eliminar")
        self.boton_eliminar.pack(side="right", padx=5)

        self.boton_agregar = ctk.CTkButton(self.frame_opciones, text="Añadir")
        self.boton_agregar.pack(side="right", padx=5)

        # ===== ZONA PRINCIPAL DIVIDIDA =====
        self.frame_principal = ctk.CTkFrame(self.frame)
        self.frame_principal.pack(expand=True, fill="both")

        # --- IZQUIERDA ---
        self.frame_izquierda = ctk.CTkFrame(self.frame_principal)
        self.frame_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.scroll_frame = ctk.CTkScrollableFrame(self.frame_izquierda, label_text="Lista de Usuarios")
        self.scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # --- DERECHA ---
        self.frame_derecha = ctk.CTkFrame(self.frame_principal)
        self.frame_derecha.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.label_avatar = ctk.CTkLabel(self.frame_derecha, text="(avatar)", font=("Arial", 14))
        self.label_avatar.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.frame_derecha, text="Nombre: -")
        self.label_nombre.pack(anchor="w", padx=20)

        self.label_edad = ctk.CTkLabel(self.frame_derecha, text="Edad: -")
        self.label_edad.pack(anchor="w", padx=20)

        self.label_genero = ctk.CTkLabel(self.frame_derecha, text="Género: -")
        self.label_genero.pack(anchor="w", padx=20)

        # ===== BARRA DE ESTADO =====
        self.frame_estado = ctk.CTkFrame(self.frame)
        self.frame_estado.pack(fill="x", pady=(10, 0))

        self.label_estado = ctk.CTkLabel(self.frame_estado, text="Ok", anchor="w")
        self.label_estado.pack(side="left", padx=10)

        self.label_recuento = ctk.CTkLabel(self.frame_estado, text="Usuarios visibles: 0", anchor="e")
        self.label_recuento.pack(side="right", padx=10)
    # ================= TOPLEVEL =================
    def abrir_toplevel(self):
        ventana = ctk.CTkToplevel(self.master)
        ventana.title("Agregar Usuario")
        ventana.geometry("400x400")
        self.top = ventana

        ctk.CTkLabel(ventana, text="Nombre:").pack(pady=(10, 0))
        self.entry_nombre = ctk.CTkEntry(ventana, placeholder_text="Introduce nombre")
        self.entry_nombre.pack(pady=5)

        self.edad_var = ctk.DoubleVar(value=0)
        self.label_edad_valor = ctk.CTkLabel(ventana, text="0")
        self.label_edad_valor.pack(pady=(5, 0))

        def actualizar_label_edad(value):
            self.label_edad_valor.configure(text=f"{int(float(value))}")

        ctk.CTkSlider(
            ventana, to=100, variable=self.edad_var,
            number_of_steps=100, command=actualizar_label_edad
        ).pack(pady=10, padx=20, fill="x")

        self.genero_var = ctk.StringVar(value="M")
        ctk.CTkLabel(ventana, text="Género:").pack(pady=(10, 0))
        for g, valor in [("Masculino", "M"), ("Femenino", "F"), ("Otro", "Otro")]:
            ctk.CTkRadioButton(ventana, text=g, variable=self.genero_var, value=valor).pack(pady=2)

        self.avatar_var = ctk.StringVar(value="avatar1")
        ctk.CTkLabel(ventana, text="Avatar:").pack(pady=(10, 0))
        for g, valor in [("Avatar1", "avatar1"), ("Avatar2", "avatar2"), ("Avatar3", "avatar3")]:
            ctk.CTkRadioButton(ventana, text=g, variable=self.avatar_var, value=valor).pack(pady=2)

        self.boton_registrar = ctk.CTkButton(
            ventana,
            text="Registrar",
            command=self.controller.registrar_usuario
        )
        self.boton_registrar.pack(pady=20)

    # ================= BÚSQUEDA =================
    def _on_busqueda(self, *args):
        texto = self.texto_busqueda.get()
        if self.controller:
            self.controller.filtrar_usuarios(texto)

    def _on_filtro_genero(self, *args):
        genero = self.genero_filtro_var.get()
        if self.controller:
            self.controller.filtrar_genero(genero)

    def actualizar_estado(self, mensaje, temporizado=True):
        self.label_estado.configure(text=mensaje)

        if temporizado:
            self.label_estado.after(3000, lambda: self.label_estado.configure(text="Listo"))

    def actualizar_recuento(self, n):
        self.label_recuento.configure(text=f"Usuarios visibles: {n}")
