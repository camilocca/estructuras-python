class Campo:

    def __init__(self):
        self.coordenadas_de_borracho = {}

    def add_borracho(self, borracho, coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada

    def move_borracho(self, borracho):
        delta_x, delta_y = borracho.walk()
        coordenada_actual = self.coordenadas_de_borracho[borracho]
        new_coordenada = coordenada_actual.move(delta_x, delta_y)

        self.coordenadas_de_borracho[borracho] = new_coordenada

    def get_coordenadas_de_borracho(self, borracho):
        return self.coordenadas_de_borracho[borracho]
