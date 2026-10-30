import heapq

class MinStack:

    def __init__(self):
        self.res = []
        self.res_min = []

    def push(self, val: int) -> None:
        self.res.append(val)
        if len(self.res_min) == 0:
            self.res_min.append(val)
        elif val <= self.res_min[-1]:
            self.res_min.append(val)

    def pop(self) -> None:
        if len(self.res_min) > 0:
            if self.res[-1] == self.res_min[-1]:
                self.res_min.pop()
        self.res.pop()
        
    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        if len(self.res_min) > 0:
            return self.res_min[-1]
        
        return None
        
        
