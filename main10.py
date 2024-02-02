my_list = ["Adam", "Emmy", "Tanya", "Emmy"]

name = []
index = 0

while index < len(my_list):
    x = my_list[index]
    if my_list.count(x) == 1:
        name.append(x)
    index += 1

print(name)
