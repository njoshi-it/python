import random
def roll(): return random.randint(1, 6)
def func() :
    for r in iter(roll, 6):   # keep rolling until we get a 6 (6 is sentinel)
    return r
