class Policy:
    def __init__(self, arg1, arg2, arg3):
        self.__policy_number= arg1
        self.__name = arg2
        self.__yearly_premium = arg3

    def __str__(self):
        return self.__policy_number + ": " + self.__name

    def get_yearly_premium(self):
        return self.__yearly_premium

    def get_name(self):
        return self.__name

