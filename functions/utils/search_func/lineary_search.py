from functions.utils.time_func.custom_sleep import sleep

# works with all lists


def lineary_search(list: list, number: int, delay_in_ms: float):
    for num in list:
        if num == number:
            return number
        sleep(delay_in_ms)
    return "number not in list"
