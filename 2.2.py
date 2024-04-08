import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\fitbit-dataset.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.set_index('Date', inplace=True)

week_calories = df['Calories'].resample('W').sum()

plot_file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\plot2.2.png'
plt.savefig(plot_file_path)

plt.figure(figsize=(11, 5))
plt.plot(week_calories.index, week_calories, label='Weekly Calories', color='blue')
plt.title('Weekly Calories')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.legend()
plt.grid(True)
plt.show()