import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\fitbit-dataset.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.set_index('Date', inplace=True)

window_sizes = [3, 5, 7, 10, 15]
rolling_means = {}
for window_size in window_sizes:
    rolling_means[window_size] = df['Calories'].rolling(window=window_size).mean()

plt.figure(figsize=(13, 9))

plt.plot(df.index, df['Calories'], label='Original', color='blue')

for window_size, rolling_mean in rolling_means.items():
    plt.plot(df.index, rolling_mean, label=f'Rolling Mean for {window_size} days')



plt.title('Time Series with Rolling Means')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.legend()
plt.grid(True)

plot_file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\plot2.4.png'
plt.savefig(plot_file_path)
plt.show()
