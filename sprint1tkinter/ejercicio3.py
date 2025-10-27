from tkinter import *

root = Tk()
root.title("Ejercicio 3")

Label(root, text="Introduce tu nombre:").pack()
entrada = Entry(root)
entrada.pack()

saludo = Label(root, text="")
saludo.pack()

def saludar():
    nombre = entrada.get()
    saludo.config(text="Buenas " + str(nombre) + "!")

Button(root, text="Saludar", command=saludar).pack()

root.mainloop()
