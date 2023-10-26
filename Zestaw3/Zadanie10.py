roman_numerals1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_numerals2 = dict()
roman_numerals1['I'] = 1
roman_numerals1['V'] = 5
roman_numerals1['X'] = 10
roman_numerals1['L'] = 50
roman_numerals1['C'] = 100
roman_numerals1['D'] = 500
roman_numerals1['M'] = 1000

keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
roman_numerals3 = {keys[i]: values[i] for i in range(len(keys))}
