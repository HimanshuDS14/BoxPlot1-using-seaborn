import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("iris.csv")
print(data)

sns.boxplot(data = data)
plt.show()

sns.boxplot(data = data )

plt.show()