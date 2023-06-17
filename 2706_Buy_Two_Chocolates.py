class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices = sorted(prices)#Ordenamos los precios para obtener la menor combinacion
        contador_compra = 1#Contador de chocolates
        dinero_inicial = money #Dienro inical para devolver en caso que no se pueda comprar

        for choco in prices:
            if contador_compra < 3 and money - choco >=0: #Si podemos comprar el chocolate y hemos comprado menos de 2
                money -= choco
                contador_compra +=1
            elif money - choco < 0 and contador_compra < 3:#Si no podemos comprar el chocolate no gastamos nada
                return dinero_inicial
            elif contador_compra == 2: #Si hemos comprado dos chocolates devolvemos lo que nos sobra
                return money
            
        return money