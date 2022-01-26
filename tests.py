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
    
    def test_LIC1(self):
        # False: If all 3-sets of consecutive datapoints
        # can be contained within the radius
        # True: If there exists at least one 3-set of 
        # consecutive datapoints that cannot be contained

        # The set of 3 datapoints should be able to be contained 
        # within the set radius andShould yield False
        parameters = PARAMETERS_T()
        parameters.radius1 = 3
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [i,i]

        CMV = cmv(parameters, coordinates)
        self.assertFalse(CMV.LIC_1())
        
        # The set of 3 datapoints should NOT be able to be able
        # to be contained within the set radius and should yield True
        parameters.radius1 = 0
        coordinates = np.zeros((3, 2))
        for i in range(len(coordinates)):
            coordinates[i] = [i,i]

        CMV = cmv(parameters, coordinates)
        self.assertTrue(CMV.LIC_1())

if __name__ == '__main__':
    unittest.main()
        