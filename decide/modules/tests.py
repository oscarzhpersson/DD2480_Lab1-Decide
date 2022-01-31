import unittest
import numpy as np
from cmv import cmv
from dataclasses import dataclass

@dataclass
class PARAMETERS_T:
    length1: float = 0 # Length in LICs 0, 7, 12.
    radius1: float = 0# Radius in LICs 1, 8, 13.
    epsilon: float = 0 # Deviation from PI in LICs 2, 9.
    area1: float = 0 # Area in LICs 3, 10, 14.
    q_Pts: int = 0 # No. of consecutive points in LIC 4.
    quads: int = 0 # No. of quadrants in LIC 4.
    dist: float = 0 # Distance in LIC 6.
    n_Pts: int = 0 # No. of consecutive points in LIC 6.
    k_Pts: int = 0 # No. of int. points in LICs 7, 12.
    a_Pts: int = 0 # No. of int. points in LICs 8, 13.
    b_Pts: int = 0 # No. of int. points in LICs 8, 13.
    c_Pts: int = 0 # No. of int. points in LIC 9.
    d_Pts: int = 0 # No. of int. points in LIC 9.
    e_Pts: int = 0 # No. of int. points in LICs 10, 14.
    f_Pts: int = 0 # No. of int. points in LICs 10, 14.
    g_Pts: int = 0 # No. of int. points in LIC 11.
    length2: float = 0 # Maximum length in LIC 12.
    radius2: float = 0 # Maximum radius in LIC 13.
    area2: float = 0 # Maximum area in LIC 14.

class TestLIC(unittest.TestCase):
    def test_LIC0(self):
        ## Test if coordinates that are sqrt(2) are accepted if length1 = 1.
        parameters = PARAMETERS_T()
        parameters.length1 = 1
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [i,i+1]
            
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_0())

        ## Test for when the points greater than length1 are not consecutive. 
        parameters = PARAMETERS_T()
        parameters.length1 = 1
        coordinates = np.zeros((3, 2))
        
        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_0())


    # Tests the LIC1 function of the CMV component.
    def test_LIC1(self):

        # Test 1: The set of 3 datapoints should be able to be contained 
        # within the set radius with the given input and should yield False

        parameters = PARAMETERS_T()
        parameters.radius1 = 3
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [i,i]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        
        # Test 2: The set of 3 datapoints should NOT be able to be able
        # to be contained within the set radius with the given input and should yield True
        
        parameters.radius1 = 0
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [i,i]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())


    # Tests the LIC3 function of the CMV component.
    def test_LIC3(self):
        parameters = PARAMETERS_T() # Import parameters
        parameters.area1 = 5 # Set the target area to an arbitrary value: 5.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        # Test 1: There exists a triangle with an area larger than area1.

        coordinates[0] = [0, 0] # Creates a triangle with area 7.5.
        coordinates[1] = [5, 3]
        coordinates[2] = [5, 0]

        CMV = cmv(parameters, coordinates) # Create an instance of the CMV component.
        self.assertTrue(CMV.LIC_3()) # Run the test.

        # Test 2: There does not exist a triangle with an area larger than area1.

        coordinates = np.zeros((5, 2)) # Reset the coordinate array.

        coordinates[0] = [0, 0] # Creates a triangle with area 1.
        coordinates[1] = [2, 1]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates) # Create an instance of the CMV component.
        self.assertFalse(CMV.LIC_3()) # Run the test."""

        # Test 3: Test 1 but with negative coordinates.

        coordinates = np.zeros((5, 2)) # Reset the coordinate array.

        coordinates[0] = [0, 0] # Creates a triangle with area 7.5.
        coordinates[1] = [-5, 3]
        coordinates[2] = [-5, 0]

        CMV = cmv(parameters, coordinates) # Create an instance of the CMV component.
        self.assertTrue(CMV.LIC_3()) # Run the test.

        # Test 4: No actual triangle exists (Straight line, should not have any area).

        coordinates = np.zeros((5, 2)) # Reset the coordinate array.

        for i in range(len(coordinates)): # Adds coordinates for a linear line.
            coordinates[i] = [i, i]

        CMV = cmv(parameters, coordinates) # Create an instance of the CMV component.
        self.assertFalse(CMV.LIC_3()) # Run the test.

    def test_LIC5(self):
        """ Tests the LIC5 function of the CMV component.

        Tests
        -----

        Test1: Asserts if function returns False when len(coordinates) < 2.
        Test2: Asserts if function returns True if there is a set of two coordinates such that X[j] - X[i] < 0. (where i = j-1).
        Test3: Asserts if function returns False if there is no set of two coordinates such that X[j] - X[i] < 0. (where i = j-1).

        See Also
        --------

        LIC5: Function of the cmv class which this test is testing.

        """

        # Test 1 - Returns False since there is not enough coordinates.
        parameters = PARAMETERS_T() # Import parameters
        coordinates = np.zeros((1, 2)) # Create an empty array of 1 coordinate pairs.

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_5())

        # Test 2 - Returns True since there is a pair of coordinates satisfying the condition.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        coordinates[0] = [1, 0]
        coordinates[1] = [25, 0]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_5())

        # Test 3 - Returns False since there is not a pair of coordinates satisfying the condition.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_5())
        
  
    def test_LIC7(self):

        """ Tests the LIC7 function of the CMV component.

        Tests
        -----
        Test1: Asserts if function returns True if there exists a pair of coordinates that are exactly K_PTS = 2 apart with distance grater than 1. 
        Test2: Asserts if function returns False if there does not exists a pair of coordinates that are exactly K_PTS = 2 apart with distance grater than 1. 
        See Also
        --------
        LIC7: Function of the cmv class which this test is testing.
        """
        # The conditions are met, coordinate[0] and [3] are distance 2 apart with two points inbetween.
        parameters = PARAMETERS_T()
        parameters.length1 = 1
        parameters.k_Pts = 2
        coordinates = np.zeros((4, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_7())

        ## Tests if it fails when there are more inbetween than specified.
        coordinates = np.zeros((5, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 1]
        coordinates[4] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_7())

    def test_LIC9(self):
        """ Tests the LIC9 function of the CMV component.

        Tests
        -----

        Test1: Asserts if function returns False when len(coordinates) < 5.
        Test2: Asserts if function returns True if angle < (pi - epsilon)
        Test3: Asserts if function returns True if angle < (pi + epsilon)


        See Also
        --------

        LIC5: Function of the cmv class which this test is testing.

        """

        # Test 1 
        parameters = PARAMETERS_T() # Import parameters
        parameters.c_Pts = 1
        parameters.d_Pts = 2

        coordinates = np.zeros((1, 2)) # Create an empty array of 1 coordinate pairs.

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_9())

        # Test 2 
        parameters.epsilon = 1
        coordinates = np.zeros((6, 2)) # Create an empty array of 5 coordinate pairs.

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 0]
        coordinates[2] = [40, 0]
        coordinates[3] = [7, 0]
        coordinates[4] = [0, 9]
        coordinates[5] = [0, 1]


        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_9())

        # Test 3 
        coordinates = np.zeros((6, 2)) # Create an empty array of 5 coordinate pairs.
        coordinates[0] = [0, 1]
        coordinates[1] = [1, 0]
        coordinates[2] = [3, 1]
        coordinates[3] = [7, 0]
        coordinates[4] = [0, 9]
        coordinates[5] = [0, 5]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_9())

if __name__ == '__main__':
    unittest.main()
        