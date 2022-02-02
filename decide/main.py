import sys
import numpy as np
import enum
from dataclasses import dataclass
from modules.cmv import cmv
from modules.pum import pum

##### CONSTANT #####

pi = np.pi #3.1415926535

##### TYPE DECLARATIONS #####

class Connectors(enum.Enum):
    "NOTUSED",
    "ORR",
    "ANDD"

##### Inputs to the DECIDE() function #####

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


##### INPUT VARIABLES #####

numpoints = 62
parameters = PARAMETERS_T()
LCM = np.ones((15, 15)) # Create a default LCM, to be imported as input.
PUV = np.ones(15, dtype=bool) # Create a default PUV, to be imported as input.
coordinates = np.zeros((numpoints, 2)) # Matrix of X, Y coordinate pairs. Replaces the coordinate X and coordinate Y variable.

#? Function you must write:

def input():
    ''' Sets up input parameters and coorinates. Reads paramteres from file, and sets coordinates.
        
        '''
    
    # Parameter input handling.
    parameters.length1 = float(sys.stdin.readline())
    parameters.radius1 = float(sys.stdin.readline())
    parameters.epsilon = float(sys.stdin.readline())
    parameters.area1 = float(sys.stdin.readline())
    parameters.q_Pts = int(sys.stdin.readline())
    parameters.quads = int(sys.stdin.readline())
    parameters.dist = float(sys.stdin.readline())
    parameters.n_Pts = int(sys.stdin.readline())
    parameters.k_Pts = int(sys.stdin.readline())
    parameters.a_Pts = int(sys.stdin.readline())
    parameters.b_Pts = int(sys.stdin.readline())
    parameters.c_Pts = int(sys.stdin.readline())
    parameters.d_Pts = int(sys.stdin.readline())
    parameters.e_Pts = int(sys.stdin.readline())
    parameters.f_Pts = int(sys.stdin.readline())
    parameters.g_Pts = int(sys.stdin.readline())
    parameters.length2 = float(sys.stdin.readline())
    parameters.radius2 = float(sys.stdin.readline())
    parameters.area2 = float(sys.stdin.readline())

    # LIC 0
    coordinates[0] = [0,1]
    coordinates[1] = [1,2]
    coordinates[2] = [2,3]
    
    # LIC 1
    coordinates[3] = [1,0]
    coordinates[4] = [2,0]
    coordinates[5] = [5,0]

    # LIC 2
    coordinates[6] = [0,1]
    coordinates[7] = [0,2]
    coordinates[8] = [0,5]

    # LIC 3
    coordinates[9] = [0, 0]
    coordinates[10] = [5, 3]
    coordinates[11] = [5, 0]

    # LIC 4
    coordinates[12] = [1, 1]
    coordinates[13] = [-1, -1]
    coordinates[14] = [1, -1]

    # LIC 5
    coordinates[15] = [1, 0]
    coordinates[16] = [25, 0]

    # LIC 6
    coordinates[17] = [0, 0]
    coordinates[18] = [5, 5]
    coordinates[19] = [2, 0]

    # LIC 7
    coordinates[20] = [0,0]
    coordinates[21] = [0, 1]
    coordinates[22] = [0, 1]
    coordinates[23] = [0, 2]

    # LIC 8
    coordinates[24] = [1,1]
    coordinates[25] = [0,0]
    coordinates[26] = [3,3]
    coordinates[27] = [0,0]
    coordinates[28] = [5,5]

    # LIC 9
    coordinates[29] = [0, 1]
    coordinates[30] = [1, 0]
    coordinates[31] = [3, 1]
    coordinates[32] = [7, 0]
    coordinates[33] = [0, 9]
    coordinates[34] = [0, 5]

    # LIC 10
    coordinates[35] = [0,0]
    coordinates[36] = [0, 4]
    coordinates[37] = [0, 3]
    coordinates[38] = [7, 0]
    coordinates[39] = [9, 4]
    coordinates[40] = [4, 0]

    # LIC 11
    coordinates[41] = [0,0]
    coordinates[42] = [0,0]
    coordinates[43] = [25, 0]
    coordinates[44] = [0,0]
    coordinates[45] = [0,0]


    #LIC 12
    coordinates[46] = [0,0]
    coordinates[47] = [0, 1]
    coordinates[48] = [0, 1]
    coordinates[49] = [0, 2]

    # LIC_13
    coordinates[50] = [1,1]
    coordinates[51] = [10,10]
    coordinates[52] = [1,1]
    coordinates[53] = [20,20]
    coordinates[54] = [1,1]
    coordinates[55] = [30,30]

    # LIC_14
    coordinates[56] = [0,0]
    coordinates[57] = [0, 4]
    coordinates[58] = [0, 3]            
    coordinates[59] = [7, 0]
    coordinates[60] = [9, 4]
    coordinates[61] = [4, 0]


def decide():
    ''' Main function that will take inputs parameters and coordinates from input() function. It will then form the LCM and PUV matrices as part of its input, in order to calculate the PUM and finally the FUV vector, yielding an answer YES or NO (Launch or not). 
    
        Input
        -----
        numpoints (int): Number of coordinates in the testing scenario.
        coordinates (int[]): The coordinates for a testing scenario.
        LCM (bool[][]): The logical connector matrix.
        PUV (int): Preliminary unlocking vector.
        Parameters (Imported from stdin): Parameters for the testing scenario.


        Returns
        -------
        True or False (Successfull launch or not)
        
        '''
    input()

    CMV = cmv(parameters, coordinates)
    condVect = CMV.return_cond_vector() # Calculate the CMV from LICs.

    PUM = pum(condVect, LCM, PUV) # Imports the PUM class with specified input values.

    PUM_matrix = PUM.compute_PUM() # Calculates the PUM.
    FUV_vector = PUM.compute_FUV(PUM_matrix) # Calculates the FUV.

    return PUM.Launch(FUV_vector) 

print(decide())