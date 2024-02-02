yigindi = 0
indeks = 0
royxat = [1, 2, 3, 4, 5]

while indeks < len(royxat):
    yigindi += indeks * royxat[indeks]
    indeks += 1
print(f"{royxat} <= royhatning yigindisi {yigindi}")