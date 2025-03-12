# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:53:21 2025

@author: Latitude 5410
"""
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
    

###Gary is an avid hiker. He tracks his hikes meticulously,
 #paying close attention to small details like topography.
#During his last hike, he took exactly n steps. 
 #For every step he took, he noted if it was an uphill (U) 
 #or a downhill (D) step. Gary’s hikes start and end 
 #at sea level.

#We define the following terms:

#A mountain is a non-empty sequence of consecutive
 #steps above sea level, starting with a step up 
 #from sea level and ending with a step down to sea level.
 #A valley is a non-empty sequence of consecutive
 #steps below sea level, starting with a step down 
 #f#rom sea level and ending with a step up to sea level.
#Given Gary’s sequence of up and down steps 
#during his last hike, find and print the number of valleys
 #he walked through.

#Gary is hiking, and he records each step as either U (uphill) or D (downhill). He always starts and ends at sea level (0 altitude).

#We need to count the number of valleys he walks through.

#What is a valley?
#A valley is when:

#Gary goes below sea level (altitude becomes negative).
#He then comes back to sea level.
#Example Walkthrough
#Let’s say Gary takes the following 8 steps:
#"DDUUUUDD"



def count_valleys(n,path):
    elevation=0# starting at sea level
    valley_count=0#counter for valley
    
    for step in path:
        if step=='U':#going up
           elevation+=1
           if elevation==0:#if we just came back to sea level, a valley ended
             valley_count+=1

        else:
            step=='D'#going down
            elevation-=1
        return valley_count      


#example usage
n=8
path="UDDDUDUU"
print("Totak valley:", count_valleys (n,path))














    
              

    
              
