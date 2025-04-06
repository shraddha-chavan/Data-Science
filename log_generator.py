# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:17:17 2025

@author: Latitude 5410
"""

import time
import random

LOG_FILE = "C:/1-python/server.log"
LOG_LEVELS=["INFO","WARNING","ERROR","CRITICAL"]
MESSAGE=["User logged in: user123",
         "High memory usage detector",
         "Database connection failed:timeout",
         "File uploaded:report.pdf",
         "Server crash detected! Restarting...",
         "User logged out:user456",
         ]
def generate_logs():
    """continuously writes logs to a file every 2 seconds"""
    with open(LOG_FILE,"a")as file:
        while True:
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
            log_level = random.choice(LOG_LEVELS)
            message=random.choice(MESSAGE)
            log_entry=f"{timestamp}{log_level}{message}\n"
            file.write(log_entry)
            file.flush()#ensure immediate writing
            print(f"Generated log :{log_entry.strip()}")
            time.sleep(2)#simulate real time logging
            
generate_logs()           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
