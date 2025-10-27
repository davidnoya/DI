from tkinter import *

root = Tk()
root.title("Ejercicio 2")

mensaje = Label(root, text="")
mensaje.pack()

def mostrar_mensaje():
    mensaje.config(text="Botón pulsado")

Button(root, text="Mostrar mensaje", command=mostrar_mensaje).pack()
Button(root, text="Salir", command=root.quit).pack()

root.mainloop()
