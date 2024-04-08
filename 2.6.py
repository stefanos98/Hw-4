import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\fitbit-dataset.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.set_index('Date', inplace=True)

df['total_activity'] = df['Minutes_of_slow_activity'] + df['Minutes_of_moderate_activity'] + df['Minutes_of_intense_activity']

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['total_activity'], label='Total Activity', color='black')
plt.plot(df.index, df['Calories'], label='Calories', color='red')
plt.title('Total Activity and Calories')
plt.xlabel('Date')
plt.ylabel('Activity level and kcal')
plt.legend()
plt.grid(True)

plot_file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\plot2.6.png'
plt.savefig(plot_file_path)

plt.show()
