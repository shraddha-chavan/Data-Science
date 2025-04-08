#create pandas dataframe from list
import pandas as pd
technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"],]
df=pd.DataFrame(technologies)
print(df)

#add column & rows label to the dataframe
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

#################################
df.dtypes#In pandas,  is an attribute used to find out the 
#data type of each column in a DataFrame or Series. 
#It is especially useful for checking the type of data 
#you're working with, such as integers, floats, strings, 
#or more specific pandas types like .


###################################


#set custom types to dataframe
types={'Couses':str,'Fee':float,'Duration':str}
df.dtypes


##creates dataframe from dictionary
technologies={'Courses':["Shraddha","Sunil","Chavan"],
              'Fee':[20000,22000,24000],
              'Duration':['10days','20days','30days'],
              'Discount':[100,200,300]
              }

df=pd.DataFrame(technologies)
df


#convert dataframe to csv
df.to_csv('data_file.csv')

#creates dataframe from csv file
df=pd.read_csv('data_file.csv')


##creates dataframe from CSV file
def_new=pd.read_csv('data_file.csv')
df_new=pd.read_csv('C:/1-python/data_file.csv')


##create dataframe with none/null to work with example
import pandas as pd
import numpy as np
technologies=({'Courses':["Shraddha","Sunil","Chavan","Pandas",None,"Python","Pandas","Java"],
               'Fee':[200,220,230,240,np.nan,250,260,270],
               'Duration':['10days','20days','30days','40days','50days','60days',' ','80days'],
               'Discount':[100,120,130,140,150,160,170,180]})

row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

##################################################
#DataFrame properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.indexdf.types

##Accessing one column contents
df['Fee'] 
#Accessing two columns contents
df[{'Fee','Duration'}]


#select certain rows and assign it to another dataframe
df2=df[6:]
df2

#accessing certain cell from the dataframe column
df['Duration'[3]]

#substrating specific value from a column
df['Fee']=df['Fee']-50
df['Fee']

#describe dataframe :: Gives a summary of your data, such as average,
# minimum, maximum, and other statistics
# (only for numeric data by default).
df.describe()#it shows 5 number summary

#rename()-Renames  pandas dataframe columns
df=pd.DataFrame(technologies,index=row_labels)

#Assign new header by setting new columns names
df.column=['A','B','C','D']
df

