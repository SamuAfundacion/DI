
import customtkinter as ctk

from registro_usuarios_ctk.controller import UsuarioController

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Ejemplo Simple de MVC")
    app.geometry("600x600")


    controller = UsuarioController(app)

    app.mainloop()