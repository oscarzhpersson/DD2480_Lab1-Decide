import sys
import numpy as np
import enum
from dataclasses import dataclass
#from modules import cmv
#from modules import pum

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

parameters = PARAMETERS_T()

#? Function you must write:

def input():

    parameters.length1 = sys.stdin.readline()
    parameters.radius1 = sys.stdin.readline()
    parameters.epsilon = sys.stdin.readline()
    parameters.area1 = sys.stdin.readline()
    parameters.q_Pts = sys.stdin.readline()
    parameters.quads = sys.stdin.readline()
    parameters.dist = sys.stdin.readline()
    parameters.n_Pts = sys.stdin.readline()
    parameters.k_Pts = sys.stdin.readline()
    parameters.a_Pts = sys.stdin.readline()
    parameters.b_Pts = sys.stdin.readline()
    parameters.c_Pts = sys.stdin.readline()
    parameters.d_Pts = sys.stdin.readline()
    parameters.e_Pts = sys.stdin.readline()
    parameters.f_Pts = sys.stdin.readline()
    parameters.g_Pts = sys.stdin.readline()
    parameters.length2 = sys.stdin.readline()
    parameters.radius2 = sys.stdin.readline()
    parameters.area2 = sys.stdin.readline()


def decide():

    