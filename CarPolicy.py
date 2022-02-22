from Policy import Policy
class CarPolicy(Policy):
    def __init__(self,arg1,arg2,arg3,arg4,arg5):
        Policy.__init__(self,arg1,arg2,arg3)
        self.__engine_size = arg4
        self.__years_no_claims = arg5

    def get_engine_size_cc(self):
        return self.__engine_size

    def get_years_no_claims(self):
        return self.__years_no_claims

    def get_discount(self):
        if (self.__years_no_claims > 5):
            return 20
        else:
            return 0

    def get_discounted_premium(self):
        yp = self.get_yearly_premium()
        disc = yp * (self.get_discount()/100)
        return yp-disc
