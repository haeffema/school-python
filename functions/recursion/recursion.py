from functions.utils.recursion_func.factorial import factorial
from functions.utils.recursion_func.flip_string import flip_string
from functions.utils.recursion_func.binary_search import binary_search


def recursion():
    x = 3
    print(f"{x}! = {factorial(x)}")
    text = "Hund"
    print(f"{text}: {flip_string(text)}")
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = 3
    print(f"{number} in {list}: {binary_search(list, number, 0)}")
