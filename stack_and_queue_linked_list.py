# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 01:06:24 2018

@author: YJ
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = Node()
    
    def pop(self):
        top_data = self.top.data
        self.top = self.top.next
        return top_data
    
    def push(self, item):
        new_item = Node(item)
        new_item.next = self.top
        self.top = new_item
        
    def peek(self):
        if self.top == None:
            print('Empty Stack')
            return
        
        return self.top.data
    
    def isEmpty(self):
        return self.top.next == None
    
    def printStack(self):
        
        temp_top = self.top
        
        while temp_top.next != None:
            print(temp_top.data)
            temp_top = temp_top.next
            
class Queue:
    def __init__(self):
        self.first = Node()
        self.last = Node()
        
    def enqueue(self, item):
        new_dat = Node(item)
        if self.last != None:
            self.last.next = new_dat
        self.last = new_dat
        if self.first == None:
            self.first = self.last
            
    def dequeue(self, item):
        first_dat = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return first_dat
    
    def peek(self):
        return self.first.data
    
    def isEmpty(self):
        return self.first == None
    
    def printQueue(self):
        queue = []
        temp = self.first
        while temp.next != None:
            queue.append(temp.data)
            temp = temp.next
            
        print('<---', queue, '<---')
    

def sortStack(stack):
    if stack.isEmpty():
        stack.printStack()
        return stack
    
    sorted_stack = Stack()
    sorted_stack.push(stack.pop())
    while stack.isEmpty() == False:
        temp = stack.pop()
        #print('pop', temp)
        while sorted_stack.isEmpty() == False and temp > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    stack.printStack()
    return sorted_stack
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
print('Pop')
s.pop()
s.printStack()
print('Current Top : ', s.peek())
print('Empty ? : ', s.isEmpty())
s.push(6)
s.printStack()
print('pop() x 3')
s.pop()
s.pop()
s.pop()
s.printStack()
print('Empty ? : ', s.isEmpty())
print('sort')
s2 = Stack()
s2.push(4)
s2.push(3)
s2.push(1)
s2.push(6)
s2.printStack()
sortStack(s2).printStack()