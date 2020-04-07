class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, value):
        if value <= self.capacity:
            return True
        else:
            return False

    def add(self, value):
        self.capacity = self.capacity - value
        return self.capacity


x = MoneyBox(15)
print(x.capacity)
print(x.can_add(1))
print(x.add(1))
