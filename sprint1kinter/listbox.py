import tkinter as tk

root = tk.Tk()
root.title("Ejercicio Listbox")
root.geometry("300x250")

label_info = tk.Label(root, text="Selecciona una fruta:")
label_info.pack(pady=10)

listbox = tk.Listbox(root, height=5)
frutas = ["Manzana", "Banana", "Naranja"]

# Agregar las frutas a la lista
for fruta in frutas:
    listbox.insert(tk.END, fruta)

listbox.pack(pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)


def mostrar_fruta():
    seleccion = listbox.curselection()  # Obtiene el índice seleccionado
    if seleccion:  # Si hay algo seleccionado
        fruta = listbox.get(seleccion)  # Obtiene el texto de ese índice
        label_resultado.config(text=f"Has seleccionado: {fruta}")
    else:
        label_resultado.config(text="No has seleccionado ninguna fruta.")

boton_mostrar = tk.Button(root, text="Mostrar selección", command=mostrar_fruta)
boton_mostrar.pack(pady=10)

root.mainloop()
