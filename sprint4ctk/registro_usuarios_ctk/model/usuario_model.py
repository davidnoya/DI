
class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.datos_ejemplo()

    def datos_ejemplo(self):
        self.usuarios = [
            Usuario("Ana López", 25, "Femenino", "avatar1.png"),
            Usuario("Carlos Pérez", 30, "Masculino", "avatar1.png"),
            Usuario("Lucía Gómez", 22, "Femenino", "avatar1.png"),
        ]

    def listar(self):
        return self.usuarios

    def obtener(self, indice):
        return self.usuarios[indice]
