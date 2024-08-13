class Fib:

    def __init__(self):
        self.curr = 1
        self.prev = 0

    def __iter__(self):
        return self

    def __next__(self):
        dummy = self.prev
        self.prev = self.curr
        self.curr = dummy + self.curr
        return self.curr
