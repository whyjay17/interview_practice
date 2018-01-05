# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:25:29 2018

@author: YJ
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        last = self.items[len(self.items) - 1]
        self.items = self.items[: -1]
        return last
    
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def isEmpty(self):
        return len(self.items) == 0
        
    def minVal(self):
        return min(self.items)
    
    def printStack(self):
        print(self.items)
    
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self, item):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def isEmpty(self):
        return self.items == []


def sortStack(stack):
    if stack.isEmpty():
        return stack
    
    sorted_stack = Stack()
    sorted_stack.push(stack.pop())
    while stack.isEmpty() == False:
        temp = stack.pop()
        while sorted_stack.isEmpty() == False and temp > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    return stack

s = Stack()
print('isEmpty', s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print('isEmpty', s.isEmpty())

print('Top : ', s.peek())
print('min val :', s.minVal())


print('sort')
s2 = Stack()
s2.push(4)
s2.push(3)
s2.push(1)
s2.push(6)

s2.printStack()

s3 = sortStack(s2)

s3.printStack()