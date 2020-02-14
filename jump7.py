i = 0
while i < 100:
    i = i + 1
    if i/7 == int(i / 7) or i % 10 == 7 or i // 7 == 10:
        continue
    else:
        print(i)
