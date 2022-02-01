import numpy as np
import enum
from dataclasses import dataclass
from modules import cmv
from modules import pum

##### CONSTANT #####

pi = np.pi #3.1415926535

##### TYPE DECLARATIONS #####

class Connectors(enum.Enum):
    "NOTUSED",
    "ORR",
    "ANDD"

# Matrix of X, Y coordinate pairs.
coordinates = np.zeros((100, 2)) #? Replaces the coordinate X and coordinate Y variable.

# 2D array of 15x15 booleans.
bMatrix = np.zeros((15, 15))

# 2D array of 15x15 connectors as defined in Connectors enum.
cMatrix = np.matrix((15, 15))

# Array of 15 booleans.
vector = np.zeros(15)

##### Inputs to the DECIDE() function #####

@dataclass
class PARAMETERS_T:
    length1: float # Length in LICs 0, 7, 12.
    radius1: float # Radius in LICs 1, 8, 13.
    epsilon: float # Deviation from PI in LICs 2, 9.
    area1: float # Area in LICs 3, 10, 14.
    q_Pts: int # No. of consecutive points in LIC 4.
    quads: int # No. of quadrants in LIC 4.
    dist: float # Distance in LIC 6.
    n_Pts: int # No. of consecutive points in LIC 6.
    k_Pts: int # No. of int. points in LICs 7, 12.
    a_Pts: int # No. of int. points in LICs 8, 13.
    b_Pts: int # No. of int. points in LICs 8, 13.
    c_Pts: int # No. of int. points in LIC 9.
    d_Pts: int # No. of int. points in LIC 9.
    e_Pts: int # No. of int. points in LICs 10, 14.
    f_Pts: int # No. of int. points in LICs 10, 14.
    g_Pts: int # No. of int. points in LIC 11.
    length2: float # Maximum length in LIC 12.
    radius2: float # Maximum radius in LIC 13.
    area2: float # Maximum area in LIC 14.

parameters = PARAMETERS_T()

#? Function you must write:

def decide():
    CMV = cmv(parameters, coordinates)
    condVect = CMV.return_cond_vector()

    LCM = np.ones((15, 15)) # Create a default LCM, to be imported as input.
    PUV = np.ones(15, dtype=bool) # Create a default PUV, to be imported as input.

    PUM = pum(condVect, LCM, PUV) # Imports the PUM class with specified input values.

    PUM_matrix = PUM.compute_PUM() # Calculates the PUM.
    FUV_vector = PUM.compute_FUV(PUM_matrix) # Calculates the FUV.

    return PUM.Launch(FUV_vector) # Return whether LAUNCH is True of False.