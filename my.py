s = input()

new = s[0].upper()

nw = s[1:]





for i in range(len(nw)):
    if nw[i-1] == " " and nw[i].isalpha():
        new =new + nw[i].upper()

    else:
        new = new + nw[i]

print(new)

