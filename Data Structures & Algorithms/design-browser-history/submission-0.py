from collections import deque
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.history.appendleft(homepage)
        self.now = 0

    def visit(self, url: str) -> None:
        for _ in range(self.now):
            self.history.popleft()
        self.history.appendleft(url)
        self.now = 0

    def back(self, steps: int) -> str:
        self.now += steps
        if self.now > len(self.history) - 1:
            self.now = len(self.history) - 1
        return self.history[self.now]

    def forward(self, steps: int) -> str:
        self.now -= steps
        self.now = 0 if self.now < 0 else self.now
        return self.history[self.now]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)