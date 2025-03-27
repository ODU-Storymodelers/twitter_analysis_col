import pandas as pd

def get_tone_per_department():
# 1) Tweets per department (per 100,000 inhabitants)

    df_with_depts = pd.read_csv('./data/geolocation/geo_tweets_with_depts_and_tone.csv')

    # Group by department and tone, count tweets for each combination
    df_counts = df_with_depts.groupby(['department', 'tone']).size().unstack(fill_value=0)
    
    # Rename columns to count_[tone]
    df_counts.columns = ['count_' + tone for tone in df_counts.columns]
    
    # Reset index to make department a column again
    df_with_depts = df_counts.reset_index()

    df_with_depts['count_total'] = df_with_depts['count_negative'] + df_with_depts['count_neutral'] + df_with_depts['count_positive']

    # Load population data (DANE 2018)
    df_population = pd.read_csv('./data/demographic/1_population_by_department_2018_DANE.csv')

    # Merge with population data
    df_with_depts = df_with_depts.merge(df_population, on='department', how='left')

    # 2.1) get Number of negative,neutral,positive tweets per department (per 100,000 inhabitants)
    for tone in ['negative', 'neutral', 'positive']:
        df_with_depts['count_per_100000_' + tone] = [100000*df_with_depts['count_' + tone][i] / df_with_depts['population_2018'][i] for i in range(len(df_with_depts))]

    # 2.2) Get the proportion of each tweet tone per department (tone/(neutral+positive+negative)/population*100000)
    for tone in ['negative', 'neutral', 'positive']:
        df_with_depts['proportion_per_100000_' + tone] = [100000*df_with_depts['count_' + tone][i] / df_with_depts['count_total'][i] for i in range(len(df_with_depts))]

    # Sort by population in descending order
    df_with_depts = df_with_depts.sort_values(by='population_2018', ascending=False)


    # Save to csv
    df_with_depts.to_csv(f'./notebooks/3_spatiotemporal/1_tweets_per_department_standardized_100000.csv', index=False)
    
    
if __name__ == "__main__":
    get_tone_per_department()