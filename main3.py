num = int(input("Sonni kiriting: "))
result = []
i = 1

while i <= num:
    if i % 4 == 0:
        number = 10 * i
        result.append(number)
    else:
        result.append(i)
    i += 1

print("Natija:", result)