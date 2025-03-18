# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for plots
sns.set_style('whitegrid')

# Read the 911 emergency calls dataset
df = pd.read_csv('911.csv')

# Display basic information about the dataframe
df.info()

# Show the first 3 rows of the dataframe
df.head(3)

# Top 5 zip codes for 911 calls
df['zip'].value_counts().head(5)

# Top 5 townships (twp) for 911 calls
df['twp'].value_counts().head(5)

# Number of unique titles in the "title" column
df['title'].nunique()

# Create a new column called 'Reason' by extracting the reason from the 'title'
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# Count of calls for each reason
df['Reason'].value_counts()

# Plot count of calls for each reason using seaborn
sns.countplot(x='Reason', data=df, palette='viridis')
plt.title('911 Calls by Reason')
plt.show()

# Check data type of 'timeStamp' column (before converting)
type(df['timeStamp'].iloc[0])

# Convert 'timeStamp' column from string to datetime object
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Create new columns for Hour, Month, and Day of Week from the timeStamp
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

# Map Day of Week integers to actual day names
dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

# Plot number of calls by day of week and reason
sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')

# Move legend outside of the plot for better visibility
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Calls by Day of Week and Reason')
plt.tight_layout()
plt.show()

# Plot number of calls by month and reason
sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Calls by Month and Reason')
plt.tight_layout()
plt.show()

# Group data by month and count number of calls per month
by_month = df.groupby('Month').count()

# Plot number of calls per month
by_month['twp'].plot()
plt.title('Calls per Month')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.show()

# Create a linear fit plot of number of calls per month
sns.lmplot(x='Month', y='twp', data=by_month.reset_index())
plt.title('Trend of Calls per Month')
plt.show()

# Convert 'timeStamp' to date (YYYY-MM-DD) and group data by date
df['Date'] = df['timeStamp'].apply(lambda t: t.date())

# Plot number of calls per date
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.title('Calls by Date')
plt.xlabel('Date')
plt.ylabel('Number of Calls')
plt.show()

# Plot for each reason over time
# Emergency type: Traffic
df[df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic Calls Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Traffic Calls')
plt.tight_layout()
plt.show()

# Emergency type: Fire
df[df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire Calls Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Fire Calls')
plt.tight_layout()
plt.show()

# Emergency type: EMS
df[df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS Calls Over Time')
plt.xlabel('Date')
plt.ylabel('Number of EMS Calls')
plt.tight_layout()
plt.show()

# Create a heatmap and clustermap to visualize calls by hour and day of week
day_hour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()

# Heatmap of calls by day of week and hour
plt.figure(figsize=(12, 6))
sns.heatmap(day_hour, cmap='viridis')
plt.title('Heatmap of Calls by Day of Week and Hour')
plt.show()

# Clustermap of calls by day of week and hour
sns.clustermap(day_hour, cmap='viridis')
plt.title('Clustermap of Calls by Day of Week and Hour')
plt.show()

# Create a heatmap and clustermap to visualize calls by month and day of week
day_month = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()

# Heatmap of calls by day of week and month
plt.figure(figsize=(12, 6))
sns.heatmap(day_month, cmap='viridis')
plt.title('Heatmap of Calls by Day of Week and Month')
plt.show()

# Clustermap of calls by day of week and month
sns.clustermap(day_month, cmap='viridis')
plt.title('Clustermap of Calls by Day of Week and Month')
plt.show()