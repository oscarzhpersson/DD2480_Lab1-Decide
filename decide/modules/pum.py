import numpy as np

class pum:
    def __init__(self, CMV, LCM, PUV):
        ## 15x15 array [1 = ANDD, 0 = ORR, -1 = NOTUSED]
        self.CMV = CMV
        self.LCM = LCM
        self.PUV = PUV

    def compute_PUM(self):
        PUM = np.ones(15, 15, dtype=bool)
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
                    PUM[i, j] = False

        return PUM


    def compute_FUV(self, PUM):
        FUV = np.zeros(15, dtype=bool)
        for i in range(len(FUV)):
            if not self.PUV[i]:
                FUV[i] = True
            else:
                FUV[i] = np.all(PUM[i])

        return FUV