list = [1, 2, 2, 3, 4, 4, 5]

result = []
[result.append(item) for item in list if item not in result]

print(result)

