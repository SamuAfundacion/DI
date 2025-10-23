import tkinter as tk


root = tk.Tk()
root.title("Ejercicio Checkbutton")
root.geometry("300x250")

leer_var = tk.IntVar()
deporte_var = tk.IntVar()
musica_var = tk.IntVar()

def actualizar():
    seleccionadas = []

    if leer_var.get() == 1:
        seleccionadas.append("Leer")
    if deporte_var.get() == 1:
        seleccionadas.append("Deporte")
    if musica_var.get() == 1:
        seleccionadas.append("Música")

    if seleccionadas:
        texto = "Aficiones: " + ", ".join(seleccionadas)
    else:
        texto = "No has seleccionado ninguna afición."

    label_resultado.config(text=texto)

check_leer = tk.Checkbutton(root, text="Leer", variable=leer_var, command=actualizar)
check_deporte = tk.Checkbutton(root, text="Deporte", variable=deporte_var, command=actualizar)
check_musica = tk.Checkbutton(root, text="Música", variable=musica_var, command=actualizar)

check_leer.pack(anchor="w", padx=20)
check_deporte.pack(anchor="w", padx=20)
check_musica.pack(anchor="w", padx=20)

label_resultado = tk.Label(root, text="Selecciona tus aficiones:")
label_resultado.pack(pady=20)

root.mainloop()
