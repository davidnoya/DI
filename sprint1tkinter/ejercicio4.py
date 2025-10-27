from tkinter import *

root = Tk()
root.title("Ejercicio 4")

leer = IntVar()
deporte = IntVar()
musica = IntVar()

def actualizar():
    aficiones = []
    if leer.get(): aficiones.append("Leer")
    if deporte.get(): aficiones.append("Deporte")
    if musica.get(): aficiones.append("Música")
    etiqueta.config(text="Aficiones: " + ", ".join(aficiones))

Checkbutton(root, text="Leer", variable=leer, command=actualizar).pack()
Checkbutton(root, text="Deporte", variable=deporte, command=actualizar).pack()
Checkbutton(root, text="Música", variable=musica, command=actualizar).pack()

etiqueta = Label(root, text="Aficiones: ")
etiqueta.pack()

root.mainloop()
