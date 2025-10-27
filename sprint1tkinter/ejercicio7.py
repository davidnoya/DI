from tkinter import *

root = Tk()
root.title("Ejercicio 7")

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

Label(root, text="x1, y1, x2, y2:").pack()
entrada = Entry(root)
entrada.pack()

def dibujar():
    x1, y1, x2, y2 = map(int, entrada.get().split(","))
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")

Button(root, text="Dibujar", command=dibujar).pack()

root.mainloop()
