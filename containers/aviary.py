class Aviary:

    def __init__(self, name):
        self.animals_within = []
        self.name = name

    def add_animal(self, animal):
        try:
            if animal.inhabits == "sky":
                self.animals_within.append(animal)
                print(f'{animal} has been added to the {self.name}.')
            else:
                print(f'{animal} is not allowed in the {self.name}.')
        except AttributeError:
            return 0