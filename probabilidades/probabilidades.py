import random

def dice_launcher(shot_numbers):
    sequence_shots = []

    for _ in range(shot_numbers):
        shot = random.choice([1,2,3,4,5,6])
        sequence_shots.append(shot)

    return sequence_shots

def main(shot_numbers, shot_tries):
    shots = []
    for _ in range(shot_tries):
        sequence_shots = dice_launcher(shot_numbers)
        shots.append(sequence_shots)
    
    shots_1 = 0
    for shot in shots:
        if 1 in shot:
            shots_1 += 1
    
    probability = shots_1 / shot_tries

    print(f'Probability to get at lest one in {shot_numbers} tries is: {probability}')

if __name__ == '__main__':
    shot_numbers = int(input('Enter a number of shots: '))
    shot_tries = int(input('Enter a number of tries: '))

    main(shot_numbers, shot_tries)

    
        