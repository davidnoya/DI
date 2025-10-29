import tkinter as tk
from tkinter import messagebox
import random

def jugar(eleccion_jugador):
    global puntos_jugador, puntos_maquina

    if puntos_jugador >= 3 or puntos_maquina >= 3:
        return

    eleccion_maquina = random.choice(["piedra", "papel", "tijera"])
    texto_eleccion_jugador.set("Tú sacas: " + str(eleccion_jugador))
    texto_eleccion_maquina.set("La máquina saca: " + str(eleccion_maquina))

    if eleccion_jugador == eleccion_maquina:
        resultado.set("EMPATE")
        return

    gana_jugador = (
        (eleccion_jugador == "piedra" and eleccion_maquina == "tijera") or
        (eleccion_jugador == "papel" and eleccion_maquina == "piedra") or
        (eleccion_jugador == "tijera" and eleccion_maquina == "papel")
    )

    if gana_jugador:
        puntos_jugador += 1
        resultado.set("TOOOOMA, le ganaste esta ronda a la máquina")
    else:
        puntos_maquina += 1
        resultado.set("Te ha ganado la máquina pringao.")

    marcador.set("Jugador: " + str(puntos_jugador) + "  -  Máquina: " + str(puntos_maquina))

    if puntos_jugador == 3:
        messagebox.showinfo("Fin del juego", "Has ganadoooo!")
    elif puntos_maquina == 3:
        messagebox.showinfo("Fin del juego", "Has perdido :(")

def nuevo_juego():
    global puntos_jugador, puntos_maquina
    puntos_jugador = 0
    puntos_maquina = 0
    texto_eleccion_jugador.set("")
    texto_eleccion_maquina.set("")
    resultado.set("")
    marcador.set("Jugador: 0  -  Máquina: 0")

def salir():
    root.quit()


root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("400x400")

puntos_jugador = 0
puntos_maquina = 0
texto_eleccion_jugador = tk.StringVar()
texto_eleccion_maquina = tk.StringVar()
resultado = tk.StringVar()
marcador = tk.StringVar(value="Jugador: 0  -  Máquina: 0")

tk.Label(root, text="Piedra, Papel o Tijera").pack()

tk.Label(root, textvariable=marcador).pack()

frame_botones = tk.Frame(root)
frame_botones.pack()

# Si tienes imágenes puedes usarlas así:
# img_piedra = tk.PhotoImage(file="piedra.png")
# tk.Button(frame_botones, image=img_piedra, command=lambda: jugar("piedra")).grid(row=0, column=0)

tk.Button(frame_botones, text="🪨 Piedra", width=10, command=lambda: jugar("piedra")).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, text="📄 Papel", width=10, command=lambda: jugar("papel")).grid(row=0, column=1, padx=10)
tk.Button(frame_botones, text="✂️ Tijera", width=10, command=lambda: jugar("tijera")).grid(row=0, column=2, padx=10)

tk.Label(root, textvariable=texto_eleccion_jugador).pack()
tk.Label(root, textvariable=texto_eleccion_maquina).pack()
tk.Label(root, textvariable=resultado).pack()

frame_controles = tk.Frame(root)
frame_controles.pack()
tk.Button(frame_controles, text="Nuevo juego", command=nuevo_juego).grid(row=0, column=0, padx=10)
tk.Button(frame_controles, text="Salir", command=salir).grid(row=0, column=1, padx=10)

root.mainloop()
