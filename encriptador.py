import numpy as np
alfabeto_hill_equivnum = { #Declaramos el alfabeto a utilizar en el cifrado de hill
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

alfabeto_hill_num_a_texto= { #Declaramos el alfabeto a utilizar en el cifrado de hill
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

f=open("texto a cifrar.txt","r") #leemos el archivo
entrada_archivo_texto=f.read()   #almacenamos en memoria el texto
texto_a_cifrar=entrada_archivo_texto.upper() #Lo convertimos a mayúsculas para poderlo manipular satisfactoriamente
equiv_num_mensaje=[] #Declaramos la variable que almacenará los equivalentes numéricos del mensaje
for letra in texto_a_cifrar:
    equiv_num_mensaje.append(alfabeto_hill_equivnum[letra]) #Convertimos cada letra del mensaje a su Equivalente numérico

m1=np.array(equiv_num_mensaje[0:]) #Partimos a la mitad y tomamos el primer segmento
#m2=np.array(equiv_num_mensaje[len(equiv_num_mensaje)//2:]) #Tomamos el segundo segmento 

clave_k=np.array([[6,24,1],[13,16,10],[20,17,15]])

determinant=int(np.round_(np.linalg.det(clave_k)))
km1=np.dot(clave_k,m1)%26
#km2=np.dot(clave_k,m2)%27

Cripto=""

for equiv_num in km1:
    Cripto=Cripto+alfabeto_hill_num_a_texto[equiv_num]
    

#for equiv_num in km2:
#    Cripto=Cripto+alfabeto_hill_num_a_texto[equiv_num]
    

print ("El mensaje cifrado es:",Cripto)


print ("Descifrando el mensaje")


determinante=np.linalg.det(clave_k)
determinanteMod=determinante%27
determinante_inv=(26+1)/determinanteMod
clave_inv= np.transpose(clave_k)
detInv=1/determinante

inv_clav=np.dot(detInv,clave_inv)

