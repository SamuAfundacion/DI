import threading
import time
from registro_usuarios_ctk.model import GestorUsuarios, Usuario
from registro_usuarios_ctk.view import UsuarioView
import customtkinter as ctk

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.view = UsuarioView(root, controller=self)
        self.usuario_seleccionado = None  # Para controlar la selección
        self.auto_guardado_activo = False  # Estado del auto-guardado

        # Botón agregar
        self.view.boton_agregar.configure(command=self.abrir_agregar_usuario)
        # Botón eliminar
        self.view.boton_eliminar.configure(command=self.eliminar_usuario)

        # Botón auto-guardado
        self.view.boton_autoguardado.configure(command=self.toggle_auto_guardado)

        # Conectar menú archivo
        self.view.menu_archivo.entryconfig("Guardar Lista", command=self.grabar_lista)
        self.view.menu_archivo.entryconfig("Cargar Lista", command=self.cargar_lista)

        # Mostrar lista inicial
        self.actualizar_lista_scroll()

        # Asegurar parada de hilos al cerrar
        self.root.protocol("WM_DELETE_WINDOW", self.salir)

        self.view.boton_autoguardado.configure(command=self.toggle_auto_guardado)

    # ===========================
    #   AUTO-GUARDADO
    # ===========================
    def toggle_auto_guardado(self):
        if not self.auto_guardado_activo:
            self.auto_guardado_activo = True
            self.view.boton_autoguardado.configure(text="Auto-guardar (10s): ON")
            self.view.actualizar_estado("Auto-guardado activado")
            threading.Thread(target=self.hilo_autoguardado, daemon=True).start()
        else:
            self.auto_guardado_activo = False
            self.view.boton_autoguardado.configure(text="Auto-guardar (10s): OFF")
            self.view.actualizar_estado("Auto-guardado desactivado")

    def hilo_autoguardado(self):
        while self.auto_guardado_activo:
            time.sleep(10)  # cada 10 segundos
            self.model.guardar_csv()
            # Comunicamos UI de forma segura con after()
            self.root.after(0, lambda: self.view.actualizar_estado("Auto-guardado ejecutado", temporizado=True))

    # ===========================
    #   SALIR
    # ===========================
    def salir(self):
        self.auto_guardado_activo = False  # parar hilo
        self.root.destroy()

    # ===========================
    #   TOPLEVEL
    # ===========================
    def abrir_agregar_usuario(self):
        self.view.abrir_toplevel()

    def registrar_usuario(self):
        nombre = self.view.entry_nombre.get()
        edad = int(self.view.edad_var.get())
        genero = self.view.genero_var.get()
        avatar = self.view.avatar_var.get()

        try:
            nuevo_usuario = Usuario(nombre, edad, genero, avatar)
            self.model.añadir(nuevo_usuario)
        except ValueError as e:
            self.view.actualizar_estado(f"Error: {str(e)}")
            return

        self.actualizar_lista_scroll()
        self.view.top.destroy()
        self.view.actualizar_estado("Usuario añadido correctamente")

    # ===========================
    #   LISTA Y FILTROS
    # ===========================
    def actualizar_lista_scroll(self, usuarios=None):
        if usuarios is None:
            usuarios = self.model.listar()

        # Limpiar scroll
        for widget in self.view.scroll_frame.winfo_children():
            widget.destroy()

        def seleccionar_usuario(u, label):
            for child in self.view.scroll_frame.winfo_children():
                child.configure(fg_color="transparent")
            label.configure(fg_color="#0078D7")
            self.usuario_seleccionado = u
            self.view.label_nombre.configure(text=f"Nombre: {u.nombre}")
            self.view.label_edad.configure(text=f"Edad: {u.edad}")
            self.view.label_genero.configure(text=f"Género: {u.genero}")
            self.view.label_avatar.configure(text=f"Avatar: {u.avatar}")

        for u in usuarios:
            label = ctk.CTkLabel(
                self.view.scroll_frame,
                text=f"{u.nombre}, {u.edad}, {u.genero}",
                width=250, height=30,
                corner_radius=8,
                fg_color="transparent"
            )
            label.pack(pady=2, padx=5, fill="x")
            label.bind("<Button-1>", lambda e, u=u, lbl=label: seleccionar_usuario(u, lbl))

        self.view.actualizar_recuento(len(usuarios))

    def filtrar_usuarios(self, texto):
        texto = texto.strip()
        usuarios = self.model.listar() if texto == "" else self.model.buscar(texto)
        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro aplicado")

    def filtrar_genero(self, genero):
        usuarios = self.model.listar() if genero == "todos" else self.model.buscar_genero(genero)
        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro de género aplicado")

    # ===========================
    #   ELIMINAR USUARIO
    # ===========================
    def eliminar_usuario(self):
        if self.usuario_seleccionado is None:
            self.view.actualizar_estado("No hay usuario seleccionado")
            return
        try:
            self.model._usuarios.remove(self.usuario_seleccionado)
            self.view.actualizar_estado(f"Usuario {self.usuario_seleccionado.nombre} eliminado")
            self.usuario_seleccionado = None
            self.view.label_nombre.configure(text="Nombre: -")
            self.view.label_edad.configure(text="Edad: -")
            self.view.label_genero.configure(text="Género: -")
            self.view.label_avatar.configure(text="(avatar)")
            self.actualizar_lista_scroll()
        except ValueError:
            self.view.actualizar_estado("Error al eliminar usuario")

    # ===========================
    #   ARCHIVOS
    # ===========================
    def grabar_lista(self):
        self.model.guardar_csv()
        self.view.actualizar_estado("Lista guardada")

    def cargar_lista(self):
        self.model.cargar_csv()
        self.actualizar_lista_scroll()
        self.view.actualizar_estado("Lista cargada correctamente")
