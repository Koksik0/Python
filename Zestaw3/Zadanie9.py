sequence = [[],[4],(1,2),[3,4],(5,6,7)]
result = []
for x in sequence:
    temp = 0
    for y in x:
        temp += y
    result.append(temp)
assert result == [0,4,3,7,18]