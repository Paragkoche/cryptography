# get plan tex
plentext = input("Enater the plan text :-")
# get key
# key = input("Enater the key text 1 ~ 9 :-")
# convet text to ascii code to bin
a = ''.join(format(ord(i), '08b') for i in plentext)
b = ''.join(format(ord(i), '08b') for i in "8")

# lbeft shift text[bin] << key[bin]
ans = "$".join(
    str(int(format(ord(i), '08b'), 2) << int(b, 2)) for i in plentext
)
# print ans
print(ans)
