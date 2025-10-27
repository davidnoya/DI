from tkinter import *

root = Tk()
root.title("Ejercicio 8")

frame_sup = Frame(root)
frame_sup.pack(pady=10)

Label(frame_sup, text="Introduce un texto:").grid(row=0, column=0)
entrada = Entry(frame_sup)
entrada.grid(row=0, column=1)

Label(frame_sup, text="Has escrito:").grid(row=1, column=0, columnspan=2)

salida = Label(frame_sup, text="")
salida.grid(row=2, column=0, columnspan=2, pady=5)

def mostrar():
    salida.config(text=entrada.get())

def borrar():
    entrada.delete(0, END)
    salida.config(text="")

frame_inf = Frame(root)
frame_inf.pack(pady=10)

Button(frame_inf, text="Mostrar", command=mostrar).grid(row=0, column=0, padx=5)
Button(frame_inf, text="Borrar", command=borrar).grid(row=0, column=1, padx=5)

root.mainloop()
