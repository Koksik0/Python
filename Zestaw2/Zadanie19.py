expected_result = "894009013347"
L = [894,9,13,347]
numbers = [str(x).zfill(3) for x in L]
assert ''.join(numbers) == expected_result