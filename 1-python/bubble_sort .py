# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:12:22 2025

@author: Latitude 5410
"""

def bubble_sort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[2,4,5,6,3]
print(bubble_sort(lst))

#finding second largest element in the sorted array
def bubble_sort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[2,4,5,6,3]
print(bubble_sort(lst))
print(lst[-2])
 
           
    
    
