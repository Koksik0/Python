x = int(input("Podaj wielkość miarki: \n"))
gap = len(str(x)) + 2
dots = '.' * gap
parts = ['|' + dots] * x
result = ''.join(parts) + '|'
temp = ""
temp2 = 2
for i in range(x+1):
    temp += str(i)
    if len(str(i)) + 1 > temp2:
        temp += ' ' * (gap - len(str(i)))
        temp2 += 1
    else:
        temp += ' ' * (gap + (1 - len(str(i))))

result += '\n'
result += temp
print(result)
