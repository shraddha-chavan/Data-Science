# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:53:21 2025

@author: Latitude 5410
"""
###################################################################################################################
#Alexa wants to buy exactly N bananas from two vendors sells bananas in fixed-sized
#bunches . Alexa can only purchases full bunches and not individual bananas.
#He needs your help to determine the min cost req. to buy exactly N bananas.


no_banana=int(input("Enter no. of bananas to be purchased:"))
lot1=int(input("What is size of lot1 that vendor1 provide:"))
price1=int(input("What is price of lot1:"))
lot2=int(input("What is size of lot2 that vendor2 provides:"))
price2=int(input("What is price of lot2:"))

def min_cost(no_banana,lot1,price1,lor2,price2):
    lot_a=no_banana//lot1
    print(f'lot_a:{lot_a}')
    
    lot_b=no_banana//lot2
    print(f'lot_b:{lot_b}')
    
    cost_a=lot_a*price1
    print(f'cost_a:{cost_a}')
    
    cost_b=lot_b*price1
    print(f'cost_b:{cost_b}')
    
    return min(cost_a,cost_b)
min_cost(no_banana,lot1,price1,lot2,price2)
    
####################################################################################################################

    
              
