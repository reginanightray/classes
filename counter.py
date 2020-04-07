class CountFromBy():
    def __init__(self, v: int = 0, st: int = 1):
        self.val = v
        self.step = st

    def __repr__(self):
        return str(self.val)

    def increase(self):
        self.val += self.step


j = CountFromBy(st = 20)
j.increase()
j.increase()
j.increase()
print(j)
