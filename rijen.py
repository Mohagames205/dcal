import math
import os
import sys

t1 = input("Typ de eerst term van de rij in ")
vq = input("Typ je Q of V in in het volgend formaat xq of xv ")
n = input("Hoeveelste term wil je? ")
n = int(n)
n -= 1
t1 = int(t1)
getal = vq[0]
getal = int(getal)

if vq[1].lower() == "q":
    deel1 = getal ** n
    deel2 = t1 * deel1


if vq[1].lower() == "v":
    deel1 = n * getal
    deel2 = t1 + deel1

print(deel2)


