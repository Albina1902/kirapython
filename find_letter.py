words = ["banana", "apple", "cherry", "grape"]
letter = "a"
result = [word for word in words if word.count(letter) ]
if result:
    print(result)
else:
    print("No words found")