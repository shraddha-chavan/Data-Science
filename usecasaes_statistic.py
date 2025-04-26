##############################################################################################
#1. Heatmap of Correlation Matrix 

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
corr_matrix = iris.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')#heatmap
plt.title("Correlation Matrix Heatmap - Iris Dataset")
plt.show()

