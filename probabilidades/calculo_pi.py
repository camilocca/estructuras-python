import math
import random
from estadisticas import standard_deviation, media

def aventar_aguja(n_agujas):
    adentro= 0
    
    for _ in range(n_agujas):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])

        distancia = math.sqrt(x*x + y*y)

        if distancia <= 1:
            adentro += 1

    return (4* adentro)/n_agujas

def estimados(n_agujas, n_intentos): 
    estimados = []
    for _ in range(n_intentos):
        estimacion_pi = aventar_aguja(n_agujas)
        estimados.append(estimacion_pi)
    
    media_estimada = media(estimados)
    sigma = standard_deviation(estimados)

    print (f'Estimado = {round(media_estimada, 5)}, sigma = {round(sigma,5)}, agujas = {n_agujas}')

    return (media_estimada, sigma)

def estimar_pi(precision, n_intentos): 
    n_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media,sigma = estimados(n_agujas, n_intentos)
        n_agujas *=2
    
    return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000)