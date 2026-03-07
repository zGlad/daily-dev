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