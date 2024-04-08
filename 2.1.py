import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\fitbit-dataset.csv'
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df.set_index('Date', inplace=True)
attributes = ["Calories", "Minutes_of_slow_activity", "Minutes_of_moderate_activity", "Minutes_of_intense_activity"]

plt.figure(figsize=(11, 5))
for attribute in attributes:
    plt.plot(df.index, df[attribute], label=attribute)

plt.title('Timeseries')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Save the plot as an image file
plot_file_path = r'C:\Users\User\Documents\UNIC_Data_Science\ΕΞΑΜΗΝΑ\ΕΞΑΜΗΝΟ 2\Managing and Visualizing Data\hw-4\plot2.1.png'
plt.savefig(plot_file_path)

plt.show()
