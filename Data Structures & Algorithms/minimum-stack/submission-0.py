class MinStack:

    def __init__(self):
        self.q = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.mini or val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        if self.q.pop() == self.getMin():
            self.mini.pop()


    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
