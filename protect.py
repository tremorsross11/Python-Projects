class protected:
    def __init__(self):
        self._protectedVar = 5

obj = protected()
obj._protectedVar = 29
print(obj._protectedVar)


class privated:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = privated()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
