'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.
'''


class Solution(object):
    def isPalindrome(self, numero):
        n = str(numero) #Convertimos el numero en cadena para trabajar en el
        n_espejo = n[::-1] #Invertimos el numero

        for index,aux in enumerate(n):
            #Si los numeros de esa misma posicion no son iguales no es palindromo
            if n[index] != n_espejo[index]:
                return False
        return True