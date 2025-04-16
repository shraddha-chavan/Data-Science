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
#Drop dataframe rows and columns
df = pd.DataFrame(technologies,index=row_labels)

#drops rows  by labels
df1 = df.drop(['r1','r2'])
df1
df=pd.DataFrame(technologies,index=row_labels)

#delete rows by position
df1=df.drop(df.index[[1,3]])

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when you have given default indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3])#it willl delete row0 n row3
df1=df.drop(range(0,2))#it will delete 0 n 1


##example
#select rows by integer index
df2=df.iloc[2]#select row by index
df2=df.iloc[[2,3,6]]#select row by index list
df2=df.iloc[1:5]#select row by integer index range
df2=df.iloc[:1]#select 1st row
df2=df.iloc[:3]#select 1st 3 rows
df2=df.iloc[-1:]#select last row
df2=df.iloc[-3]#select last 3 rows
df2=df.iloc[::2]#select alternate rows

#select rows by index labels
df2=df.loc['r2']#select row by index label
df2=df.loc[['r2','r3','r6']]#select row by index label
df2=df.loc['r1':'r5']#select row by label index range
df2=df.loc['r1':'r5':2]#select alternative row by index 


#pandas select columns by name of index
#by using df[] notation
df2=df['Courses']
#select multiple columns
df2=df.loc[:,['Courses','Fee','Duration']]
#select columns between 2 columns
df2=df.loc[:,'Fee':'Discount']
#select column by range
df2=df.loc[:,'Duration':]
#select every alternate column
df2=df.loc[:,::2]

#delete rows with Nan,None,Null values
import pandas as pd
import numpy as np
technologies={'Courses':["Spark","PySpark","Hadoop","Python"],
              'Fee':[20000,25000,26000,22000],
              'Duration':['','40days',np.nan,None],
              'Discount':[1000,2300,1500,1200]
              }

indexes=['r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=indexes)
print(df)
df=pd.DataFrame(technologies,index=indexes)
df2=df.dropna()
print(df2)

#How to clean empty string
#first drop rows with Nan (np.nan and None
df_clean=df.dropna(subset=['Duration'])

#Then drop rows with empty strings
df_clean=df_clean[df_clean['Duration'] !='']
print(df_clean)


#Change all columns to same type in pandas
#df.astype(str)converts all columns of pandas DataFrame
df=df.astype(str)
print(df.dtypes)

#Changing type for one or multiple columns in pandas
#changing type for one or multipple columns
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

##convert data types for all columns in a list
df=pd.DataFrame(technologies)
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#By using a loop
for col in ['Fee','Discount']:
    df[col]=df[col].astype('float')


#Raise or ignore error when convert colun type fail
df=df.astype({"Courses":int},errors='ignore')
df.dtypes
#generate error
df=df.astype({"Courses":int},errors='raise')

#convert feed column to numeric type
df['Fee']=pd.to_numeric(df['Fee'])
print(df.dtypes)

#convert fee and discount to numeric type
df=pd.DataFrame(technologies)
df.dtypes
df[['Fee','Discount']]=df[['Fee','Discount']].apply(pd.to_numeric)
print(df.dtypes)

#quick example of get the number of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count

#using dataframe .apply()to apply function add column
import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])
print(df)

def add_3(x):
    return x+3
def2=df.apply(add_3)
df2



##using apply function single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]
df=pd.DataFrame(data,columns=['A','B','C'])
#apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_3)
df=pd.DataFrame(data,columns=['A','B','C'])
#apply a lambda function to each colum
df2=df.apply(lambda x:x+10)


#apply lambda function to single column
df["A"]=df["A"].apply(lambda x:x-2)
print(df)

#using pandas.dataframe.transform()
#to apply function  column
#using dataframe.transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)


#using pandas.dataframe.map() to single column
df['A']=df['A'].map(lambda A:A/2)
print(df)

import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])
print(df)
#using numpy function on single column
#using dataframe.apply()&[]operator
df['A']=df['A'].apply(np.square)
print(df)
'''df['C']=df['C'].apply(np.square)
print(df)'''


#Pandas groupby()with example
import pandas as pd
technologies=({'Courses':["shraddha","samu","teju","rutu","goti","goti","kittu","laduu","NA"],
               'Fee':[200,210,220,230,240,250,260,270,280],
               'Duration':['1days','2days','3days','4days','5days','6days','7days','8days','9days'],
               'Discount':[10,20,30,40,50,60,70,80,90]})
df=pd.DataFrame(technologies)
print(df)

#use groupby()  to compute the sum
df2=df.groupby(['Courses']).sum()
print(df2)

#use groupby()  to compute the sum of multiple
df2=df.groupby(['Courses','Duration']).sum()
print(df2)



