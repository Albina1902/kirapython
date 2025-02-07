sentence = "python is a great programming language"

words = sentence.split()

if len(words) < 2:
    print("Too short to modify")
else:
    for i in range(0, len(words), 2):
        words[i] = words[i].capitalize()
    result = " ".join(words)
    print(result)
