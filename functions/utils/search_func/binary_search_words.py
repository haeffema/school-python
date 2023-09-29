from python.functions.utils.time_func.custom_sleep import sleep

# only works with sorted lists


def binary_search_words(dictionary: list, word: str, delay_in_ms: float):
    low = 0
    high = len(dictionary) - 1
    while low <= high:
        mid = (low + high) // 2
        if word == dictionary[mid]:
            return True
        elif word_smaller_than_dict_entry(word, dictionary[mid]):
            high = mid - 1
        else:
            low = mid + 1
        sleep(delay_in_ms)
    return False

def word_smaller_than_dict_entry(word: str, dict_entry: str):
    for x in range(len(word)):
        if len(dict_entry) < x - 1:
            return False
        if ord(word[x].lower()) < ord(dict_entry[x].lower()):
            return True
        if ord(word[x].lower()) > ord(dict_entry[x].lower()):
            return False
    return True
        