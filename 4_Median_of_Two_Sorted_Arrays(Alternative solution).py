'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numeros = sorted(nums1 + nums2) #Unimos las dos listas y lo ordenamos
        if len(numeros) %2 == 0: # Si es par nos quedamos con los dos valores
            return float((numeros[(len(numeros)//2)-1] + numeros[len(numeros)//2])/2)
        else:#Si es impar nos quedamos con el del medio
            return float(numeros[round(len(numeros)/2)-1])