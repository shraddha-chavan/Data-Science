import pandas as pd
import numpy as np
###############################
df = pd.read_csv("C:/3-python statistic/income.csv")
df
###############################
df=df.rename({"Monthly Income ($)":"income"},axis=1)
############################
df.income.describe()
#########################
df.income.quantile(0)
##############################
df.income.quantile(0.75)
df
#for inserting null value
df['income'][3]=np.NaN
df
############################
