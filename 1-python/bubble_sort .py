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
def second_largest_element(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[2,4,5,6,3]
print(second_largest_element(lst))
print(lst[-2])

#finding second smallest element in the sorted array
def second_smallest_element(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[2,4,5,6,3]
print(second_smallest_element(lst))
print(lst[1])

#finding second largest number in an array for duplicate values
#for smallest print unique_nums[-2]
def second_largest_element(lst):
    unique_nums=list(set(lst))#list is converted in to set
    unique_nums.sort(reverse=True)#it is comverted back into a list
    # the sort (reverse = true)method in python sorts
    #a list in desending order(from highest to lowest)
    if len(unique_nums)>1:
        
        return unique_nums[1]
    else:
        return None
lst=[10,20,40,53,99]
print("Second largest:", second_largest_element(lst))    


#for smallest print unique_nums[-2]
#finding second smallest element in an sorted array
def second_smallest_element(lst):
    unique_nums=list(set(lst))#list is converted in to set
    unique_nums.sort(reverse=True)#it is comverted back into a list
    # the sort (reverse = true)method in python sorts
    #a list in desending order(from highest to lowest)
    if len(unique_nums)>1:
        
        return unique_nums[-2]
    else:
        return None
lst=[10,20,40,53,99]
print("Second smallest:", second_smallest_element(lst))    












 
           
    
    
