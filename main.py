""" 
Proxy es un patrón de diseño estructural que te permite proporcionar un sustituto o marcador 
de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote 
hacer algo antes o después de que la solicitud llegue al objeto original.

"""
from abc import ABC, abstractmethod

class Imagen(ABC):
    @abstractmethod
    def mostrar(self):
        pass


class ImagenReal(Imagen):
    def __init__(self, archivo):
        self.archivo = archivo
        self._cargar_imagen()

    def _cargar_imagen(self):
        print(f"Cargando imagen...")
        # Simulación de una carga pesada de recursos
        import time
        time.sleep(2)

    def mostrar(self):
        print(f"Mostrando imagen: {self.archivo}")


class ProxyImagen(Imagen):
    def __init__(self, archivo):
        self.archivo = archivo
        self._imagen_real = None

    def mostrar(self):
        if self._imagen_real is None:
            print("Imagen aún no cargada")
            self._imagen_real = ImagenReal(self.archivo)
        self._imagen_real.mostrar()


def cliente(imagen: Imagen):
    imagen.mostrar()


if __name__ == "__main__":
    print("Primera vez que se accede a la imagen:\n")
    proxy = ProxyImagen("imagen_ejemplo.png")
    cliente(proxy)
    
    print("\nSegunda vez que se accede a la misma imagen:\n")
    cliente(proxy)
    