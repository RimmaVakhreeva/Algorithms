import time
from itask import ITask


class LuckyTickets(ITask):
    def __init__(self):
        self.n = None
        self.q = None

    def calculate(self):
        self.q = 0
        for a1 in range(10):
            for a2 in range(10):
                for a3 in range(10):
                    sum1 = a1 + a2 + a3
                    for b1 in range(10):
                        for b2 in range(10):
                            for b3 in range(10):
                                sum2 = b1 + b2 + b3
                                if sum1 == sum2:
                                    self.q += 1

    def next_digit(self, digit, sum1, sum2):
        if digit == self.n:
            if sum1 == sum2:
                self.q += 1
            return
        for a in range(10):
            for b in range(10):
                self.next_digit(digit + 1, sum1 + a, sum2 + b)

    def run(self, data):
        # before = time.time()
        self.n = int(data[0])
        self.q = 0
        self.calculate()
        # self.next_digit(0, 0, 0)
        # after = time.time()
        # print(f'{after - before} seconds')
        return str(self.q)
