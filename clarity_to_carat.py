import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the file and create a dataframe
dataframe = pd.read_csv(r'/Users/nnamdi/Documents/Data project/diamonds.csv')

print(dataframe.head(10))
print('Done')

#Calculate the sum price of all the diamonds
sum = dataframe.price.sum()
print(f"The total Value of Diamonds is : {sum:,}$")

#Calculate the mean price of all diamonds
mean = dataframe.price.mean()
print(f"The mean Value of Diamonds is : {mean:,.2f}$")

#Get extra info about carat in diamonds
describe = dataframe.carat.describe()
print(describe)


#visualize the data
#the clarity compared to the size,
# IF , VVS1, VVS2, VS1, VS2,SI1, I1 (from the purest to the least pure)

carat = dataframe.carat
clarity = dataframe.clarity

plt.scatter(clarity, carat)
plt.title('Diamond clarity compared to size in carat')
plt.xlabel('Clarity')
plt.ylabel('Carat')
plt.savefig("claritytocarat1.png")