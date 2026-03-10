wyniki = []
for i in range(1, 101):
    if i == 50:
        wyniki.append("127859")
    elif i % 15 == 0:
        wyniki.append("LoveUEP")
    elif i % 3 == 0:
        wyniki.append("Love")
    elif i % 5 == 0:
        wyniki.append("UEP")
    else:
        wyniki.append(str(i))
print(', '.join(wyniki))