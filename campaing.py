from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import *

#a. En un archivo campaña.py, definir la clase que permita crear instancias de tipo Campaña.

class Campaing: #Si se tiene que instanciar con un componente de la clase Anuncio, la clase debe existir antes.
    #Uso de función __init__, para asignar valores.
    def __init__(self, nombre, fecha_inicio, fecha_termino):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.componer_anuncios()]

    def componer_anuncios(self):

        opcion = int(input("Que tipo de anuncio quieres agregar? (1- Video | 2- Display | 3- Social)"))
        if opcion == 1:
            duracion = int(input("Ingrese la duración del video (en segundos): "))
            new_anuncio = Video(duracion)
        elif opcion == 2:
            new_anuncio = Display()
        elif opcion == 3:
            new_anuncio == Social ()
        
        return new_anuncio

    
    def agregar_anuncio(self):
        #Opcion que el usuario entra a bucle en agregar anuncios.?
        while True:
            try:
                opcion = int(input("Que tipo de anuncio quieres agregar? (1- Video | 2- Display | 3- Social | 4- Para Salir)"))
                        
                if opcion == 1:
                    duracion = int(input("Ingrese la duración del video (en segundos): "))
                    new_anuncio = Video(duracion)
                elif opcion == 2:
                    new_anuncio = Display()
                elif opcion == 3:
                    new_anuncio == Social ()          
                else:
                    break
                
                self.__anuncios.append(new_anuncio)

            except Exception as e:
                pass


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
        return f"nombre de campaña: {self.nombre} - {self.__anuncios}"
