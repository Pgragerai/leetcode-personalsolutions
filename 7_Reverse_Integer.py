'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution(object):
    def reverse(self, numero):
        """
        :type x: int
        :rtype: int
        """
        cadena = str(numero)# Convertimos a cadena el numero

        if "-" in cadena:
            cadena = cadena[1:]#Le quitamos el menos
            cadena = "-"+ cadena[::-1] #Le anadimos un menos y le damos la vuelta al numero
        else:
            cadena = cadena[::-1] #Le damos la vuelta al numero
        
        #Si el nuevo numero es mas grande que el limite de integer
        if (int(cadena) >= 2147483647 or int(cadena) <= -2147483648):
            return 0
        else:
            return int(cadena)