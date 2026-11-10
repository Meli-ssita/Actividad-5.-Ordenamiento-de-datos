def ordenamiento_seleccion(arr: list[float], mostrar_traza: bool = True) -> list[float]:
    """
    Ordena una lista de números flotantes usando el algoritmo de Selección.
    Modifica una copia de la lista para conservar los datos originales.
    """
    datos = arr.copy()
    n = len(datos)
    
    if mostrar_traza:
        print(f"Estado inicial: {datos}\n" + "-" * 45)
    
    for i in range(n - 1):
        min_idx = i
        
        # Buscar el índice del menor elemento en la porción no ordenada
        for j in range(i + 1, n):
            if datos[j] < datos[min_idx]:
                min_idx = j
                
        # Intercambiar solo si el mínimo encontrado está en una posición distinta
        if min_idx != i:
            valor_original = datos[i]
            datos[i], datos[min_idx] = datos[min_idx], datos[i]
            if mostrar_traza:
                print(f"Paso {i + 1}: Intercambio {valor_original} ↔ {datos[i]}")
        else:
            if mostrar_traza:
                print(f"Paso {i + 1}: {datos[i]} ya está en su posición correcta")
                
        if mostrar_traza:
            print(f"  Arreglo actual: {datos}\n")
            
    return datos


# Dataset de temperaturas
temperaturas = [25.4, 12.8, 35.1, 4.2, 18.5]

resultado = ordenamiento_seleccion(temperaturas, mostrar_traza=True)
print(f"Arreglo final ordenado: {resultado}")
