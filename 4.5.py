import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a DataFrame
file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\cereals.csv'
df = pd.read_csv(file_path)

# Map shelf codes to their respective meanings
shelf_mapping = {1: 'Low', 2: 'Medium', 3: 'High'}
df['Shelf'] = df['Shelf'].map(shelf_mapping)

# Create a box plot
plt.figure(figsize=(11, 7))
sns.boxplot(data=df, x='Shelf', y='Sugars', palette='Oranges')
plt.title('Relation between placement and sugar')
plt.xlabel('Shelf Placement')
plt.ylabel('Sugars')
plt.tight_layout()

plt.savefig(r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\FifhtPlot.png')

# Display the plot
plt.show()
