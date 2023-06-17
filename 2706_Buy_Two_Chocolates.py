'''
You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
'''
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