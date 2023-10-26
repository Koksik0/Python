def make_ruler(x) -> str:
    if not isinstance(x,int):
        raise ValueError("Podany argument musi być całkowitoliczbowy")
    gap = len(str(x)) + 2
    dots = '.' * gap
    parts = ['|' + dots] * x
    result = ''.join(parts) + '|'
    temp = ""
    temp2 = 2
    for i in range(x + 1):
        temp += str(i)
        if len(str(i)) + 1 > temp2:
            temp += ' ' * (gap - len(str(i)))
            temp2 += 1
        else:
            temp += ' ' * (gap + (1 - len(str(i))))

    result += '\n'
    result += temp
    return result

def make_grid(width, height) -> str:
    if not isinstance(width,int) or not isinstance(height,int):
        raise ValueError("Podane argumenyy muszą być całkowitoliczbowy")
    parts = ["+"] * (width + 1)
    parts = '---'.join(parts)

    parts1 = ["|"] * (width + 1)
    parts1 = "   ".join(parts1)

    parts += "\n"
    parts1 += "\n"

    temp = [parts] * (height + 1)
    result = parts1.join(temp)
    return result
