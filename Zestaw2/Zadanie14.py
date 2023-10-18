expected_word = "consectetur"
expected_length = 11
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = line.split(" ")
longest_word = max(words,key=len)
max_length = len(longest_word)
assert longest_word == expected_word
assert max_length == expected_length