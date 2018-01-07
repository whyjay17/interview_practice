# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 00:54:00 2018

@author: YJ
"""

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
       
        
def inOrderTraversal(node):
    if node != None:
        inOrderTraversal(node.left)
        print(node.data)
        inOrderTraversal(node.right)
        
def preOrderTraversal(node):
    if node != None:
        print(node.data)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def postOrderTraversal(node):
    if node != None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data)
        
root = TreeNode(3)
root.insert(1)
root.insert(5)

print('root', root.data)
print('root.left', root.left.data)
print('root.right', root.right.data)

print('inOrder')
inOrderTraversal(root)
print('preOrder')
preOrderTraversal(root)
print('postOrder')
postOrderTraversal(root)