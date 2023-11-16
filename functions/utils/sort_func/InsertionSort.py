from functions.utils.time_func.custom_sleep import sleep


class InsertionSort:
    @staticmethod
    def sort(random_list: list, delay_ms: float = 0):
        for i in range(1, len(random_list)):
            j = i
            while (j > 0) and (random_list[j] < random_list[j-1]):
                sleep(delay_ms)
                random_list[j - 1], random_list[j] = random_list[j], random_list[j - 1]
                j = j - 1
