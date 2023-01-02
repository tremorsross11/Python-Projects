from abc import ABC, abstractmethod

class Height(ABC):
    def tall(self, inches):
        print("Lets see how much you've grown!")

    @abstractmethod
    def oldtall(self, inches):
        pass

class diagnosis(Height):
    def oldtall(self, inches):
        tall = input("Input height: ")
        oldtall = "5"
        print("You are {} inches tall. You grew {} inches this year!".format(tall, oldtall))


obj = diagnosis()
obj.tall(input)
obj.oldtall("5")
