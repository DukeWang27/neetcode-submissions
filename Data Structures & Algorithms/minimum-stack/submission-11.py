class MinStack:
    def __init__(self):
        self.s = []      # all values
        self.mins = []   # mins[i] = smallest value in s[0..i]

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.mins.pop()   # keep both lists the same length

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1]