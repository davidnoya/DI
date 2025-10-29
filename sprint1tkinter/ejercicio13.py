from tkinter import *

root = Tk()
root.title("Ejercicio 13")

canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def dibujar(event):
    x, y = event.x, event.y
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

def limpiar(event):
    if event.char == "c":
        canvas.delete("all")

canvas.bind("<Button-1>", dibujar)
root.bind("<Key>", limpiar)

root.mainloop()
