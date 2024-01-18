class Stack:
    def __init__(self):
        self._list = list()

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

def calculate_operation(number1_str: str, number2_str: str, operation: str):
    number1 = int(number1_str)
    number2 = int(number2_str)
    match operation:
        case '+':
            return str(number1 + number2)
        case '-':
            return str(number1 - number2)
        case '*':
            return str(number1 * number2)
        case '/':
            return str(number1 / number2)
    


example = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'

operator_stack = Stack()
number_stack = Stack()

for char in example:
    if char != ' ' and char != '(':
        if char == ')':
            number_stack.push(calculate_operation(number_stack.pop(), number_stack.pop(), operator_stack.pop()))
        if char.isdigit():
            number_stack.push(char)
        elif char != ')':
            operator_stack.push(char)

print(number_stack.pop())
