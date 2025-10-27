from tkinter import *

root = Tk()
root.title("Ejercicio 11")

valor = Label(root, text="Valor: 0")
valor.pack()

def actualizar(n):
    valor.config(text="Valor: " + str(n))

Scale(root, from_=0, to=100, orient=HORIZONTAL, command=actualizar).pack()

root.mainloop()
