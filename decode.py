# import textwaper to split te numders
import textwrap

# get incoded text and key
plentext = str(input("Enater the encode text :-"))
key = input("Enater the key text 0 ~ 9 :-")
# kdy convert to ascii code to bin
b = ''.join(format(ord(i), '08b') for i in key)
aa = ""
# right shift to reversh the lift shif
for i in plentext.split("$"):
    ans = int(i) >> int(b, 2)
    s = textwrap.wrap(str(ans), 3)
    aa += ''.join(map(chr, [int(i) for i in s]))
# print the plantex
print(aa)
