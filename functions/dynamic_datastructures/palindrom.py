from queue import Queue
from linked_list import Stack

if __name__ == '__main__':
    string_to_test = 'A man, a plan, a canal, Panama.'

    queue = Queue()
    stack = Stack()

    for char in string_to_test:
        if char.isalpha():
            queue.enqueue(char.lower())
            stack.push(char.lower())

    queue_result = queue.dequeue()
    stack_result = stack.pop()
    while queue_result is not None and stack_result is not None:
        if queue_result == stack_result:
            queue_result = queue.dequeue()
            stack_result = stack.pop()
        else:
            print('not a palindrom')
            quit()
    print('a palindrom')
