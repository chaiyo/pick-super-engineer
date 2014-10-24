# import random module
import random

# initial object engineer to None
engineers = None


def pick_engineer():
    """
    Function: pick_engineer
    Description: pick an engineer from file.
    """
    global engineers
    if not engineers:
        engineers = open('engineers.txt').read().splitlines()
    return random.choice(engineers)

if __name__ == '__main__':
    
    print(pick_engineer())

