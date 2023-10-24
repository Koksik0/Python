def odwracanieIteracyjnie(L: list, left:int, right:int) -> list:
    if left >= right or right >= len(L):
        raise ValueError("Błąd")
    while left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    return L


def odwracanieRekurencyjnie(L: list, left: int, right: int) -> list:
    if left >= right or right >= len(L):
        raise ValueError("Nieprawidłowe indeksy")
    L[left], L[right] = L[right], L[left]
    if left + 1 < right - 1:
        return odwracanieRekurencyjnie(L, left + 1, right - 1)

    return L

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers1 = [1,2,3,4,5,6,7,8,9,10]
print(odwracanieIteracyjnie(numbers,4,5))
print(odwracanieRekurencyjnie(numbers1,2,9))