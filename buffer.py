class Buffer:
    def __init__(self):
        self.spisok = []

    def __repr__(self):
        return str (list(self.spisok))

    def add(self, *a):
        self.spisok += a
        for i in range(len(self.spisok)):
            if len(self.spisok)>=5:
                print(sum(self.spisok[0:5]))
                for i in range(5):
                    self.spisok.pop(0)

    def get_current_part(self):
        return str (list(self.spisok))

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]







