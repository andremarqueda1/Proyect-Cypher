##################################################
# Archivo: Playfair
# Lenguaje: Python v.3.10.0
# Autor: García Villegas Daniel
# Fecha de creación/modificación: 10/10/21
# Descripción: Encripta un mensaje obtenido desde
# un string implementando el algoritmo Playfair
# para posteriormente desencriptarlo.
##################################################

######################################################################
#
# Funciones para cifrar el mensaje obtenido del algoritmo Hill
#
######################################################################

def GeneraListaAlfabeto():  # Genera una lista con el alfafabeto definido.
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Alfabeto a implementar, no se incluye las letras J ni Ñ
    lista = []
    
    for letra in alfabeto:
        lista.append(letra) # Añadimos elemento a elemento del alfabeto dentro de la lista.
    
    return lista    # Regresamos la lista con el alfabeto completo.

def NormalizaMsj(MsjOriginal):    # Normaliza el mensaje cifrado obtenido en el algoritmo Series
    #MsjOriginal = MsjOriginal.upper()   # Convierte el mensaje cifrado a mayúsculas.
    #MsjOriginal = MsjOriginal.replace(" ","")   # Elimina espacios.
    #MsjOriginal = MsjOriginal.replace(",","")   # Elimina comas.
    #MsjOriginal = MsjOriginal.replace(".","")   # Elimina puntos.
    MsjOriginal = MsjOriginal.replace("J","I")   # Reemplaza "J" por "I".
    posicion = 0    # Declaración de variables.
    MsjNormalizado = ""
    
    while (posicion < len(MsjOriginal)-1):    # Valida que en cada dupla no se repita la letra y de ser así, remplaza la segunda por "x".
        primera_letra = MsjOriginal[posicion]
        segunda_letra = MsjOriginal[posicion+1]

        if(primera_letra == segunda_letra):
            MsjNormalizado += primera_letra + "X"   # Reemplaza con una "X" la segunda letra de la dupla repetida.
            posicion += 1
        else:
            MsjNormalizado += primera_letra + segunda_letra
            posicion += 2
    
    if(posicion < len(MsjOriginal)):
        MsjNormalizado += MsjOriginal[posicion] + "X"   # Añade una "X" al mensaje para tener una longitud de cadena par.
    
    return MsjNormalizado    # Regresa el mensaje normalizado

def GeneraMatriz(key):
    alfabeto = GeneraListaAlfabeto()    #Generamos una lista con el alfabeto a implementar.
    matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]  # Declaramos una matriz de 5x5.
    fila = 0    # Declaramos variables.
    columna = 0
    posicion = 0
    
    for letra in key:   # Definimos la fila en donde se encuentra la letra de la llave en análisis.
        if(posicion < 5):
            fila = 0
        elif (posicion < 10):
            fila = 1
        elif (posicion < 15):
            fila = 2
        elif (posicion < 20):
            fila = 3
        elif (posicion < 25):
            fila = 4
        columna = posicion % 5

        if(letra in alfabeto):
            alfabeto.remove(letra)  # Eliminamos de la lista aquellas letras que contenga la llave.
            matriz[fila][columna] = letra   # Insertamos la letra del alfabeto en la matriz de 5x5.
            posicion += 1
    
    while (len(alfabeto) > 0):
        if(posicion < 5):   # Definimos la fila en donde se encuentra la letra de la llave en análisis.
            fila = 0
        elif (posicion < 10):
            fila = 1
        elif (posicion < 15):
            fila = 2
        elif (posicion < 20):
            fila = 3
        elif (posicion < 25):
            fila = 4
        columna = posicion % 5
        matriz[fila][columna] = alfabeto.pop(0) # Insertamos las letras restantes de la lista a la matriz de 5x5.
        posicion += 1
    
    return matriz

def IndiceDeElementoEnMatriz(matriz, letra):    # Obtenemos el índice de la letra buscada
    posicionMatriz = 0
    for fila in matriz:
        for columna in fila:
            if(columna == letra):
                if(posicionMatriz < 5): # Definimos la fila en donde se encuentra la letra de la llave en análisis.
                    i = 0
                elif (posicionMatriz < 10):
                    i = 1
                elif (posicionMatriz < 15):
                    i = 2
                elif (posicionMatriz < 20):
                    i = 3
                elif (posicionMatriz < 25):
                    i = 4
                return [i, posicionMatriz % 5]  # Regresamos el índice de la letra encontrada.
            posicionMatriz += 1

def CifraMsj(MsjNormalizado, matriz):   #Ciframos el mensaje en claro.
    posicion = 0
    MsjCifrado = "" # Declaramos la cadena de caracteres que almacenará el mensaje cifrado por el algoritmo Playfair.
    while (posicion < len(MsjNormalizado)):
        primera_letra = MsjNormalizado[posicion]    # Seleccionamos de par en par las letras que conforman el mensaje normalizado.
        segunda_letra = MsjNormalizado[posicion+1]
        
        indice_primera_letra = IndiceDeElementoEnMatriz(matriz, primera_letra)  # Obtenemos los índices de las letras de par en par.
        indice_segunda_letra = IndiceDeElementoEnMatriz(matriz, segunda_letra)

        if (indice_primera_letra[0] == indice_segunda_letra[0]): # Ambas letras están en la misma fila
            MsjCifrado += matriz[ indice_primera_letra[0]][(indice_primera_letra[1]+1)%5] + matriz[indice_segunda_letra[0]][(indice_segunda_letra[1]+1)%5]
        
        if (indice_primera_letra[1] == indice_segunda_letra[1]): # Ambas letras están en la misma columna
            MsjCifrado += matriz[(indice_primera_letra[0]+1)%5][indice_primera_letra[1]] + matriz[(indice_segunda_letra[0]+1)%5][indice_segunda_letra[1]]
    
        if (indice_primera_letra[0] != indice_segunda_letra[0] and indice_primera_letra[1] != indice_segunda_letra[1]): # Ambas letras están en filas y columnas diferentes
            MsjCifrado += matriz[indice_primera_letra[0]][indice_segunda_letra[1]] + matriz[indice_segunda_letra[0]][indice_primera_letra[1]]
        posicion += 2
        
    return MsjCifrado

