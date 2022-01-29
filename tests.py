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
    
    # def test_LIC0(self):
    #     parameters = PARAMETERS_T()
    #     parameters.length1 = 1
    #     coordinates = np.zeros((5, 2))
    #     for i in range(len(coordinates)):
    #         coordinates[i] = [i,i+1]
            
    #     CMV = cmv(parameters, coordinates)
    #     self.assertTrue(CMV.LIC_0())

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

if __name__ == '__main__':
    unittest.main()
        