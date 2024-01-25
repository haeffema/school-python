class ListElement:
    def __init__(self, data, reference) -> None:
        self.data = data
        self.reference = reference


class Stack:
    def __init__(self) -> None:
        self.last_element: ListElement | None = None

    def push(self, data) -> None:
        list_element = ListElement(data, self.last_element)
        self.last_element = list_element

    def pop(self) -> any:
        list_element = self.last_element
        if list_element is None:
            return
        self.last_element = list_element.reference
        return list_element.data

if __name__ == '__main__':
    stack = Stack()
    stack.push('der')
    stack.push('alte')
    stack.push('Baum')
    print(stack.pop())
