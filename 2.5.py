import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\fitbit-dataset.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.set_index('Date', inplace=True)

df['total_activity'] = df['Minutes_of_slow_activity'] + df['Minutes_of_moderate_activity'] + df['Minutes_of_intense_activity']

plt.figure(figsize=(11, 5))
plt.plot(df.index, df['total_activity'], label='Total Activity', color='orange')
plt.title('Time Series of Total Activity')
plt.xlabel('Date')
plt.ylabel('Total Activity')
plt.legend()
plt.grid(True)

plot_file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\plot2.5.png'
plt.savefig(plot_file_path)

plt.show()
