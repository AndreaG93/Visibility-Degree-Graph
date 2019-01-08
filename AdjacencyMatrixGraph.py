'''
Created on 01 gen 2018

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from AcyclicDirectGraph import AcyclicDirectGraph
from GraphNode import GraphNode


class AdjacencyMatrixGraph(AcyclicDirectGraph):
    '''
    This class represents a graph rappresented with adjacency matrix
    '''
    
    # Some useful constans...
    NOT_ADJACENT = 0
    ADJACENT = 1
 
    def __init__(self):
        '''
        Constructs a newly allocated 'AdjacencyMatrixGraph' object.
        '''
        
        super().__init__()
        self._adjacencyMatrix = list()
    
    def addNewNode(self, value):
        """        
        @see: AcyclicDirectGraph.addNewNode
        """
        
        # Creation new 'GraphNode' object...
        # ---------------------------------------------------- #   
        newGraphNode = GraphNode(self._nextKey, value)

        # Adding it to node set...
        # ---------------------------------------------------- #   
        self._nodeSet[self._nextKey] = newGraphNode
        self._nextKey += 1
        
        # Update adjacency Matrix
        # ---------------------------------------------------- #      
        newList = list()
        for x in range(self._nextKey):
            newList.append(AdjacencyMatrixGraph.NOT_ADJACENT)
     
        self._adjacencyMatrix.append(newList)
        
        # Adapt adjacency matrix after new node insertion...
        # ---------------------------------------------------- #
        for x in range(self._nextKey - 1):
            self._adjacencyMatrix[x].append(AdjacencyMatrixGraph.NOT_ADJACENT)
            
    def insertNewEdge(self, predecessor, successor):
        """        
        @see: AcyclicDirectGraph.insertNewEdge
        """
        
        self._adjacencyMatrix[predecessor][successor] = AdjacencyMatrixGraph.ADJACENT
    
    def getSuccessors(self, nodeID):
        """
        @see: getSuccessors()
        """
        
        # Output list...
        outputList = list() 
        
        # Checking...
        # ---------------------------------------------------- #
        for j in range(len(self._adjacencyMatrix)):
            if(self._adjacencyMatrix[nodeID][j]):
                outputList.append(self._nodeSet[j]._nodeID)
    
        return outputList
    
    def printAdjacencyMatrix(self):
        """
        This function is used to print adjacency matrix.
        """
             
        print("\n\n{0}".format("-"*70))
        
        # Check if empty...
        # ---------------------------------------------------- #
        if (self.isNodeSetEmpty()):
            print("Graph is empty!")
        else:
            
            # Creation head of matrix...
            # ---------------------------------------------------- #
            head = list()
            for x in range(len(self._adjacencyMatrix)):
                head.append(str(x)) 
            
            # Following index is used to print left head matrix...
            index = 0
                
            # Print matrix...
            # ---------------------------------------------------- #
            print("   %s" % '  '.join(head))
            for row in self._adjacencyMatrix:
                print("{0} {1}".format(head[index], row))
                index += 1
                
        print("{0}".format("-"*70))
        
