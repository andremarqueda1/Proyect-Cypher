import numpy as np

def matrix_cofactor(matrix):
    return np.linalg.inv(matrix).T * np.linalg.det(matrix)

alfabeto_hill_equivnum = { #Declaramos el diccionario  a utilizar en el cifrado de hill
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'W' : 22,
    'X' : 23,
    'Y' : 24,
    'Z' : 25
    }

alfabeto_hill_num_a_texto= { #Declaramos el alfabeto a utilizar en el descifrado de hill
     0 : 'A',
     1 : 'B',
     2 : 'C',
     3 : 'D',
     4 : 'E',
     5 : 'F',
     6 : 'G',
     7 : 'H',
     8 : 'I',
     9 : 'J',
    10 : 'K',
    11 : 'L',
    12 : 'M',
    13 : 'N',
    14 : 'O',
    15 : 'P',
    16 : 'Q',
    17 : 'R',
    18 : 'S',
    19 : 'T',
    20 : 'U',
    21 : 'V',
    22 : 'W',
    23 : 'X',
    24 : 'Y',
    25 : 'Z'
    } 

"""
#######################################
CIFRADO DEL MENSAJE (ALGORITMO DE HILL)
#######################################
"""
print("Leyendo archivo....\n")
f=open("texto a cifrar.txt","r") #leemos el archivo
entrada_archivo_texto=f.read()   #almacenamos en memoria el texto
texto_a_cifrar=entrada_archivo_texto.upper() #Lo convertimos a mayúsculas para poderlo manipular satisfactoriamente
print("Texto a cifrar: ",texto_a_cifrar)
equiv_num_mensaje=[] #Declaramos la variable que almacenará los equivalentes numéricos del mensaje
mensaje_segmentado=[]
for letra in texto_a_cifrar:
    equiv_num_mensaje.append(alfabeto_hill_equivnum[letra]) #Convertimos cada letra del mensaje a su Equivalente numérico

for i in range (len(equiv_num_mensaje)): #Debido a que la clave es una matriz de 3X3 , segmentamos
    i=i*3 #el mensaje en trigramas (vectores individuales de cardinalidad de grado 3)
    mensaje_segmentado.append(equiv_num_mensaje[i:i+3]) #Tomamos 3 elementos y 
    if i+3>len(equiv_num_mensaje): # y posteriormente tres elementos
        break
    #Debido a que la matriz debe contener forzozamente tres elementos por vector
    #Es necesario acompletar (en caso de ser necesario) el vector con menos de tres elementos
while len(mensaje_segmentado[len(mensaje_segmentado)-1])<3 and len(mensaje_segmentado[len(mensaje_segmentado)-1])>0 :
    mensaje_segmentado[len(mensaje_segmentado)-1].append(23) #Donde 23 es el equivalente numérico de 'X'

if mensaje_segmentado[len(mensaje_segmentado)-1]==[] :
    mensaje_segmentado.pop()
    
clave_k=np.array([[6,24,1],[13,16,10],[20,17,15]])

km=[]
for i in range (len(mensaje_segmentado)):    #Realizamos la multiplicación
    km.append(np.round(np.dot(clave_k,mensaje_segmentado[i]))%26)  #y almacenamos el resultado

cifrado_EquivNum=[] #Declaramos la variable que almacenará como vector  
for lst in km: #El resultado concatenado de todas las multiplicaciónes
    for j in range(len(lst)): #De los trigramas por la clave
        cifrado_EquivNum.append(lst[j])
cifrado_texto_hill=""

for i in range(len(cifrado_EquivNum)): #Regresamos a su análogo textual y concatenamos el mensaje
    cifrado_texto_hill=cifrado_texto_hill+alfabeto_hill_num_a_texto[cifrado_EquivNum[i]] 
    
print("El mensaje cifrado es: ",cifrado_texto_hill)
    
"""
#######################################
DECIFRADO DEL MENSAJE (ALGORITMO DE HILL)
#######################################
"""
print ("***Descifrando el mensaje***")

determinant=int(np.round_(np.linalg.det(clave_k)))
determinantmod=determinant%26
m_cofactores=matrix_cofactor(clave_k)
m_cofactores_trans=m_cofactores.transpose()
claveinversa=(determinantmod*m_cofactores_trans)%26

descipher_vec=[] #Descipher_vec mantendrá los vectores individuales multiplicados por la inversa
for i in range (len(km)): #de la clave K por cada uno de los trigramas 
    descipher_vec.append(np.round(np.dot(claveinversa,km[i]))%26)

descipher_vec_unitario=[]
for lst in descipher_vec: #El resultado concatenado de todas las multiplicaciónes
    for j in range(len(lst)): #De los trigramas por la clave
        descipher_vec_unitario.append(lst[j])

descifrado_hill_texto=""
for i in range (len(descipher_vec_unitario)):
    descifrado_hill_texto=descifrado_hill_texto+alfabeto_hill_num_a_texto[descipher_vec_unitario[i]]

print("El texto descifrado es: ",descifrado_hill_texto)
