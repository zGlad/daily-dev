from art import text2art
import time


lineas = [
    "Nadie nadie sabra jamas",
    "Cuanto te quise",
    "Nadie nadie comprendera",
    "Que nos paso",
    "Aunque el mundo ria feliz",
    "Yo estare triste", 
    "Esperando el retorno",     
    "De nuestro amor"]



def ejecutar_cancion():
    for linea in lineas:
        
            cancion = text2art(linea)
            print(cancion, flush=True)
            time.sleep(2.8)  
    


if __name__ == "__main__":
    try:
        ejecutar_cancion()
    except KeyboardInterrupt:
            print("\n[!] Ejecución pausada por el usuario.")
    
    
