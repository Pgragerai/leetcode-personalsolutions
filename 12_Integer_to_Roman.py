'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
'''

class Solution(object):
    def intToRoman(self, numero):
        """
        :type num: int
        :rtype: str
        """
        equivalencia = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"} #Tabla con las equivalencias
        romano = "" #Palabra que se va formando
        lista_numero = sorted(equivalencia.keys(), reverse=True) #Obtenemos los numeros ordenados de mayor a menor
        cont = 0 #Posicion de la lista que se va a mirar

        #Mientras el numero que estamos transformando sea mayor que 0 y no se acaben las equivalencias
        while numero > 0 and cont <= len(lista_numero) :
            if numero - lista_numero[cont] >= 0:
                #Si el numero contiene un 900
                if numero < 1000 and numero > 899: 
                    romano += "CM"
                    numero = numero - 900
                #Si el numero contiene un 400
                elif numero < 500 and numero > 399:
                    romano += "CD"
                    numero = numero - 400
                #Si el numero contiene un 90
                elif numero < 100  and numero > 89:
                    romano += "XC"
                    numero = numero - 90
                #Si el numero contiene un 40
                elif numero < 50 and numero > 39:
                    romano += "XL"
                    numero = numero - 40
                elif numero == 9:
                    romano += "IX"
                    numero = numero - 9
                elif numero == 4:
                    romano += "IV"
                    numero = numero - 4
                else:
                    romano += equivalencia[lista_numero[cont]]
                    numero = numero - lista_numero[cont] 
                
            elif numero - lista_numero[cont] > 0:
                return romano
            else:
                cont +=1

        return romano