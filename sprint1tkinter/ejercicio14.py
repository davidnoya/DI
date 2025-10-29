from tkinter import *
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 14")

        Label(root, text="Nombre:").grid(row=0, column=0)
        self.nombre = Entry(root)
        self.nombre.grid(row=0, column=1)

        Label(root, text="Edad:").grid(row=1, column=0)
        self.edad = Scale(root, from_=0, to=100, orient=HORIZONTAL)
        self.edad.grid(row=1, column=1)

        Label(root, text="Género:").grid(row=2, column=0)
        self.genero = StringVar()
        Radiobutton(root, text="Masculino", variable=self.genero, value="Masculino").grid(row=2, column=1)
        Radiobutton(root, text="Femenino", variable=self.genero, value="Femenino").grid(row=3, column=1)
        Radiobutton(root, text="Otro", variable=self.genero, value="Otro").grid(row=4, column=1)

        self.lista = Listbox(root, width=40)
        self.lista.grid(row=5, column=0, columnspan=2)

        Button(root, text="Añadir", command=self.añadir_usuario).grid(row=6, column=0)
        Button(root, text="Eliminar", command=self.eliminar_usuario).grid(row=6, column=1)
        Button(root, text="Salir", command=self.salir).grid(row=6, column=2)

    def añadir_usuario(self):
        if self.nombre.get() and self.genero.get():
            self.lista.insert(END, f"{self.nombre.get()} - {self.edad.get()} años - {self.genero.get()}")
            self.nombre.delete(0, END)
        else:
            messagebox.showwarning("Error", "Introduce nombre y género")

    def eliminar_usuario(self):
        sel = self.lista.curselection()
        if sel:
            self.lista.delete(sel)
        else:
            messagebox.showwarning("Error", "Selecciona un usuario")

    def salir(self):
        self.root.quit()

root = Tk()
app = RegistroApp(root)
root.mainloop()
