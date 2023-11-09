from statistics import mean
from time import time as tm

from functions.utils.search_func.binary_search import binary_search
from functions.utils.search_func.lineary_search import lineary_search
from functions.utils.search_func.list_generator import generate_list

filename_list = ["ints_8.txt", "ints1k.txt", "ints2k.txt", "ints8k.txt",
                 "ints16k.txt", "ints32k.txt", "ints64k.txt", "ints128k.txt"]

delay_in_ms: float = 0.1 / 1000  # miliseconds
amount_of_random_numbers = 10


def time_binary(int_list: list, numbers: list):
    times = []
    for number in numbers:
        start_time = tm()
        binary_search(int_list, number, delay_in_ms)
        times.append(tm() - start_time)
    return round(mean(times), 3)


def time_lineary(int_list: list, numbers: list):
    times = []
    for number in numbers:
        start_time = tm()
        lineary_search(int_list, number, delay_in_ms)
        times.append(tm() - start_time)
    return round(mean(times), 3)


def time_comparison():
    print(
        f"calculates the average time it takes for {amount_of_random_numbers} random number(s) to be found in a sorted list with a binary and a lineray searching algorithm were every step has a delay of {delay_in_ms}ms")
    for filename in filename_list:
        amount, int_list, numbers = generate_list(
            filename, amount_of_random_numbers)
        print(f"{amount} Numbers:\n\tBinary:  {round(time_binary(int_list, numbers), 3)}s\n\tLineary: {round(time_lineary(int_list, numbers), 3)}s")
