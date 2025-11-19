# view/main_view.py
import os
import customtkinter as ctk
import tkinter as tk

class MainView:
    def __init__(self, root):
        self.root = root

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=3)
        root.grid_rowconfigure(0, weight=1)

        contenedorIzquierdo = ctk.CTkFrame(root)
        contenedorIzquierdo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        tituloIzquierda = ctk.CTkLabel(contenedorIzquierdo, text="Usuarios", font=("Arial", 18, "bold"))
        tituloIzquierda.pack(pady=(5, 10))

        self.lista_frame = ctk.CTkScrollableFrame(contenedorIzquierdo, width=200)
        self.lista_frame.pack(fill="both", expand=True, padx=5, pady=5)

        contenedorDerecho = ctk.CTkFrame(root)
        contenedorDerecho.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        tituloDerecha = ctk.CTkLabel(contenedorDerecho, text="Detalles del Usuario", font=("Arial", 18, "bold"))
        tituloDerecha.pack(pady=(5, 10))

        info = ctk.CTkFrame(contenedorDerecho)
        info.pack(fill="both", expand=True, padx=10, pady=10)

        self.nombre = ctk.CTkLabel(info, text="Nombre:", font=("Arial", 16))
        self.nombre.pack(pady=5)

        self.edad = ctk.CTkLabel(info, text="Edad:", font=("Arial", 16))
        self.edad.pack(pady=5)

        self.genero = ctk.CTkLabel(info, text="Género:", font=("Arial", 16))
        self.genero.pack(pady=5)

        self.avatar = ctk.CTkLabel(info, text="")
        self.avatar.pack(pady=20)

        self._imagen_avatar = None

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_frame,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=5)

    def mostrar_detalles_usuario(self, usuario):
        self.nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.edad.configure(text=f"Edad: {usuario.edad}")
        self.genero.configure(text=f"Género: {usuario.genero}")

        ruta = os.path.join("assets", usuario.avatar)
        if os.path.exists(ruta):
            self._imagen_avatar = tk.PhotoImage(file=ruta)
            self.avatar.configure(image=self._imagen_avatar, text="")
        else:
            self.avatar.configure(text="Sin imagen", image=None)
