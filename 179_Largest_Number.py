'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''


from functools import cmp_to_key
class Solution(object):

    def largestNumber(self,nums):

        def comparador_cifras(x, y):
                if x + y > y + x:
                    return 1
                elif x == y:
                    return 0
                else:
                    return -1


        numeros_una_cifra = []#Array que contiene los numeros con una cifra (Ej. 456 --> 4.56)
        mayor_num_posible = ""

        #Convertimos los numeros para que tengan un cifra
        numeros_una_cifra = [str(num) for num in nums]

        #Ordenamos los numeros de mayor a menor
        numeros_una_cifra = sorted(numeros_una_cifra, reverse=True,key = cmp_to_key(comparador_cifras))

        #Concatenamos los numeros
        for palabra in numeros_una_cifra:
            mayor_num_posible = mayor_num_posible + str(palabra)
        
        #Le quitamos los puntos a la cadena
        return str(int(mayor_num_posible))