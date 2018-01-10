# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:18:51 2018

@author: YJ
"""

# Graph implementation in Adjacency List

class Graph(dict):
    def __init__(self, node_list, edge_list):
        for n in node_list:
            self[n] = set()
        for e in edge_list:
            self.add_edge(e)
            
    def add_edge(self, edge):
        self[edge[0]].add(edge[1])
        self[edge[1]].add(edge[0])
        
    def add_node(self, node):
        self[node] = set()
        
    def delete_edge(self, edge):
        self[edge[0]].remove(edge[1])
        self[edge[1]].remove(edge[0])
        
    def delete_node(self, node):
        temp_neighbor_set = self[node].copy()
        for neighbor_node in temp_neighbor_set:
            self.delete_edge((neighbor_node, node))
        del self[node]
g = Graph(['A', 'B'], [('A', 'B')])
g.add_node('C')
g.add_node('D')
g.add_edge(('A', 'C'))
g.add_edge(('A', 'D'))
g.add_edge(('B', 'D'))

print('Neighbors of A', g['A'])
print('Neighbors of B', g['B'])
print('Neighbors of C', g['C']) 

print('Delete B')
g.delete_node('B')
print(g)