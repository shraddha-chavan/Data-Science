# Example 1: File Handling (Read CSV)

import pandas as pd

try:
    df = pd.read_csv("data.csv")
    print("File loaded successfully.")
except FileNotFoundError:
    print("Error: The file was not found.")

