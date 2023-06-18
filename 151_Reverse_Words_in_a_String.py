'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution(object):
    def reverseWords(self, frase):
        """
        :type s: str
        :rtype: str
        """
        frase_nueva = ""#Frase que se va a formar
        palabras = " ".join(frase.split())#Eliminamos los dobles espacios
        palabras = palabras.split(' ')#Obtenemos las palabras
        
        #Recorremos las palabras al reves y las vamos guardando
        for i in reversed(range(len(palabras))):
            if len(palabras) == i:
                frase_nueva = palabras[i]
            else:
                frase_nueva = frase_nueva+ " " +palabras[i]
            
        return frase_nueva.strip()