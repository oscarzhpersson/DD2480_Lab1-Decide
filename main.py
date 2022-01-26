import numpy as np
import enum
from dataclasses import dataclass

##### CONSTANT #####

pi = np.pi #3.1415926535

##### TYPE DECLARATIONS #####

class Connectors(enum.Enum):
    "NOTUSED",
    "ORR",
    "ANDD"

# Matrix of X, Y coordinate pairs.
coordinate = np.zeros((100, 2)) #? Replaces the coordinate X and coordinate Y variable.

bMatrix = np.zeros((15, 15))

cMatrix = np.matrix((15, 15))

vector = np.zeros(15)

##### Inputs to the DECIDE() function #####

@dataclass
class PARAMETERS_T:
    length1: float
    radius1: float
    epsilon: float
    area1: float
    q_Pts: int
    quads: int
    dist: float
    n_Pts = int
    k_Pts = int
    a_Pts = int
    b_Pts = int
    c_Pts = int
    d_Pts = int
    e_Pts = int
    f_Pts = int
    g_Pts = int
    length2: float
    radius2: float
    area2: float

parameters = PARAMETERS_T()

# TODO Import PUM
# TODO Import CMV
# TODO Import FUV

#? Function you must write:

def decide():
    #Do something.
    print("")