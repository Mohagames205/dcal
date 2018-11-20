import math
import re 
import sys
vergelijking = input("Typ de vergelijking in ")
test = re.split("[-+]", vergelijking)
abc = vergelijking.split(" ")

term1 = test[0]
term2 = test[1]
term3 = test[2]

term1 = term1.split("x²")
term2 = term2.split("x")

if term1[0].isalpha() == True:
    print("We kunnen nog niet rekenen met letters.")
    sys.exit()

a = int(term1[0])
b = int(term2[0])
c = int(term3)

if "-" in abc:
    if abc.count("-") == 2:
        c = c
    c = -c



berekenen = b**2 - 4 * a * c
print (berekenen)