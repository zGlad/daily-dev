# pip install yt-dlp - librería

# Importamos la librería bajo el alias 'yt' para escribir menos código
import yt_dlp as yt 

# 1. Captura de datos: Pedimos al usuario la dirección del video
url = input("Enter YouTube Video Link: ") 

# 2. Configuración: Creamos un diccionario con las opciones de descarga
# 'format': 'best' le indica al programa que busque la resolución más alta combinada
yt_opts = {'format' : 'best'} 

# 3. Ejecución Segura: Usamos la sentencia 'with' para abrir el descargador.
# Esto asegura que los recursos se cierren correctamente al terminar.
with yt.YoutubeDL(yt_opts) as ydl:
    # El método download recibe una LISTA [] de URLs, por eso usamos los corchetes
    ydl.download([url])
    
# 4. Feedback: Avisamos al usuario que el proceso terminó con éxito
print("¡Descarga completada!")




