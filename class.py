#parent class
class Organism:
    name = 'Hello'
    species = 'hey'
    legs = 0
    arms = 0
    dna = 'sequence a'
    origin = 'unknown'
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg
#Child class
class Human(Organism):
    name = 'Ross'
    species = 'human'
    legs = 2
    arms = 2
    origin = 'earth'

    def ingenuity(self):
        msg = "\nCreate a deadly weapon"
        return msg

class Dog(Organism):
    name = "Spot"
    species = 'dog'
    legs = 4
    arms = 0
    dna = 'sequence b'
    origin = 'earth'

    def bit(self):
        msg = "\nbarks a lot"
        return msg





if __name__ == "__main__":
    x = Human()
    print(x.information())
    print(x.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())
