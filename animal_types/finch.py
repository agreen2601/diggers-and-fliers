from interfaces import Fliers

class Finch(Fliers):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name} the Finch'