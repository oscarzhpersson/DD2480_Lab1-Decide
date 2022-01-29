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

    def test_LIC2(self):

       #Test 1: The input will a staight line with a 180 degree angle and epsilon set to pi
       #This should yield false
        parameters = PARAMETERS_T()
        parameters.epsilon = np.pi
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [1,0]
        coordinates[2] = [2,0]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_2())


        #Test 2: This will give right angled and which should yield true
        parameters.epsilon = 0
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 1]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_2())

    # Tests the LIC3 function of the CMV component.
    def test_LIC3(self):
        parameters = PARAMETERS_T() # Import parameters
        parameters.area1 = 5 # Set the target area to an arbitrary value: 5.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        # Test 1: There exists a triangle with an area larger than area1.

        for i in range(len(coordinates)):
            coordinates[i] = [i, i]

        CMV = cmv(parameters, coordinates) # Create an instance of the CMV component.
        self.assertFalse(CMV.LIC_3()) # Run the test.

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


    def test_LIC6(self):
        #Test 1: Having the distance larger in every comparision
        parameters = PARAMETERS_T()
        parameters.dist = 1000
        parameters.n_Pts = 3
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 1]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_6())

        #TEST 2: Having the Distance smaller than in every comparision
        parameters.dist = 1
        parameters.n_Pts = 3
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0, 0]
        coordinates[1] = [5, 5]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_6())


if __name__ == '__main__':
    unittest.main()
        