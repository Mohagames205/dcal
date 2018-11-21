import math
import re
import sys 

term1 = input("Typ de eerste term van de vergelijking in. ")
term1 = term1.split("x²")[0]
if term1.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()

term2 = input("Typ de tweede term van de vergelijking in. ")
if term2.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()
    
term3 = input("Typ de derde term van de vergelijking in. ")
if term3.isalpha() == True:
    print("Deze versie kan nog niet rekenen met letters!")
    sys.exit()

term2 = term2.split("x")[0]

if term1.isalpha() == True or term2.isalpha() == True or term3.isalpha() == True:
    print("We kunnen nog niet rekenen met letters.")
    sys.exit()

print(term1)
print(term2)
print(term3)