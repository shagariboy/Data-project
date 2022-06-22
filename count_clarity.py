import matplotlib.pyplot as plt
import pandas as pd


#count the number of Diamonds for each Clarity Type

#Read the file and create a dataframe with pandas
df = pd.read_csv(r'/Users/nnamdi/Documents/Data project/diamonds.csv')


#count the number for each type of clarity using value_counts index and values
clarityind = df.clarity.value_counts().index.tolist()
claritycount = df.clarity.value_counts().values


#visualize them iwith matplotlib
# IF , VVS1, VVS2, VS1, VS2,SI1, I1 (from the purest to the least pure)
plt.bar(clarityind, claritycount)
plt.title('Distribution of Diamonds according to their clarity')
plt.xlabel('Clarity')
plt.ylabel('Number of Diamonds')
plt.savefig("countClarity2.png")