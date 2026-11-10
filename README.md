# Actividad-5.-Ordenamiento-de-datos
Problema de Ordenamiento Problema:  Dataset numérico desorganizado: Un arreglo o vector compuesto por 5 números flotantes reales desordenados que representan los promedios de temperatura de la estación meteorológica.  Con los siguientes datos.  [25.4, 12.8, 35.1, 4.2, 18.5]  Aplicando el Algoritmo de Ordenamiento por Selección (Selection Sort)

#¿Qué hace?
El método de selección busca el elemento más pequeño de la lista y lo intercambia con el elemento de la primera posición. Luego, busca el segundo más pequeño y lo intercambia con la segunda posición, repitiendo el proceso secuencialmente hasta recorrer todo el arreglo.


#Pseudocodigo
Algoritmo OrdenamientoPorSeleccion
    Definir arreglo como Arreglo de Reales
    arreglo <- [25.4, 12.8, 35.1, 4.2, 18.5]
    Definir n, i, j, indice_minimo como Entero
    Definir auxiliar como Real
    
    n <- Longitud(arreglo)  // n = 5
    
    // Recorrer el arreglo hasta la penúltima posición
    Para i <- 0 Hasta n - 2 Con Paso 1 Hacer
        indice_minimo <- i
        
        // Buscar el índice del menor elemento en el subarreglo no ordenado
        Para j <- i + 1 Hasta n - 1 Con Paso 1 Hacer
            Si arreglo[j] < arreglo[indice_minimo] Entonces
                indice_minimo <- j
            FinSi
        FinPara
        
        // Intercambiar si se encontró un mínimo menor en otra posición
        Si indice_minimo != i Entonces
            auxiliar <- arreglo[i]
            arreglo[i] <- arreglo[indice_minimo]
            arreglo[indice_minimo] <- auxiliar
        FinSi
    FinPara

    Escribir "Arreglo ordenado:", arreglo
FinAlgoritmo
