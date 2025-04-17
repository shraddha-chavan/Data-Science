# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:03:34 2025

@author: Latitude 5410
"""

######################################################################################  
#for numerical data the catogorical plots used are
#heatmark
#histogram
#joint plot
#box plot
#these are used for 
#EDA=exploratory data analysis

#when the graph is decreasing from left to right is called as 
#positively skewed or right skewed 
#vice versa for left skewed or negatively skewed 
#bell shaped data called as symetrical normally distributed data
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
sns.displot(tips.total_bill,kde=True)
sns.displot(tips.tip,kde=True)
#size
#numerical continues data== its a float values data
#numerical descrit data==> int data
#sns.displot(tips.size,kde=True)

######################################################################################  
#scatter plot 
#it also give histogram on opposit of the axis
sns.jointplot(x=tips.tip,y=tips.total_bill) 

#to show the linearity of graph
#positively linaer=line from  middle              
#vice versa for negative linearity
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')
#give scatter plot in hexagonal shape
#all plots
sns.pairplot(tips,kind='reg')#gives line
#but only fr scatter not to bar graph
''' we have to define corelation b2in the values in x and y '''


######################################################################################  
#catogorical data
#Categorical data refers to information that can be divided into 
#distinct groups or categories. These categories are 
#usually labels rather than numerical values.
'''Types of Categorical Data
- Nominal Data – Categories without any inherent order.- Examples: Colors (Red, Blue, Green), Cities (Delhi, Mumbai, Chennai), Types of fruits (Apple, Banana, Mango).

- Ordinal Data – Categories with a meaningful order or ranking.- Examples: Customer satisfaction levels (Low, Medium, High), Education qualifications (High School, Bachelor’s, Master’s), Clothing sizes (Small, Medium, Large).

'''

tips.time.value_counts()
sns.pairplot(tips,hue='time')
#colcusion is that the in dinner there is more orders and they are having 
#higher bills than lunch so this is bcz of party's which where happening at dinner time
sns.pairplot(tips,hue='day')
#it show the no of bills ccomes per day
#here we are using day as catogorical data
sns.heatmap(tips.corr(numeric_only=True),annot=True)#shows correlations
#ranges from -1 to +1
#understand correlation coefficient
####################################################################################
#boxplot
sns.boxplot(tips.total_bill)#there are outliers in total_bill
sns.boxplot(tips.tip)
sns.countplot(tips.day)
sns.countplot(tips.sex)
tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')
sns.countplot(data=tips[tips.time=='Dinner'],x='day')
sns.countplot(data=tips[tips.time=='Lunch'],x='day')



'''
1. **Dinner Insights**:
   - Typically, the number of customers is higher
   during dinner compared to lunch.
   - Certain days, like Friday or Saturday, might show 
   a peak in counts, indicating busier evenings.

2. **Lunch Insights**:
   - Lunch counts are generally lower than dinner.
   - Weekdays like Thursday or Friday might have more activity,
   possibly due to workday lunch breaks.
   

'''
fg=sns.FacetGrid(tips,row='smoker',col='time')
fg.map(sns.histplot,'total_bill')
'''this is a facet grid histrograms showing the
 distribution of total bills acrosss different 
 smoking statuses and time of day (lunch vs dinner)
 top-left:smokers during lunch
 top=right:smokes during dinner
 bottom-left:non-smokers during lunch
 bottom-right:non-smokers during dinner
 smokers vs non-smokers
 



'''


















######################################################################################  
#line plot
sns.lineplot(x=tips.tip,y=tips.total_bill) 
sns.barplot(x=tips.tip,y=tips.total_bill) 

# Example using Matplotlib
plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()

#######################################################################################

#usecases:example
import pandas as pd
df=pd.read_csv("C:/2-python_ds/Salary_Data.csv")
df.dtypes
df.columns
df.columns.values
df.index
df['Price']
df[['Price','Rooms']]
df2=df[6:]
df.describe()
df2=df.rename({'Years of Experience':'yoe'},axis=1)
df2
df['Price']=df['Price']-1000
df.shape
##
import matplotlib.pyplot as plt
import seaborn as sns
#1)
sns.displot(df.age,kde=True)
sns.displot(df.Gender,kde=False)
#2)
sns.jointplot(x=df2.Salary,y=df2.yoe,kind='hex') 
#3)
sns.pairplot(df2,kind='yoe')
#4)
sns.heatmap(df2.corr(numeric_only=True),annot=True)
#5)
sns.boxplot(df2.Age)
sns.boxplot(df2.Gender)
sns.countplot(df2.Salary)
sns.countplot(df2.Gender)

def maximize_efficiency(N, efficiencies):
    if N < 5:
        return format(0, ".5f")
    
    components_to_keep = []
    
    # Divide efficiencies into groups of 5 and handle each group
    for i in range(0, N, 5):
        group = efficiencies[i:i+5]
        group.sort()  # Sort to find the least efficient component
        components_to_keep.extend(group[1:])  # Keep the top 4 components from the group
    
    # Calculate the average of the kept components
    average_efficiency = sum(components_to_keep) / len(components_to_keep)
    
    return format(average_efficiency, ".5f")

# User Input Section
try:
    N = int(input("Enter the number of components (N): "))
    if N % 5 != 0:
        print("Error: The number of components must be a multiple of 5.")
    else:
        efficiencies = list(map(int, input("Enter the efficiencies, separated by spaces: ").split()))
        if len(efficiencies) != N:
            print("Error: Number of efficiency values does not match the specified N.")
        else:
            result = maximize_efficiency(N, efficiencies)
            print("The highest possible average efficiency is:", result)
except ValueError:
    print("Invalid input. Please enter integers only.")


#usecase:fdata
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#load and rename columns
df=pd.read_csv('C:/Users/Latitude 5410/Downloads/Mall_Customers.csv')
df.columns=['cust_id','Genre','Age','Ann_income','Score']


#basic histogram
#age distribution
plt.hist(df.Age,bins=10,alpha=0.7,edgecolor='red')
#here alpha is for color transparency of graph color,
#bins is the rows how many rows should there 
#if 5 then in graph there is 5 rows
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
#annual income distribution
plt.hist(df.Ann_income,bins=10,alpha=0.7,edgecolor='black')
plt.title('Annual Income Distribution')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Frequency')
plt.show()


#spending score distribution
plt.hist(df.Score,bins=10,alpha=0.7,edgecolor='black')
plt.title('Spending Score Distribution')
plt.xlabel('Spending Score')
plt.ylabel('Frequency')
plt.show()
#scatter plots(replacing jointplots)
plt.scatter(df.Age,df.Score,alpha=0.6,color='red')
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()
corr=df.corr(numeric_only=True)

#scatter plot with regression line
from numpy.polynomial.polynomial import polyfit
x=df.Age
y=df.Score
b,m=polyfit(x,y,1)#1 is degree of polynomial
plt.scatter(x,y,alpha=0.5)
plt.plot(x,m*x+b,color='red')#here is line equation
plt.title('Age vs Score with Trend Line')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()
#pairwise scatter matrix (subset of features)
pd.plotting.scatter_matrix(df[['Age','Ann_income','Score']],figsize=(10,10))
#here figsize is the dimensions means weight & height 
plt.suptitle('Pairwise Sctter Mtrix')
plt.show()

#Gender distribution
gender_counts=df.Genre.value_counts()

#pie chart
gender_counts.plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.title('Gendre Distribution')
plt.show()

#bar chart
gender_counts.plot(kind='bar',color=['skyblue','salmon'])
plt.title('Gendre Count')
plt.ylabel('Count')
plt.show()






















