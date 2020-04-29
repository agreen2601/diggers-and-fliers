from interfaces import Swimmers

class Fish(Swimmers):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name} the Beta Fish'