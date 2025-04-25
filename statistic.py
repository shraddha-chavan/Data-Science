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
#step4:SD
#its the square root of the variance
std_dev=np.std(data)
print("SD:",std_dev)

#######################################################################
#history and math test score from the image
history_scores=[75,72,68,65,67,73]
math_scores=[93,96,43,47,51,90]

def calculate_mad(scores):
    mean=sum(scores)/len(scores)
    mad=sum(abs(x-mean)for x in scores)/len(scores)
    return mad
#calculate MAD
history_mad=calculate_mad(history_scores)
math_mad=calculate_mad(math_scores)

print("Mean Absolute Deviation(MAD):")
print(f"History test:{history_mad:.2f}")
print(f"Math Test:{math_mad:.2f}")

'''👉 Interpretation: Students' performance was 
more consistent in History, while Math scores 
varied widely — possibly indicating that some
 students struggled significantly more than
 others in Math.
 
 👉Strategic Decision:The math scores show a big 
 difference between students, meaning some are 
 doing very well while others are struggling. 
 To fix this, teachers can first find out which 
 topics are hard for students. They should give
 extra help to those who need it and let strong 
 students help others. Using fun methods like games,
 pictures, or real-life examples can make learning easier. 
 Regular small tests can help check understanding early.
 Teachers should also talk to parents for support 
 and encourage students to keep trying, so they 
 feel confident in math again. The goal is to help
 every student improve, not just raise the class average.

'''
##################################################################################
