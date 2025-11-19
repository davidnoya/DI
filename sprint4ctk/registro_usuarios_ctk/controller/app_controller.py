from tkinter import messagebox

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, NuevoUsuario
from pathlib import Path

class AppController:
    def __init__(self, root):
        self.root = root
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        self.avatar_images = {}

        self.modelo = GestorUsuarios()
        self.vista = MainView(root)

        self.refrescar_lista_usuarios()

        self.vista.boton_añadir.configure(command=self.abrir_ventana_añadir)

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()

        self.vista.actualizar_lista_usuarios(
            usuarios,
            self.seleccionar_usuario
        )

    def seleccionar_usuario(self, indice):
        usuario = self.modelo.obtener(indice)
        self.vista.mostrar_detalles_usuario(usuario)

    def abrir_ventana_añadir(self):
        add_view = NuevoUsuario(self.root, self.ASSETS_PATH)
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))

    def añadir_usuario(self, add_view):
        datos = add_view.get_data()
        try:
            nombre = datos["nombre"].strip()
            edad = int(datos["edad"])
            genero = datos["genero"]
            avatar = datos["avatar"]

            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if genero == "Seleccione un género":
                raise ValueError("Debe seleccionar un género válido.")
            if avatar == "Seleccione un avatar":
                raise ValueError("Debe seleccionar un avatar válido.")

            usuario = Usuario(nombre, edad, genero, avatar)
            self.modelo.agregar_usuario(usuario)
            self.refrescar_lista_usuarios()
            add_view.window.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))