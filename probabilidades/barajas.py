import random 
import collections

PALOS = ['trebol', 'diamante', 'corazon', 'pica']
VALORES= ['as','1','2','3','4','5','6','7','8','9','10','jota','reina', 'rey']

def create_baraja():
    barajas =[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas

def get_mano(barajas, size_mano):
    mano = random.sample(barajas, size_mano)
    return mano

def main(size_mano, tries):
    barajas = create_baraja()
    manos = []

    for _ in range(tries):
        mano = get_mano(barajas, size_mano)
        manos.append(mano)
    
    pares = 0

    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    
    probability_even = pares/tries

    print(f'probability to find a even in a mano of {size_mano} is: {probability_even}')
    




if __name__ == '__main__':
    size_mano =int(input("how many carts are by mano? "))
    tries = int(input("how many times would you like to try?"))
    
    main(size_mano, tries)


