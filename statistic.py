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
df.income.mean()
###################for mean
df_new=df.fillna(df.income.mean())
df_new
##################for median
df_new=df.fillna(df.income.median())
df_new
############################################################################

import numpy as np
#sample dataset
data = [10,12,23,23,16,23,21,16]
print("Original Data:",data)


#step1:mean of the data
mean=np.mean(data)
print("\nMean (Average):",mean)

#step2:mean absolute deviation(MAD)
#Its the average of absolute deviations from the mean
mad = np.mean([abs(x-mean)for x in data])
print("Mean Absolute Deviation(MAD):",mad)

#step3:Variance
#its the average of square differnce from the mean
variance=np.var(data)
print("Variance:",variance)
