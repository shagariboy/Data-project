import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read the file and create a dataframe with pandas
df = pd.read_csv(r'/Users/nnamdi/Documents/Data project/diamonds.csv')

#Count the number of Diamonds for each color
colorind = df.color.value_counts().index.tolist()
colorcount = df.color.value_counts().values.tolist()


#visualize this with a bar plot
# Note that D is the best color and J is the worst
plt.bar(colorind, colorcount)
plt.title('Distribution of Diamonds according to their clarity')
plt.xlabel('Color')
plt.ylabel('Number of Diamonds')
plt.savefig("countcolors3.png")