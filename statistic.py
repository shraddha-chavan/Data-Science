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
#usecase
import math
#sample dataset1
scores_1 = [75,72,68,67,73]
#sample dataset2
scores_2 = [83,70,70,63,70,70]

def calculate_standard_deviation(scores):
    mean=sum(scores)/len(scores)
    squared_diffs=[(x-mean)**2 for x in scores]
    variance=sum(squared_diffs)/len(scores)
    std_dev=math.sqrt(variance)
    return std_dev

#calculate SD
std_dev_1=calculate_standard_deviation(scores_1)
std_dev_2=calculate_standard_deviation(scores_2)

print("SD(Population):")
print(f"Dataset 1:{std_dev_1:2f}")
print(f"Dataset 2:{std_dev_2:2f}")

'''
📌 Takeaway:
Dataset 1 scores are closer to the average, 
meaning students performed more consistently.
 Dataset 2 scores vary more, even though many
 students scored 70, a few scored much higher or lower, 
 which pulled the SD up. This means some students 
 in Dataset 2 are either struggling or doing much 
 better than the rest.

🎯 Strategic Decision:
For Dataset 2, the teacher should look closely at 
students scoring much higher or lower than the rest. 
The ones scoring low may need extra help, while high 
scorers can be given challenging tasks to keep them
 engaged. The teacher should aim to reduce this gap by 
 offering support where needed and encouraging all 
 students to reach a more balanced performance level.

'''
########################################################################
import numpy as np
#original weights
original_weights=[105,156,145,172,100]
#add 5 pounds for winter clothing
adjusted_weights=[weight+5 for weight in original_weights]
#calculate  mean nd SD
mean_original=np.mean(original_weights)
std_original=np.std(original_weights,ddof=1)
mean_adjusted=np.mean(adjusted_weights)
std_adjusted=np.std(adjusted_weights,ddof=1)
'''
ddof=1 in np.std()



'''

###################################################################################################
import numpy as np
#original data
weights=[105,156,145,172,100]
#water formula:(weight*2.5)+750
water_intake=[(w*2.5)+750 for w in weights]
#calculate original states
mean_weight=np.mean(weights)
std_weight=np.std(weights,ddof=1)
#calculate new states
mean_water=mean_weight*2.5+7.5
std_water=std_weight*2.5
print(f"original mean weight:{mean_weight:.2f},originalstd Dev:{std_weight:.2f}")
print(f'mean water intake:{mean_water:.2f} ml')
print(f'std Dev of water intake:{std_water:.2f}ml')

#######################################################################################################
import numpy as np
import pylab
import scipy.stats as stats

measurements=np.random.normal(loc=20,scale=5,size=100)
stats.probplot(measurements,dist='norm',plot=pylab)
pylab.show()
#######################################################################################################

