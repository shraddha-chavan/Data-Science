# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:38:30 2025

@author: Latitude 5410
"""

#Polymorphism

#Polymorphism in Python is the ability of objects or
# methods to take on different forms based on their context. 
#It allows the same function or operation to work with 
#different types of objects. For instance,
# a method like  can behave differently for a  
#class (printing "Woof!") and a  class (printing "Meow!") 
#through method overriding. Similarly,
# Python supports operator overloading, enabling operators like
#  to perform customized actions for objects,
# such as adding two  objects. Another form, duck typing, 
#lets objects be used based on their behavior rather than 
#their class type—for example, calling a  method on any object 
#that implements it, whether it's a  or an . Polymorphism enhances
# flexibility and reusability in code, making it 
#easier to handle diverse scenarios with clean and adaptable designs.
class Cat:
    def speak(self):
        print("Meow")
animals=[Dog(),Cat()]
for animal in animals:
          animal.speak()
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
