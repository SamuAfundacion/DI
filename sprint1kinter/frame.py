import tkinter as tk

root = tk.Tk()
root.title("Ejercicio Frame")
root.geometry("400x300")

#  FRAME SUPERIOR
frame_sup = tk.Frame(root, bg="#e0e0e0", bd=2, relief="sunken")
frame_sup.pack(padx=20, pady=20, fill="both", expand=True)

titulo = tk.Label(frame_sup, text="Introduce un texto:", bg="#e0e0e0")
titulo.grid(row=0, column=0, padx=10, pady=5)

entry_texto = tk.Entry(frame_sup, width=25)
entry_texto.grid(row=0, column=1, padx=10, pady=5)

label_resultado = tk.Label(frame_sup, text="Aquí aparecerá tu texto", bg="#e0e0e0")
label_resultado.grid(row=1, column=0, columnspan=2, pady=10)

#  FRAME INFERIOR
frame_inf = tk.Frame(root, bg="#e0e0e0", bd=2, relief="sunken")
frame_inf.pack(fill="x", padx=20, pady=10)

def mostrar_texto():
    texto = entry_texto.get()
    label_resultado.config(text=texto if texto else "No has escrito nada")

def borrar_texto():
    entry_texto.delete(0, tk.END)
    label_resultado.config(text="Contenido borrado")

button_mostrar = tk.Button(frame_inf, text="Mostrar", command=mostrar_texto)
button_borrar = tk.Button(frame_inf, text="Borrar", command=borrar_texto)

button_mostrar.grid(row=0, column=0, padx=20, pady=10)
button_borrar.grid(row=0, column=1, padx=20, pady=10)

root.mainloop()
