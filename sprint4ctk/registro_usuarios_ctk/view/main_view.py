import os
import tkinter
from pathlib import Path
import customtkinter as ctk
from PIL import Image


class NuevoUsuario:
    def __init__(self, master, assets_path):
        self.assets_path = assets_path
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")
        self.window.grab_set()

        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=(10, 0))
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=(10, 0))
        self.edad_var = ctk.IntVar(value=18)
        self.edad_slider = ctk.CTkSlider(self.window, from_=0, to=120, number_of_steps=120, variable=self.edad_var,
                                         command=self.actualizar_label_edad)
        self.edad_slider.pack(pady=5, fill="x", padx=10)
        self.edad_label = ctk.CTkLabel(self.window, text=f"{self.edad_var.get()} años")
        self.edad_label.pack(pady=(0, 5))

        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 0))
        self.genero_var = ctk.StringVar(value="Seleccione un género")
        self.genero_option = ctk.CTkOptionMenu(
            self.window,
            values=["Femenino", "Masculino", "Otro"],
            variable=self.genero_var
        )
        self.genero_option.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(10, 0))
        self.avatar_var = ctk.StringVar(value="Seleccione un avatar")

        avatares = [f.name for f in Path(self.assets_path).glob("*.png")]
        if not avatares:
            avatares = ["No hay avatares"]

        self.avatar_option = ctk.CTkOptionMenu(
            self.window,
            values=avatares,
            variable=self.avatar_var
        )
        self.avatar_option.pack(pady=5, fill="x", padx=10)

        self.guardar_button = ctk.CTkButton(self.window, text="Añadir Usuario")
        self.guardar_button.pack(pady=20, fill="x", padx=10)

    def actualizar_label_edad(self, valor):
        self.edad_label.configure(text=f"{int(float(valor))} años")

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_var.get(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get()
        }


class MainView:
    def __init__(self, root):
        self.root = root

        # Configuración de la rejilla principal
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=3)
        root.grid_rowconfigure(0, weight=1)
        # Añadimos una nueva fila para el status y el botón (row=2, aunque es la tercera fila)
        root.grid_rowconfigure(1, weight=0)  # Fila 1 para el nuevo contenedor

        contenedorIzquierdo = ctk.CTkFrame(root)
        contenedorIzquierdo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        tituloIzquierda = ctk.CTkLabel(contenedorIzquierdo, text="Usuarios", font=("Arial", 18, "bold"))
        tituloIzquierda.pack(pady=(5, 10))

        self.buscar_var = ctk.StringVar()
        self.buscar_entry = ctk.CTkEntry(
            contenedorIzquierdo,
            placeholder_text="Buscar por nombre",
            textvariable=self.buscar_var
        )
        self.buscar_entry.pack(fill="x", padx=5, pady=(0, 5))

        self.filtro_genero = ctk.CTkComboBox(
            contenedorIzquierdo,
            values=["Todos", "Femenino", "Masculino", "Otro"]
        )
        self.filtro_genero.set("Todos")
        self.filtro_genero.pack(fill="x", padx=5, pady=(0, 10))

        self.lista_frame = ctk.CTkScrollableFrame(contenedorIzquierdo, width=200)
        self.lista_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Botones inferiores del contenedor izquierdo
        self.boton_añadir = ctk.CTkButton(contenedorIzquierdo, text="Añadir Usuario", hover_color="#0b6730",
                                          fg_color="#008f39")
        self.boton_añadir.pack(pady=(10, 5), fill="x", padx=10)

        self.boton_salir = ctk.CTkButton(contenedorIzquierdo, text="Salir", command=root.destroy, hover_color="#b81414",
                                         fg_color="#FF0000")
        self.boton_salir.pack(pady=(0, 10), fill="x", padx=10)

        # Contenedor Derecho
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

        self.eliminar_button = ctk.CTkButton(info, text="Eliminar Usuario", hover_color="#b81414", fg_color="#FF0000")
        self.eliminar_button.pack(pady=5)

        # --- INICIO: REUBICACIÓN SOLICITADA ---

        # Nuevo contenedor para el Status y el Botón, ocupando ambas columnas
        status_container = ctk.CTkFrame(root, height=25, fg_color="transparent")
        status_container.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=(0, 10))
        status_container.grid_columnconfigure(0, weight=1)  # Columna para el status (izquierda)
        status_container.grid_columnconfigure(1, weight=0)  # Columna para el botón (derecha)

        # 1. Barra de estado (Status) - Izquierda
        self.barra_estado = ctk.CTkLabel(
            status_container,
            text="Listo",
            height=25,
            anchor="w"  # Alineación a la izquierda
        )
        self.barra_estado.grid(row=0, column=0, sticky="w", padx=(5, 10), pady=0)

        # 2. Botón de Auto-Guardado - Derecha
        self.boton_guardar_csv = ctk.CTkButton(
            status_container,
            text="Activar Guardado CSV",
            hover_color="#0066AA",
            fg_color="#007BFF",
            width=200  # Ancho fijo para que no se estire
        )
        self.boton_guardar_csv.grid(row=0, column=1, sticky="e", padx=(10, 5), pady=0)

        # --- FIN: REUBICACIÓN SOLICITADA ---

        self.menubar = tkinter.Menu(root, tearoff=0)
        root.config(menu=self.menubar)

        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.menu_ayuda = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Ayuda", menu=self.menu_ayuda)

        # Imagen por defecto
        self.avatar_default_img = ctk.CTkImage(light_image=Image.new("RGB", (150, 150), color="gray"), size=(150, 150))
        # Imagen actual
        self._imagen_avatar = self.avatar_default_img
        self.avatar.configure(image=self._imagen_avatar)

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

            btn.bind("<Double-Button-1>", lambda e, idx=i: on_seleccionar_callback(idx, editar=True))

    def mostrar_detalles_usuario(self, usuario):
        self.nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.edad.configure(text=f"Edad: {usuario.edad}")
        self.genero.configure(text=f"Género: {usuario.genero}")

        if usuario.avatar:
            ruta = os.path.join("assets", usuario.avatar)
            if os.path.exists(ruta):
                img = Image.open(ruta)
                self._imagen_avatar = ctk.CTkImage(light_image=img, size=(150, 150))
            else:
                self._imagen_avatar = self.avatar_default_img
        else:
            self._imagen_avatar = self.avatar_default_img

        self.avatar.configure(image=self._imagen_avatar, text="")