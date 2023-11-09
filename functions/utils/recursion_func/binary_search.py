from functions.utils.time_func.custom_sleep import sleep


# only works with sorted lists


def binary_search(list: list, wanted, delay_in_ms: float):
    sleep(delay_in_ms)
    if len(list) == 1 and list[0] != wanted:
        return False
    mid = len(list) // 2
    if wanted == list[mid]:
        return True
    elif wanted < list[mid]:
        return binary_search(list[:mid], wanted, delay_in_ms)
    else:
        return binary_search(list[mid + 1:], wanted, delay_in_ms)
