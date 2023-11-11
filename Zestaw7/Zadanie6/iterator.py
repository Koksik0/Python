import random


class Binary_iterator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            self.number = 1
            return self.number
        self.number = 0
        return self.number


class Random_iterator:
    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(['N', 'E', 'S', 'W'])


class Weekly_iterator:
    def __init__(self):
        self.number = 6

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            self.number = 1
            return self.number
        elif self.number == 1:
            self.number = 2
            return self.number
        elif self.number == 2:
            self.number = 3
            return self.number
        elif self.number == 3:
            self.number = 4
            return self.number
        elif self.number == 4:
            self.number = 5
            return self.number
        elif self.number == 5:
            self.number = 6
            return self.number
        else:
            self.number = 0
            return self.number
