from python.functions.utils.time_func.custom_sleep import sleep

# only works with sorted lists


def binary_search(list: list, number: int, delay_in_ms: float):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if number == list[mid]:
            return number
        elif number < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
        sleep(delay_in_ms)
    return "number not in list"