######################################################################
#
# Funciones para descifrar el mensaje obtenido del algoritmo Playfair
#
######################################################################

def NormalizaMsjDescifrado(MsjDescifrado):    # Normaliza el mensaje descifrado obtenido en el algoritmo PlayFair
    #MsjOriginal = MsjOriginal.upper()   # Convierte el mensaje cifrado a mayúsculas.
    #MsjOriginal = MsjOriginal.replace(" ","")   # Elimina espacios.
    #MsjOriginal = MsjOriginal.replace(",","")   # Elimina comas.
    #MsjOriginal = MsjOriginal.replace(".","")   # Elimina puntos.
    MsjDescifrado = MsjDescifrado.replace("I","J")   # Reemplaza "J" por "I".
    posicion = 0    # Declaración de variables.
    MsjNormalizado = ""
    
    while (posicion < len(MsjDescifrado)-1):
        primera_letra = MsjDescifrado[posicion]
        segunda_letra = MsjDescifrado[posicion+1]

        if(primera_letra != segunda_letra and segunda_letra != "X"):
            MsjNormalizado += primera_letra + segunda_letra
            posicion += 2
        elif (posicion < len(MsjDescifrado)-2):
            if(primera_letra == MsjDescifrado[posicion+2]):
                MsjNormalizado += primera_letra + MsjDescifrado[posicion+2]
            else:
                MsjNormalizado += primera_letra
            posicion += 3
    
    return MsjNormalizado    # Regresa el mensaje normalizado


def DescifraMsj(MsjCifrado, matriz):   #Desciframos el mensaje.
    posicion = 0
    MsjDescifrado = "" # Declaramos la cadena de caracteres que almacenará el mensaje descifrado por el algoritmo Playfair.
    while (posicion < len(MsjCifrado)):
        primera_letra = MsjCifrado[posicion]    # Seleccionamos de par en par las letras que conforman el mensaje cifrado.
        segunda_letra = MsjCifrado[posicion+1]
        
        indice_primera_letra = IndiceDeElementoEnMatriz(matriz, primera_letra)  # Obtenemos los índices de las letras de par en par.
        indice_segunda_letra = IndiceDeElementoEnMatriz(matriz, segunda_letra)

        if (indice_primera_letra[0] == indice_segunda_letra[0]): # Ambas letras están en la misma fila
            MsjDescifrado += matriz[ indice_primera_letra[0]][(indice_primera_letra[1]-1)%5] + matriz[indice_segunda_letra[0]][(indice_segunda_letra[1]-1)%5]
        
        if (indice_primera_letra[1] == indice_segunda_letra[1]): # Ambas letras están en la misma columna
            MsjDescifrado += matriz[(indice_primera_letra[0]-1)%5][indice_primera_letra[1]] + matriz[(indice_segunda_letra[0]-1)%5][indice_segunda_letra[1]]
    
        if (indice_primera_letra[0] != indice_segunda_letra[0] and indice_primera_letra[1] != indice_segunda_letra[1]): # Ambas letras están en filas y columnas diferentes
            MsjDescifrado += matriz[indice_primera_letra[0]][indice_segunda_letra[1]] + matriz[indice_segunda_letra[0]][indice_primera_letra[1]]
        posicion += 2
        
    return MsjDescifrado

######################################################################
#
# Programa Principal
#
######################################################################

key = "CLAVE"
print ("\nKey: " + key)
mensaje = "MENSAJEENCLARO"
print ("\nMensaje en claro: " + mensaje)
print ("\nGenerando matriz...")
matriz = GeneraMatriz(key)
print ("\nLa matriz generada es", end=":")

for fila in range(5):
    print("\n")
    for columna in range(5):
        print (matriz[fila][columna], end="  ")

print("\n\nNormalizando mensaje...")
MsjNormalizado = NormalizaMsj(mensaje)
print("\nEl mensaje normalizado es: " + MsjNormalizado)
print("\nCifrando mensaje...")
MsjCifrado = CifraMsj(MsjNormalizado,matriz)
print("\nEl mensaje cifrado es: " + MsjCifrado)
print("\nDescifrando mensaje...")
MsjDescifrado = DescifraMsj(MsjCifrado,matriz)
print("\nEl mensaje descifrado es: " + MsjDescifrado)
print("\nNormalizando mensaje descifrado...")
MsjNormalizadoDecifrado = NormalizaMsjDescifrado(MsjDescifrado)
print("\nEl mensaje descifrado normalizado es: " + MsjNormalizadoDecifrado)
print("\nEl programa ha finalizado.\n")