'''
Created on 01 gen 2018

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from GraphNode import GraphAdjacencyListNode
from AcyclicDirectGraph import AcyclicDirectGraph


class AdjacencyListGraph(AcyclicDirectGraph):
    '''
    This class represents a graph rappresented with adjacency list.
    '''

    def __init__(self):
        '''
        Constructs a newly allocated 'AdjacencyListGraph' object.
        '''
    
        super().__init__()
        
    def addNewNode(self, value):
        """        
        @see: AcyclicDirectGraph.addNewNode
        """
        
        # Creation new 'GraphNode' object...
        # ---------------------------------------------------- #   
        newGraphAdjacencyListNode = GraphAdjacencyListNode(self._nextKey, value)
        
        # Adding it to node set...
        # ---------------------------------------------------- #   
        self._nodeSet[self._nextKey] = newGraphAdjacencyListNode
        self._nextKey += 1
        
    def insertNewEdge(self, predecessor, successor):
        """        
        @see: AcyclicDirectGraph.insertNewEdge
        """
        
        self._nodeSet[predecessor]._adjacencyList.append(successor)
        
    def getSuccessors(self, nodeId):
        """        
        @see: AcyclicDirectGraph.getSuccessors
        """
        return self._nodeSet[nodeId]._adjacencyList
    
    def printAdjacencyList(self):
        """
        This function is used to print adjacency lists.
        """
        
        print("\n\n{0}".format("-"*70))
        
        # Check if empty...
        # ---------------------------------------------------- #
        if (self.isNodeSetEmpty()):
            print("Graph is empty!")
        else:
            
            for elem in self._nodeSet:
                print(" {0} -> {1}".format(elem, self._nodeSet[elem]._adjacencyList))
        print("\n\n{0}".format("-"*70))
                
