satrlar = ["a", "ccc", "dddd", "bb"]

i = 0
while i < len(satrlar):
    j = i + 1
    while j < len(satrlar):
        if len(satrlar[i]) > len(satrlar[j]):
            satrlar[i], satrlar[j] = satrlar[j], satrlar[i]
        j += 1
    i += 1

print(satrlar)