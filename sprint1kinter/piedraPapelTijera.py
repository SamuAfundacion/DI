import random
import tkinter as tk

root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("700x700")
root.config(bg="#f0f0f0")

# --- CONFIGURACIÓN GENERAL ---
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# --- FRAME DEL JUGADOR ---
frame_jugador = tk.Frame(root, borderwidth=2, relief="groove", padx=15, pady=15, bg="#e8f4fc")
frame_jugador.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

etiqueta_nombre = tk.Label(frame_jugador, text="Escoge tu opción:", font=("Arial", 12, "bold"), bg="#e8f4fc")
etiqueta_nombre.grid(row=0, column=0, columnspan=3, pady=(5, 15))

# --- FRAME DE LA MÁQUINA ---
frame_maquina = tk.Frame(root, borderwidth=2, relief="groove", padx=15, pady=15, bg="#fce8e8")
frame_maquina.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

etiqueta_maquina = tk.Label(frame_maquina, text="Máquina", font=("Arial", 12, "bold"), bg="#fce8e8")
etiqueta_maquina.pack(pady=(0, 10))

etiqueta_jugada = tk.Label(frame_maquina, text="Esperando tu jugada...", bg="#fce8e8", font=("Arial", 10))
etiqueta_jugada.pack()

# --- FRAME DEL RESULTADO ---
frame_resultado = tk.Frame(root, borderwidth=2, relief="ridge", padx=10, pady=10, bg="#e8fce8")
frame_resultado.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

etiqueta_resultado = tk.Label(frame_resultado, text="Resultado: Esperando...", font=("Arial", 12, "bold"), bg="#e8fce8")
etiqueta_resultado.pack()

contador_jugador = 0
contador_maquina = 0
contador_partidas_jugador=0
contador_partidas_maquina=0

etiqueta_contador_jugador = tk.Label(frame_resultado, text="Partidas ganadas jugador: 0", font=("Arial", 12, "bold"), bg="#e8fce8")
etiqueta_contador_jugador.pack()
etiqueta_contador_maquina = tk.Label(frame_resultado, text="Partidas ganadas máquina: 0", font=("Arial", 12, "bold"), bg="#e8fce8")
etiqueta_contador_maquina.pack()

# --- FRAME CONTADOR DE PARTIDAS GANADAS ---
frame_total = tk.Frame(root, borderwidth=2, relief="ridge", padx=10, pady=10, bg="#f5f5dc")
frame_total.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

titulo_total = tk.Label(frame_total, text="Partidas ganadas", font=("Arial", 13, "bold"), bg="#f5f5dc")
titulo_total.pack(pady=(0, 10))

etiqueta_partidas_jugador = tk.Label(frame_total, text="Jugador: 0", font=("Arial", 11), bg="#f5f5dc")
etiqueta_partidas_jugador.pack()
etiqueta_partidas_maquina = tk.Label(frame_total, text="Máquina: 0", font=("Arial", 11), bg="#f5f5dc")
etiqueta_partidas_maquina.pack()

