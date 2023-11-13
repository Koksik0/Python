class BinarySearch:
    def __init__(self, n):
        self.list = [x*2 for x in range(n)]

    def binarne_rek(self, left, right, y) -> int:
        if left > right:
            return -1

        middle = (left + right) // 2
        if self.list[middle] == y:
            return middle
        elif self.list[middle] > y:
            return self.binarne_rek(left, middle - 1, y)
        else:
            return self.binarne_rek(middle + 1, right, y)
