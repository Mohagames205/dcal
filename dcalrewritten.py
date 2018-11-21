import math
import re
import sys 
import os

def clear():
    os.system("cls")

print("Welkom bij D-Cal rewritten. Een programma gemaakt door Mohamed El Yousfi")
print(" ")
while True:
    print("=============================")
    term1 = input("Typ de eerste term van de vergelijking in. ")
    a = term1.split("x²")[0]
    
    if term1.lower() == "exit":
        sys.exit()

    if term1.isalpha() == True:
        print("Deze versie kan nog niet rekenen met letters!")
        sys.exit()

    term2 = input("Typ de tweede term van de vergelijking in. ")
    b = term2.split("x")[0]
    
    if term1.lower() == "exit":
        sys.exit()

    if term2.isalpha() == True:
        print("Deze versie kan nog niet rekenen met letters!")
        sys.exit()
        
    term3 = input("Typ de derde term van de vergelijking in. ")
    if term1.lower() == "exit":
        sys.exit()

    if term3.isalpha() == True:
        print("Deze versie kan nog niet rekenen met letters!")
        sys.exit()

    c = term3


    #Dit is voor debugging
    """
    print(a)
    print(b)
    print(c)
    vergelijking = term1+term2+term3
    print(vergelijking)
    """
    a = int(a)
    b = int(b)
    c = int(c)

    b_pow = pow(b, 2)
    #print(b_pow)
    rest = 4 * a * c
    uitkomst = b_pow - rest
    uitkomst_sqrt = math.sqrt(uitkomst)
    #print(rest)
    clear()
    print("=============================")
    print(f"D = {uitkomst}")
    print("=============================")
    print(f"√D = {uitkomst_sqrt}")
    
