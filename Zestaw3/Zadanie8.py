first_sequence = input("Podaj pierwszą sekwencje")
second_sequence = input("Podaj drugą sekwencje")
first_set = set()
second_set = set()
for x in first_sequence:
    first_set.add(x)
for x in second_sequence:
    second_set.add(x)
print(first_set & second_set)
print(first_set | second_set)