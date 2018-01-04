# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:09:41 2017

@author: YJ
"""

class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node
        
        
    def length(self):
        
        curr = self.head
        length = 0
        
        while curr.next != None:
            length += 1
            curr = curr.next
        
        return length
        
    def display(self):

        elems = []
        curr = self.head
        if curr.data is not None:
            elems.append(curr.data)
        
        while curr.next != None:
            
            curr = curr.next
            if curr.data is not None:
                elems.append(curr.data)
            
        print(elems)
        
    def get(self, index):
        
        if index >= self.length():
            print('Index out of range')
            return None
        
        curr_idx = 0
        curr = self.head
        
        while True:
            curr = curr.next
            if curr_idx == index:
                return curr.data
            curr_idx += 1
            
    def delete(self, index):
        if index >= self.length():
            print('Index out of range')
            return None
        
        curr_idx = 0
        curr = self.head
        
        while True:
            last_node = curr
            curr = curr.next
            if curr_idx == index:
                last_node.next = curr.next
                return
            curr_idx += 1
                
    def removeDups(self):
        
        curr = self.head
        used = []
        prev = None
        
        while curr.next != None:
            if curr.data in used:
                prev.next = curr.next
            else:
                used.append(curr.data)
                prev = curr
            curr = curr.next
            
    def kthToLast(self, k):
        
        if k >= self.length():
            print('Index k out of range')
            return None
        
        curr_index = 0
        find_index = self.length() - k - 1
        
        curr = self.head
        
        while True:
            curr = curr.next
            if curr_index == find_index:
                return curr.data
            curr_index += 1
            
    def reverseList(self):
        
        curr = self.head

        prev = None

        
        while curr is not None:
            
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            #curr.next, prev, curr = prev, curr, curr.next
            
        self.head = prev
            
    def isPalindrome(self):
        
        if not self.head and not self.head.next:
            return True
        
        curr = slow = fast = self.head
        
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            
        stack = [slow.data]
        
        while slow.next:
            slow = slow.next
            stack.append(slow.data)
            
        while stack:
            if stack.pop() != curr.next.data:
                return False
            curr = curr.next
            
        return True
            
my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.reverseList()

my_list.display()

palin_list = linked_list()
palin_list.append(1)
palin_list.append(2)
palin_list.append(3)
palin_list.append(2)
palin_list.append(1)
palin_list.display()
print(palin_list.isPalindrome())
