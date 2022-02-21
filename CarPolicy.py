from Policy import Policy
class CarPolicy(Policy):
    def __init__(self,arg1,arg2,arg3,arg4,arg5):
        Policy.__init__(self,arg1,arg2,arg3)
        self.__engineSize = arg4
        self.__yearsNoClaims = arg5

    def getEngineSizeInCC(self):
        return self.__engineSizeInCC

    def getYearsNoClaims(self):
        return self.__yearsNoClaims

    def getDiscount(self):
        if (self.__yearsNoClaims > 5):
            return 20
        else:
            return 0

    def getDiscountedPremium(self):
        yp = self.getYearlyPremium()
        disc = yp * (self.getDiscount()/100)
        return yp-disc
