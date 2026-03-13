'''

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

def construir_equipo_pokemon(Cantidad: int, Lista_pkmn: list) -> list:
    """
    Determina si Ash puede formar un equipo de Pokémon seudolegendarios.
    Retorna la lista de nombres si se completa la cantidad, de lo contrario None.
    """
    cumplen = []
    
    for pokemon in Lista_pkmn:
        # Calculamos la suma de las 6 estadísticas base
        suma_stats = (
            pokemon["vida"] + 
            pokemon["ataque"] + 
            pokemon["defensa"] + 
            pokemon["ataque_especial"] + 
            pokemon["defensa_especial"] + 
            pokemon["velocidad"]
        )
        
        # Si es seudolegendario (600+), lo añadimos a nuestra lista temporal
        if suma_stats >= 600:
            cumplen.append(pokemon["nombre"])
        
        # Si ya alcanzamos la cantidad exacta requerida, dejamos de buscar
        if len(cumplen) == Cantidad:
            return cumplen
            
    # Si terminamos de recorrer la lista y no completamos la 'Cantidad', retornamos None
    return None
'''

def producto_mas_barato(catalogo:dict) -> str:
    """Retorna el producto mas barato del catalogo"""
    # Si el catalogo esta vacio, retornamos un mensaje 
    if not catalogo:
        return "No hay productos para escoger"

    # Con la funcion min obtenemos el elemento mas barato, tanto el precio como el nombre
    elemento_mas_barato = min(catalogo, key=lambda x: (catalogo[x], x))
    print ("Elemento mas barato:", elemento_mas_barato)
    
    # Buscamos el valor del elemento mas barato en el diccionario
    precio_mas_barato = catalogo[elemento_mas_barato]
    print ("precio de " , elemento_mas_barato, ":", precio_mas_barato)

    # Si el precio es mayor a 10000, retornamos None, de lo contrario retornamos el elemento
    return None if precio_mas_barato > 10000 else elemento_mas_barato

# Prueba de la Función
print(producto_mas_barato({"p1": 10000, "p2": 20000, "argon": 5000, "uranio": 5000}))
    
    
    
    
    


