'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ultimo_indice_valido = len(nums)-1 #Cogemos la posicion que queremos llegar
        #Nos recorremos la lista de derecha a izquierda y nos quedamos con la ultima posicion valida
        for i in range(len(nums)-1, -1, -1):
            if nums[i]-(ultimo_indice_valido-i)>=0:
                ultimo_indice_valido=i
            
        #Si la ulyima poscion valida es un 0 siguinfica que hemos podido llegar al principio de la lista y por tanto se puede saltar
        if ultimo_indice_valido==0:
            return True
        else:
            return False