#Add index to grouped data
#add row index to the group by result:
df2=df.groupby(['Courses','Duration']).sum


#########################################################
    

#get the list of all column names from header
column_headers=list(df.columns.values)
print("The column Header:",column_headers)

#using list(df) to get column headers as a list
column_headers=list(df.columns)
column_headers

#using list(df)to get the list of all column names
column_headers=list(df)
column_headers

#pandas shuffle dataframe rows
import pandas as pd
technologies=({'Courses':["shraddha","samu","teju","rutu","goti","goti","kittu","laduu","NA"],
               'Fee':[200,210,220,230,240,250,260,270,280],
               'Duration':['1days','2days','3days','4days','5days','6days','7days','8days','9days'],
               'Discount':[10,20,30,40,50,60,70,80,90]})
df=pd.DataFrame(technologies)
print(df)

#shuffle the dataframe row and return all rows
df1=df.sample(frac=1)
print(df1)

#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)


#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)

#########################################################################
import pandas as pd
technologies={'Courses':["Spark","PySpark","Python","pandas"],
              'Fee':[20000,25000,22000,30000],
              'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]}

index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)

#pandas join
df3=df1.join(df2,lsuffix="left",rsuffix="_right")
print(df3)

'''output: 
    Coursesleft    Fee Duration Courses_right  Discount
 r1       Spark  20000   30days         Spark    2000.0
 r2     PySpark  25000   40days           NaN       NaN
 r3      Python  22000   35days        Python    1200.0
 r4      pandas  30000   50days           NaN       NaN '''
 
 

# pandas inner join dataframe 
df3=df1.join(df2,lsuffix="left",rsuffix="_right",how='inner')
print(df3)
'''output: 
    Coursesleft    Fee Duration Courses_right  Discount
 r1       Spark  20000   30days         Spark      2000
 r3      Python  22000   35days        Python      1200'''
 
 
 
# pandas right join dataframe 
df3=df1.join(df2,lsuffix="left",rsuffix="_right",how='right')
print(df3)
'''output: 
   Coursesleft      Fee Duration Courses_right  Discount
r1       Spark  20000.0   30days         Spark      2000
r6         NaN      NaN      NaN          Java      2300
r3      Python  22000.0   35days        Python      1200
r5         NaN      NaN      NaN            Go      2000'''

#using pandas.merge()
df3=pd.merge(df1,df2)

#################################################################
# concatenate multiple dataframes 
import pandas as pd
df=pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
              'Fee':[20000,25000,22000,24000]} )             

df1=pd.DataFrame({'Courses':["Unix","Hadoop","Hypersion","Java"],
              'Fee':[25000,25200,24500,24900]} )             

df2=pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
              'Discount':[1000,2300,2500,2000,3000]} )             


df3=pd.concat([df,df1,df2])
print(df3)


#read the data
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head())


#2. Create DataFrame and display info

import pandas as pd
data=({'Name':['Alice','Bob','Charlie','David','Eva'],
       'Age':[25,30,35,45,28],
       'Depaetment':['HR','IT','Finance','IT','HR'],
       'Joining_year':[2018,2016,2015,2019,2020]})

df=pd.DataFrame(data)#creating a dataframe
print(df.head(2)) #the first 2 rows

'''   output:    Name  Age Depaetment  Joining_year
             0  Alice   25         HR          2018
             1    Bob   30         IT          2016'''

print(df.columns.tolist())#the columns names

'''output:['Name', 'Age', 'Depaetment', 'Joining_year']'''

print(df.dtypes)#data type of each column

'''output:Name            object
          Age              int64
         Depaetment      object
         Joining_year     int64
         dtype: object'''

print(df.describe())#summary statistics for numeric columns

'''output:                        Age      Joining_year
                       count   5.000000      5.000000
                       mean   32.600000   2017.600000
                       std     7.829432      2.073644
                       min    25.000000   2015.000000
                       25%    28.000000   2016.000000
                       50%    30.000000   2018.000000
                       75%    35.000000   2019.000000
                       max    45.000000   2020.000000'''



############################################################################################
#3. Extend the DataFrame

import pandas as pd

#Create the data
data = ({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 45, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining_Year': [2018, 2016, 2015, 2019, 2020]
})

df = pd.DataFrame(data)
# Add Salary
df['Salary'] = [50000, 60000, 70000, 65000, 48000]

# Add Experience
df['Experience'] = 2025 - df['Joining_Year']

#  Add Seniority
seniority = []

for exp in df['Experience']:
    if exp < 5:
        seniority.append('Junior')
    elif exp < 8:
        seniority.append('Mid')
    else:
        seniority.append('Senior')

df['Seniority'] = seniority
print(df)





































































































