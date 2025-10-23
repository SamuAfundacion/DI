import tkinter as tk

def mostrar_mensaje():
    nombre = entrada.get()
    saludo.config(text=f"Saludos, {nombre}!")

root = tk.Tk()
root.title("Ejercicio Entry")
root.geometry("300x200")

etiqueta = tk.Label(root,text="Escribe tu nombre ")
etiqueta.pack(pady=10)

entrada = tk.Entry(root,width=30)
entrada.pack(pady=10)

boton_mostrar = tk.Button(root, text="Mostrar saludo", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)


saludo = tk.Label(root,text="")
saludo.pack(pady=10)




root.mainloop()
