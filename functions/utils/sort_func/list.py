import random


class ListHelper:
    @staticmethod
    def generate(length: int, print_list: bool = True) -> list:
        generated_list: list = []
        for i in range(length):
            generated_list.append(random.random())
        if print_list:
            ListHelper.print_list(generated_list)
        return generated_list

    @staticmethod
    def print_list(generated_list: list):
        for num in generated_list:
            print(num)
