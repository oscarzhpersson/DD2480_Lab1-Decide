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

        # Test if it fails when the distance is not grather than length1
        parameters = PARAMETERS_T()
        parameters.length1 = 1
        coordinates = np.zeros((2, 2))
        
        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_0())

        ## Test for when the distance greater than length1 are not consecutive. 
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
        """ Tests the LIC1 function of the CMV component.

        Tests
        -----

        Test1: Asserts if function returns False when RADIUS1 = 0.
        Test2: Asserts if function returns False if three consecutive datapoints are the same and form a single point (RADIUS1 > 0).
        Test3: Asserts if function returns True or False (depending on RADIUS1) when three consecutive datapoints have the same x value.
        Test4: Asserts if function returns True or False (depending on RADIUS1) when three consecutive datapoints have the same y value.
        Test5: Asserts if function returns True or False (depending on RADIUS1) when two out of the three points are the same.
        Test6: Asserts if function returns True or False (depending on RADIUS1) when all three consecutive datapoints are unique.

        See Also
        --------

        LIC1: Function of the cmv class which this test is testing.

        """

        parameters = PARAMETERS_T()

        # Test 1
        parameters.radius1 = 0
        coordinates = np.zeros((3, 2))
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())

        # Test 2: If all 3 coordinates are the same, they become a single point.
        # This point should be able to be contained within RADIUS1 yielding FALSE
        parameters.radius1 = 1
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [0,5]
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())

        # Test 3: If all 3 coordinates have the same x value, the radius will be
        # the distance between the two most separated y coordinate values divided by two.
        # Radius of circle formed by coordinates is 2
        coordinates[0] = [0,1]
        coordinates[1] = [0,2]
        coordinates[2] = [0,5]
        # The given RADIUS1 should output FALSE 
        parameters.radius1 = 2
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        # The given RADIUS1 should output TRUE 
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

        # Test 4: If all 3 coordinates have the same y value, the radius will be
        # the distance between the two most separated points divided by two.
        # Radius of circle formed by coordinates is 2
        coordinates[0] = [1,0]
        coordinates[1] = [2,0]
        coordinates[2] = [5,0]
        # The given RADIUS1 should output FALSE 
        parameters.radius1 = 2
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        # The given RADIUS1 should output TRUE 
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

        # Test 5: If two out of the three points are the same, only two unique points
        # exist. The radius will be the distance between these two points.
        # Radius of circle formed by coordinates is 1.41...
        coordinates[0] = [3,2]
        coordinates[1] = [1,0]
        coordinates[2] = [3,2]
        # The given RADIUS1 should output FALSE 
        parameters.radius1 = 2
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        # The given RADIUS1 should output TRUE 
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

        # Same test (Test 5), switching position of coordinates
        coordinates[0] = [3,2]
        coordinates[1] = [3,2]
        coordinates[2] = [1,0]
        # The given RADIUS1 should output FALSE 
        parameters.radius1 = 2
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        # The given RADIUS1 should output TRUE 
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

        # Test 6: If all three points are unique, a circle can be formed and a
        # radius can be derived directly.
        # Radius of circle formed by coordinates is 5
        coordinates[0] = [1,-6]
        coordinates[1] = [2,1]
        coordinates[2] = [5,2]
        # The given RADIUS1 should output FALSE 
        parameters.radius1 = 5
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        # The given RADIUS1 should output TRUE 
        parameters.radius1 = 4
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

    # Tests the LIC3 function of the CMV component.
    def test_LIC2(self):

        """ Tests the LIC2 function of the CMV component.

                       Tests
                       -----

                       Test1: Asserts if the functions returns False if angle is larger than pi - epsilon
                       Test2: Asserts if the function returns True if the angle is smaller than pi - epsilon.

                       See Also
                       --------

                       LIC2: Function of the cmv class which this test is testing.

        """

        # Test 1: returns false because angle is larger than pi-epsilon, epsilon is set to 1
        parameters = PARAMETERS_T()
        parameters.epsilon = np.pi - 1
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 0]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_2())

        # Test 2: returns True because the angle formed is 90 degrees and is smaller than pi - epsilon, epsilon set to 0
        parameters.epsilon = 0
        coordinates = np.zeros((3, 2))

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 1]
        coordinates[2] = [2, 0]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_2())

    # Tests the LIC3 function of the CMV component.
    def test_LIC3(self):

        """ Tests the LIC3 function of the CMV component.

        Tests
        -----

        Test1: Asserts if there exists a triangle with an area larger than area1, in a scenario where it should.
        Test2: Asserts if there does not exist a triangle with an area larger than area1 in a scenario when it should not.
        Test3: Asserts if test 1 works using negative coordinates.

        See Also
        --------

        LIC3: Function of the cmv class which this test is testing.

        """

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

    def test_LIC4(self):

        """ Tests the LIC4 function of the CMV component.
            The tests try different combination of where the points does not fulfill the requirement of the having QUADS quadrants fulfilled
            and other tests that do so.


             Tests
             -----

            Test1: Tests the function when it the three different quadrants are fulfilled and the QUADS parameter is set to 2
            Test2: Tests the function when the functions is not fulfilled and the Quads parameter is larger than the quadrants filled by the points
            Test3: Test with more points but the number of quadrants are not filled
            Test4: Test with more points and the number of quadrants are filled

             See Also
             --------
             LIC4: Function of the cmv class which this test is testing.

        """

        #Test 1: The quadrants filled are more than QUADS required
        parameters = PARAMETERS_T()
        parameters.q_Pts = 3
        parameters.quads = 2

        coordinates = np.zeros((3, 2))
        coordinates[0] = [1, 1]
        coordinates[1] = [-1, -1]
        coordinates[2] = [1, -1]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_4())

        #Test 2: The quadrants filled are less than QUADS required
        parameters.q_Pts = 3
        parameters.quads = 2

        coordinates = np.zeros((3, 2))
        coordinates[0] = [1, 1]
        coordinates[1] = [1, 1]
        coordinates[2] = [1, 1]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_4())

        #Test 3: The quadrants filled are less than QUADS required and with more points
        parameters.q_Pts = 3
        parameters.quads = 2

        coordinates = np.zeros((5, 2))
        coordinates[0] = [1, 1]
        coordinates[1] = [1, 1]
        coordinates[2] = [1, 1]
        coordinates[3] = [1, 1]
        coordinates[4] = [1, 1]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_4())

        #Test 3: The quadrants filled are more than QUADS required and is inbetween points
        parameters.q_Pts = 3
        parameters.quads = 2

        coordinates = np.zeros((5, 2))
        coordinates[0] = [1, 1]
        coordinates[1] = [1, 1]
        coordinates[2] = [-1, -1]
        coordinates[3] = [1, -1]
        coordinates[4] = [1, 1]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_4())

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

        # Tests if it fails when there are more inbetween than specified.
        coordinates = np.zeros((5, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 1]
        coordinates[4] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_7())


    def test_LIC8(self):
        """ Tests the LIC8 function of the CMV component.

        Tests
        -----
        Test1: Asserts if function returns False when NUMPOINTS < 5
        Test2: Asserts if function returns False when RADIUS1 == 0
        Test3: Asserts if function returns False when A_PTS + B_PTS < 2
        Test4: Asserts if function returns False when A_PTS + B_PTS > NUMPOINTS - 3
        Test5: Asserts if function returns False when all pairs of points are the same.
        Test6: Tests functionality of conditional which handles the case of all coordinates having the same x values.
        Test7: Tests functionality of conditional which handles the case of all coordinates having the same y values.
        Test8: Tests functionality of conditional which handles the case where there only exist two unique points.
        Test9: Tests functionality of conditional which handles the case where there exist three unique points.

        LIC8: Function of the cmv class which this test is testing.

        """

        # Test 1
        parameters = PARAMETERS_T()
        coordinates = np.zeros((4, 2))
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_8())

        # Test 2
        parameters = PARAMETERS_T()
        coordinates = np.zeros((5, 2))
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        parameters.radius1 = 0
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_8())

        # Test 3
        parameters = PARAMETERS_T()
        coordinates = np.zeros((5, 2))
        parameters.a_Pts = 0
        parameters.b_Pts = 1
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_8())

        # Test 4
        parameters = PARAMETERS_T()
        coordinates = np.zeros((5, 2))
        parameters.a_Pts = 5
        parameters.b_Pts = 5
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_8())

        # Test 5
        parameters = PARAMETERS_T()
        parameters.radius1 = 10
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates = np.zeros((6, 2))
        coordinates[0] = [1,1]
        coordinates[1] = [0,0]
        coordinates[2] = [1,1]
        coordinates[3] = [0,0]
        coordinates[4] = [1,1]
        coordinates[5] = [0,0]
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_8())

        # Test 6
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates[0] = [0,1]
        coordinates[1] = [0,0]
        coordinates[2] = [0,2]
        coordinates[3] = [0,0]
        coordinates[4] = [0,5] 
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_8())

        # Test 7
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates[0] = [1,0]
        coordinates[1] = [0,0]
        coordinates[2] = [2,0]
        coordinates[3] = [0,0]
        coordinates[4] = [5,0]
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_8())

        # Test 8
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates[0] = [3,2]
        coordinates[1] = [0,0]
        coordinates[2] = [1,0]
        coordinates[3] = [0,0]
        coordinates[4] = [3,2]
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_8())

        # Same test, switching position of coordinates
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates[0] = [3,2]
        coordinates[1] = [0,0]
        coordinates[2] = [3,2]
        coordinates[3] = [0,0]
        coordinates[4] = [1,0]
        parameters.radius1 = 1
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_8())

        # Test 9 
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates[0] = [1,-6]
        coordinates[1] = [0,0]
        coordinates[2] = [2,1]
        coordinates[3] = [0,0]
        coordinates[4] = [5,2]
        parameters.radius1 = 4
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_8())


    def test_LIC9(self):
        """ Tests the LIC9 function of the CMV component.

        Tests
        -----

        Test1: Asserts if function returns False when len(coordinates) < 5.
        Test2: Asserts if function returns True if angle < (pi - epsilon)
        Test3: Asserts if function returns True if angle < (pi + epsilon)
        Test4: Asserts if function returns False if angle criteria is not met

        See Also
        --------

        LIC9: Function of the cmv class which this test is testing.

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
        coordinates = np.zeros((6, 2)) # Create an empty array of 6 coordinate pairs.

        coordinates[0] = [0, 0]
        coordinates[1] = [1, 0]
        coordinates[2] = [40, 0]
        coordinates[3] = [7, 0]
        coordinates[4] = [0, 9]
        coordinates[5] = [0, 1]


        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_9())

        # Test 3 
        coordinates = np.zeros((6, 2)) # Create an empty array of 6 coordinate pairs.
        coordinates[0] = [0, 1]
        coordinates[1] = [1, 0]
        coordinates[2] = [3, 1]
        coordinates[3] = [7, 0]
        coordinates[4] = [0, 9]
        coordinates[5] = [0, 5]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_9())

        #Test 4
        parameters.epsilon = 3
        parameters.c_Pts = 1
        parameters.d_Pts = 1
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.
        coordinates[0] = [0, 0]
        coordinates[1] = [1, 0]
        coordinates[2] = [0, 1]
        coordinates[3] = [7, 0]
        coordinates[4] = [50, 0]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_9())

        

    def test_LIC11(self):
        """ Tests the LIC5 function of the CMV component.
        Tests
        -----
        Test1: Asserts if function returns False when len(coordinates) < 3.
        Test2: Asserts if function returns True if there is a set of two coordinates such that X[j] - X[i] < 0. (where i = j-1).
        Test3: Asserts if function returns False if there is no set of two coordinates such that X[j] - X[i] < 0. (where i = j-1).
        Test4: Asserts if function returns False if there are not enough points between the pair of coordinates satisfying the condition.
        See Also
        --------
        LIC5: Function of the cmv class which this test is testing.
        """

        # Test 1 - Returns False since there is not enough coordinates.
        parameters = PARAMETERS_T() # Import parameters
        parameters.g_Pts = 1
        coordinates = np.zeros((1, 3)) # Create an empty array of 1 coordinate pairs.

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_11())

        # Test 2 - Returns True since there is a pair of coordinates satisfying the condition.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        coordinates[2] = [25, 0]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_11())

        # Test 3 - Returns False since there is not a pair of coordinates satisfying the condition.
        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_11())

        # Test 4 - Returns False since there is not enough points between the pair of coordinates satisfying the condition.
        parameters.g_Pts = 3

        coordinates = np.zeros((5, 2)) # Create an empty array of 5 coordinate pairs.

        coordinates[2] = [25, 0]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_11())

    def test_LIC12(self):

        """ Tests the LIC12 function of the CMV component.
        Tests
        -----
        Test1: Asserts if function returns True if there exists a pair of coordinates that are exactly K_PTS = 2 apart with distance greater than lenght1 and less than length2. 
        Test2: Asserts if function returns False if there does not exists a pair of coordinates that are exactly K_PTS = 2 apart with distance greater than 1 and less than length2. 
        Test3: Asserts if function returns False if there if there does not exists a pair of coordinates that are exactly K_PTS = 2 apart with distance greater than lenght1.  
        Test4: Asserts if function returns False if there if there does not exists a pair of coordinates that are exactly K_PTS = 2 apart with distance less than length2.    
        See Also
        --------
        LIC12: Function of the cmv class which this test is testing.
        """

        # Test standard criterias 
        parameters = PARAMETERS_T()
        parameters.length1 = 1
        parameters.length2 = 3
        parameters.k_Pts = 2
        coordinates = np.zeros((4, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_12())

        ## Tests if it fails when there are more inbetween than specified.
        coordinates = np.zeros((5, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 1]
        coordinates[4] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_12())

        ## Tests if it fails when the distance is equal to length2
        parameters.length1 = 2
        coordinates = np.zeros((4, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_12())

        ## Tests if it fails when the distance is equal to length2
        parameters.length2 = 2
        coordinates = np.zeros((4, 2))

        coordinates[0] = [0,0]
        coordinates[1] = [0, 1]
        coordinates[2] = [0, 1]
        coordinates[3] = [0, 2]
            
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_12())

    def test_LIC13(self):

        #Test1: Asserts if function returns False if RADIUS2 = 0
        #Test2: Asserts if function returns False if NUMPOINTS < 5
        #Test3: Asserts if function returns False if A_PTS + B_PTS < 2
        #Test4: Asserts if function returns False if A_PTS + B_PTS > NUMPOINTS - 3
        #Test5: Asserts if function returns False when given correct input which should yield False
        #Test6: Tests several valid input cases where the function should return True
        

        # Test 1
        parameters = PARAMETERS_T()
        parameters.radius2 = 0
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates = np.zeros((6, 2))
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_13())

        # Test 2
        parameters = PARAMETERS_T()
        parameters.radius2 = 10
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates = np.zeros((4, 2))
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_13())

        # Test 3
        parameters = PARAMETERS_T()
        parameters.radius2 = 10
        parameters.a_Pts = 1
        parameters.b_Pts = 0
        coordinates = np.zeros((6, 2))
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_13())

        # Test 4
        parameters = PARAMETERS_T()
        parameters.radius2 = 10
        parameters.a_Pts = 10
        parameters.b_Pts = 10
        coordinates = np.zeros((6, 2))
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_13())

        # Test 5
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        coordinates = np.zeros((6, 2))
        # Will only satisfy radius > self.PARAMS.radius2
        coordinates[0] = [1,-6]
        coordinates[1] = [0,0]
        coordinates[2] = [2,-5]
        coordinates[3] = [5,5]
        coordinates[4] = [5,2]
        coordinates[5] = [10,10]
        parameters.radius2 = 4
        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_13())

        # Test 6
        parameters = PARAMETERS_T()
        parameters.a_Pts = 1
        parameters.b_Pts = 1
        parameters.radius2 = 10
        coordinates = np.zeros((6, 2))
        # [0] == [2] == [4]
        coordinates[0] = [1,1]
        coordinates[1] = [10,10]
        coordinates[2] = [1,1]
        coordinates[3] = [20,20]
        coordinates[4] = [1,1]
        coordinates[5] = [30,30]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())

        # [0].x == [2].x == [4].x
        coordinates[0] = [1,2]
        coordinates[2] = [1,4]
        coordinates[4] = [1,5]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())

        # [0].y == [2].y == [4].y
        coordinates[0] = [2,1]
        coordinates[2] = [4,1]
        coordinates[4] = [5,1]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())

        # Points are colinear
        coordinates[0] = [1,1]
        coordinates[2] = [2,2]
        coordinates[4] = [3,3]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())

        # [0] == [2] (Only two unique points)
        coordinates[0] = [1,1]
        coordinates[2] = [1,1]
        coordinates[4] = [3,3]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())

        # Three unique points
        coordinates[0] = [1,2]
        coordinates[2] = [3,2]
        coordinates[4] = [4,1]
        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_13())



if __name__ == '__main__':
    unittest.main()