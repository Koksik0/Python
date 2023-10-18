expected_result = "Przykładowy tekst Guido van Rossum"
line = "Przykładowy tekst GvR"
line_replaced = line.replace("GvR","Guido van Rossum")
assert line_replaced ==expected_result