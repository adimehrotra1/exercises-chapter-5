from math import sin , cos
from numbers import Number
class RPCalc:

    def __init__(self):
        self.stack = []

    def push(self, n):
        operators = ["+", "-", "*", "/", "sin", "cos"]
        if isinstance(n, Number):
            self.stack.append(n)
        elif n in operators:
            if n == "+":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a + b)
                print(self.stack)
            if n == "-":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b - a)
                print(self.stack)
            if n == "*":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a * b)
                print(self.stack)
            if n == "/":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b / a)
                print(self.stack)
            if n == "sin":
                a = self.stack.pop()
                self.stack.append(sin(a))
            if n == "cos":
                a = self.stack.pop()
                self.stack.append(cos(a))

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

