import os
import random

ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH = f'{ROOT_DIR}\\functions\\ressources\\number_lists'


def generate_list(filename: str, amount_of_random_numbers: int):
    ROOT_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    int_list = [int(i) for i in open(f'{PATH}\\{filename}').readlines()]
    amount = int_list.pop(0)
    int_list.sort()
    return amount, int_list, [random.choice(int_list) for _ in range(amount_of_random_numbers)]
