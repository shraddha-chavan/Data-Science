##############################################################################################
#1. Heatmap of Correlation Matrix 

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
corr_matrix = iris.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')#heatmap
plt.title("Correlation Matrix Heatmap - Iris Dataset")
plt.show()
################################################################################################
#2. Box Plot of Test Scores by School

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data =({
    'score': [78, 85, 90, 88, 76, 95, 92, 89, 84, 80, 70, 60],
    'school': ['school1', 'school1', 'school1', 'school2', 'school2', 'school2', 'school3', 'school3', 'school3', 'school1', 'school2', 'school3']
})
df = pd.DataFrame(data)

# Box plot
sns.boxplot(x='school', y='score', data=df)
plt.title("Test score distribution by school")
plt.show()

#takeaway: here school2 have good test score
# distribution than school1 and school2 so to increase the school
# distribution.
#we should focus on the lacking points of the students of school1
# and school2 
#also we should take extra clasees for students who are afraid of test


#########################################################################################################
#3. Bar Chart of Product Sales by Category

categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
sales = [150, 200, 300, 120, 90]
colors = ['blue', 'green', 'orange', 'red', 'pink']

plt.bar(categories, sales, color=colors)

for i, val in enumerate(sales):
    plt.text(i, val + 5, str(val), ha='center')

plt.xlabel("Categories")
plt.ylabel("units sold")
plt.title("product sales")
plt.xticks(rotation=35)
plt.show()
#takeaway: groceries have more number of sales so we should increase the quantity 
#of groceries compare to others and also focus that why other products are
#not sales yet.
#########################################################################################################
#4. Line Chart of Monthly Average Temperature

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [4, 16, 9, 14, 18, 22, 25, 24, 20, 15, 19, 15]

plt.plot(months, temperatures, linestyle='--', marker='o', color='blue')
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
#takeaway:here we can say the monthly average temperature of june,july,august
#september is stable or we can say it is average.
######################################################################################################

#5. Scatter Plot 
tips =sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", size="size", sizes=(20, 20))
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()
plt.show()
sns.scatterplot(data=tips,x="total_bills",)
####################################################################################################
