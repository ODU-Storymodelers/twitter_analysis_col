# 5_correlation_homicides_tone.py
# This script calculates the correlation between the tone of tweets and the homicide rate in Colombia in 2018.
import pandas as pd
from scipy import stats

# Load tone data
df_tone = pd.read_csv('./notebooks/3_spatiotemporal/1_negative_tweets_per_department_standardized_100000.csv')

# Load homicide rate data
df_homicides = pd.read_csv('./data/demographic/6_homicides_rate_by_department_2018_DANE.csv')

# Merge tone and homicide rate data
df_merged = pd.merge(df_homicides, df_tone, on='department', how='inner')

# Export merged data
# df_merged.to_csv('./notebooks/3_spatiotemporal/5_correlation_homicides_tone.csv', index=False)

# Calculate correlation coefficient and p-value for (1) homicide rate:
correlation, p_value = stats.pearsonr(df_merged['homicides_rate_per_100000'], df_merged['proportion'])


print(f"Correlation between tone and homicide rate: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
    print("there is a statistically significant correlation between negative tweet")
    print("frequency and homicide rate across departments.")
else:
    print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
    print("there is not enough evidence to conclude a statistically significant")
    print("correlation between negative tweet frequency and homicide rate.")
