import tkinter as tk


root = tk.Tk()
root.title("Ejercicio Checkbutton")
root.geometry("300x250")

def actualizar_valor(val):
    etiqueta.config(text=f"Valor: {val}")

scale= tk.Scale(root,from_=0, to=100,orient='horizontal', command=actualizar_valor)
scale.pack(pady=20)

etiqueta = tk.Label(root,text="Ningún valor seleccionado")
etiqueta.pack(pady=10)



root.mainloop()