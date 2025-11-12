from registro_usuarios_ctk.model import GestorUsuarios
from registro_usuarios_ctk.view import UsuarioView

class UsuarioController:
    def __init__(self, root):
        self.root = root
        # Modelo
        self.model = GestorUsuarios()
        # Vista
        self.view = UsuarioView(root)

        # Conectar botones con métodos del controlador
        self.view.boton_agregar.configure(command=self.abrir_agregar_usuario)
        # Aquí podrías conectar otros botones como eliminar o buscar

    def abrir_agregar_usuario(self):
        # Llama al Toplevel de la vista
        self.view.abrir_toplevel()
