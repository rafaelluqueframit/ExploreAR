import json

class Monumento:

    def __init__(self, nombre='', info='', ruta='', ruta_imagen='', ruta_ruta='', caracteristicas_monu=[]):
        self.nombre = nombre
        self.info = info
        self.ruta = ruta
        self.ruta_imagen = ruta_imagen
        self.ruta_ruta = ruta_ruta
        self.caracteristicas_monu = caracteristicas_monu
    
    def guardar_datos(self, archivo):
        datos = {
            "nombre": self.nombre,
            "info": self.info,
            "ruta": self.ruta,
            "ruta_imagen": self.ruta_imagen,
            "ruta_ruta": self.ruta_ruta,
            "caracteristicas_monu": self.caracteristicas_monu.tolist()  # Convertir a lista
        }
        with open(archivo, 'w') as file:
            json.dump(datos, file)

    @classmethod
    def cargar_datos(cls, archivo):
        with open(archivo, 'r') as file:
            datos = json.load(file)

        monumento = cls()
        monumento.nombre = datos["nombre"]
        monumento.info = datos["info"]
        monumento.ruta = datos["ruta"]
        monumento.ruta_imagen = datos["ruta_imagen"]
        monumento.ruta_ruta = datos["ruta_ruta"]
        monumento.caracteristicas_monu = datos.get("caracteristicas_monu", [])  # Si no hay características guardadas, devuelve una lista vacía
        
        return monumento
    
    def get(self, atributo):
        """Obtiene el valor del atributo especificado."""
        return getattr(self, atributo, None)