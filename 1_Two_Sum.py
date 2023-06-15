'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,aux in enumerate(nums):
            #Recorremos el array menos el elemento obtenido inicialmente
            for index2,aux2 in enumerate(nums[index:]):
                # Si la suma de ambos numeros es igual a lo deseado
                # Si no es el mismo array ( Comprobamos la longuitud del array)
                # Que no sea el mismo numero ( Comprobamos el indice en el array)
                if aux + aux2 == target and (len(nums) != len(nums[index:]) or index != index2):
                    #Obtenemos las posiciones del numero en el array inicial
                    pos = [i for i in range(len(nums)) if nums[i]==aux]
                    # Si los numeros son iguales 
                    # Si la longuitd del array de posiciones es mayor a 1
                    if aux == aux2 and len(pos)>1:
                        return [pos[0],pos[1]]
                    elif aux != aux2:
                        return [index,index+index2]
            
        