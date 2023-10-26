first_sequence = input("Podaj pierwszą sekwencje: ")
second_sequence = input("Podaj drugą sekwencje: ")

result1 = []
for x in first_sequence:
    for y in second_sequence:
        if x == y and x not in result1:
            result1.append(x)

result2 = list(first_sequence)
for x in second_sequence:
    if x not in first_sequence:
        result2.append(x)

print(result1)
print(result2)