# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:38:27 2021

@author: AndreDesktop
"""

#transpoInversa="SARAR TNOCN EONIM AGREP LENEA IBASA RBALAP"[::-1]#Texto a transponer inversamente
#print(transpoInversa)

def transposicionSimple(transpoSimple):
    transpoSimple=transpoSimple.strip()
    transpoSimple=transpoSimple.replace(" ","")
    lstTranspoSimple=[]
    for caracter in transpoSimple:
        lstTranspoSimple.append(caracter)
    registro1=[]
    registro2=[]
    for i in range(len(lstTranspoSimple)):
        if len(lstTranspoSimple)==0:
            break
        else:
            registro1.append(lstTranspoSimple.pop(0))
            if len(lstTranspoSimple)==0:
                break
            else:    
                registro2.append(lstTranspoSimple.pop(0))    
    cadenaTranspuesta1=""
    cadenaTranspuesta1.join(registro1)
    cadenaTranspuesta2=""
    cadenaTranspuesta2.join(registro2)
    transpoCompleta=cadenaTranspuesta1+cadenaTranspuesta2
    print (registro1)
    print (registro2)
    return transpoCompleta

    
    
    

cadena2=""
cadena="SOPADELLETRAS"
cadena2=cadena2+transposicionSimple(cadena)

