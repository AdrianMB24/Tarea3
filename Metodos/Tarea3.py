from PIL import Image
from playsound import playsound
from tabulate import tabulate
import sys
import cv2, numpy
import argparse
import time
# ---Parser---
parser = argparse.ArgumentParser(description="El script tiene la capacidad de ver imagenes, reproducir audio y realizar un conteo en el texto \n Intrucciones: \n Escribir la operación a realizar con -o y luego cumplir con los parámetros por función ")
parser.add_argument("-s","--size", type=float, help="Escala de la imagen disponible: 0.5, 1 y 2")
parser.add_argument("-i","--imagen", type=str, help="PathWay de la imagen, archivo jpg")
parser.add_argument("-c","--Cant", type=int, help="Indicar la cantidad de veces que se repite un audio")
parser.add_argument("-m","--Sound", type=str, help="PathWay del audio, archivo mp3")  
parser.add_argument("-t","--Texto", type=str, help="PathWay del texto, archivo txt")                
parser.add_argument("-o","--opcion", type=int, help="Seleccionar número de operación a ejecutar: \n Presentador de Imagen (1)\n Presentador de sonido(2)\n Analizador de texto(3)\n Exit(0)\n")                
parser.add_argument("-T","--time", type=int, help="Muestra el tiempo de procesamiento del programa. Para que funcione indicar un 1 en la bandera para Enable")                
args = parser.parse_args()
# -----Funciones-----
def Imagen(size, imagen):
    try:
        img = Image.open(imagen)
    except:
        print("Imagen No Encontrada")
        sys.exit(1)
    x = len(imagen)
    x1 = imagen[x-3]+imagen[x-2]+imagen[x-1]
    if (x1 == "jpg"):
        print("El archivo es formato jpg")
    else:
        print("El archivo no es formato jpg")
        sys.exit(1)
        
    ancho, alto = img.size
    if (size == 1):
        img.show()
    elif (size == 0.5):
        img2 = img.copy()
        img2.thumbnail((ancho//2, alto//2))
        img2.show()
    elif (size == 2):
        img3 = cv2.imread(imagen, 0)
        H, W = img3.shape[:2]
        img32 = cv2.resize(img3, (int(2*H), int(2*W)), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("img32.jpg", img32)
        #cv2.imshow("img32.jpg", img32)
        img323 = Image.open("img32.jpg")
        img323.show()
        #time.sleep(3)
    
def Sonido(Cant, Sound):
    x = len(Sound)
    x1 = Sound[x-3]+Sound[x-2]+Sound[x-1]
    if (x1 == "mp3"):
        print("El archivo es formato mp3")
    else:
        print("El archivo no es formato mp3")
        sys.exit(1)
    for i in range (0, Cant):
        try:
            playsound(Sound)
        except:
            print("Sonido No Encontrado")
            sys.exit(1)
        
def Analizador(Texto):
    cont = 0
    l1 = ""
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    try:
        fic = open(Texto , "r")
    except:
        print("Doumento No Encontrado")
        sys.exit(1)
    lines = fic.readlines()
    l0 = str(lines[0])
    i = 0
    fic.close()
    while (1):
        if (l0[i] == "_"):
            z = 0
            for l in range (0, len(l2)):
                if (l2[l] == l1):
                    l3[l] = l3[l] + 1
                    z = 1
                    break
            if(z == 0):
                l2.append(l1)
                l3.append(1)
            l1 = ""
        else:
            l1 = l1 + l0[i]
        i = i+1
        try:
            l0[i]
        except:
            break
    z = 0 
    for l in range (0, len(l2)):
        if (l2[l] == l1):
            l3[l] = l3[l] + 1
            z = 1
            break
    if(z == 0):
        l2.append(l1)
        l3.append(1)
    for p in range (0, len(l2)):
        #l4.append(l2[p])
        #l4.append(13[p])
        l4 = [l2[p], l3[p]]
        l5.append(l4)
    Sal = open("Analizado.txt", "w")
    Sal.write(tabulate(l5, ["Item", "Cantidad"],tablefmt="github"))
    Sal.close()
# ---Seleccionador---
def Main():
     if(args.opcion == 1):
       start = time.perf_counter() 
       Imagen(args.size, args.imagen)
       end = time.perf_counter()
       if(args.time):
           print("El tiempo de procesamiento es:",end-start)
     elif(args.opcion == 2):
        start = time.perf_counter()
        Sonido(args.Cant, args.Sound)
        end = time.perf_counter()
        if(args.time):
           print("El tiempo de procesamiento es:",end-start)
     elif(args.opcion == 3):
        start = time.perf_counter()
        Analizador(args.Texto)
        end = time.perf_counter()
        if(args.time):
           print("El tiempo de procesamiento es:",end-start)
     elif(args.opcion == 0):
         return 0
# ---Ejecutando script---
Main()
# ---End---
        
            
    
