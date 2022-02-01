import numpy as np
from sympy import Point, Circle
import math

# Helper functions
def find_radius(min_coordinate, max_coordinate):
    '''Takes two coordinates and calculates the radius of the circle that would pass through them

        Parameters
        ----------
        two coordinates

        Returns
        -------
        radius: distance between the coordinates divided by two     

        '''
    x = max_coordinate[0] - min_coordinate[0]
    y = max_coordinate[1] - min_coordinate[1]
    diameter = math.sqrt(x ** 2 + y ** 2)
    radius = diameter / 2
    return radius

def distance(self, i, j):
    '''Takes two indexes i and j and calculates the distance between coordinate[i] and coordinate[j]

        Parameters
        ----------
        index for coordinate array: i, j

        Returns
        -------
        distance between coordinates            

        '''
    x = self.coordinates[i, 0] - self.coordinates[j, 0]
    y = self.coordinates[i, 1] - self.coordinates[j, 1]
    return math.sqrt(x ** 2 + y ** 2)

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
        '''Checks if there is a set of three coordinates that cannot all be contained within a circle of radius RADIUS1. This is done by forming a circle from the datapoints and comparing its radius to RADIUS1.

        Function iterates through the array of coordinates in sets of three. A satisfying set of coordinates is described through the condition:
        radius > self.PARAMS.radius1
        or
        self.PARAMS.radius1 == 0

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

        if self.PARAMS.radius1 == 0:
            return True
        
        for i in range(len(self.coordinates)-2):

            # Points generated by x,y values of 3 consecutive coordinates
            p1 = Point(self.coordinates[i, 0], self.coordinates[i, 1])
            p2 = Point(self.coordinates[i+1, 0], self.coordinates[i+1, 1])
            p3 = Point(self.coordinates[i+2, 0], self.coordinates[i+2, 1])
            list = [(p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y)]
            radius = 0

            # This set of coordinates can be contained within RADIUS1
            if p1 == p2 == p3:
                continue

            # Same x coordinates
            elif p1.x == p2.x == p3.x:
                y_min = min(list, key = lambda t: t[1])
                y_max = max(list, key = lambda t: t[1])
                radius = find_radius(y_min, y_max)

            # Same y coordinates    
            elif p1.y == p2.y == p3.y:
                x_min = min(list, key = lambda t: t[0])
                x_max = max(list, key = lambda t: t[0])
                radius = find_radius(x_min, x_max)

            # Two unique points instead of three
            elif p1 == p3 or p2 == p3:
                radius = distance(self, i, i+1) / 2
            elif p2 == p1:
                radius = distance(self, i+1, i+2) / 2
            
            # Three unique points, radius can be derived from circle
            else:
                radius = Circle(p1, p2, p3).radius
            
            # True if p1, p2 and p3 cannot all be contained within a circle of radius RADIUS1
            if (radius > self.PARAMS.radius1):
                return True
            
        # All sets of 3-consecutive points are within a circle with set radius
        return False

        return 0
    
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

        # If the angle is larger or smaller, output true else outputs false
        if (angle < (np.pi - self.PARAMS.epsilon) or angle > (np.pi + self.PARAMS.epsilon)):
            return True
        else:
            return False

    # Set Condvector[3]
    # Input: Array of coordinates.
    # Output: True if there exists three consecutive datapoints
    #         making up the area of a triangle with an area larger than AREA1.
    def LIC_3(self):

        '''Function checks if there exists three consecutive datapoints who's collective area is larger than the specified AREA1 from PARAMETERS_T.

        By using the determinant method, the function creates a triangle and calculates its area using three consecutive points from the coordinates. If three
        consecutive points exist, return True. Otherwise return False.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if three consecutive datapoints make up a triangle with an area larger than AREA1 exists.
            False if three consecutive datapoints make up a triangle with an area larger than AREA1 does not exist.

        See Also
        --------
        PARAMETERS_T object: Provides a full overview of the input data to the function (coordinates array).

        '''

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

    def LIC_4(self):

        '''Checks if there exist a Q_pts consecutive data points that lie in more than QUADS quadrants.
               The function checks a set of coordinates that are in different quadrants and returns true if the points are in more than QUADS quadrant.

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

        #storing the values in parameter
        qpts = int(self.PARAMS.q_Pts)
        quads = self.PARAMS.quads
        length = int(len(self.coordinates))

        #Checking the first prerequisite
        if (quads <= 1 or quads >= 3):
            return False

        #Checking the second prerequisite
        if (2 > qpts or len(self.coordinates) < qpts):
            return False

        #Checking the number of quadrants the points fulfill
        for i in range(length):
            pointlist = []
            for j in range(qpts):
                if (i + qpts) > length:
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
        '''Checks if there is a set of three coordinates, separated by A_PTS and B_PTS intervening points, that cannot all be contained within a circle of radius RADIUS1. This is done by forming a circle from the datapoints and comparing its radius to RADIUS1.

        Function iterates through the array of coordinates in sets of three. A satisfying set of coordinates is described through the condition:
        radius > self.PARAMS.radius1

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

        # Prerequisite checks
        if self.PARAMS.radius1 == 0:
            return False
        if len(self.coordinates) < 5: 
            return False
        if self.PARAMS.a_Pts + self.PARAMS.b_Pts < 2:
            return False
        if (self.PARAMS.a_Pts + self.PARAMS.b_Pts) > len(self.coordinates) - 3: 
            return False

        # Iterating with regards to intervene point distance from a_Pts and b_Pts
        for i in range(len(self.coordinates) - (2 + self.PARAMS.a_Pts + self.PARAMS.b_Pts)):

            mid_index = i + 1 + self.PARAMS.a_Pts
            last_index = mid_index + 1 + self.PARAMS.b_Pts
            # Points generated by x,y values of coordinates separated by a_Pts and b_Pts
            p1 = Point(self.coordinates[i, 0], self.coordinates[i, 1])
            p2 = Point(self.coordinates[mid_index, 0], self.coordinates[mid_index, 1])
            p3 = Point(self.coordinates[last_index, 0], self.coordinates[last_index, 1])
            list = [(p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y)]
            radius = 0

            # This set of coordinates can be contained within RADIUS1
            if p1 == p2 == p3:
                continue

            # Same x coordinates
            elif p1.x == p2.x == p3.x:
                y_min = min(list, key = lambda t: t[1])
                y_max = max(list, key = lambda t: t[1])
                radius = find_radius(y_min, y_max)

            # Same y coordinates    
            elif p1.y == p2.y == p3.y:
                x_min = min(list, key = lambda t: t[0])
                x_max = max(list, key = lambda t: t[0])
                radius = find_radius(x_min, x_max)
            
            # radius = (distance between p1 and p2) / 2
            elif p1 == p3 or p2 == p3:
                radius = distance(self, i, i+1) / 2

            # radius = (distance between p2 and p3) / 2
            elif p2 == p1:
                radius = distance(self, i+1, i+2) / 2

            # 3 unique points, radius can be derived from circle
            else:
                radius = Circle(p1, p2, p3).radius

            # True if points cannot be contained within a circle of radius RADIUS1
            if (radius > self.PARAMS.radius1):
                return True

        return False

    # Set Condvector[9]
    def LIC_9(self):
        ''' Check if there exist one set of three data points 
            separated by exactly C PTS and D PTS respectively 
            and that the angle formed will be either  
            (angle < (pi-epsilon)) OR (angle > (pi+epsilon)).

        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if a set satisfying the conditions exist.
            False if a set of satisfying conditions does not exist & when condition is not met (NUMPOINTS<5).
        See Also
        --------
        PARAMETERS_T object: Provides a full overview of the input data to the function (coordinates array).
        '''

        if (len(self.coordinates) < 5) :
            return False
        if (self.PARAMS.c_Pts < 1):
            return False
        if (self.PARAMS.d_Pts < 1):
            return False
        if (self.PARAMS.c_Pts + self.PARAMS.d_Pts > len(self.coordinates) - 3):
            return False
        for i in range( len(self.coordinates) - self.PARAMS.c_Pts - self.PARAMS.d_Pts - 2): # Iterate all coordinates, till coordinates are out of range.
            c1, c2, c3 = (self.coordinates[i], self.coordinates[i + self.PARAMS.c_Pts + 1], self.coordinates[i + self.PARAMS.c_Pts + 1 + self.PARAMS.d_Pts + 1])
            c    = np.sqrt((c3[0] - c1[0])**2 + (c3[1] - c1[1])**2)
            a    = np.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)
            b  = np.sqrt((c3[0] - c2[0])**2 + (c3[1] - c2[1])**2)
            angle = np.arccos((a**2 + b**2 - c**2)/ (2*a*b))
            
            if (angle < (np.pi - self.PARAMS.epsilon)) or (angle > (np.pi + self.PARAMS.epsilon)) :
                return True

        return False

    # Set Condvector[10]
    def LIC_10(self):
        return 0

    # Set Condvector[11]
    def LIC_11(self):
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
        if len(self.coordinates) < 3:
            return False

        for i in range(len(self.coordinates) - self.PARAMS.g_pts - 1):
            (x1, y1) = self.coordinates[i]
            (x2, y2) = self.coordinates[i + self.PARAMS.g_pts + 1]

            # If a satisfying set is found, return True.
            if (x2 - x1) < 0:
                return True

        return False

    # Set Condvector[12]
    def LIC_12(self):
        return 0

    # Set Condvector[13]
    def LIC_13(self):
        # Prerequisite checks
        if self.PARAMS.radius2 == 0:
            return False
        if len(self.coordinates) < 5: 
            return False
        if self.PARAMS.a_Pts + self.PARAMS.b_Pts < 2:
            return False
        if (self.PARAMS.a_Pts + self.PARAMS.b_Pts) > len(self.coordinates) - 3: 
            return False

        # Both must be True for function to return True
        ret_flag_1 = False
        ret_flag_2 = False

        # Iterating with regards to intervene point distance from a_Pts and b_Pts
        for i in range(len(self.coordinates) - (2 + self.PARAMS.a_Pts + self.PARAMS.b_Pts)):
            mid_index = i + 1 + self.PARAMS.a_Pts
            last_index = mid_index + 1 + self.PARAMS.b_Pts
            # Points generated by x,y values of coordinates separated by a_Pts and b_Pts
            p1 = Point(self.coordinates[i, 0], self.coordinates[i, 1])
            p2 = Point(self.coordinates[mid_index, 0], self.coordinates[mid_index, 1])
            p3 = Point(self.coordinates[last_index, 0], self.coordinates[last_index, 1])
            list = [(p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y)]
            radius = 0

            # This set of coordinates can be contained within RADIUS2
            if p1 == p2 == p3:
                ret_flag_2 = True

            # Same x coordinates
            elif p1.x == p2.x == p3.x:
                y_min = min(list, key = lambda t: t[1])
                y_max = max(list, key = lambda t: t[1])
                radius = find_radius(y_min, y_max)

            # Same y coordinates    
            elif p1.y == p2.y == p3.y:
                x_min = min(list, key = lambda t: t[0])
                x_max = max(list, key = lambda t: t[0])
                radius = find_radius(x_min, x_max)

            # radius = (distance between p1 and p2) / 2
            elif p1 == p3 or p2 == p3:
                radius = distance(self, i, i+1) / 2

            # radius = (distance between p2 and p3) / 2
            elif p2 == p1:
                radius = distance(self, i+1, i+2) / 2

            # True if points cannot be contained within a circle of radius RADIUS2
            if (radius > self.PARAMS.radius1):
                ret_flag_1 = True
            # True if points can be contained within or on a circle of radius RADIUS2
            if (radius <= self.PARAMS.radius1):
                ret_flag_2 = True
            
            # Function conditional met
            if ret_flag_1 and ret_flag_2:
                return True


        return False

    # Set Condvector[14]
    def LIC_14(self):
        return 0
      
    def return_cond_vector(self):
        return 0
