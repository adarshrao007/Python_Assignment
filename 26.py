
line1 = input ('Enter your string: ')
g = ""
for ch in line1:
    if ord (ch) >= 97 and ord(ch) <= 122:
        x = ord(ch) - 32
        y = chr (x)
        g = g + y
print(g)