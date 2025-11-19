
import customtkinter as ctk

from registro_usuarios_ctk.controller import UsuarioController

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Ejemplo Simple de MVC")
    app.geometry("800x800")


    controller = UsuarioController(app)

    app.mainloop()