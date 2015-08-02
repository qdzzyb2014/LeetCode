class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stact = []
        self.size = 0

# @paramx, an integer
# @return nothing
    def push(self, x):
        helper = []
        for _ in range(self.size):
            helper.append(self.stack.pop())
        self.stack.append(x)
        for _ in range(self.size):
            self.stack.append(helper.pop())
        self.size += 1

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.size -= 1

    # @return an integer
    def peek(self):
        return self.stack[-1]

    def empyty(self):
        return self.size == 0