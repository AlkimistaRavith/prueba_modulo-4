from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import *

#a. En un archivo campaña.py, definir la clase que permita crear instancias de tipo Campaña.

class Campaign: #Si se tiene que instanciar con un componente de la clase Anuncio, la clase debe existir antes.
    #Uso de función __init__, para asignar valores.
    def __init__(self, nombre, fecha_inicio, fecha_termino):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        self.agregar_anuncio()


    
    def agregar_anuncio(self):
        while True:
            try:
                opcion = int(input("Qué tipo de anuncio quieres agregar? (1- Video | 2- Display | 3- Social | 4- Salir): "))

                if opcion == 1:
                    duracion = int(input("Ingrese la duración del video (en segundos): "))
                    sub_tipo = input("Ingrese el subtipo del video (Instream/Outstream): ")
                    new_anuncio = Video(duracion, sub_tipo)

                elif opcion == 2:
                    ancho = int(input("Ingrese el ancho: "))
                    alto = int(input("Ingrese el alto: "))
                    url_archivo = input("Ingrese la URL del archivo: ")
                    url_click = input("Ingrese la URL de clic: ")
                    sub_tipo = input("Ingrese el subtipo (Tradicional/Native): ")
                    new_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)

                elif opcion == 3:
                    ancho = int(input("Ingrese el ancho: "))
                    alto = int(input("Ingrese el alto: "))
                    url_archivo = input("Ingrese la URL del archivo: ")
                    url_click = input("Ingrese la URL de clic: ")
                    sub_tipo = input("Ingrese el subtipo (Facebook/LinkedIn): ")
                    new_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)

                elif opcion == 4:
                    break
                else:
                    print("Opción inválida.")
                    continue

                self.__anuncios.append(new_anuncio)

            except Exception as e:
                print(f"Error al agregar anuncio: {e}")


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
        count_video = sum(1 for a in self.__anuncios if isinstance(a, Video))
        count_display = sum(1 for a in self.__anuncios if isinstance(a, Display))
        count_social = sum(1 for a in self.__anuncios if isinstance(a, Social))
        
        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Anuncios: {count_video} Video, {count_display} Display, {count_social} Social")
