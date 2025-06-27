from abc import abstractmethod, ABC
from error import LargoExcedidoError

class Anuncio(ABC):
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.__ancho = ancho if ancho > 0 else 1 #Puede ser: = validar_dimension(ancho) donde validar_dimension() esta en un archivo de validadores.
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
#ancho
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho
#alto
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        self.__alto = alto
#url_archivo
    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
#url_clic
    @property
    def url_clic(self):
        return self.__url_clic
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic
#sub_tipo
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        pass

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass



class Campaing: #Si se tiene que instanciar con un componente de la clase Anuncio, la clase debe existir antes.
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = list[Anuncio]

    def componer_anuncios(self):
        anuncios = []
        opcion = int(input("Que tipo de anuncio quieres agregar? (1- Video | 2- Display | 3- Social)"))
        if opcion == 1:
            duracion = int(input("Ingrese la duración del video (en segundos): "))
            new_anuncio = Video(duracion)
        elif opcion == 2:
            new_anuncio = Display()
        elif opcion == 3:
            new_anuncio == Social ()
        
        return new_anuncio
        #self.__anuncios.append()
        


#nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoError("El largo ingresado supera los 250 carácteres.")
#fecha_inicio
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
#fecha_termino
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino
#anuncios
    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        return f"""Nombre de la campaña: 
Campaña 1 Anuncios: 1 Video, 2 Display, 0 Social
"""

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPO = ("instream","outstream")

    def __init__(self, duracion):
        self.ancho = 1
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")



class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPO = ("tradicional", "native")

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPO = ("facebook", "linkedin")

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
