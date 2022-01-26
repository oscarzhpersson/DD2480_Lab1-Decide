import numpy as np
class CMV:
    def __init__(self, PARAMS, coordinates):
        self.PARAMS = PARAMS # Check main file for structure
        self.coordinates = coordinates
        self.CondVector = np.array(15, dtype=bool)

    # Set Condvector[0]
    def LIC_0(self):
        return 0
    
    # Set Condvector[1]
    def LIC_1(self):
        for i in range(len(self.coordinates)-2): 
            x_center = self.coordinates[i+1, 0]
            y_center = self.coordinates[i+1, 1]
            x_left = self.coordinates[i, 0]
            y_left = self.coordinates[i, 1]
            x_right = self.coordinates[i+2, 0]
            y_right = self.coordinates[i+2, 0]
            
        return False
    

    # Set Condvector[2]
    def LIC_2(self):
        return 0
    
    # Set Condvector[3]
    def LIC_3(self):
        return 0

    # Set Condvector[4]
    def LIC_4(self):
        return 0
    
    # Set Condvector[5]
    def LIC_5(self):
        return 0

    # Set Condvector[6]
    def LIC_6(self):
        return 0

    # Set Condvector[7]
    def LIC_7(self):
        return 0

    # Set Condvector[8]
    def LIC_8(self):
        return 0

    # Set Condvector[9]
    def LIC_9(self):
        return 0

    # Set Condvector[10]
    def LIC_10(self):
        return 0

    # Set Condvector[11]
    def LIC_11(self):
        return 0

    # Set Condvector[12]
    def LIC_12(self):
        return 0

    # Set Condvector[13]
    def LIC_13(self):
        return 0

    # Set Condvector[14]
    def LIC_14(self):
        return 0

    def return_cond_vector(self):
        return 0
