import numpy as np
class cmv:
    def __init__(self, PARAMS, coordinates):
        self.PARAMS = PARAMS # Check main file for structure
        self.coordinates = coordinates
        self.CondVector = np.zeros(15, dtype=bool)

    # Set Condvector[0]
    def LIC_0(self):
        return self.__calculate_distance_LICs(self.PARAMS.length1)
    
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
        return 0
    
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
        
        return self.__calculate_distance_LICs(self.PARAMS.length1, offset=k_Pts)


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
        k_Pts = self.PARAMS.k_Pts

        # Checks pre-condition
        if len(self.coordinates) < 3:
            return False
        if not (1 <= k_Pts <= (len(self.coordinates)-2)):
            return False

        check1 = self.__calculate_distance_LICs(self.PARAMS.length1, offset=k_Pts, greater_than_flag=True)
        check2 = self.__calculate_distance_LICs(self.PARAMS.length2, offset=k_Pts, greather_than_flag=False)
        return check1 and check2

    # Set Condvector[13]
    def LIC_13(self):
        return 0

    # Set Condvector[14]
    def LIC_14(self):
        return 0
      
    def return_cond_vector(self):
        return 0

    def __euclidean_distance(self, c1, c2):
        x = c1[0] - c2[0]
        y = c1[1] - c2[1]

        return np.sqrt(x ** 2 + y ** 2)

    def __calculate_distance_LICs(self, distance, offset=0, greater_than_flag = True):
        for i in range(len(self.coordinates)-offset- 1):
            c1 = self.coordinates[i]
            c2 = self.coordinates[i+offset+1]
            if self.__euclidean_distance(c1, c2) > distance and greater_than_flag:
                return True
            if self.__euclidean_distance(c1, c2) < distance and greater_than_flag:
                return True
        return False

