# 3_correlation_unemplyoment_tone.py
# This script calculates the correlation between the tone of tweets and the unemployment rate in Colombia in 2018.
import pandas as pd
from scipy import stats

def get_correlation_unemployment_tone(tone):
    # Load tone data
    df_tone = pd.read_csv(f'./notebooks/3_spatiotemporal/1_tweets_per_department_standardized_100000.csv')

    # Load unemployment rate data
    df_unemployment = pd.read_csv('./data/demographic/4_unemployment_rate_by_department_2018_DANE.csv')

    # Merge tone and unemployment rate data
    df_merged = pd.merge(df_unemployment, df_tone, on='department', how='inner')

    # Export merged data
    # df_merged.to_csv('./notebooks/3_spatiotemporal/3_correlation_unemployment_tone.csv', index=False)

    # Calculate correlation coefficient and p-value
    correlation, p_value = stats.pearsonr(df_merged['unemployment_rate_per_100000'], df_merged['proportion_per_100000_' + tone])

    print("================================================")
    print(f"Correlation between {tone} tone and unemployment rate: {correlation:.3f}")
    print(f"P-value: {p_value:.3f}")

    # Interpret p-value
    alpha = 0.05
    if p_value < alpha:
        print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
        print(f"there is a statistically significant correlation between {tone} tone")
        print("frequency and unemployment rate across departments.")
    else:
        print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
        print(f"there is not enough evidence to conclude a statistically significant")
        print(f"correlation between {tone} tone and unemployment rate.")
    print("================================================")
    return correlation, p_value


# Run the function for each tone
get_correlation_unemployment_tone('negative')
get_correlation_unemployment_tone('neutral')
get_correlation_unemployment_tone('positive')