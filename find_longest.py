words = ["apple", "banana", "cherry", "blueberry"]

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is", longest_word)
