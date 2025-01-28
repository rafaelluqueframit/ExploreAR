import json

class Usuario:

    def __init__(self, nombre='', edad=0, foto='', caracteristicas_cara=[]):
        self.nombre = nombre
        self.edad = edad
        self.foto = foto
        self.caracteristicas_cara = caracteristicas_cara
    
    def registarse(self, archivo):
        datos = {
            "nombre": self.nombre,
            "edad": self.edad,
            "foto": self.foto,
            "caracteristicas_cara": self.caracteristicas_cara.tolist()  # Convertir a lista
        }
        with open(archivo, 'w') as file:
            json.dump(datos, file)

    @classmethod
    def cargar_datos(cls, archivo):
        with open(archivo, 'r') as file:
            datos = json.load(file)

        usuario = cls()
        usuario.nombre = datos["nombre"]
        usuario.edad = datos["edad"]
        usuario.foto = datos["foto"]
        usuario.caracteristicas_cara = datos.get("caracteristicas_cara", [])  # Si no hay características guardadas, devuelve una lista vacía
        
        return usuario
    
    def get(self, atributo):
        """Obtiene el valor del atributo especificado."""
        return getattr(self, atributo, None)
