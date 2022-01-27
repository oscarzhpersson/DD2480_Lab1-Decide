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

if __name__ == '__main__':
    unittest.main()
        