import os

ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH = f'{ROOT_DIR}\\functions\\ressources\\spell_check\\dictionary.txt'


def generate_dictionary():
    return [i.replace("\n", "") for i in open(PATH).readlines()]
