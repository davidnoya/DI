from tkinter import *

root = Tk()
root.title("Ejercicio 10")

texto = Text(root, wrap=WORD)
scroll = Scrollbar(root, command=texto.yview)
texto.config(yscrollcommand=scroll.set)

texto.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

texto.insert(END, "Ruleta...\n" * 100)

root.mainloop()
