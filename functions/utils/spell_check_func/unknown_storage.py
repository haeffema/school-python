import os

ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH = f'{ROOT_DIR}\\functions\\ressources\\spell_check\\unknown_words.txt'


def clear_unknown_storage():
    open(PATH, "w").close()


def add_to_unknown_storage(word: str):
    old = open(PATH, "r").read()
    clear_unknown_storage()
    with open(PATH, "a") as file:
        if old == "":
            file.write(word)
        else:
            file.write(f"{old}\n{word}")
