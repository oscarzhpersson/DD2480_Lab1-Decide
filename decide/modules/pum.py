import numpy as np

class pum:
    def __init__(self, CMV, LCM, PUV):
        ## 15x15 array [1 = ANDD, 0 = ORR, -1 = NOTUSED]
        self.CMV = CMV
        self.LCM = LCM
        self.PUV = PUV

    #Creates the PUM
    def compute_PUM(self):

        """ The Conditions Met Vector (CMV) can now be used in conjunction with the Logical Connector Matrix (LCM) to form the Preliminary Unlocking Matrix (PUM)

            Parameters
            -----
            PUM: Preliminary Unlocking Matrix (PUM)

            Returns
            -----
            a PUM Matrix

            """

        PUM = np.ones((15, 15), dtype=bool)
        
        for i in range(self.LCM.shape[0]):
            for j in range(self.LCM.shape[0]):
                if i == j:
                    continue
                op = self.LCM[i,j]
                if op == 1:
                    PUM[i, j] = self.CMV[i] and self.CMV[j]
                if op == 0:
                    PUM[i, j] = self.CMV[i] or self.CMV[j]
                if op == -1:
                    PUM[i, j] = True

        return PUM

    #Creates the FUV
    def compute_FUV(self, PUM):
        """ The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. The input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling interceptor launch.

            Parameters
            -----
            FUV: Final Unlocking Vector (FUV)

            Returns
            -----
            The FUV vector

            """
        FUV = np.zeros(15, dtype=bool)
        for i in range(len(FUV)):
            if not self.PUV[i]:
                FUV[i] = True
            else:
                FUV[i] = np.all(PUM[i])

        return FUV

    #Checks that all launch conditions are satisfied before launch
    def Launch(self, FUV):
        """
        The final launch/no launch decision is based on the FUV. The decision to launch requires that all elements in the FUV be true, i.e. LAUNCH

            Parameters
            -----
            FUV: Final Unlocking Vector (FUV)

            Returns
            -----
            Returns True or False

            """
        return np.all(FUV)