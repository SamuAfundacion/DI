import customtkinter as ctk
import tkinter as tk

class UsuarioView:
    def __init__(self, master):
        self.master = master
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(padx=20, pady=20, expand=True)

        # Frame de opciones
        self.frame_opciones = ctk.CTkFrame(self.frame)
        self.frame_opciones.pack(fill="x", pady=(0, 10))

        self.boton_agregar = ctk.CTkButton(self.frame_opciones, text="Agregar")
        self.boton_agregar.pack(side="left", padx=5, pady=5)

        self.boton_eliminar = ctk.CTkButton(self.frame_opciones, text="Eliminar")
        self.boton_eliminar.pack(side="left", padx=5, pady=5)

        self.label_busqueda = ctk.CTkLabel(self.frame_opciones, text="Buscar:")
        self.label_busqueda.pack(side="left", padx=(5, 2), pady=5)

        self.texto_busqueda = ctk.StringVar()
        self.busqueda = ctk.CTkEntry(self.frame_opciones, textvariable=self.texto_busqueda)
        self.busqueda.pack(side="left", padx=(0, 10), expand=True, fill="x")
        self.texto_busqueda.trace_add("write", self.actualizar_busqueda)

        # Frame lista
        self.frame_lista = ctk.CTkFrame(self.frame)
        self.frame_lista.pack(pady=10, expand=True, fill="both")

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.frame_lista, label_text="Lista de Usuarios"
        )
        self.scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def abrir_toplevel(self, controlador):
        """TopLevel para agregar usuario"""
        self.top = ctk.CTkToplevel(self.master)
        self.top.title("Agregar Usuario")
        self.top.geometry("400x400")

        # Campos como atributos de instancia
        ctk.CTkLabel(self.top, text="Nombre:").pack(pady=(10, 0))
        self.entry_nombre = ctk.CTkEntry(self.top, placeholder_text="Introduce nombre")
        self.entry_nombre.pack(pady=5)

        ctk.CTkLabel(self.top, text="Edad:").pack(pady=(10, 0))
        self.edad_var = ctk.DoubleVar(value=0)
        self.slider_edad = ctk.CTkSlider(self.top, to=120, variable=self.edad_var, number_of_steps=120)
        self.slider_edad.pack(pady=10, fill="x", padx=20)

        ctk.CTkLabel(self.top, text="Género:").pack(pady=(10, 0))
        self.genero_var = ctk.StringVar(value="Otro")
        self.radio_m = ctk.CTkRadioButton(self.top, text="Masculino", variable=self.genero_var, value="M")
        self.radio_f = ctk.CTkRadioButton(self.top, text="Femenino", variable=self.genero_var, value="F")
        self.radio_o = ctk.CTkRadioButton(self.top, text="Otro", variable=self.genero_var, value="Otro")
        self.radio_m.pack(pady=2)
        self.radio_f.pack(pady=2)
        self.radio_o.pack(pady=2)

        # Botón registrar
        ctk.CTkButton(self.top, text="Registrar", command=controlador.registrar_usuario).pack(pady=10)

    def actualizar_busqueda(self, *args):
        valor = self.texto_busqueda.get()
        print("Buscando:", valor)
