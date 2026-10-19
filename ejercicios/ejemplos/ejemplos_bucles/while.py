# Con while
numbers = [10,14,21,22,26,56]
index = 0
found = None
while index < len(numbers) and found is None:
    if numbers[index] % 7 == 0:
        found = numbers[index]
    index += 1
print(f"Encontrado con while: {found}")