import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 7")
root.geometry("400x450")

canvas = tk.Canvas(root, width=300, height=200, bg="white", relief="solid", borderwidth=1)
canvas.pack(pady=20)


label_coords = tk.Label(root, text="Introduce coordenadas (x1, y1, x2, y2):")
label_coords.pack()


entry_x1 = tk.Entry(root, width=5)
entry_y1 = tk.Entry(root, width=5)
entry_x2 = tk.Entry(root, width=5)
entry_y2 = tk.Entry(root, width=5)

entry_x1.pack(side="left", padx=5)
entry_y1.pack(side="left", padx=5)
entry_x2.pack(side="left", padx=5)
entry_y2.pack(side="left", padx=5)


label_info = tk.Label(root, text="")
label_info.pack(pady=10)


def validar_coordenadas(x1, y1, x2, y2):
    if not (0 <= x1 <= 300 and 0 <= x2 <= 300 and 0 <= y1 <= 200 and 0 <= y2 <= 200):
        label_info.config(text="Las coordenadas deben estar entre 0-300 (x) y 0-200 (y).", fg="red")
        return False
    return True

# Función para dibujar un rectángulo
def dibujar_rectangulo():
    try:
        x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())

        if validar_coordenadas(x1, y1, x2, y2):
            canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)
            label_info.config(text=f"Rectángulo: ({x1},{y1}) a ({x2},{y2})", fg="black")
    except ValueError:
        label_info.config(text=" Introduce solo números enteros.", fg="red")

# Función para dibujar un círculo
def dibujar_circulo():
    try:
        x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())

        if validar_coordenadas(x1, y1, x2, y2):
            canvas.create_oval(x1, y1, x2, y2, outline="red", width=2)
            label_info.config(text=f"Círculo: ({x1},{y1}) a ({x2},{y2})", fg="black")
    except ValueError:
        label_info.config(text="Introduce solo números enteros.", fg="red")


frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_rect = tk.Button(frame_botones, text="Dibujar rectángulo", command=dibujar_rectangulo)
btn_circ = tk.Button(frame_botones, text="Dibujar círculo", command=dibujar_circulo)

btn_rect.pack(side="left", padx=10)
btn_circ.pack(side="left", padx=10)

root.mainloop()
