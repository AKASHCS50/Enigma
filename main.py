import os
import time
import sys


class rotor:

    def __init__(self, x, m):

        self.reference = list(m)

        self.notch = x

    def rotation(self, *args):

        c = self.reference.pop(0)
        self.reference.append(c)

    def rotor_output(self, ex):

        r = self.reference.index(ex)
        return self.reference[r]

    def initial_rotation(self, i):
        for v in range(i):
            self.rotation()


class reflector:
    def __init__(self, mr):

        self.ref = list(mr)

    # def reflector_reference(self, exer):

    #     rt = self.ref.index(exer)
    #     print(rt)
    #     return self.ref[rt]


# main

def rev_rotat(s, n):

    for m in range(n):
        c = s.pop(25)
        s.insert(0, c)


def rot(s, n):

    for m in range(n):
        c = s.pop(0)
        s.append(c)


exact = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
exact1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
exact2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
exact3 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
exact4 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
exact5 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")



Rotor1 = rotor("Q", "EKMFLGDQVZNTOWYHXUSPAIBRCJ")
Rotor2 = rotor("E", "AJDKSIRUXBLHWTMCQGZNPYFVOE")
Rotor3 = rotor("V", "BDFHJLCPRTXVZNYEIWGAKMUSQO")
Rotor4 = rotor("J", "ESOVPZJAYQUIRHXLNFTGKDCMWB")
Rotor5 = rotor("Z", "VZBRGITYUPSDNHLXAWMJQOFECK")

rotor1 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor3 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor4 = list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotor5 = list("VZBRGITYUPSDNHLXAWMJQOFECK")
# ABCDEFGHIJKLM
ReflectorB = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
ReflectorC = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

m1, m2, m3 = input("Enter the rotor numbers : ").split(" ")
r = int(input("Enter the reflector number : "))
m1 = int(m1)
m2 = int(m2)
m3 = int(m3)

c1, c2, c3 = input("Enter the initial configuration : ").split()

if m1 == 1:
    main_rotor1 = Rotor1
    temp_main_rotor1 = rotor1
elif m1 == 2:
    main_rotor1 = Rotor2
    temp_main_rotor1 = rotor2
elif m1 == 3:
    main_rotor1 = Rotor3
    temp_main_rotor1 = rotor3
elif m1 == 4:
    main_rotor1 = Rotor4
    temp_main_rotor1 = rotor4
else:
    main_rotor1 = Rotor5
    temp_main_rotor1 = rotor5


if m2 == 1:
    main_rotor2 = Rotor1
    temp_main_rotor2 = rotor1
elif m2 == 2:
    main_rotor2 = Rotor2
    temp_main_rotor2 = rotor2
elif m2 == 3:
    main_rotor2 = Rotor3
    temp_main_rotor2 = rotor3
elif m2 == 4:
    main_rotor2 = Rotor4
    temp_main_rotor2 = rotor4
else:
    main_rotor2 = Rotor5
    temp_main_rotor2 = rotor5


if m3 == 1:
    main_rotor3 = Rotor1
    temp_main_rotor3 = rotor1
elif m3 == 2:
    main_rotor3 = Rotor2
    temp_main_rotor3 = rotor2
elif m3 == 3:
    main_rotor3 = Rotor3
    temp_main_rotor3 = rotor3
elif m3 == 4:
    main_rotor3 = Rotor4
    temp_main_rotor3 = rotor4
else:
    main_rotor3 = Rotor5
    temp_main_rotor3 = rotor5

if r == 1:
    main_reflector = ReflectorB
else:
    main_reflector = ReflectorC


a1 = exact.index(c1)
print(a1)
main_rotor1.initial_rotation(a1)
a2 = exact.index(c2)
print(a2)
main_rotor2.initial_rotation(a2)
a3 = exact.index(c3)
print(a3)
main_rotor3.initial_rotation(a3)


def result(c):

    i1 = exact.index(c)
    main_rotor1.rotation()
    i1 = main_rotor1.reference[i1]

    if main_rotor1.reference[25] == main_rotor1.notch:
        c = 1
        m = main_rotor2.reference[0]
        main_rotor2.rotation()
    print(i1)

    diff1 = temp_main_rotor1.index(
        main_rotor1.reference[0]) - temp_main_rotor2.index(main_rotor2.reference[0])
    if diff1 < 0:
        diff1 = 26 + diff1
    print(diff1)
    i2 = exact.index(i1)
    rev_rotat(exact1, diff1)
    print(exact1)
    i2 = exact1[i2]
    i2 = exact.index(i2)
    i2 = temp_main_rotor2[i2]
    print(i2)

    if c == 1:
        if m == main_rotor2.notch:
            c = 0
            main_rotor3.rotation()

    diff2 = temp_main_rotor2.index(
        main_rotor2.reference[0]) - temp_main_rotor3.index(main_rotor3.reference[0])
    if diff2 < 0:
        diff2 = 26 + diff2
    print(diff2)
    i3 = exact.index(i2)
    rev_rotat(exact2, diff2)
    print(exact2)
    i3 = exact2[i3]
    i3 = exact.index(i3)
    i3 = temp_main_rotor3[i3]
    print(i3)

    i4 = main_rotor3.reference[0]
    i4 = temp_main_rotor3.index(i4)
    print(i4)
    rev_rotat(exact3, i4)
    print(exact3)
    i4 = exact3[exact.index(i3)]
    print(i4)
    i4 = main_reflector.ref[exact.index(i4)]
    print(i4)

    i5 = exact4.index(i4)
    rev_rotat(exact4, i5)
    i5 = temp_main_rotor3.index(main_rotor3.reference[0])
    i5 = exact[i5]
    i5 = exact4.index(i5)
    i5 = exact[i5]
    i5 = temp_main_rotor3.index(i5)
    i5 = exact[i5]
    print(i5)
    
    i6 = exact2.index(i5)
    i6 = exact[i6]
    i6 = temp_main_rotor2.index(i6)
    i6 = exact[i6]
    print(i6)
    
    i7 = exact1.index(i6)
    i7 = exact[i7]
    i7 = temp_main_rotor1.index(i7)
    i7 = exact[i7]
    print(i7)
    
    i8 = main_rotor1.reference[0]
    i8 = temp_main_rotor1.index(i8)
    diff3 = exact.index(i7) - i8
    if diff3 < 0:
        diff3 = 26 + diff3    
    i8 = exact[diff3]
    return i8


output = ""
plugs = []

str = input("Enter the string : ")


pg = int(input("Enter the number of plugs : "))
for x in range(pg):
    n1, n2 = input("Enter the", x, "plug : ").split(" ")
    plugs.append(n1)
    plugs.append(n2)
    for s in range(len(str)):
        if str[x] == n1:
            str[x] = n2
        elif str[x] == n2:
            str[x] = n1


for c in str:
    ot = result(c)
    exact = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    exact1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    exact2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    exact3 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    exact4 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    exact5 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = output+ot

r = 0

for x in range(pg):
    for s in range(len(output)):
        if output[x] == plugs[r]:
            output[x] = plugs[r+1]
        elif output[x] == plugs[r+1]:
            output[x] = plugs[r]
    r += 2

print("Encoded string : ", output)
