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
        longuitud=len(numeros) #Longitud de la lista

        if longuitud%2==0:#Si la longuitud es par
            num = numeros[(longuitud/2)-1]+numeros[(longuitud/2)]
            return num*0.5
        else:
            return numeros[(longuitud-1)/2]