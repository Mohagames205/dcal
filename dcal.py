import math
import re 
import sys
vergelijking = input("Typ de vergelijking in ")
test = re.split("[-+]", vergelijking)
abc = vergelijking.split(" ")
print(abc)
term1 = test[0]
term2 = test[1]
term3 = test[2]

term1 = term1.split("x²")
term2 = term2.split("x")

if term1[0].isalpha() == True:
    print("We kunnen nog niet rekenen met letters.")
    sys.exit()

if term1[0] == ' ':
    a = 1
    print("check1")
    print (a)
    b = int(term2[0])
    c = int(term3)
elif term2[0] == ' ':
    b = 1
    print("check2")
    print (b)
    a = int(term1[0])
    c = int(term3)
elif term3 == ' ':
    c = 1
    print("check3")
    print (c)
    a = int(term1[0])
    b = int(term2[0])

else:
    a = int(term1[0])
    b = int(term2[0])
    c = int(term3)

print (term1[0] + term2[0] + term3)

if "-" in abc:
    if abc.count("-") == 2:
        c = c
    c = -c
print (c)



z = pow(b, 2)
a_str = str(a)
c_str = str(c)
b_str = str(b)
y = 4 * a * c
print(y)
ya = str(y)
print (ya)
if "-" in ya:

    if abc.count("-") == 2:
        ya = int(ya)
        #ya = abs(ya)
        berekenen = z + ya
        print("plus weg, 2 minnen")

    else:
        z = str(z)
        totaal = (z+ "-" + ya)
        berekenen = eval(totaal)
        print("min")
else:
    ya = int(ya)
    ya = abs(ya)
    berekenen = z + ya
    print("plus 1 weg")

print("========================")
print(f"De discriminant is {berekenen}")
b_sqr = math.sqrt(berekenen)
b_sqrf = math.floor(b_sqr)

print(f"De vierkantswortel van de discriminant is {b_sqr}")
print("===========================")