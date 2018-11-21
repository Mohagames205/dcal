import math
import re
import sys 

term1 = input("Typ de eerste term van de vergelijking in. ")
a = term1.split("x²")[0]
if term1.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()

term2 = input("Typ de tweede term van de vergelijking in. ")
b = term2.split("x")[0]
if term2.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()
    
term3 = input("Typ de derde term van de vergelijking in. ")
if term3.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()

c = term3

if term1.isalpha() == True or term2.isalpha() == True or term3.isalpha() == True:
    print("We kunnen nog niet rekenen met letters.")
    sys.exit()




print(a)
print(b)
print(c)
vergelijking = term1+term2+term3
print(vergelijking)

a = int(a)
b = int(b)
c = int(c)

b_pow = pow(b, 2)
print(b_pow)
rest = 4 * a * c
uitkomst = b_pow - rest
print(rest)
print (uitkomst)

