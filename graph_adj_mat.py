# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:00:12 2018

@author: YJ
"""

# Graph implementation in Adjacency Matrix
# Graph implementation does not save information
# about non-existing edges

class Graph(dict):
    def __init__(self, nodes):
        self.nodes = nodes # list or set
        
    def addEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            self[n1, n2] = 1
            self[n2, n1] = 1
    
    # If we use list implementation instead of graph implementation,
    # we need to add a new col and row, so we have to iterate
    # over all vertices lists and append n there.
    # then we have to create an array of nodes for n (new row)
    # ==> O(|V|) and O(|2V|) space
    
    def addNode(self, n):
        self.nodes.append(n)
    
    # O(1)
    
    def removeEdge(self, n1, n2):
        del self[n1, n2]
        del self[n2, n1]
        
    def removeNode(self, n):
        keys = list(self.keys())
        for n1, n2 in keys:
            if n1 == n or n2 == n and self.get((n1, n2)):
                del self[n1, n2]
        self.nodes.remove(n)
        
g = Graph(['A','B','C','D'])
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('A','D')
g.addEdge('B','A')
g.addEdge('B','D')
print(g)
print('Remove B')
g.removeNode('B')
print(g)
print('Remove A <-> C')
g.removeEdge('A','C')
print(g)