from registro_usuarios_ctk.model import GestorUsuarios, Usuario
from registro_usuarios_ctk.view import UsuarioView
import customtkinter as ctk

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.view = UsuarioView(root, controller=self)

        # Botón agregar
        self.view.boton_agregar.configure(command=self.abrir_agregar_usuario)

        # Conectar menú archivo
        self.view.menu_archivo.entryconfig("Guardar Lista", command=self.grabar_lista)
        self.view.menu_archivo.entryconfig("Cargar Lista", command=self.cargar_lista)

        # Mostrar lista inicial
        self.actualizar_lista_scroll()

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

        # Dibujar usuarios
        for u in usuarios:
            ctk.CTkLabel(
                self.view.scroll_frame,
                text=f"{u.nombre}, {u.edad}, {u.genero}"
            ).pack(pady=2)

        # Actualizar recuento
        self.view.actualizar_recuento(len(usuarios))

    def filtrar_usuarios(self, texto):
        texto = texto.strip()

        if texto == "":
            usuarios = self.model.listar()
        else:
            usuarios = self.model.buscar(texto)

        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro aplicado")

    def filtrar_genero(self, genero):
        if genero == "todos":
            usuarios = self.model.listar()
        else:
            usuarios = self.model.buscar_genero(genero)

        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro de género aplicado")

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
