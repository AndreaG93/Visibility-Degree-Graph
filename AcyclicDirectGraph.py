'''
Created on 01 gen 2018

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

from abc import ABCMeta, abstractmethod
from Queue import Queue


class AcyclicDirectGraph(object, metaclass=ABCMeta):
    '''
    This class represents a simple acyclic direct graph.
    '''

    def __init__(self):
        '''
        Constructs a newly allocated 'AcyclicDirectGraph' object.
        '''
        
        self._nodeSet = dict()
        
        # Next node identifier to use to add new nodes...
        self._nextKey = 0
    
    def isNodeSetEmpty(self):
        """
        This function is used to check if the graph is empty.
        @return: It returns 'True' if node set is empty, otherwise 'False'.
        """
        return not any(self._nodeSet)
        
    @abstractmethod
    def insertNewEdge(self, predecessor, successor):
        """
        This function is used to insert a new edge.
        
        @param predecessor: Represents node id of predecessor of new edge.
        @param successor: Represents node id of successor of new edge.
        """  
        ...
    
    @abstractmethod
    def getSuccessors(self, nodeID):
        """
        This function is used to retrieve all 'successors' of a specified node.
        
        For example: Let G be an acyclic directed graph with 2 nodes (A and B) and one edge (A, B) (from A to B).
        In this case, B is 'successor' of A.
 
        @param nodeID: A node identifier.
        @return: It returns a 'list' object containing node's identifiers.
        @see: http://www.di.unito.it/~locatell/didattica/ro1/grafi-sl-bf.pdf
        """
        ...
        
    @abstractmethod
    def addNewNode(self, value):
        """
        This function is used to add a new node to graph.
        
        @param value: Represents node value.
        """
        ...
    
    def getMaxVisibilityDegreeNodeID(self):
        """
        This function is used to get node with max visibility degree.
        @return: It returns a node identifier.
        """
        
        maxVisibilityNodeIdentifier = 0
        maxVisibilityValue = self.calcNodeVisibilityDegree(0)
      
        for nodeID in range(1, len(self._nodeSet)):
            currentMaxVisibilityValue = self.calcNodeVisibilityDegree(nodeID)
            
            if (currentMaxVisibilityValue >= maxVisibilityValue):
                maxVisibilityValue = currentMaxVisibilityValue
                maxVisibilityNodeIdentifier = nodeID
        
        return maxVisibilityNodeIdentifier
    
    
    def calcNodeVisibilityDegree(self, nodeID):
        """
        This function is used to calculate visibility degree of a specified node.
        
        @param nodeId: A node identifier.
        @return: It returns a visibility degree of specified node.
        """

        # Visibility degree of specified node...
        visibilityDegree = 0     
        # 'successorsNodeQueue' is used to store successors nodes...
        successorsNodeQueue = Queue()    
        # 'supportList' is used to unmark all visited nodes during operation...
        supportList = list()
        # Number intermediate nodes...
        intermediateNodes = 0
           
        # Add node for which the visibility is calculated...
        # ---------------------------------------------------- #
        successorsNodeQueue.enqueue(nodeID)
        
        while(not successorsNodeQueue.isEmpty()):
            
            # Get current queue size..
            # ---------------------------------------------------- #.
            successorsNodeQueueSize = successorsNodeQueue.getSize()
            
            # Get all successors of nodes stored in 'successorsNodeQueue'...
            # ---------------------------------------------------- #
            for _ in range(successorsNodeQueueSize):
                
                # Get all successors of element at the head of the queue...
                # ---------------------------------------------------- #
                successors = self.getSuccessors(successorsNodeQueue.dequeue())
                
                for elem in successors:
                    
                    if(not self._nodeSet[elem]._isVisited):
                        
                        # Visit found nodes...
                        # ---------------------------------------------------- #
                        
                        # Mark as visited...
                        self._nodeSet[elem]._isVisited = True
                        
                        # Checking visibility...
                        if (intermediateNodes <= self._nodeSet[elem]._value):
                            visibilityDegree += 1
                        
                        # Update data structure...
                        successorsNodeQueue.enqueue(elem)
                        supportList.append(elem)
                        
            # Update number of intermediate nodes...     
            intermediateNodes += 1
                        
        # Remark all visited node as not-visited...
        for nodeID in supportList:
            self._nodeSet[nodeID]._isVisited = False
                
        # Return visibility degree...
        return visibilityDegree  