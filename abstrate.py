# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:44:30 2025

@author: Latitude 5410
"""

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius*self.radius
##usage example
Circle1=Circle(5)
print("Area of circle:",Circle1.area())    
