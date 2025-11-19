
class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def listar(self):
        return self.usuarios

    def obtener(self, indice):
        return self.usuarios[indice]

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)