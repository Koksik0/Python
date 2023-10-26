def flatten(sequence) -> list:
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Podano zły argument")
    result = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

assert flatten([[1,2,3,[1,[100,(999)]]],(5,6,7)]) == [1,2,3,1,100,999,5,6,7]
