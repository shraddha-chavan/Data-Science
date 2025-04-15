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



























