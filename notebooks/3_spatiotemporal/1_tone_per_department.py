import pandas as pd

# 1) Negative tweets per department (per 100,000 inhabitants)

df_with_depts = pd.read_csv('./data/geolocation/geo_tweets_with_depts_and_tone.csv')

# Only keep tweets with negative tone
df_with_depts = df_with_depts[df_with_depts['tone'] == 'negative']

# Group by department and count the number of tweets
df_with_depts = df_with_depts.groupby('department').size().reset_index(name='count')

# Sort by count in descending order
df_with_depts = df_with_depts.sort_values(by='count', ascending=False)

# Load population data (DANE 2018)
df_population = pd.read_csv('./data/demographic/1_population_by_department_2018_DANE.csv')

# Merge with population data
df_with_depts = df_with_depts.merge(df_population, on='department', how='left')

# get Number of negative tweets per department (per 100,000 inhabitants)
df_with_depts['proportion'] = [100000*df_with_depts['count'][i] / df_with_depts['population_2018'][i] for i in range(len(df_with_depts))]

# Sort by proportion in descending order
df_with_depts = df_with_depts.sort_values(by='proportion', ascending=False)


print("================================================")
print("Number of negative tweets per department by population (all years)")
print(df_with_depts)
print("================================================")


# Save to csv
df_with_depts.to_csv('./notebooks/3_spatiotemporal/1_negative_tweets_per_department_standardized_100000.csv', index=False)



# 2) Neutral tweets per department (per 100,000 inhabitants)

df_with_depts = pd.read_csv('./data/geolocation/geo_tweets_with_depts_and_tone.csv')

# Only keep tweets with neutral tone
df_with_depts = df_with_depts[df_with_depts['tone'] == 'neutral']

# Group by department and count the number of tweets
df_with_depts = df_with_depts.groupby('department').size().reset_index(name='count')

# Sort by count in descending order
df_with_depts = df_with_depts.sort_values(by='count', ascending=False)

# Merge with population data
df_with_depts = df_with_depts.merge(df_population, on='department', how='left')

# get Number of neutral tweets per department (per 100,000 inhabitants)
df_with_depts['proportion'] = [100000*df_with_depts['count'][i] / df_with_depts['population_2018'][i] for i in range(len(df_with_depts))]

# Sort by proportion in descending order
df_with_depts = df_with_depts.sort_values(by='proportion', ascending=False)

print("================================================")
print("Number of neutral tweets per department by population (all years)")
print(df_with_depts)
print("================================================")


# Save to csv
df_with_depts.to_csv('./notebooks/3_spatiotemporal/1_neutral_tweets_per_department_standardized_100000.csv', index=False)



# 3) Positive tweets per department (per 100,000 inhabitants)

df_with_depts = pd.read_csv('./data/geolocation/geo_tweets_with_depts_and_tone.csv')

# Only keep tweets with positive tone
df_with_depts = df_with_depts[df_with_depts['tone'] == 'positive']  

# Group by department and count the number of tweets
df_with_depts = df_with_depts.groupby('department').size().reset_index(name='count')

# Sort by count in descending order
df_with_depts = df_with_depts.sort_values(by='count', ascending=False)


# Merge with population data
df_with_depts = df_with_depts.merge(df_population, on='department', how='left')

# get Number of positive tweets per department (per 100,000 inhabitants)
df_with_depts['proportion'] = [100000*df_with_depts['count'][i] / df_with_depts['population_2018'][i] for i in range(len(df_with_depts))]

# Sort by proportion in descending order
df_with_depts = df_with_depts.sort_values(by='proportion', ascending=False)

print("================================================")
print("Number of positive tweets per department by population (all years)")
print(df_with_depts)
print("================================================")


# Save to csv
df_with_depts.to_csv('./notebooks/3_spatiotemporal/1_positive_tweets_per_department_standardized_100000.csv', index=False)
