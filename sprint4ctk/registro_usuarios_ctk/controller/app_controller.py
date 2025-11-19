from tkinter import messagebox
from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, NuevoUsuario
from pathlib import Path
import threading
import time


class AppController:
    def __init__(self, root):
        self.root = root
        self.modelo = GestorUsuarios()
        self.vista = MainView(root)

        self.auto_guardar_activo = False
        self.auto_guardar_hilo = None
        self.RUTACSV = Path(__file__).resolve().parent.parent / "usuarios.csv"
        self.usuarios_actuales = []

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        self.avatar_images = {}

        self.cargar_usuarios()
        self.refrescar_lista_usuarios()

        self.vista.boton_añadir.configure(command=self.abrir_ventana_añadir)
        self.vista.boton_guardar_csv.configure(command=self.toggle_auto_guardado)

        self.vista.buscar_var.trace_add("write", lambda *args: self.refrescar_lista_usuarios())
        self.vista.filtro_genero.configure(command=lambda value: self.refrescar_lista_usuarios())

        self.vista.menu_archivo.add_command(label="Guardar", command=self.guardar_csv_manual)
        self.vista.menu_archivo.add_command(label="Cargar", command=self.cargar_usuarios)

        self.vista.boton_salir.configure(command=self.salir)
        self.vista.menu_ayuda.add_command(label="Salir", command=self.salir)
        self.root.protocol("WM_DELETE_WINDOW", self.salir)


    def guardar_csv(self, ruta_csv=None):
        if ruta_csv is None:
            ruta_csv = self.RUTACSV
        try:
            self.modelo.guardar_csv(ruta_csv)
            return True
        except Exception as e:
            print(f"Error en guardar_csv: {e}")
            return False

    def guardar_csv_manual(self):
        if self.guardar_csv():
            self.set_status("Usuarios guardados manualmente.")
        else:
            self.set_status(f"Error al guardar: Consulte la consola para más detalles.")

    def toggle_auto_guardado(self):
        if not self.auto_guardar_activo:
            self.auto_guardar_activo = True
            self.vista.boton_guardar_csv.configure(
                text="Desactivar Guardado CSV",
                fg_color="#CC0000",
                hover_color="#AA0000"
            )
            self.auto_guardar_hilo = threading.Thread(target=self.auto_guardar_loop, daemon=True)
            self.auto_guardar_hilo.start()
            self.set_status("Guardado automático activado.")
        else:
            self.auto_guardar_activo = False
            self.vista.boton_guardar_csv.configure(
                text="Activar Guardado CSV",
                fg_color="#007BFF",
                hover_color="#0066AA"
            )
            self.set_status("Guardado automático desactivado.")

    def auto_guardar_loop(self):
        while self.auto_guardar_activo:
            time.sleep(10)

            if not self.auto_guardar_activo:
                break

            guardado_exitoso = self.guardar_csv(self.RUTACSV)

            if guardado_exitoso:
                self.root.after(0, lambda: self.set_status(f"Auto-guardado OK en {time.strftime('%H:%M:%S')}"))
            else:
                self.root.after(0, lambda: self.set_status("Error en Auto-guardado."))

    def salir(self):
        self.auto_guardar_activo = False
        self.guardar_csv()
        self.root.destroy()

    def refrescar_lista_usuarios(self):
        nombre_busqueda = self.vista.buscar_var.get().lower()
        genero_filtro = self.vista.filtro_genero.get()

        usuarios = self.modelo.listar()

        if nombre_busqueda:
            usuarios = [u for u in usuarios if nombre_busqueda in u.nombre.lower()]

        if genero_filtro != "Todos":
            usuarios = [u for u in usuarios if u.genero == genero_filtro]

        self.usuarios_actuales = usuarios

        self.vista.actualizar_lista_usuarios(self.usuarios_actuales, self.seleccionar_usuario)

        total = len(self.usuarios_actuales)
        if total == 1:
            self.set_status("1 usuario encontrado")
        else:
            self.set_status(f"{total} usuarios encontrados")

    def seleccionar_usuario(self, indice, editar=False):
        try:
            usuario = self.usuarios_actuales[indice]
        except IndexError:
            self.set_status("Error: Índice de usuario no válido en la lista actual.")
            return

        self.vista.mostrar_detalles_usuario(usuario)
        self.vista.eliminar_button.configure(command=lambda: self.eliminar_usuario(usuario))

        if editar:
            self.abrir_modal_editar(usuario)

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

    def cargar_usuarios(self):
        ruta_csv = self.BASE_DIR / "usuarios.csv"
        try:
            self.modelo.cargar_csv(ruta_csv)
            self.refrescar_lista_usuarios()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar: {e}")

    def set_status(self, mensaje):
        self.vista.barra_estado.configure(text=mensaje)

    def abrir_modal_editar(self, usuario):
        add_view = NuevoUsuario(self.root, self.ASSETS_PATH)

        add_view.nombre_entry.insert(0, usuario.nombre)
        add_view.edad_var.set(usuario.edad)
        add_view.genero_var.set(usuario.genero)
        add_view.avatar_var.set(usuario.avatar)

        add_view.guardar_button.configure(
            text="Actualizar",
            command=lambda: self.actualizar_usuario(usuario, add_view)
        )

    def actualizar_usuario(self, usuario, add_view):
        try:
            datos = add_view.get_data()
            usuario.nombre = datos['nombre']
            usuario.edad = datos['edad']
            usuario.genero = datos['genero']
            usuario.avatar = datos['avatar']

            self.refrescar_lista_usuarios()
            self.set_status("Usuario actualizado correctamente")
            add_view.window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_usuario(self, usuario):
        if messagebox.askyesno("Confirmar", f"¿Deseas eliminar a {usuario.nombre}?"):
            self.modelo.usuarios.remove(usuario)
            self.refrescar_lista_usuarios()
            self.vista.mostrar_detalles_usuario(Usuario("", 0, "", ""))
            self.set_status(f"Usuario {usuario.nombre} eliminado")