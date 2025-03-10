# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:31:01 2025

@author: Latitude 5410
"""

    #main.py
from salary import calculate_salary
from validation import validate_experience,validate_role
from display import display_salary
def main():
    try:
        
       name=input("Enter employee name:")
       experience=int(input("Enter year of experience:"))    
       role=input("Enter job role(Intern,Junior,Mid-level,Senior")
   
   #validate inputs
       experience=validate_experience(experience)
       role=validate_role(role)
   
   #Calculate salary
       salary=calculate_salary(experince,role)
   
   #display result
       display_salary(name,experince,role,salary)
       
     expect ValueError as e: 
           print(f"Error:{e}")


       
   
