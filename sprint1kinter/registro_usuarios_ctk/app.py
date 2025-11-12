
import customtkinter as ctk

from registro_usuarios_ctk.controller import UsuarioController

if __name__ == "__main__":
    # 1. Configurar la ventana principal de la aplicación
    app = ctk.CTk()
    app.title("Ejemplo Simple de MVC")
    app.geometry("600x600")

    # 2. Crear una instancia del Controlador
    # Esto inicializará el Modelo y la Vista, y los conectará.
    controller = UsuarioController(app)

    # 3. Iniciar el bucle principal de la aplicación
    app.mainloop()