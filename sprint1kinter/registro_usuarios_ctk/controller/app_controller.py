import threading
import time
from registro_usuarios_ctk.model import GestorUsuarios, Usuario
from registro_usuarios_ctk.view import UsuarioView
import customtkinter as ctk
from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton  # usados en editor

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.view = UsuarioView(root, controller=self)
        self.usuario_seleccionado = None
        self.auto_guardado_activo = False

        # Conectar botones / menú
        self.view.boton_agregar.configure(command=self.abrir_agregar_usuario)
        self.view.boton_eliminar.configure(command=self.eliminar_usuario)
        self.view.boton_autoguardado.configure(command=self.toggle_auto_guardado)
        self.view.menu_archivo.entryconfig("Guardar Lista", command=self.grabar_lista)
        self.view.menu_archivo.entryconfig("Cargar Lista", command=self.cargar_lista)

        # Mostrar lista inicial
        self.actualizar_lista_scroll()

        # Parar hilo
        self.root.protocol("WM_DELETE_WINDOW", self.salir)

    # --- AUTO-GUARDADO ---
    def toggle_auto_guardado(self):
        if not self.auto_guardado_activo:
            self.auto_guardado_activo = True
            self.view.boton_autoguardado.configure(text="Auto-guardar (10s): ON")
            self.view.actualizar_estado("Auto-guardado activado")
            threading.Thread(target=self.hilo_autoguardado, daemon=True).start()
        else:
            self.auto_guardado_activo = False
            self.view.boton_autoguardado.configure(text="Auto-guardar (10s): OFF")
            self.view.actualizar_estado("Auto-guardado desactivado")

    def hilo_autoguardado(self):
        while self.auto_guardado_activo:
            time.sleep(10)
            self.model.guardar_csv()
            # comunicar a UI con after()
            self.root.after(0, lambda: self.view.actualizar_estado("Auto-guardado ejecutado", temporizado=True))

    # --- SALIR ---
    def salir(self):
        self.auto_guardado_activo = False
        # darle un pequeño tiempo para que el hilo termine si está durmiendo no es estrictamente necesario
        self.root.destroy()

    # --- TOPLEVEL (añadir) ---
    def abrir_agregar_usuario(self):
        self.view.abrir_toplevel()

    def registrar_usuario(self):
        nombre = self.view.entry_nombre.get()
        try:
            edad = int(self.view.edad_var.get())
        except Exception:
            self.view.actualizar_estado("Edad no válida")
            return
        genero = self.view.genero_var.get()
        avatar = self.view.avatar_var.get()

        try:
            nuevo_usuario = Usuario(nombre, edad, genero, avatar)
            self.model.añadir(nuevo_usuario)
        except ValueError as e:
            self.view.actualizar_estado(f"Error: {str(e)}")
            return

        self.actualizar_lista_scroll()
        self.view.actualizar_avatar(nuevo_usuario.avatar)

        if hasattr(self.view, "top"):
            self.view.top.destroy()
        self.view.actualizar_estado("Usuario añadido correctamente")

    # --- LISTA Y FILTROS ---
    def actualizar_lista_scroll(self, usuarios=None):
        if usuarios is None:
            usuarios = self.model.listar()

        # limpiar contenedor
        for widget in self.view.scroll_frame.winfo_children():
            widget.destroy()

        def seleccionar_usuario(u, label):
            for child in self.view.scroll_frame.winfo_children():

                try:
                    child.configure(fg_color="transparent")
                except Exception:
                    pass
            label.configure(fg_color="#0078D7")
            self.usuario_seleccionado = u
            # actualizar panel derecho
            self.view.label_nombre.configure(text=f"Nombre: {u.nombre}")
            self.view.label_edad.configure(text=f"Edad: {u.edad}")
            self.view.label_genero.configure(text=f"Género: {u.genero}")
            self.view.actualizar_avatar(u.avatar)

        for u in usuarios:
            label = ctk.CTkLabel(
                self.view.scroll_frame,
                text=f"{u.nombre}, {u.edad}, {u.genero}",
                width=250, height=30,
                corner_radius=8,
                fg_color="transparent",
                anchor="w"
            )
            label.pack(pady=2, padx=5, fill="x")

            label.bind("<Button-1>", lambda e, u=u, lbl=label: seleccionar_usuario(u, lbl))

            label.bind("<Double-Button-1>", lambda e, u=u: self.abrir_editor_usuario(u))

        self.view.actualizar_recuento(len(usuarios))

    def filtrar_usuarios(self, texto):
        texto = texto.strip()
        usuarios = self.model.listar() if texto == "" else self.model.buscar(texto)
        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro aplicado")

    def filtrar_genero(self, genero):
        usuarios = self.model.listar() if genero == "todos" else self.model.buscar_genero(genero)
        self.actualizar_lista_scroll(usuarios)
        self.view.actualizar_estado("Filtro de género aplicado")

    # --- ELIMINAR ---
    def eliminar_usuario(self):
        if self.usuario_seleccionado is None:
            self.view.actualizar_estado("No hay usuario seleccionado")
            return
        try:
            self.model._usuarios.remove(self.usuario_seleccionado)
            self.view.actualizar_estado(f"Usuario {self.usuario_seleccionado.nombre} eliminado")
            self.usuario_seleccionado = None
            self.view.label_nombre.configure(text="Nombre: -")
            self.view.label_edad.configure(text="Edad: -")
            self.view.label_genero.configure(text="Género: -")
            self.view.actualizar_avatar("avatar1")
            self.actualizar_lista_scroll()
        except ValueError:
            self.view.actualizar_estado("Error al eliminar usuario")

    # --- ARCHIVOS ---
    def grabar_lista(self):
        self.model.guardar_csv()
        self.view.actualizar_estado("Lista guardada")

    def cargar_lista(self):
        self.model.cargar_csv()
        self.actualizar_lista_scroll()
        self.view.actualizar_estado("Lista cargada correctamente")

    # --- editor
    def abrir_editor_usuario(self, usuario):
        ventana = CTkToplevel(self.root)
        ventana.title(f"Editar usuario: {usuario.nombre}")
        ventana.geometry("320x300")

        CTkLabel(ventana, text="Nombre:").pack(pady=(10, 0))
        entry_nombre = CTkEntry(ventana)
        entry_nombre.insert(0, usuario.nombre)
        entry_nombre.pack(padx=10, pady=5, fill="x")

        CTkLabel(ventana, text="Edad:").pack(pady=(10, 0))
        entry_edad = CTkEntry(ventana)
        entry_edad.insert(0, str(usuario.edad))
        entry_edad.pack(padx=10, pady=5, fill="x")

        CTkLabel(ventana, text="Género (M/F/Otro):").pack(pady=(10, 0))
        entry_genero = CTkEntry(ventana)
        entry_genero.insert(0, usuario.genero)
        entry_genero.pack(padx=10, pady=5, fill="x")

        def guardar_cambios():
            new_nombre = entry_nombre.get().strip()
            if new_nombre == "":
                self.view.actualizar_estado("Nombre vacío")
                return
            try:
                new_edad = int(entry_edad.get())
            except Exception:
                self.view.actualizar_estado("Edad inválida")
                return
            new_genero = entry_genero.get().strip()
            if new_genero not in ("M", "F", "Otro"):
                # permitir otras cadenas si quieres; aquí validamos
                self.view.actualizar_estado("Género debe ser M, F u Otro")
                return


            usuario.nombre = new_nombre
            usuario.edad = new_edad
            usuario.genero = new_genero


            self.actualizar_lista_scroll()

            self.usuario_seleccionado = usuario
            self.view.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
            self.view.label_edad.configure(text=f"Edad: {usuario.edad}")
            self.view.label_genero.configure(text=f"Género: {usuario.genero}")
            self.view.actualizar_avatar(usuario.avatar)

            ventana.destroy()
            self.view.actualizar_estado("Usuario actualizado correctamente")

        CTkButton(ventana, text="Guardar cambios", command=guardar_cambios).pack(pady=15)
