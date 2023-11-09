from functions.utils.time_func.custom_sleep import sleep


class SelectionSort:
    @staticmethod
    def sort(random_list: list, delay_ms: float = 0):
        for x in range(len(random_list) - 1):
            min_index = x
            for i in range(x + 1, len(random_list)):
                sleep(delay_ms)
                if random_list[i] < random_list[min_index]:
                    min_index = i
            random_list[x], random_list[min_index] = random_list[min_index], random_list[x]
