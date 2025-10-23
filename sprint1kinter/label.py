import tkinter as tk


ventana = tk.Tk()
ventana.title("Ejercicio 1 - Labels")
ventana.geometry("300x200")  # Tamaño de la ventana


label_bienvenida = tk.Label(ventana, text="Primer Ejercicio")
label_bienvenida.pack(pady=10)


label_nombre = tk.Label(ventana, text="Samuel Paz Muiño")
label_nombre.pack(pady=10)

label_cambia = tk.Label(ventana, text="Texto original")
label_cambia.pack(pady=10)

# Función que cambia el texto de la tercera etiqueta
def cambiar_texto():
    label_cambia.config(text="¡El texto ha cambiado!")

# Botón que ejecuta la función
boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()
