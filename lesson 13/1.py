import pandas as pd

df = pd.read_csv('data1.csv')

print(df.info())

print(df.head())

country_data=df['Country']

print(country_data)

subset = df[['Country', 'Average IQ']]

print(subset)

filtered_df = subset[subset['Average IQ']>100]
print(filtered_df)

null_mask = df.isnull()

null_count = null_mask.sum()

print(null_count)

df.dropna(inplace=True)

print(df.info())
duplicated_count = df.duplicate().sum()
print(duplicated_count)

average_iq_continent = df.groupby('Continent')['Average IQ'].mean

sorted_avg_by_continent = average_iq_continent.sort_values(ascending=True)

total_nobel_by_country = df.groupby('Country')['Nobel Prices'].sum()

print(total_nobel_by_country)

sorted_total_nobel_by_country = total_nobel_by_country.sort_values(ascending=False)

print(sorted_total_nobel_by_country)

sorted = sorted_total_nobel_by_country[sorted_total_nobel_by_country=0]

print(sorted)

