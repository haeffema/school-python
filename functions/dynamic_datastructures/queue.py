class ListElement:
    def __init__(self, text) -> None:
        self.text = text
        self.reference = None

class Queue:
    def __init__(self) -> None:
        self.top: ListElement | None = None
        self.bottom: ListElement | None = None
        self.size = 0

    def enqueue(self, text):
        list_element = ListElement(text)
        if self.size == 0:
            self.top = list_element
            self.bottom = list_element
        else:
            old_bottom = self.bottom
            old_bottom.reference = list_element
            self.bottom = list_element
        self.size += 1

    def dequeue(self):
        top_element = self.top
        if top_element is None:
            return top_element
        self.top = top_element.reference
        self.size -= 1
        return top_element.text

    def size(self):
        return self.size

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('der')
    queue.enqueue('alte')
    queue.enqueue('Baum')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
