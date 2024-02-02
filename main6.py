letters = input("harif kriting: ")
list2 = []
list = [
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
]

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        if letters == list[i][j]:
            list2.append(list[i][j])
        j += 1
    i += 1

print(len(list2))

