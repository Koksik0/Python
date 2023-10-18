expected_result = "12345678910"
L = [1,2,3,4,5,6,7,8,9,10]
string = ("".join(str(x) for x in L))
assert string == expected_result