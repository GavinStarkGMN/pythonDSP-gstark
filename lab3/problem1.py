import random
import numpy as np

def make_birthdays(n):
    birthdays = np.arange(n)
    for i in range(n):
        birthdays[i] = random.randrange(1, 367)
    birthdays.sort()
    return birthdays

def run_trial(n):
    bdays = make_birthdays(n)
    for i in range(n):
        if bdays[i] in bdays[i+1:]:
            return 1
    return 0

sample_size = int(input("How many people are in the room? "))
results = np.array([run_trial(23) for i in range(100000)])
print("With {} people in the room, there is a {:.4g}% chance that 2 people will share a birthday".format(sample_size, float(np.mean(results) * 100)))