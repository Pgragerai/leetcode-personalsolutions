'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    #Metodo que nos permite transformar una listnode a una lista
    def listnode_to_pylist(self, listnode):
        ret = []
        while True:
            ret.append(listnode.val)
            if listnode.next != None:
                listnode = listnode.next
            else:
                return ret

    #Metodo que nos permite transformar una lista en una listnode
    def pylist_to_listnode(self, pylist, link_count):
        if len(pylist) > 1:
            ret = precompiled.listnode.ListNode(pylist.pop())
            ret.next = self.pylist_to_listnode(pylist, link_count)
            return ret
        else:
            return precompiled.listnode.ListNode(pylist.pop(), None)
    
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lista1 = self.listnode_to_pylist(l1)
        lista2 = self.listnode_to_pylist(l2)
        aux_l1 = 0
        aux_l2 = 0
        #Obtenemos los elementos de la lista y los multiplicamos por su potencia en base 10 (Ej. 52 = 2*10^0+5*10^1)
        for index,aux in enumerate(lista1):
            aux_l1 = aux_l1 + (aux*(10**index))
        for index,aux in enumerate(lista2):
            aux_l2 = aux_l2 + (aux*(10**index))
        
        res = [int(x) for x in str(aux_l1+aux_l2)] 
        return self.pylist_to_listnode(res,len(res))