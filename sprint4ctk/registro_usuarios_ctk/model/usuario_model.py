import csv


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

    def guardar_csv(self, ruta_csv):
        try:
            with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["nombre", "edad", "genero", "avatar"])  # cabecera
                for u in self.usuarios:
                    escritor.writerow([u.nombre, u.edad, u.genero, u.avatar])
        except Exception as e:
            print("Error al guardar CSV:", e)

    def cargar_csv(self, ruta_csv):
        self.usuarios.clear()
        try:
            with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for fila in lector:
                    try:
                        nombre, edad, genero, avatar = fila
                        edad = int(edad)
                        self.usuarios.append(Usuario(nombre, edad, genero, avatar))
                    except Exception as e_fila:
                        print("Fila inválida en CSV:", fila, e_fila)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error al cargar CSV:", e)