width = int(input("Podaj szerokość: "))
height = int(input("Podaj wysokość: "))

parts = ["+"] * (width+1)
parts = '---'.join(parts)

parts1 = ["|"] * (width+1)
parts1 = "   ".join(parts1)

parts += "\n"
parts1 += "\n"

temp = [parts] * (height + 1)
result = parts1.join(temp)
print(result)