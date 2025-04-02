# 2_correlation_mugging_tone.py
# This script calculates the correlation between the tone of tweets and the number of mugging incidents in Colombia in 2018.
import pandas as pd
from scipy import stats

def get_correlation_mugging_tone(tone):
    # Load tone data
    df_tone = pd.read_csv(f'./notebooks/3_spatiotemporal/1_tweets_per_department_standardized_100000.csv')

    # Load mugging data
    df_mugging = pd.read_csv('./data/demographic/3_mugging_by_department.csv')

    # Merge tone and mugging data
    df_merged = pd.merge(df_mugging, df_tone, on='department', how='inner')

    # print(df_merged)

    # Export merged data
    # df_merged.to_csv('./notebooks/3_spatiotemporal/2_correlation_mugging_tone.csv', index=False)

    # Calculate correlation coefficient and p-value
    # correlation, p_value = stats.pearsonr(df_merged['population_2018_x'], df_merged['count'])
    correlation, p_value = stats.spearmanr(df_merged['proportion_per_100000_' + tone], df_merged['mugging_per_100000'])

    # print(f"Correlation between tone and mugging: {correlation:.3f}")
    print("================================================")
    print(f"Correlation between {tone} tone and mugging: {correlation:.3f}")
    print(f"P-value: {p_value:.3f}")

    # Interpret p-value
    alpha = 0.05
    if p_value < alpha:
        print(f"\nThe p-value ({p_value:.3f}) is less than {alpha}, suggesting that")
        print("there is a statistically significant correlation between {tone} tone")
        print("frequency and mugging incidents across departments.")
    else:
        print(f"\nThe p-value ({p_value:.3f}) is greater than {alpha}, suggesting that")
        print("there is not enough evidence to conclude a statistically significant")
        print(f"correlation between {tone} tone and mugging incidents.")
    print("================================================")
    return correlation, p_value


# Run the function for each tone
get_correlation_mugging_tone('negative')
get_correlation_mugging_tone('neutral')
get_correlation_mugging_tone('positive')

# Collinearity check between tone and mugging using VIF

# # Import necessary libraries
# import statsmodels.api as sm
# from statsmodels.stats.outliers_influence import variance_inflation_factor

# # Create a DataFrame with the independent variables
# X = df_merged[['population_2018_x', 'count']]

# # Add a constant column to the independent variables
# X = sm.add_constant(X)


# Calculate VIF for each independent variable
# vif = pd.DataFrame()
# vif["Variable"] = X.columns
# vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# # Print the VIF results
# print(vif)

# # interpret VIF results
# # VIF values close to 1 indicate no multicollinearity, while values above 5 or 10 suggest moderate to high multicollinearity.
