import csv

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        if not usuario.nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not (0 <= usuario.edad <= 120):
            raise ValueError("La edad debe estar entre 0 y 120")
        if usuario.genero not in ("M", "F", "Otro"):
            raise ValueError("El genero debe ser M, F u Otro")
        self._usuarios.append(usuario)

    def guardar_csv(self, ruta="usuarios.csv"):
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(["Nombre", "Edad", "Genero", "Avatar"])
            for usuario in self._usuarios:
                escritor.writerow([usuario.nombre, usuario.edad, usuario.genero, usuario.avatar])

    def cargar_csv(self, ruta="usuarios.csv"):
        self._usuarios.clear()
        try:
            with open(ruta, 'r', encoding="utf-8") as f:
                lector = csv.reader(f)
                next(lector, None)
                for fila in lector:
                    if len(fila) == 4:
                        nombre, edad, genero, avatar = fila
                        self._usuarios.append(Usuario(nombre, int(edad), genero, avatar))
        except FileNotFoundError:
            print("No existe archivo, se creará al guardar.")

    def buscar(self, texto):
        texto = texto.lower()
        return [u for u in self._usuarios if texto in u.nombre.lower()]

    def buscar_genero(self,genero):
        return [u for u in self._usuarios if genero in u.genero]

