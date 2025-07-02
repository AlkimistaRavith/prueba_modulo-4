from abc import abstractmethod, ABC
from error import LargoExcedidoError, SubTipoInvalidoError

#b. En un archivo anuncio.py, definir la clase Anuncio y las clases que permitan crear instancias de tipo Video, Display y Social
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
        if (isinstance(self,Video) and sub_tipo in Video.SUB_TIPO
            or isinstance(self,Social) and sub_tipo in Social.SUB_TIPO
            or isinstance(self,Display) and sub_tipo in Display.SUB_TIPO):
            self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoError("Error de tipo inválido.")


    @staticmethod
    def mostrar_formatos():
        return {Video.FORMATO} - {Social.FORMATO}

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass

#Clase Video
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPO = ("Instream", "Outstream")

    def __init__(self, duracion, sub_tipo):
        super().__init__(ancho=1, alto=1, url_archivo="default.mp4", url_clic="https://clic.com", sub_tipo=sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"Video(duración: {self.duracion}, tipo: {self.sub_tipo})"

#Clase Display
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPO = ("Tradicional", "Native")

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"Display({self.ancho}x{self.alto}, sub_tipo: {self.sub_tipo})"

#Clase Social
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPO = ("Facebook", "LinkedIn")

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"Social({self.ancho}x{self.alto}, sub_tipo={self.sub_tipo})"