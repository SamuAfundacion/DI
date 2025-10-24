import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ejercicio Registro")
root.geometry("300x450")

frame = tk.Frame(root)
frame.pack(expand=True)

        # Nombre
etiqueta_nombre = tk.Label(frame, text="Escribe tu nombre:")
etiqueta_nombre.pack(pady=(10, 5))

entrada_nombre = tk.Entry(frame, justify="center")
entrada_nombre.pack(pady=(0, 15))

        # Edad
etiqueta_edad = tk.Label(frame, text="Escoge tu edad:")
etiqueta_edad.pack(pady=(0, 5))

scale = tk.Scale(frame, from_=0, to=100, orient='horizontal')
scale.pack(pady=(0, 20))

        # Género
label_info = tk.Label(frame, text="Género")
label_info.pack(pady=(0, 10))

genero_var = tk.StringVar(value="None")

        # Género
genero_masculino = tk.Radiobutton(frame, text="Masculino", variable=genero_var, value="masculino")
genero_femenino = tk.Radiobutton(frame, text="Femenino", variable=genero_var, value="femenino")
genero_otro = tk.Radiobutton(frame, text="Otro", variable=genero_var, value="otro")

genero_masculino.pack(pady=2)
genero_femenino.pack(pady=2)
genero_otro.pack(pady=2)


registro= []
# Registro
def mostrar_mensaje():

    usuario_registrado = {
        "nombre": entrada_nombre.get(),
        "edad": scale.get(),
        "genero": genero_var.get()
    }

    registro.append(usuario_registrado)
    etiqueta_registro.config(text="Usuario registrado correctamente ✅")
    listbox.insert(tk.END, f"{usuario_registrado['nombre']} - {usuario_registrado['edad']} años - {usuario_registrado['genero']}")

    entrada_nombre.delete(0, tk.END)
    genero_var.set("None")
    scale.set(0)

def eliminar_mensaje():
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        registro.pop(indice)
        listbox.delete(indice)
        etiqueta_registro.config(text="Usuario eliminado ✅", fg="red")
    else:
        etiqueta_registro.config(text="Selecciona un usuario para eliminar", fg="orange")


boton_registrar = tk.Button(frame, text="Registrar usuario", command=mostrar_mensaje)
boton_registrar.pack(pady=10)

boton_eliminar = tk.Button(frame, text="Eliminar usuario",bg="red", command=eliminar_mensaje)
boton_eliminar.pack(pady=10)

etiqueta_registro = tk.Label(frame, text="", fg="green")
etiqueta_registro.pack(pady=(5, 10))


# ListBox
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10, expand=True, fill="both")

listbox = tk.Listbox(frame_lista, height=6)
listbox.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(frame_lista, orient="vertical")
scroll.pack(side="right", fill="y")

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)


def salir_app():
    root.quit()


boton_salir = tk.Button(frame,text="Salir",command=salir_app)
boton_salir.pack(pady=10)

# ====== Menú principal ======
def guardar_lista():
    messagebox.showinfo("Guardar Lista", "La lista de usuarios se ha guardado correctamente.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "La lista de usuarios se ha cargado correctamente.")

menubar = tk.Menu(root)
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)


menubar.add_cascade(label="Opciones", menu=menu_archivo)
root.config(menu=menubar)

root.mainloop()
