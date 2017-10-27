# coding=utf-8
#================================================
# Proyecto Segundo Parcial Matemáticas Computacionales: Cocke–Younger–Kasami Algorithm
# octubre de 2017
#
# Autores:
#          A01234223 Daniel Amezcua Sánchez  
#          A01201954 Alejandro Salmón Félix Díaz
#          A01700585 Javier Iñaqui Aicinena Vargas
#
# Programa desarrollado usando Python 2.7.6
#
#=================================================
import fileinput

def concatenar(string1, string2):
    resultau = [] 
    string1 = str(string1)
    string2 = str(string2)
    for i in range(len(string1)):
        for j in range(len(string2)):
            aux = string1[i] + string2[j]
            resultau.append(aux)
    return resultau 
    
#Inicializa una matriz de n*n. Input: n(tamaño del arreglo) Output: Matriz inicializada a 0
def inicializarMatriz(n):
    return [['0' for j in range(n)] for i in range(n)]
    
#Llena la primer fila de la patriz con las producciones de los simbolos terminales 
def llenarPrimeraFila(matriz,string,producciones):
    n = len(matriz)
    for i in range(0,n):
        simbolo=string[i]
        #Iterar sobre el diccionario de producciones
        for key,values in producciones.items():
            if simbolo in values:
                if matriz[i][0] == '0':
                    matriz[i][0] = ''
                matriz[i][0]+=key

#Del archivo dado, obtiene las tanto las Producciones de la forma A->a y A->BC, como los strings de prueba
def leerInput():
    #Inicializar Arreglos y Diccionarios
    producciones={}
    strings=[]
    archivo = []
    
    #Iterar sobre el input dado y construir un arreglo con las líneas de este
    for linea in fileinput.input():
        fileinput.isfirstline()
        archivo.append(linea)
        if fileinput.isfirstline():
            simboloInicial = linea.split()[0]
    
    #Iterar sobre las líneas del input para construir las producciones y los strings de prueba
    for linea in archivo:
        linea=linea.split()
        n = len(linea)
        if (n==1): #Es un string
            strings=strings + [linea[0]]
        else: #Es es una producción
            producciones[linea[0]]=[]
            for i in range(1,n):
                producciones[linea[0]]+=[linea[i]]
    return [producciones,strings,simboloInicial]

#Algoritmo CYK
def cyk(matriz, producciones):
    n = len(matriz)
    for y in range(1, n):
        concatenaciones = []
        for x in range(n-y):
            for k in range(0, y):
                string1 = matriz[x][k]
                string2 = matriz[x+k+1][y-k-1]
                concatenaciones = concatenar(string1, string2)
                for concatenacion in concatenaciones:
                    for key in producciones:
                        if concatenacion in producciones[key]:
                            if matriz[x][y] == '0':
                                matriz[x][y] = ''
                            if key not in matriz[x][y]:
                                matriz[x][y] += key
            if matriz[x][y] == '0':
                matriz[x][y] = '-'

inpt = leerInput()
producciones = inpt[0]
strings = inpt[1]
simboloInicial = inpt[2]

#Probar con cada uno de los strings
numeroDeStrings = len(strings)
for i in range(0,numeroDeStrings):
    matriz = inicializarMatriz(len(strings[i]))
    llenarPrimeraFila(matriz,strings[i],producciones)
    cyk(matriz,producciones)
    if simboloInicial in matriz[0][len(matriz)-1]:
        print('Accepted')
    else:
        print('Rejected')
        
#Last commit
