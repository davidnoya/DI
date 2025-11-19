from model.usuario_model import GestorUsuarios
from view.main_view import MainView

class AppController:
    def __init__(self, root):
        self.root = root

        self.modelo = GestorUsuarios()
        self.vista = MainView(root)

        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()

        self.vista.actualizar_lista_usuarios(
            usuarios,
            self.seleccionar_usuario
        )

    def seleccionar_usuario(self, indice):
        usuario = self.modelo.obtener(indice)
        self.vista.mostrar_detalles_usuario(usuario)
