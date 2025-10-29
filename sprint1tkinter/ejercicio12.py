from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ejercicio 12")

Label(root, text="Nombre:").grid(row=0, column=0)
nombre = Entry(root)
nombre.grid(row=0, column=1)

Label(root, text="Edad:").grid(row=1, column=0)
edad = Scale(root, from_=0, to=100, orient=HORIZONTAL)
edad.grid(row=1, column=1)

Label(root, text="Género:").grid(row=2, column=0)
genero = StringVar()
Radiobutton(root, text="Masculino", variable=genero, value="Masculino").grid(row=2, column=1)
Radiobutton(root, text="Femenino", variable=genero, value="Femenino").grid(row=3, column=1)
Radiobutton(root, text="Otro", variable=genero, value="Otro").grid(row=4, column=1)

lista = Listbox(root, width=40)
lista.grid(row=5, column=0, columnspan=2)

scroll = Scrollbar(root, command=lista.yview)
scroll.grid(row=5, column=2, sticky="ns")
lista.config(yscrollcommand=scroll.set)

def añadir_usuario():
    lista.insert(END, str(nombre.get()) + " - " + str(edad.get()) + " años - " + str(genero.get()))
    nombre.delete(0, END)

def eliminar_usuario():
    sel = lista.curselection()
    lista.delete(sel)

def guardar():
    messagebox.showinfo("Guardar", "Lista guardada (simulado).")

def cargar():
    messagebox.showinfo("Cargar", "Lista cargada (simulado).")

menubar = Menu(root)
menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Guardar lista", command=guardar)
menu_archivo.add_command(label="Cargar lista", command=cargar)
menubar.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=menubar)

Button(root, text="Añadir", command=añadir_usuario).grid(row=6, column=0)
Button(root, text="Eliminar", command=eliminar_usuario).grid(row=6, column=1)
Button(root, text="Salir", command=root.quit).grid(row=6, column=2)

root.mainloop()
