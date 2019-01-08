'''
Created on 01 gen 2018

@author: Andrea Graziani - matricola 0189326
@version: 1.0
'''

import random
import unittest
import timeit
import functools

from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from AdjacencyListGraph import AdjacencyListGraph

class graphAdjacencyMatrixTest(unittest.TestCase):
    """
    This class is used to test correctness of method decribed into 'graphAdjacencyMatrix' class.
    
    @note: testcase is created by subclassing unittest.TestCase.
    """
    
    def test_CreationAdjacencyListGraph(self):
        """
        This test is used to test creation of one graph with 5 vertices with following edges:
        (1, 3); (2, 4); (1, 0)
        """
        
        # Allocate a new 'AdjacencyListGraph' object
        # ---------------------------------------------------- #
        newAdjacencyListGraph = AdjacencyListGraph()
        
        # Adding 5 vertices...
        # ---------------------------------------------------- #
        for _ in range(5):
            newAdjacencyListGraph.addNewNode(None)
            
        # Adding edge...
        # ---------------------------------------------------- #
        newAdjacencyListGraph.insertNewEdge(1, 3)
        newAdjacencyListGraph.insertNewEdge(2, 4)
        newAdjacencyListGraph.insertNewEdge(1, 0)
    
        self.assertIn(3, newAdjacencyListGraph._nodeSet[1]._adjacencyList)
        self.assertIn(0, newAdjacencyListGraph._nodeSet[1]._adjacencyList)
        self.assertIn(4, newAdjacencyListGraph._nodeSet[2]._adjacencyList)
        
        # Print for debug.
        newAdjacencyListGraph.printAdjacencyList()
    
    def test_CreationAdjacencyMatrixGraph(self):
        """
        This test is used to test creation of one graph with 5 vertices with following edges:
        (1, 3); (2, 4); (1, 0)
        """
        
        # Allocate a new 'AdjacencyMatrixGraph' object
        # ---------------------------------------------------- #
        newAdjacencyMatrixGraph = AdjacencyMatrixGraph()
        
        # Adding 5 vertices...
        # ---------------------------------------------------- #
        for _ in range(5):
            newAdjacencyMatrixGraph.addNewNode(None)
            
        # Adding edge...
        # ---------------------------------------------------- #
        newAdjacencyMatrixGraph.insertNewEdge(1, 3)
        newAdjacencyMatrixGraph.insertNewEdge(2, 4)
        newAdjacencyMatrixGraph.insertNewEdge(1, 0)
        
        self.assertEqual(newAdjacencyMatrixGraph._adjacencyMatrix[1][3], 1)
        self.assertEqual(newAdjacencyMatrixGraph._adjacencyMatrix[2][4], 1)
        self.assertEqual(newAdjacencyMatrixGraph._adjacencyMatrix[1][0], 1)
        self.assertEqual(newAdjacencyMatrixGraph._adjacencyMatrix[0][0], 0)
        
        # Print for debug...
        newAdjacencyMatrixGraph.printAdjacencyMatrix()
        
    def test_successors(self):
        """
        This test is used to test getSuccessor() methods using a graph with 5 vertices with following edges:
        (3, 2); (3, 4); (0, 1); 
        """
        
        def test(myGraph):
            
            # Adding 5 vertices...
            # ---------------------------------------------------- #
            for _ in range(5):
                myGraph.addNewNode(None)
            
            # Adding some edges...
            # ---------------------------------------------------- #
            myGraph.insertNewEdge(3, 2)
            myGraph.insertNewEdge(3, 4)
            myGraph.insertNewEdge(0, 1)
            
            # Getting all successors of node 3...
            # ---------------------------------------------------- #
            myList = myGraph.getSuccessors(3)
        
            self.assertIn(2, myList)
            self.assertIn(4, myList)

            # Getting all successors of node 0...
            # ---------------------------------------------------- #
            myList = myGraph.getSuccessors(0)
        
            self.assertIn(1, myList)
        
            # Getting all successors of node 1...
            # ---------------------------------------------------- #
            myList = myGraph.getSuccessors(1)
        
            self.assertEqual(len(myList), 0)
        
        # Allocate a new 'AdjacencyMatrixGraph' and a 'AdjacencyListGraph' objects...
        # ---------------------------------------------------- #
        newAdjacencyMatrixGraph = AdjacencyMatrixGraph()
        newAdjacencyListGraph = AdjacencyListGraph()
        
        # Run test (Polymorphism is powerful :) )...
        # ---------------------------------------------------- #
        test(newAdjacencyMatrixGraph)
        test(newAdjacencyListGraph)
         
    def test_visibilityDegreeCalculation(self):
        """
        This test is used to test visibility degree calculation using a graph with 6 vertices with following edges:
        (2, 3); (3, 5); (5, 1); (3, 4); (4, 5); (4, 0); (2, 1)
        
        Values:
        0: 2
        1: 0
        2: 8
        3: 7
        4: 1
        5: 6       
        """
        
        def init(myGraph):
            
            # Adding vertices...
            # ---------------------------------------------------- #
            myGraph.addNewNode(2)
            myGraph.addNewNode(0)
            myGraph.addNewNode(8)
            myGraph.addNewNode(7)
            myGraph.addNewNode(1)
            myGraph.addNewNode(6)
            
            # Adding edge...
            # ---------------------------------------------------- #
            myGraph.insertNewEdge(2, 1)
            myGraph.insertNewEdge(2, 3)
            myGraph.insertNewEdge(3, 5)
            myGraph.insertNewEdge(3, 4)
            myGraph.insertNewEdge(4, 5)
            myGraph.insertNewEdge(4, 0)
            myGraph.insertNewEdge(5, 1)
            
            # Checking values...
            # ---------------------------------------------------- #
            self.assertEqual(myGraph._nodeSet[0]._value, 2)
            self.assertEqual(myGraph._nodeSet[1]._value, 0)
            self.assertEqual(myGraph._nodeSet[2]._value, 8)
            self.assertEqual(myGraph._nodeSet[3]._value, 7)
            self.assertEqual(myGraph._nodeSet[4]._value, 1)
            self.assertEqual(myGraph._nodeSet[5]._value, 6)
        
        def test(graph):
            
            # Calculation visibility degree...
            # ---------------------------------------------------- #
            self.assertEqual(graph.calcNodeVisibilityDegree(3), 3)
            self.assertEqual(graph.calcNodeVisibilityDegree(2), 5)
            self.assertEqual(graph.calcNodeVisibilityDegree(4), 2)
            self.assertEqual(graph.calcNodeVisibilityDegree(0), 0)
            self.assertEqual(graph.calcNodeVisibilityDegree(1), 0)
            self.assertEqual(graph.calcNodeVisibilityDegree(5), 1)
            
            self.assertEqual(graph.getMaxVisibilityDegreeNodeID(), 2)
        
        def test_timing_1(graph):
            
            # Calculation node ID with max visibility degree...
            # ---------------------------------------------------- #
            graph.getMaxVisibilityDegreeNodeID()
            
        def test_timing_2(graph):
            
            # Calculation visibility degree node...
            # ---------------------------------------------------- #
            graph.calcNodeVisibilityDegree(3)

        # Allocate a new 'AdjacencyMatrixGraph' and a 'AdjacencyListGraph' objects...
        # ---------------------------------------------------- #
        newAdjacencyMatrixGraph = AdjacencyMatrixGraph()
        newAdjacencyListGraph = AdjacencyListGraph()
        
        # Initialitation...
        # ---------------------------------------------------- #
        init(newAdjacencyMatrixGraph)
        init(newAdjacencyListGraph)
        
        # Run test (Polymorphism is powerful :) )...
        # ---------------------------------------------------- #
        test(newAdjacencyMatrixGraph)
        test(newAdjacencyListGraph)
        
        print("\nTime to get max Visibility degree node")
        print("AdjacencyMatrixGraph:     %.20f" % min(timeit.Timer(functools.partial(test_timing_1, newAdjacencyMatrixGraph)).repeat(repeat=1, number=1)))
        print("AdjacencyListGraph:       %.20f" % min(timeit.Timer(functools.partial(test_timing_1, newAdjacencyListGraph)).repeat(repeat=1, number=1)))
        
        print("Time to get visibility degree of a specified node")
        print("AdjacencyMatrixGraph:     %.20f" % min(timeit.Timer(functools.partial(test_timing_2, newAdjacencyMatrixGraph)).repeat(repeat=1, number=1)))
        print("AdjacencyListGraph:       %.20f" % min(timeit.Timer(functools.partial(test_timing_2, newAdjacencyListGraph)).repeat(repeat=1, number=1)))
    
    def test_visibilityDegreeCalculation_2(self):
        """
        This test is used to test visibility degree calculation using a graph with 4 vertices with following edges:
        (0, 2); (0, 1); (1, 3); (2, 3); 
        
        Values:
        0: 10
        1: 10
        2: 10
        3: 10    
        
        In this case we have two walk with same lenght!
        """   
        
        # Allocate a new 'AdjacencyListGraph' objects...
        # ---------------------------------------------------- #
        myGraph = AdjacencyListGraph()
        
        # Adding vertices...
        # ---------------------------------------------------- #
        myGraph.addNewNode(10)
        myGraph.addNewNode(10)
        myGraph.addNewNode(10)
        myGraph.addNewNode(10)
           
        # Adding edge...
        # ---------------------------------------------------- #
        myGraph.insertNewEdge(0, 1)
        myGraph.insertNewEdge(0, 2)
        myGraph.insertNewEdge(2, 3)
        myGraph.insertNewEdge(1, 3)
        
        # Calculation visibility degree...
        # ---------------------------------------------------- #
        self.assertEqual(myGraph.calcNodeVisibilityDegree(0), 3)
        self.assertEqual(myGraph.calcNodeVisibilityDegree(1), 1)
        self.assertEqual(myGraph.calcNodeVisibilityDegree(2), 1)
        self.assertEqual(myGraph.calcNodeVisibilityDegree(3), 0)
            
        self.assertEqual(myGraph.getMaxVisibilityDegreeNodeID(), 0)


if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(graphAdjacencyMatrixTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
