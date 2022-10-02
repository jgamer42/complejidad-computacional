import random

def generate(data_size):
    return [random.randint(1,500) for _ in range(data_size)]