roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman2int(roman_numeral: str, roman_numerals: dict) -> int:
    result = 0
    prev_value = 0
    for x in reversed(roman_numeral):
        temp = roman_numerals[x]
        if temp < prev_value:
            result -= temp
        else:
            result += temp
        prev_value = temp
    return result


roman_numeral = "MCMXCIV"
print(roman2int(roman_numeral, roman_numerals))
