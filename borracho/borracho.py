import random


class Borracho:

    def __init__(self, name):
        self.name = name


class BorrachoTradicional(Borracho):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])


class BorrachoNorte(Borracho):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 2), (2, 0), (0, -1), (-1, 0)])
