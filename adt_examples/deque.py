class Deque:

    def __init__(self, len):
        self.len = len
        self.list = [None] * len
        self.lpointer = 0
        self.rpointer = 0

    def append(self, x):
        if all(_ is None for _ in self.list):
            self.list[self.rpointer]=x
        else:
            self.rpointer = (self.rpointer + 1) % self.len
            self.list[self.rpointer]= x


    def appendleft(self, x):
        if all(_ is None for _ in self.list):
            self.list[self.lpointer] = x
        else:
            self.lpointer = (self.lpointer - 1) % self.len
            self.list[self.lpointer] = x


    def pop(self):
        dummy  = self.list[self.rpointer]
        self.list[self.rpointer] = None
        self.rpointer = (self.rpointer -1) % self.len
        return dummy

    def popleft(self):
        dummy = self.list[self.lpointer]
        self.list[self.lpointer] = None
        self.lpointer = (self.lpointer + 1) % self.len
        return dummy

    def peek(self):
        return self.list[self.rpointer]

    def peekleft(self):
        return self.list[self.lpointer]

    def __len__(self):
        u = self.len
        for i in range(self.len):
            if self.list[i] == None:
                u -=1
        return u

    def __iter__(self):
        return DequeIterator(self)


class DequeIterator:

    def __init__(self, deque: Deque):
        self.deque = deque
        self.curr = self.deque.lpointer
        self.flag = False

    def __iter__(self):
        return self

    def __next__(self):
        dummy = self.deque.list[self.curr]
        if self.curr == self.deque.lpointer and self.flag==True:
            raise StopIteration
        self.curr = (self.curr + 1) % self.deque.len
        #print(self.curr)

        self.flag = True
        return dummy
Q = Deque(3)
Q.append(2)
Q.append(4)
Q.appendleft(0)
for i in Q:
    print(i)
#print(Q.rpointer, Q.lpointer)
#print(Q.list[Q.lpointer], Q.list[Q.rpointer])

