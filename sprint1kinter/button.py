import tkinter as tk

root = tk.Tk()
root.title("Ejercicio Button")
root.geometry("300x200")

label_mensaje = tk.Label(root, text="")
label_mensaje.pack(pady=20)

def mostrar_mensaje():
    label_mensaje.config(text="¡Has presionado el botón!")

boton_mostrar = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=10)

# Bucle principal
root.mainloop()
