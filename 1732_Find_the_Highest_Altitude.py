'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]#Añadimos el primer punto que es el (0,0)

        #Vamos sumando las ganacias con las altitudes que vamos obteniendo
        for index,aux in enumerate(gain):
            altitudes.append(altitudes[index]+gain[index])

        return max(altitudes)