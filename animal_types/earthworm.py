from interfaces import Diggers

class Earthworm(Diggers):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name} the Earthworm'