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

#correlation heatmap
import numpy as np
import seaborn as sns

corr=df[['Age','Ann_income','Score']].corr()
plt.imshow(corr,cmap='coolwarm',interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=45)
plt.yticks(range(len(corr)),corr.columns)
plt.title("Correlation  Heatmap")
plt.show()

#boxplot
plt.boxplot(df.Age)
plt.title('Boxplot:Age')
plt.show()

plt.boxplot(df.Score)
plt.title('Boxplot:Score')
plt.show()



################################################################################################
#write a python program to draw a line with
#suitable label in the x axis, y axis and a title
import matplotlib.pyplot as plt
x=range(1,50)
y=[value*3 for value in x]
print("Values of x:")
print(*range(1,50 ))
print("Values of y (thrice of x):")
print(y)
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.xlabel('y - axis')
#set a title
plt.title('Draw a line.')
#Display the figure
plt.show()
##################################################################################


#write a python program to draw a line using given axis
# values with suitable label in the x axis , y axis and a title
import matplotlib.pyplot as plt
#x axis values
x=[1,2,3]
#y axis values
y=[2,4,1]
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.xlabel('y - axis')
#set a title
plt.title('Sample graph!.')
#Display the figure
plt.show()

#write a python code to plot 2 or more
#lines with legends differnt widths and colors
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#;line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.xlabel('y - axis')
#set a title
plt.title('Two or more lines with different width and graph.')
#Display the figure
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-width-3')
plt.plot(x2,y2, color='red',linewidth=5,label='line1-width-5')
#show a legend on the plot
plt.show()
plt.legend()
########################################################################

#write  a code where lines with different styles
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#;line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.xlabel('y - axis')
#set a title
plt.title('Two or more lines with different width and graph.')
#Display the figure
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth=5,label='line2-dashed',linestyle='dashed')
#show a legend on the plot
plt.show()
plt.legend()
########################################################################

#write a python code to plot 2 or more lines and set the line marker
import matplotlib.pyplot as plt
#x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
#set the y-limits of the current axes
plt.ylim(1,8)
#set the x-limits of the current axes
plt.xlim(1,8)
#naming the x axis
plt.xlabel('x-axis')
#naming the y axis
plt.ylabel('y-axis')
#giving title to my graph
plt.title('Display marker')
#function to show plot
plt.show()
#######################################################################

#Write a python code to plot several lines
#with different format styles in one command using arrays
import numpy as np
import matplotlib.pyplot as plt

#sampled time at 200ms intervals
t=np.arange(0.,5.,0.2)

#green dashes,blue sqaures and red triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
'''x=t,y=t
'g--'=green (g)dashed line(--)
plot a diagonal dashed green line (y=x)

t,t**2,'bs'
x=t,y=t**2(sqaures)
'bs'=blue(b)sqaures (s) as markers
plots t sqaure as blue sqaure

t,t**3,'r^'
x=t,y=t**3(cubes)
'r^'=red(r)triangle-up markers(^)
plots t cube as a red triangles
'''
plt.show()
#####################################################################################################

#use of plt.xticks
import matplotlib.pyplot as plt
x_pos=[0,1,2,3]
x=['Apple','Banana','Mango','Orange']
plt.bar(x_pos,[10,15,7,12])
plt.xticks(x_pos,x)
plt.ylabel('Quantity')
plt.title('Fruit Stock')
plt.show()

##########################################################################################################
#write python code to display bar chart
#of popularity of programming languages
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
'''The code creates:
- `x`: List of programming languages.
- `popularity`: List of their popularity percentages.
- `x_pos`: List of positions `[0, 1, 2, 3, 4, 5]`, 
   representing the index of each language in `x`.

This helps in plotting their popularity in a graph, like a bar chart.
'''

plt.bar(x_pos,popularity,color='blue')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of Programming languages\n"+"worlwide , oct 2017 ")
plt.xticks(x_pos,x)
plt.show()
#########################################################################


#write python code to display horizontal bar chart
#of popularity of programming languages
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
'''The code creates:
- `x`: List of programming languages.
- `popularity`: List of their popularity percentages.
- `x_pos`: List of positions `[0, 1, 2, 3, 4, 5]`, 
   representing the index of each language in `x`.

This helps in plotting their popularity in a graph, like a bar chart.
'''

plt.barh(x_pos,popularity,color='green')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of Programming languages\n"+"worlwide , oct 2017 ")
plt.yticks(x_pos,x)
plt.show()
#########################################################################

#write a python code to craete bar plot of scores by group
# and gender use multiple 
import numpy as np
import matplotlib.pyplot as plt
#data to plot
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)
#create a plot
fig,ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1=plt.bar(index,men_means,bar_width,alpha=opacity,color='g',label='Men')
rects2=plt.bar(index+bar_width,women_means,bar_width,alpha=opacity,color='r',label='Women')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.xlabel('Scores by Person')
plt.xticks(index + bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()







































