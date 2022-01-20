

def main():
    print("escribe dos numeros entre 0 y 9999")
    primero = int(input("Escriba el primer número: "))
    stprimero=str(primero)
    segundo = int(input("Escriba el segundo número: "))
    stsegundo=str(segundo)
    while((primero and segundo) <0) and ((primero and segundo) <9999):
        suma1=primero[0]+primero[1]+primero[2]+primero[3]
        suma2=segundo[0]+segundo[1]+segundo[2]+segundo[3]
        if suma1!=suma2:
            print("los numeros no son iguales")
        else:("los numeros suman los mismo y por lo tanto no puedo asegurar q sean iguales")
        

main()