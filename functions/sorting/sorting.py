from time import time

from functions.utils.sort_func.SelectionSort import SelectionSort
from functions.utils.sort_func.list import ListHelper


def sort_with_given_algorithm(sorting_algorithm, length: int = 100, print_list: bool = True, take_time: bool = True, delay_ms: float = 0):
    generated_list = ListHelper.generate(length, print_list)
    print(f"Sorting {length} entries with {sorting_algorithm.__name__} ...")
    start_time = time()
    sorting_algorithm.sort(generated_list, delay_ms)
    duration = time() - start_time
    if print_list:
        ListHelper.print_list(generated_list)
    if take_time:
        print(
            f"Sorted List with {length} entries in {duration.__round__(2)} seconds with {sorting_algorithm.__name__}.\nThere was a custom delay of {delay_ms} ms for every step.")


def sort():
    length = 5
    sort_with_given_algorithm(SelectionSort, length, False, True)
