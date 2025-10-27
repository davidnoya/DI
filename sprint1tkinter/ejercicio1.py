from tkinter import *

root = Tk()
root.title("Ejercicio 1")

Label(root, text="Bienvenido!!").pack()
Label(root, text="David Noya Vázquez").pack()

etiqueta3 = Label(root, text="texto viejo")
etiqueta3.pack()

def cambiar_texto():
    etiqueta3.config(text="nuevo texto")

Button(root, text="Cambiar texto", command=cambiar_texto).pack()

root.mainloop()
