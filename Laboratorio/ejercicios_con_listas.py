def promedio_lista(numeros: list) -> float:
    """Calcula el promedio de los números mayores a cero en una lista."""
    sumatoria = 0 
    total = 0 
    
    for num in numeros:
        if num > 0: 
            sumatoria += num
            total += 1
    
    # Nota: Podría dar ZeroDivisionError si la lista está vacía o solo tiene negativos
    return sumatoria / total

def menor_posicion_lista(numeros: list) -> int:
    """Retorna el índice del número más pequeño de la lista."""
    menor = numeros[0]
    indice = 0
    
    for i in range(1, len(numeros)):
        if numeros[i] < menor:
            menor = numeros[i]
            indice = i
    return indice

def buscar_elemento(entrada: list, buscado: int) -> int:
    """
    Busca un elemento y retorna su posición. 
    Si no existe, retorna -1 en lugar de lanzar un error.
    """
    try: 
        return entrada.index(buscado)
    except ValueError: 
        return -1

# --- Casos de Prueba ---
print("Promedio de la lista:", promedio_lista([1, 2, 3, 4, 5]))
print("Índice del menor:", menor_posicion_lista([1, 2, 3, 4, 5]))
print("Búsqueda exitosa (3):", buscar_elemento([1, 2, 3, 4, 5], 3))
print("Búsqueda fallida (6):", buscar_elemento([1, 2, 3, 4, 5], 6))

def encontrar_mayor(entrada: list) -> int:
    """Retorna el mayor número de la lista."""
    # Verificamos que la lista no este vacia
    if not entrada:
            return -1 # No hay elementos en la lista, retornamos -1
        
    # Asignamos el primer elemento como el mayor    
    mayor = entrada[0]

    # Recorremos la lista y actualizamos el mayor
    for i in range(1, len(entrada)):
        if entrada[i] > mayor:
            mayor = entrada[i]
        if entrada[i] < 0: # Si encuentra un negativo, retorna 0
            return 0
    return mayor

def intercalar_palabras(cad1:str, cad2:str) -> str:
    """Intercala las palabras de dos cadenas de texto."""
    resultado = ""
    palabras_1 = cad1.split()
    palabras_2 = cad2.split()

    for i in range(len(palabras_1)):
        resultado += f"{palabras_1[i]} {palabras_2[i]} "

    return resultado


def calcular_definitivas(estudiantes:list) -> list:
    """Calcula la nota definitiva de los estudiantes aproximando"""
    
    # Recorremos la lista de diccionarios de estudiantes
    for estudiante in estudiantes:
        nota = estudiante["nota"]
        
        # Aproximamos la nota segun cada caso
        if nota >= 4.5: 
            nota = 5.0
        elif nota >= 3.5:
            nota = 4.0
        elif nota >= 2.5: 
            nota = 3.0
        else: 
            nota = 1.5  
        
        # Actualizamos "nota" en el diccionario con la variable local 
        estudiante["nota"] = nota
    
    return estudiantes # Retornamos la lista actualizada

# Prueba de la Función
print(calcular_definitivas([{"nombre": "Carlos", "nota": 3.9},
                            {"nombre": "Ana", "nota": 4.6},
                            {"nombre": "alberto", "nota": 4.0},
                            {"nombre": "Zulema", "nota": 3.0},
                            {"nombre": "Bernardo", "nota": 2.0}]))
        
        
        
        
            
        
        
        
    
    


