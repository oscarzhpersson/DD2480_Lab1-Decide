import numpy as np
class cmv:
    def __init__(self, PARAMS, coordinates):
        self.PARAMS = PARAMS # Check main file for structure
        self.coordinates = coordinates
        self.CondVector = np.zeros(15, dtype=bool)

    # Set Condvector[0]
    def LIC_0(self):
        for i in range(len(self.coordinates)-1):
            x = self.coordinates[i, 0] - self.coordinates[i+1, 0]
            y = self.coordinates[i, 1] - self.coordinates[i+1, 1]
            if np.sqrt(x ** 2 + y ** 2) > self.PARAMS.length1:
                return True
        return False
    
    # Set Condvector[1]
    # Input: Array of coordinates.
    # Output: True If there exists at least one 3-set of 
    # consecutive datapoints that cannot be contained.
    # False if all 3-sets of consecutive datapoints
    # can be contained within the radius
    def LIC_1(self):
        for i in range(len(self.coordinates)-2): 
            x_center = self.coordinates[i+1, 0]
            y_center = self.coordinates[i+1, 1]
            x_left = self.coordinates[i, 0]
            y_left = self.coordinates[i, 1]
            x_right = self.coordinates[i+2, 0]
            y_right = self.coordinates[i+2, 0]
            radius = self.PARAMS.radius1
            
            # Checks if left adjacent point is outside radius
            if (x_left - x_center)**2 + (y_left - y_center)**2 > radius**2:
                return True

            # Checks if right adjacent point is outside radius
            if (x_right - x_center)**2 + (y_right - y_center)**2 > radius**2:
                return True

        # All sets of 3-consecutive points are within a circle with set radius
        return False
    

    # Set Condvector[2]
    # Input: Array of coordinates.
    # Output: True If there exists an angle that
    # Is larger than epsilon + pi or epsilon - pi
    def LIC_2(self):

    #Pick out three consecutive points
        for i in range(len(self.coordinates) - 2):
            point_1_x = self.coordinates[i, 0]
            point_1_y = self.coordinates[i, 1]
            point_2_x = self.coordinates[i+1, 0]
            point_2_y = self.coordinates[i+1, 1]
            point_3_x = self.coordinates[i+2, 0]
            point_3_y = self.coordinates[i+2, 1]

    # Create line 12
        line12_x = (point_2_x - point_1_x)
        line12_y = (point_2_y - point_1_y)
        line_12 = math.sqrt((line12_x**2) + (line12_y**2))

    # Create line 13
        line23_x = (point_3_x - point_2_x)
        line23_y = (point_3_y - point_2_y)
        line23 = math.sqrt((line23_x**2) + (line23_y**2))

    # Create line 23
        line13_x = (point_3_x - point_1_x)
        line13_y = (point_3_y - point_1_y)
        line13 = math.sqrt((line13_x**2) + (line13_y**2))

    # Gets the angle, uses the formula orignal formula:
    # c^2 = a^2 + b^2 - 2ab cos(C)
    # Can be restructured as:
    # C = arccos(line_12^2 + line_23^2 - line_13^2 / 2 * line12 * line13)
        angle = math.acos(((line12**2) + (line23**2) - (line13**2)) / (2*line_12*line23))

    #If the angle is larger or smaller, output true else outputs false
        if (angle < (np.pi - self.PARAMS.epsilon) or angle > (np.pi + self.PARAMS.epsilon)):
            return true
        else:
            return false
    
    # Set Condvector[3]
    # Input: Array of coordinates.
    # Output: True if there exists three consecutive datapoints
    #         making up the area of a triangle with an area larger than AREA1.
    def LIC_3(self):
        for i in range( len(self.coordinates) - 2 ): # Iterate all coordinates, leaving an offset to pair triplets.

            # Read the coordinates from the array into a tuple.
            c1, c2, c3 = (self.coordinates[i], self.coordinates[i + 1], self.coordinates[i + 2])

            # Calculates the area of the triangle using the determinant method.
            area = 0.5 * np.abs( (c1[0] * (c2[1] - c3[1]) + c2[0] * (c3[1] - c1[1]) + c3[0] * (c1[1] - c2[1])) )

            if area > self.PARAMS.area1:
                return True

        return False

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
