'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, palabra):

        palabra_act = "" #Palabra que vamos formando
        mayor_longitud = "" #Palabra que contiene mayor longitud
        posicion_act = 0 #Primera posicion que estamos mirando
        pos = 0 #Posicion que comprobamos

        while posicion_act < len(palabra):
            while pos < len(palabra):

                #Si la letra esta en la palabra que vamos formando actualizamos los valores maximos
                #si no vamos agregando letras a la subpalabra
                if palabra[pos] in palabra_act:
                    if len(palabra_act) > len(mayor_longitud):
                        mayor_longitud = palabra_act
                    posicion_act +=1
                    pos = posicion_act
                    palabra_act = ""
                else:
                    palabra_act += palabra[pos]
                    pos +=1

            if len(palabra_act) > len(mayor_longitud):
                mayor_longitud = palabra_act
            posicion_act +=1

        return len(mayor_longitud)
