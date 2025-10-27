from tkinter import *

root = Tk()
root.title("Ejercicio 6")

lista = Listbox(root)
frutas = ["Manzana", "Banana", "Naranja"]
for f in frutas:
    lista.insert(END, f)
lista.pack()

etiqueta = Label(root, text="")
etiqueta.pack()

def mostrar_fruta():
    seleccion = lista.curselection()
    fruta = lista.get(seleccion)
    etiqueta.config(text=f"Has seleccionado: {fruta}")

Button(root, text="Mostrar fruta", command=mostrar_fruta).pack()

root.mainloop()
