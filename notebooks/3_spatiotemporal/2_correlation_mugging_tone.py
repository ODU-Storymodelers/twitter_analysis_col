# 2_correlation_mugging_tone.py
# This script calculates the correlation between the tone of tweets and the number of mugging incidents in Colombia in 2018.
import pandas as pd
from scipy import stats

# Load tone data
df_tone = pd.read_csv('./notebooks/3_spatiotemporal/1_negative_tweets_per_department_standardized_100000.csv')

# Load mugging data
df_mugging = pd.read_csv('./data/demographic/3_mugging_by_department.csv')

# Merge tone and mugging data
df_merged = pd.merge(df_tone, df_mugging, on='department', how='inner')

# Export merged data
df_merged.to_csv('./notebooks/3_spatiotemporal/2_correlation_mugging_tone.csv', index=False)

# Calculate correlation coefficient and p-value
correlation, p_value = stats.pearsonr(df_merged['proportion'], df_merged['mugging'])

print(f"Correlation between tone and mugging: {correlation}")
print(f"P-value: {p_value}")

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print(f"\nThe p-value ({p_value:.4f}) is less than {alpha}, suggesting that")
    print("there is a statistically significant correlation between negative tweet")
    print("frequency and mugging incidents across departments.")
else:
    print(f"\nThe p-value ({p_value:.4f}) is greater than {alpha}, suggesting that")
    print("there is not enough evidence to conclude a statistically significant")
    print("correlation between negative tweet frequency and mugging incidents.")