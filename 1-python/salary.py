# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:29:18 2025

@author: Latitude 5410
"""

def calculate_salary(experince,role):
    base_salary={
        "Intern":30000,
        "Junior":50000,
        "Mid-level":80000,
        "Senior":120000,
        "Manager":150000
        }
    if role not in base_salary:
        raise ValueError("Invalid job role")
        return base_salary[role]+(experience*2000)
    