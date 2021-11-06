
from borracho import BorrachoTradicional, BorrachoNorte
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def walking(campo, borracho, pasos):
    inicio = campo.get_coordenadas_de_borracho(borracho)

    for _ in range(pasos):
        campo.move_borracho(borracho)

    return inicio.distance(campo.get_coordenadas_de_borracho(borracho))


def simular(pasos, number_tries, tipo_borracho):
    borracho = tipo_borracho(name='camilo')
    origen = Coordenada(0, 0)
    distance = []

    for _ in range(number_tries):
        campo = Campo()
        campo.add_borracho(borracho, origen)
        simulation = walking(campo, borracho, pasos)
        distance.append(round(simulation, 1))

    return distance

def graficar(x,y):
    grafica = figure(title = 'camino aleatorio', x_axis_label = 'pasos', y_axis_label = 'distancia')
    grafica.line(x,y, legend = 'distancia media')

    show(grafica)

def main(walking_distance, number_tries, tipo_borracho):
    distancia_media_caminata = []

    for pasos in walking_distance:
        distance = simular(pasos, number_tries, tipo_borracho)
        medium_distance = round(sum(distance)/len(distance), 4)
        maximal_distance = max(distance)
        minimal_distance = min(distance)
        distancia_media_caminata.append(medium_distance)

        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {medium_distance}')
        print(f'Max = {maximal_distance}')
        print(f'Min = {minimal_distance}')
    
    graficar(walking_distance, distancia_media_caminata)

if __name__ == "__main__":
    walking_distance = [10, 100, 1000, 10000]
    number_tries = 100

    main(walking_distance, number_tries, BorrachoTradicional)
    main(walking_distance, number_tries, BorrachoNorte)

