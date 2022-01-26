import numpy as np
class CMV:
    def __init__(self, PARAMS, coordinates):
        self.PARAMS = PARAMS # Check main file for structure
        self.coordinates = coordinates
        self.CondVector = np.zeros(15, dtype=bool)

    # Set Condvector[0]
    def LIC_0():
    
        # Set Condvector[1]
    def LIC_1():
        return 0

    # Set Condvector[2]
    def LIC_2():
        return 0
    
    # Set Condvector[3]
    # Input: Array of coordinates.
    # Output: True if there exists three consecutive datapoints
    #         making up the area of a triangle with an area larger than AREA1.
    def LIC_3(self):


        return 0

    # Set Condvector[4]
    def LIC_4():
        return 0
    
    # Set Condvector[5]
    def LIC_5():
        return 0

    # Set Condvector[6]
    def LIC_6():
        return 0

    # Set Condvector[7]
    def LIC_7():
        return 0

    # Set Condvector[8]
    def LIC_8():
        return 0

    # Set Condvector[9]
    def LIC_9():
        return 0

    # Set Condvector[10]
    def LIC_10():
        return 0

    # Set Condvector[11]
    def LIC_11():
        return 0

    # Set Condvector[12]
    def LIC_12():
        return 0

    # Set Condvector[13]
    def LIC_13():
        return 0

    # Set Condvector[14]
    def LIC_14():
        return 0


    def return_cond_vector():
        return self.CondVector
