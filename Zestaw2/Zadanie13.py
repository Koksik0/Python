expected_result = 49
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
assert sum(len(x) for x in line.split()) == expected_result