# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:30:41 2017

@author: YJ
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

head = ListNode(None)
head.next = l1
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(2)
l4 = ListNode(3)

l1.next = l2
l2.prev = l1
l2.next = l3
l3.prev = l2
l3.next = l4
l4.prev = l3

def removeDup(head):
    
    used = []
    
    n = head
    
    while n.next != None:
        
        if n.val in used:
            n.prev.next = n.next
            n.next.prev = n.prev
            n = n.next
            
        else:
            used.append(n.val)
            n = n.next
            
    return head
        