#create pandas dataframe from list
import pandas as pd
technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"],]
df=pd.DataFrame(technologies)
print(df)


