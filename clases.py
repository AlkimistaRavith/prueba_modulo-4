from abc import abstractmethod, ABC

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
    pass


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
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPO = ("facebook", "linkedin")