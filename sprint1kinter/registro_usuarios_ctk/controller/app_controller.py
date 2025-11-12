from registro_usuarios_ctk.model import GestorUsuarios, Usuario
from registro_usuarios_ctk.view import UsuarioView
import customtkinter as ctk

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.view = UsuarioView(root)

        # Configurar botón agregar
        self.view.boton_agregar.configure(command=self.abrir_agregar_usuario)

        # Mostrar usuarios iniciales
        self.actualizar_lista_scroll()

    def abrir_agregar_usuario(self):
        self.view.abrir_toplevel(self)

    def registrar_usuario(self):
        """Leer campos de la vista, crear usuario y actualizar lista"""
        nombre = self.view.entry_nombre.get()
        edad = int(self.view.edad_var.get())
        genero = self.view.genero_var.get()

        try:
            nuevo_usuario = Usuario(nombre, edad, genero, avatar="")
            self.model.añadir(nuevo_usuario)
        except ValueError as e:
            print("Error:", e)
            return

        # Actualizar scroll
        self.actualizar_lista_scroll()

        # Cerrar top-level
        self.view.top.destroy()

    def actualizar_lista_scroll(self):
        # Limpiar scroll
        for widget in self.view.scroll_frame.winfo_children():
            widget.destroy()

        # Mostrar usuarios
        for u in self.model.listar():
            ctk.CTkLabel(
                self.view.scroll_frame, text=f"{u.nombre}, {u.edad}, {u.genero}"
            ).pack(pady=2)
