import os
import math
from Numeros import *

def main():
    number = int(input("Ingresar número: "))
    numero = Numero(number)
    if numero.comprobarPrimo():
        print("Es primo")
    
    else:
        print("No es primo")
        
    x = math.log(number+1, 10)/math.log(2,10)
    if x - math.floor(x) == 0:
        print("n:", int(x))
        
    print("digitos: " + str(numero.mostrarLongitud()))
    print("suma de digitos: " + str(numero.mostrarSumaDeDigitos()))
    #print("divisores: " + str(numero.mostrarDivisores()))
    input("Presiona enter para continuar")
    
if __name__ == "__main__":
    main()


