'''
You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
'''

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        words = words[left:right+1] #Acotamos las palabras que queremos mirar
        vowels = ["a", "e", "i", "o", "u"]#Vocales
        result = []

        for word in words:
            #Si empieza por vocal y termina por vocal guardamos
            if word[0] in vowels and word[::-1][0] in vowels:
                result.append(word)

        return len(result)
