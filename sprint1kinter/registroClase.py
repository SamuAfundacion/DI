import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Ejercicio 14")
        self.root.geometry("400x700")

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Nombre
        self.etiqueta_nombre = tk.Label(self.frame, text="Escribe tu nombre:")
        self.etiqueta_nombre.pack(pady=(10, 5))

        self.entrada_nombre = tk.Entry(self.frame, justify="center")
        self.entrada_nombre.pack(pady=(0, 15))

        # Edad
        self.etiqueta_edad = tk.Label(self.frame, text="Escoge tu edad:")
        self.etiqueta_edad.pack(pady=(0, 5))

        self.scale = tk.Scale(self.frame, from_=0, to=100, orient='horizontal')
        self.scale.pack(pady=(0, 20))

        # Género
        self.label_info = tk.Label(self.frame, text="Género")
        self.label_info.pack(pady=(0, 10))

        self.genero_var = tk.StringVar(value="None")

        # Género
        self.genero_masculino = tk.Radiobutton(self.frame, text="Masculino", variable=self.genero_var, value="masculino")
        self.genero_femenino = tk.Radiobutton(self.frame, text="Femenino", variable=self.genero_var, value="femenino")
        self.genero_otro = tk.Radiobutton(self.frame, text="Otro", variable=self.genero_var, value="otro")

        self.genero_masculino.pack(pady=2)
        self.genero_femenino.pack(pady=2)
        self.genero_otro.pack(pady=2)


        self.entrada_nombre.delete(0, tk.END)
        self.genero_var.set("None")
        self.scale.set(0)

        self.registro = []

        self.boton_registrar = tk.Button(self.frame, text="Registrar usuario", command=self.mostrar_mensaje)
        self.boton_registrar.pack(pady=10)

        self.boton_eliminar = tk.Button(self.frame, text="Eliminar usuario", bg="red", command=self.eliminar_mensaje)
        self.boton_eliminar.pack(pady=10)

        self.etiqueta_registro = tk.Label(self.frame, text="", fg="green")
        self.etiqueta_registro.pack(pady=(5, 10))

        # ListBox
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10, expand=True, fill="both")

        self.listbox = tk.Listbox(self.frame_lista, height=6)
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scroll = tk.Scrollbar(self.frame_lista, orient="vertical")
        self.scroll.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox.yview)

        self.boton_salir = tk.Button(self.frame, text="Salir", command=self.salir_app)
        self.boton_salir.pack(pady=10)

        self.menubar = tk.Menu(root)
        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        self.menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)

        self.menubar.add_cascade(label="Opciones", menu=self.menu_archivo)
        root.config(menu=self.menubar)

    def mostrar_mensaje(self):

        usuario_registrado = {
            "nombre": self.entrada_nombre.get(),
            "edad": self.scale.get(),
            "genero": self.genero_var.get()
        }

        self.registro.append(usuario_registrado)
        self.etiqueta_registro.config(text="Usuario registrado correctamente ✅")
        self.listbox.insert(tk.END,
                            f"{usuario_registrado['nombre']} - {usuario_registrado['edad']} años - {usuario_registrado['genero']}")

        self.entrada_nombre.delete(0, tk.END)
        self.scale.set(0)
        self.genero_var.set("None")
    def eliminar_mensaje(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            self.registro.pop(indice)
            self.listbox.delete(indice)
            self.etiqueta_registro.config(text="Usuario eliminado ✅", fg="red")
        else:
            self.etiqueta_registro.config(text="Selecciona un usuario para eliminar", fg="orange")

    def salir_app(self):
        self.root.quit()

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "La lista de usuarios se ha guardado correctamente.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "La lista de usuarios se ha cargado correctamente.")


if __name__ == "__main__":

    root= tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
