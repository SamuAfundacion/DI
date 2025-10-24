import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(expand=True, fill="both")

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 20
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="skyblue", outline="black")

# Borrar circulos
def limpiar_canvas(event):
    if event.char == "c":
        canvas.delete("all")

# Asociar evento de clic izquierdo al dibujo del círculo
canvas.bind("<Button-1>", dibujar_circulo)

# Asociar evento de teclado a la función de limpieza
root.bind("<Key>", limpiar_canvas)

# Mostrar ventana
root.mainloop()