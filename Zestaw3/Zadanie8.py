first_sequence = "12345qwerty"
second_sequence = "345rty"

result1 = []
for x in first_sequence:
    for y in second_sequence:
        if x == y and x not in result1:
            result1.append(x)

result2 = list(first_sequence)
for x in second_sequence:
    if x not in first_sequence:
        result2.append(x)

assert result1 == ['3','4','5','r','t','y']
assert result2 == ['1','2','3','4','5','q','w','e','r','t','y']