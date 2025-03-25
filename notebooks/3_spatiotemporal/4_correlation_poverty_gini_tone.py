# 4_correlation_poverty_gini_tone.py
# This script calculates the correlation between the tone of tweets and the poverty rate and Gini index in Colombia in 2018.
import pandas as pd
from scipy import stats

# Load tone data
df_tone = pd.read_csv('./notebooks/3_spatiotemporal/1_negative_tweets_per_department_standardized_100000.csv')

# Load poverty rate and Gini index data
df_poverty = pd.read_csv('./data/demographic/5_poverty_rate_by_department_2018_DANE.csv')

# Merge tone and poverty rate and Gini index data
df_merged = pd.merge(df_poverty, df_tone, on='department', how='inner')

# Export merged data
# df_merged.to_csv('./notebooks/3_spatiotemporal/4_correlation_poverty_gini_tone.csv', index=False)

# Calculate correlation coefficient and p-value for (1) poverty rate:
correlation, p_value = stats.pearsonr(df_merged['poverty_rate_per_100000'], df_merged['proportion'])


print(f"Correlation between tone and poverty rate: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
    print("there is a statistically significant correlation between negative tweet")
    print("frequency and poverty rate across departments.")
else:
    print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
    print("there is not enough evidence to conclude a statistically significant")
    print("correlation between negative tweet frequency and poverty rate.")

# Calculate correlation coefficient and p-value for (2) extreme poverty rate:
correlation, p_value = stats.pearsonr(df_merged['extreme_poverty_rate_per_100000'], df_merged['proportion'])

print("--------------------------------")
print(f"Correlation between tone and extreme poverty rate: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
    print("there is a statistically significant correlation between negative tweet")
    print("frequency and extreme poverty rate across departments.")
else:
    print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
    print("there is not enough evidence to conclude a statistically significant")
    print("correlation between negative tweet frequency and extreme poverty rate.")

# Calculate correlation coefficient and p-value for (3) Gini index:
correlation, p_value = stats.pearsonr(df_merged['gini_coefficient_per_100000'], df_merged['proportion'])

print("--------------------------------")
print(f"Correlation between tone and Gini index: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
    print("there is a statistically significant correlation between negative tweet")
    print("frequency and Gini index across departments.")
else:
    print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
    print("there is not enough evidence to conclude a statistically significant")
    print("correlation between negative tweet frequency and Gini index.")
    
    