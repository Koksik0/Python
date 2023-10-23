x = int(input("Podaj wielkość miarki: \n"))
gap = len(str(x)) + 2
dots = '.' * gap
parts = ['|' + dots] * x
result = ''.join(parts) + '|'
temp = ""
for x in range(x+1):
    temp += str(x)
    if x%10 == 9 and str(x)[0]=='9':
        temp += ' ' * (gap + (0 - len(str(x))))
    else:
        temp += ' ' * (gap + (1 - len(str(x))))
print(result)
print(temp)