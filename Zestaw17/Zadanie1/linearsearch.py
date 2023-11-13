import random


class LinearSearch:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.list = [random.randint(0, k) for _ in range(n)]

    def search(self, number: int) -> int:
        if number >= self.k or number < 0:
            raise ValueError("Błędna liczba")
        result = 0
        for x in self.list:
            if x == number:
                result += 1
        return result

    def print_list(self):
        for x in self.list:
            print(x)