# --- FUNCIÓN DE JUEGO ---
def jugar_mostrar(eleccion):
    global contador_jugador, contador_maquina,contador_partidas_maquina,contador_partidas_jugador

    etiqueta_jugada.config(text=f"Has escogido: {eleccion}")
    opcion_maquina = random.choice(["piedra", "papel", "tijera"])
    etiqueta_maquina.config(text=f"Máquina escogió: {opcion_maquina}")

    if opcion_maquina == eleccion:
        etiqueta_resultado.config(text="Resultado: ¡Empate! :0", bg="#fff3b0")
    elif (eleccion == "piedra" and opcion_maquina == "tijera") or \
         (eleccion == "papel" and opcion_maquina == "piedra") or \
         (eleccion == "tijera" and opcion_maquina == "papel"):
        etiqueta_resultado.config(text="Resultado: ¡Has ganado! :)", bg="#c8f7c5")
        contador_jugador += 1
    else:
        etiqueta_resultado.config(text="Resultado: ¡Has perdido! :(", bg="#f7c5c5")
        contador_maquina += 1

    etiqueta_contador_jugador.config(text=f"Partidas ganadas jugador: {contador_jugador}")
    etiqueta_contador_maquina.config(text=f"Partidas ganadas máquina: {contador_maquina}")

    # --- Condición de fin de partida ---
    if contador_jugador == 3:
        etiqueta_resultado.config(text="Has ganado la partida! :D", bg="#a4f9a4")
        contador_partidas_jugador+=1
        desactivar_botones()
        actualizar_contador_total()

    elif contador_maquina == 3:
        etiqueta_resultado.config(text="Ha ganado la máquina D:", bg="#f9a4a4")
        contador_partidas_maquina+=1
        desactivar_botones()
        actualizar_contador_total()


def actualizar_contador_total():
    etiqueta_partidas_jugador.config(text=f"Jugador: {contador_partidas_jugador}")
    etiqueta_partidas_maquina.config(text=f"Máquina: {contador_partidas_maquina}")

# --- FUNCIÓN PARA DESACTIVAR LOS BOTONES Y MOSTRAR "NUEVA PARTIDA" ---
def desactivar_botones():
    boton_piedra.config(state="disabled")
    boton_papel.config(state="disabled")
    boton_tijera.config(state="disabled")

    # Crear botón de nueva partida
    global boton_nueva_partida
    boton_nueva_partida = tk.Button(frame_jugador, text="Nueva partida", font=("Arial", 11, "bold"),
                                    bg="#d6f5d6", command=reinciar_partida)
    boton_nueva_partida.grid(row=2, column=2, pady=10, padx=5, sticky="e")

# --- FUNCIÓN PARA REINICIAR LA PARTIDA ---
def reinciar_partida():
    global contador_jugador, contador_maquina
    contador_jugador = 0
    contador_maquina = 0

    # Reactivar botones
    boton_piedra.config(state="normal")
    boton_papel.config(state="normal")
    boton_tijera.config(state="normal")

    # Actualizar textos
    etiqueta_resultado.config(text="Resultado: Esperando...", bg="#e8fce8")
    etiqueta_jugada.config(text="Esperando tu jugada...")
    etiqueta_maquina.config(text="Máquina")
    etiqueta_contador_jugador.config(text="Partidas ganadas jugador: 0")
    etiqueta_contador_maquina.config(text="Partidas ganadas máquina: 0")

    # Eliminar el botón de nueva partida
    boton_nueva_partida.destroy()

def reiniciar_marcador_total():
    global contador_partidas_jugador, contador_partidas_maquina
    contador_partidas_jugador = 0
    contador_partidas_maquina = 0
    reinciar_partida()
    actualizar_contador_total()
# --- BOTONES ---
boton_piedra = tk.Button(frame_jugador, text="Piedra", width=10, height=2, command=lambda: jugar_mostrar("piedra"))
boton_papel = tk.Button(frame_jugador, text="Papel", width=10, height=2, command=lambda: jugar_mostrar("papel"))
boton_tijera = tk.Button(frame_jugador, text="Tijera️", width=10, height=2, command=lambda: jugar_mostrar("tijera"))

boton_piedra.grid(row=1, column=0, padx=10, pady=10)
boton_papel.grid(row=1, column=1, padx=10, pady=10)
boton_tijera.grid(row=1, column=2, padx=10, pady=10)

# --- BOTÓN REINICIAR MARCADOR ---
boton_reiniciar_marcador = tk.Button(frame_jugador, text="Reiniciar marcador", bg="#ffcccc", font=("Arial", 10, "bold"),
                                     command=reiniciar_marcador_total)
boton_reiniciar_marcador.grid(row=2, column=0, columnspan=1, pady=10, padx=5, sticky="w")

root.mainloop()
