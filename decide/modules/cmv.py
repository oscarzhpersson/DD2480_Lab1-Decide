import numpy as np
import math
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
    def LIC_2(self):

        '''Checks if the angle formed by three consecutive points are larger than pi+epsilon or smaller pi-epsilon.
                The function creates a trinagle from the different points and uses the cosinus formula:
                C = arccos(line_12^2 + line_23^2 - line_13^2 / 2 * line12 * line13)
                C is the angle that is compared to pi+epsilon or pi-epsilon.
                Parameters
                ----------
                None
                Returns
                -------
                bool
                    True if pi+epsilon is larger than the angle or pi-epsilon is smaller than the angle
                    False if the above clauses is not satisfied
                See Also
                --------
                PARAMETERS_T object: Provides a full overview of the input data to the function (coordinates array).
                '''

        # Pick out three consecutive points
        for i in range(len(self.coordinates) - 2):
            point_1_x = self.coordinates[i, 0]
            point_1_y = self.coordinates[i, 1]
            point_2_x = self.coordinates[i + 1, 0]
            point_2_y = self.coordinates[i + 1, 1]
            point_3_x = self.coordinates[i + 2, 0]
            point_3_y = self.coordinates[i + 2, 1]

        # Create line 12
        line12_x = (point_2_x - point_1_x)
        line12_y = (point_2_y - point_1_y)
        line12 = math.sqrt((line12_x ** 2) + (line12_y ** 2))

        # Create line 13
        line23_x = (point_3_x - point_2_x)
        line23_y = (point_3_y - point_2_y)
        line23 = math.sqrt((line23_x ** 2) + (line23_y ** 2))

        # Create line 23
        line13_x = (point_3_x - point_1_x)
        line13_y = (point_3_y - point_1_y)
        line13 = math.sqrt((line13_x ** 2) + (line13_y ** 2))

        # Finding the angle
        angle = math.acos(((line12 ** 2) + (line23 ** 2) - (line13 ** 2)) / (2 * line12 * line23))

        if (angle < (np.pi - self.PARAMS.epsilon) or angle > (np.pi + self.PARAMS.epsilon)):
            return True
        else:
            return False

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

    def check_quadrants(self, coor, qpts):
        first_quadrent = 0
        sec_quadrent = 0
        fourth_quadrent = 0
        third_quadrent = 0
        coor = np.array(coor)

        for i in range(qpts):
            if coor[i, 0] > 0 and coor[i, 1] > 0:
                first_quadrent = 1
                # check for 2nd quadrant
            elif coor[i, 0] < 0 and coor[i, 1] > 0:
                sec_quadrent = 1
                # check for 3rd quadrant
            elif coor[i, 0] < 0 and coor[i, 1] < 0:
                third_quadrent = 1
                # check for fourth quadrant
            elif coor[i, 0] > 0 and coor[i, 1] < 0:
                fourth_quadrent = 1
                # Else its the origin
            else:
                first_quadrent = 1

        total_quad = first_quadrent + sec_quadrent + third_quadrent + fourth_quadrent

        return total_quad

    # Set Condvector[4]
    def LIC_4(self):
        print("Print 1")
        qpts = int(self.PARAMS.q_Pts)
        quads = self.PARAMS.quads
        lenght = int(len(self.coordinates))
        print("Print 2")

        if (quads <= 1 or quads >= 3):
            return False
        print("Print 3")

        print("Len: ", len(self.coordinates))
        print("qpts: ", qpts)
        if (2 > qpts or len(self.coordinates) < qpts):
            return False
        print("Print 4")
        for i in range(lenght):
            pointlist = []
            for j in range(qpts):
                if (i + qpts) > lenght:
                    return False
                pointlist.append(self.coordinates[i + j])

            total_quad = self.check_quadrants(pointlist, qpts)
            if total_quad > quads:
                return True

        return False

    # Set Condvector[5]
    def LIC_5(self):
        '''Checks if there is a set of two coordinates such that X[j] - X[i] < 0. (where i = j-1).

        Function iterates through the array of coordinates in sets of two. A satisfying set of coordinates is described through the condition:
        X[j] - X[i] < 0. (where i = j-1).

        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if a set satisfying the conditions exist.
            False if a set of satisfying conditions does not exist.

        See Also
        --------
        PARAMETERS_T object: Provides a full overview of the input data to the function (coordinates array).

        '''

        # If an insufficient amount of points are present (< 2), return false.
        if len(self.coordinates) < 2:
            return False

        for i in range(len(self.coordinates) - 1):
            (x1, y1) = self.coordinates[i]
            (x2, y2) = self.coordinates[i + 1]

            # If a satisfying set is found, return True.
            if (x2 - x1) < 0:
                return True

        return False

    # Set Condvector[6]
    def LIC_6(self):
        return 0

    # Set Condvector[7]
    def LIC_7(self):
        '''Checks if There exists at least one set of two data points separated by exactly K PTS consecutive intervening points that are a distance greater than the length, LENGTH1, apart.
        The function checks pairs of coordinates that are K_PTS apart to see if they pass the distance criteria.
        Parameters
        ----------
        None
        Returns
        -------
        bool
            True if a set satisfying the conditions exist.
            False if a set of satisfying conditions does not exist.
        See Also
        --------
        PARAMETERS_T object: Provides a full overview of the input data to the function (coordinates array).
        '''
        k_Pts = self.PARAMS.k_Pts

        # Checks pre-condition
        if len(self.coordinates) < 3:
            return False
        if not (1 <= k_Pts <= (len(self.coordinates)-2)):
            return False
        
        for i in range(len(self.coordinates)-self.PARAMS.k_Pts - 1):
            ## This can probably be refactored with LIC0, uses same Euclidean Distance.
            x = self.coordinates[i, 0] - self.coordinates[i+k_Pts+1, 0]
            y = self.coordinates[i, 1] - self.coordinates[i+k_Pts+1, 1]
            if np.sqrt(x ** 2 + y ** 2) > self.PARAMS.length1:
                return True
        return False

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
