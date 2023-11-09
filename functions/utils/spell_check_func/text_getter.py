import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH = f'{ROOT_DIR}\\functions\\ressources\\spell_check\\text.txt'


def get_text():
    return open(PATH).read()
