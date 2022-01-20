import random
from time import process_time
def solitarioUax():
    velegido1=int(input("Escriba el primer valor: "))
    velegido2=int(input("Escriba el segundo valor: "))
    velegido3=int(input("Escriba el tercer valor: "))
    dado=random.randint (0,7)
    contador=0
    while dado!=velegido1 and dado!=velegido2 and dado!=velegido3:
        print("El numero no coincide con el valor elegido")
        dado=random.randint (0,7)
        contador=contador+1
    if dado==velegido1:
        print("el valor elegido coincide con el dado")
    


solitarioUax()

