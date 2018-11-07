line1 = input ("Enter here: ")
g = ""
for ch in line1:
    if ord (ch) >= 65 and ord(ch) <= 90:
        x = ord(ch) + 32
        y = chr (x)
        g = g + y
print(g)