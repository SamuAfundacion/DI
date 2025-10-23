import tkinter as tk


root = tk.Tk()
root.title("Ejercicio Radiobutton")
root.geometry("300x250")

color_var = tk.StringVar(value="white")

def cambiar_color():
    color_elegido= color_var.get()
    root.config(bg=color_elegido)


radio_rojo= tk.Radiobutton(root,text="Rojo",variable=color_var, value="red", command=cambiar_color)
radio_verde= tk.Radiobutton(root,text="Verde",variable=color_var, value="green",command=cambiar_color)
radio_azul= tk.Radiobutton(root,text="Azul",variable=color_var, value="blue",command=cambiar_color)

label_info = tk.Label(root, text="Elige tu color favorito")
label_info.pack(pady=10)

radio_rojo.pack(anchor="w", padx=20, pady=5)
radio_verde.pack(anchor="w", padx=20, pady=5)
radio_azul.pack(anchor="w", padx=20, pady=5)


root.mainloop()