def sum_seq(sequence) -> int:
    if not isinstance(sequence, (list,tuple, int)):
        raise ValueError("Podany argument musi być liczbą, listą lub krotką")
    result = 0
    for x in sequence:
        if isinstance(x,(list,tuple)):
            result += sum_seq(x)
        else:
            result += x
    return result

assert sum_seq([1,2,3,4,[1,2,3,4,[100,300]],(10,20,30)]) == 480