from functions.utils.time_func.custom_sleep import sleep

# only works with sorted lists


def binary_search(list: list, wanted, delay_in_ms: float):
    low = 0
    high = len(list) - 1
    while low <= high:
        sleep(delay_in_ms)
        mid = (low + high) // 2
        if wanted == list[mid]:
            return True
        elif wanted < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
