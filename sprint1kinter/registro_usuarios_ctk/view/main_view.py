import customtkinter as ctk
import tkinter as tk


class UsuarioView:
    def __init__(self,master):
        self.master = master
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(padx=20, pady=20, expand=True)

        self.frame_opciones = ctk.CTkFrame(self.frame)
        self.frame_opciones.pack(fill="x",pady=(0,10))

        menubar = tk.Menu(master)  # master es la ventana raíz
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista")
        menu_archivo.add_command(label="Cargar Lista")
        menubar.add_cascade(label="Opciones", menu=menu_archivo)
        master.config(menu=menubar)

        self.boton_agregar = ctk.CTkButton(self.frame_opciones,text="Agregar")
        self.boton_agregar.pack(side="left", padx=5, pady=5)

        self.boton_eliminar = ctk.CTkButton(self.frame_opciones, text="Eliminar")
        self.boton_eliminar.pack(side="left", padx=5, pady=5)


        self.texto_busqueda = ctk.StringVar()
        self.texto_busqueda.trace_add("write",self.actualizar_busqueda)

        self.busqueda = ctk.CTkEntry(self.frame_opciones,placeholder_text="Busqueda",textvariable=self.texto_busqueda)
        self.busqueda.pack(side="left", padx=10, expand=True, fill="x")


        # ListBox
        self.frame_lista = ctk.CTkFrame(self.frame)
        self.frame_lista.pack(pady=10, expand=True, fill="both")

        self.scroll_frame = ctk.CTkScrollableFrame(self.frame_lista, label_text="Lista de Usuarios")
        self.scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)



    def abrir_toplevel(self):
        ventana = ctk.CTkToplevel(self.master)
        ventana.title("Agregar Usuario")
        ventana.geometry("400x500")

        ctk.CTkLabel(ventana,text="Nombre:").pack(pady=(10,0))
        entry_nombre = ctk.CTkEntry(ventana, placeholder_text="Introduce nombre")
        entry_nombre.pack(pady=5)

        edad_var= ctk.DoubleVar(value=0)
        ctk.CTkLabel(ventana, text="Edad:").pack(pady=(10, 0))
        slider_edad = ctk.CTkSlider(ventana,to=100, variable=edad_var,number_of_steps=120)
        slider_edad.pack(pady=20, padx=20, fill="x")



        genero_var =ctk.StringVar(value="None")
        ctk.CTkLabel(ventana, text="Selecciona tu género:").pack(pady=(0, 10))

        # Botones de opción
        genero_masculino = ctk.CTkRadioButton(ventana, text="Masculino", variable=genero_var, value="masculino")
        genero_femenino = ctk.CTkRadioButton(ventana, text="Femenino", variable=genero_var, value="femenino")
        genero_otro = ctk.CTkRadioButton(ventana, text="Otro", variable=genero_var, value="otro")

        genero_masculino.pack(pady=2)
        genero_femenino.pack(pady=2)
        genero_otro.pack(pady=2)


        boton_registrar= ctk.CTkButton(ventana,text="Registrar")
        boton_salir = ctk.CTkButton(ventana,text="Salir")

    def actualizar_busqueda(self, *args):
        valor = self.texto_busqueda.get()
        print("Buscando:", valor)  # aquí iría la lógica de filtrado
