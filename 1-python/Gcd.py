# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:26:32 2025

@author: Latitude 5410
"""

def gcd(a,b):
    while b:
        a,b=b,a%b#replace a with b and b with remainder
    return a
#input
num1=int(input("enter first no.:"))    
num2=int(input("enter second no.:"))    

#output
ans=gcd(num1,num2)
print(f"GCD of {num1} and{num2} is:{ans}")


#finding gcd using math function
import math
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
ans=math.gcd(num1,num2)
print(f"GCD of {num1} and {num2} is :{ans} ")














