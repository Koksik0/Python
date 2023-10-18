expected_result1 = ['adipiscing', 'amet,', 'consectetur', 'dolor', 'elit.', 'ipsum', 'Lorem', 'sit']
expected_result2 = ['sit', 'Lorem', 'ipsum', 'dolor', 'amet,', 'elit.', 'adipiscing', 'consectetur']
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = line.split()
sorted1 = sorted(words,key=str.lower)
sorted2 = sorted(words,key=len)
assert sorted1 == expected_result1
assert sorted2 == expected_result2
