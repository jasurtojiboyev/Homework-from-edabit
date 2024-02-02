numbers = [3, 3, 3, 7, 3, 3, 3]

number = "yoq"
index = 0

while index < len(numbers):
    num = numbers[index]
    if numbers.count(num) == 1:
        print(numbers)
        break
    print(num)
    index += 1

print("Unikal son:", number)