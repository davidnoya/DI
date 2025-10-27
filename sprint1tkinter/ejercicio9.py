from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ejercicio 9")

def abrir():
    messagebox.showinfo("Abrir", "Has pulsado 'Abrir'.")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Carlos guapetón.\nEjercicio 9 de Tkinter.")

menubar = Menu(root)

archivo = Menu(menubar, tearoff=0)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_separator()
archivo.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=archivo)

ayuda = Menu(menubar, tearoff=0)
ayuda.add_command(label="Acerca de", command=acerca_de)
menubar.add_cascade(label="Ayuda", menu=ayuda)

root.config(menu=menubar)
root.mainloop()
