from abc import ABC, abstractmethod

class Height(ABC):
    def tall(self, inches):
        print("You are {} inches tall!".format(inches))

    @abstractmethod
    def oldtall(self, inches):
        pass

class diagnosis(Height):
    def oldtall(self, inches):
        print("You are {} inches tall. You grew {} inches this year!".format(tall, oldtall))


obj = diagnosis()
obj.tall("72")
obj.oldtall("5")
