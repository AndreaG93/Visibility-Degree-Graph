'''
Created on 01 gen 2018

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''


class GraphNode(object):
    '''
    This class represents a generic node of a graph.
    '''
    
    def __init__(self, nodeID, value):
        '''
        Constructs a newly allocated 'GraphNode' object.
        
        @param id: Represents node identifier.      
        @param value: Represents a value. 
        '''
        self._nodeID = nodeID
        self._value = value 
        
        # This flag is used to mark current node as visited...
        self._isVisited = False


class GraphAdjacencyListNode(GraphNode):
    '''
    This class represents a node of a graph rappresented with adjacency lists.
    '''
    
    def __init__(self, nodeID, value):
        '''
        Constructs a newly allocated 'GraphAdjacencyListNode' object.
        
        @param id: Represents node identifier.      
        @param value: Represents a value. 
        '''
        
        super().__init__(nodeID, value)
        self._adjacencyList = list()
    
