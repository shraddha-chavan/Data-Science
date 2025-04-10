# Example 1: File Handling (Read CSV)

import pandas as pd

try:
    df = pd.read_csv("data.csv")
    print("File loaded successfully.")
except FileNotFoundError:
    print("Error: The file was not found.")

# Example 2: Data Type Conversion
data = {"age": ["25", "thirty", "40"]}
import pandas as pd

df = pd.DataFrame(data)

try:
    df["age"] = df["age"].astype(int)
except ValueError as e:
    print("Data conversion error:", e)
