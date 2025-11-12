import csv


class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar  # ruta relativa en assets/

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []  # lista de Usuario
        self._usuarios.append(Usuario("Ana", 25, "F", "avatar_ana.png"))
        self._usuarios.append(Usuario("Luis", 30, "M", "avatar_luis.png"))
        self._usuarios.append(Usuario("Alex", 22, "Otro", "avatar_alex.png"))
    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        # validaciones mínimas (nombre no vacío, edad en rango, genero permitido)
        if not usuario.nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not (0 <=usuario.edad <=120):
            raise  ValueError("La edad debe estar entre 0 y 120")
        if usuario.genero not in ("M","F","Otro"):
            raise  ValueError("El genero debe ser M,F u Otro")
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        if 0<=indice < len(self._usuarios):
            self._usuarios.pop(indice)
        else:
            raise IndexError("Índice fuera de rango")

    def actualizar(self, indice: int, usuario_actualizado: Usuario):
        if 0 <= indice < len(self._usuarios):
            self._usuarios[indice] = usuario_actualizado
        else:
            raise IndexError("Índice fuera de rango")

    def guardar_csv(self, ruta: str = "usuarios.csv"):
       try:
            with open(ruta, 'w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerow(["Nombre","Edad","Genero","Avatar"])
                for usuario in self._usuarios:
                    escritor.writerow([usuario.nombre,usuario.edad,usuario.genero,usuario.avatar])
            print(f"Usuarios guardados correctamente")
       except Exception as e:
           print(f"Error al guardar el archivo : {e}")

    def cargar_csv(self, ruta: str = "usuarios.csv"):
        # limpia y repuebla _usuarios; maneja FileNotFoundError y filas corruptas
        self._usuarios.clear()
        try:
            with open(ruta,'r',encoding="utf-8") as f:
                lector= csv.reader(f)
                next(lector,None)
                for fila in lector:
                    if len(fila)==4:
                        nombre,edad,genero,avatar = fila
                        try:
                            edad= int(edad)
                            self._usuarios.append(Usuario,nombre,edad,genero,avatar)
                        except ValueError:
                            print(f"Edad no numerica{fila}")
                    else:
                        print(f"Fila erronea{fila}")
        except FileNotFoundError:
            print(f"No se encontró el archivo {ruta}. Se creará al guardar.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
