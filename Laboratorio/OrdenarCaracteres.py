def ordenar_cadena(cadena:str)->str:
    
    CadenaOrdena = "".join(sorted(cadena))
    
    
    return CadenaOrdena

print(ordenar_cadena("python"))