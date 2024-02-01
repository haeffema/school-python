class Knot:
    def __init__(self, value, left_element = None, right_element = None) -> None:
        self.value = value
        self.left_element: Knot = left_element
        self.right_element: Knot = right_element

    def traverse(self):
        if self.left_element is not None:
            self.left_element.traverse()
        if self.right_element is not None:
            self.right_element.traverse()
        print(self.value)

a = Knot(3)
b = Knot(5, left_element=a)
c = Knot(7, right_element=b)
d = Knot(8)
e = Knot(4)
f = Knot(6, left_element=d, right_element=e)
root = Knot(2, left_element=c, right_element=f)
root.traverse()
