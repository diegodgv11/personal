class Numero():
    def __init__(self, numero = 0):
        self.__numero = numero
        self.__longitud = len(str(numero))
        self.__primer = int(str(numero)[0])
        self.__ultimo = int(str(numero)[len(str(numero))-1])
        self.__lista = []

    def __comprobarDividendos(self): 
        divisorDeDos = False
        divisorDeTres = False
        divisorDeCinco = False
        divisorDeSiete = False
        
        #Comprobacion division entre dos
        if self.__ultimo % 2 == 0:
            divisorDeDos = True

        #Comprobacion division entre tres
        contador = 0
        for i in str(self.__numero):
            contador += int(i)

        if contador % 3 == 0:
            divisorDeTres = True

        #Comprobacion division entre cinco
        if self.__ultimo == 0 or self.__ultimo == 5:
            divisorDeCinco = True

        #Comprobacion division entre siete
        if self.__numero % 7 == 0:
            divisorDeSiete = True

        return [divisorDeDos, divisorDeTres, divisorDeCinco, divisorDeSiete]

    #Si es falso no es primo
    def comprobarPrimo(self):
        comprobacionAnterior = self.__comprobarDividendos()
        dos = comprobacionAnterior[0]
        tres = comprobacionAnterior[1]
        cinco = comprobacionAnterior[2]
        siete = comprobacionAnterior[3]

        lista = []
        if dos:
            if self.__numero == 2:
                return True
            else:
                return False

        elif tres:
            if self.__numero == 3:
                return True

            else:
                return False

        elif cinco:
            if self.__numero == 5:
                return True

            else:
                return False

        elif siete:
            if self.__numero == 7:
                return True

            else:
                return False

        else:
            for gt in range(1, self.__numero+1):
                if self.__numero % gt == 0:
                    lista.append(gt)

            if len(lista) == 2:
                return True

            else:
                return False
        
    def mostrarLongitud(self):
        return self.__longitud

    def mostrarSumaDeDigitos(self):
        contador = 0
        for i in str(self.__numero):
            contador += int(i)
        return contador

    def mostrarDivisores(self):
        return self.__lista

