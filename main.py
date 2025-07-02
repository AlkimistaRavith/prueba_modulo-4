from campaign import *
from datetime import date




c = Campaign("Campaña 1", "12/06/2025", "22/07/2025")

print(f"{c}\n")

#Muestra de los métodos comprimir y redimensionar anuncio para cada tipo:
#VIDEO
print("### PRUEBAS CLASE VIDEO ###")
video1 = Video(-10, "Instream")
video1.comprimir_anuncio()
video1.redimensionar_anuncio()
print(f"Duración de video: {video1.duracion}")

print("\n### PRUEBAS CLASE DISPLAY ###")
display1 = Display(300, 250, "url_archivo", "url_click", "Native")
display1.comprimir_anuncio()
display1.redimensionar_anuncio()

print("\n### PRUEBAS CLASE SOCIAL ###")
social1 = Social(400, 400, "archivo_social", "clic_social", "Facebook")
social1.comprimir_anuncio()
social1.redimensionar_anuncio()