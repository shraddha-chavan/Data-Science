# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:39:41 2025

@author: Latitude 5410
"""

def validate_experience(exp):
    if not isinstane(exp,int)or exp<0:
        raise ValueError("Experince must be a non-negative integer")
    return exp
def validate_role(role):
    if role not in valid_roles:
        raise ValueError(f"Invalid role Choose from {valid_role}")
    