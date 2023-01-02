class protected:
    def __init__(self):
        self._protectedVar = 5

obj = protected()
obj._protectedVar = 29
print(obj._protectedVar)


class privated:
    def __init__(self):
        self._privateVar = 12

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

obj = privated()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
