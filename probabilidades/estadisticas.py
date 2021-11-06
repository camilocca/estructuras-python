import random
import math

def media(X):
    return sum(X)/ len(X)

def variance(X):
    mu = media(X)

    acomulador = 0
    for x in X:
        acomulador += (x-mu)**2

    return acomulador/len(X)

def standard_deviation(X):
    return math.sqrt(variance(X))

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    Var = variance(X)
    Sigma = standard_deviation(X)

    print('lista:',X)
    print('media: ',mu)
    print('Varianza: ',Var)
    print('Desviacion Estandar: ',Sigma)

