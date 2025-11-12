import tkinter as tk
from tkinter import messagebox

def nueva_ventana():
    messagebox.showinfo("Este mensaje es de prueba.\n\n"
                        "                               ")


def salir_app():
    root.quit()

root= tk.Tk()
root.title("Ejemplo de Menú")
root.geometry("300x200")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Archivo",menu=menu_archivo)
menu_archivo.add_command(label="Abrir",command=nueva_ventana)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=salir_app)

def nueva_ventana():
    messagebox.showinfo("Este mensaje debería ayudarte.\n\n"
        "                               ")

menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de",command=nueva_ventana)


root.mainloop()