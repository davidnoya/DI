from tkinter import *

root = Tk()
root.title("Ejercicio 5")

color = StringVar()
color.set("white")

def cambiar_color():
    root.config(bg=color.get())

Radiobutton(root, text="Rojo", variable=color, value="red", command=cambiar_color).pack()
Radiobutton(root, text="Verde", variable=color, value="green", command=cambiar_color).pack()
Radiobutton(root, text="Azul", variable=color, value="blue", command=cambiar_color).pack()

root.mainloop()
