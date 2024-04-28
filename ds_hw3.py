import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#(a)
df = pd.read_csv('Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv')
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
weekdays = df[df['hour_beginning'].dt.dayofweek < 5]
grouped = weekdays.groupby(weekdays['hour_beginning'].dt.dayofweek)['Pedestrians'].sum()
weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

plt.figure(figsize=(10, 6))
plt.plot(weekdays_list, grouped)
plt.title('Pedestrian Counts by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.show()

#(b)
df_2019 = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]
counts_by_weather = df_2019.groupby('weather_summary')['Pedestrians'].sum().reset_index()
pedestrian_pivot = df_2019.pivot_table(index='hour_beginning', columns='weather_summary', values='Pedestrians', aggfunc='sum')
correlation_matrix = pedestrian_pivot.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix: Weather vs Pedestrian Counts')
plt.show()

#(c)
hour = 4
if 0 <= hour < 6:
        categorize_time = 'Night'
elif 6 <= hour < 12:
        categorize_time ='Morning'
elif 12 <= hour < 18:
        categorize_time = 'Afternoon'
else:
        categorize_time = 'Evening'
df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time)
activity_by_time = df.groupby('time_of_day')['Pedestrians'].mean().reset_index()

print(activity_by_time)
