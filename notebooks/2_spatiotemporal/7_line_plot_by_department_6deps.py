import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/geolocation/geo_tweets_with_depts_and_tone.csv')

# Create 6 line plots (using plt) of the frequency (count) of positive, neutral and negative tweets over time for 6 departments defined by the user, in a 2x3 grid/ Including a start date and end date for the time period
departments = ['Bogotá Distrito Capital', 'Antioquia', 'Valle del Cauca', 'Cundinamarca', 'Santander', 'Atlántico']
proportion = False
# include_retweets = False
start_date = '2018-01-01'
end_date = '2020-04-01'


color_mapping = {
    'positive': '#1e81a2',
    'neutral': '#c4c4c4',
    'negative': '#fa8b02',
    'positive no RT': '#1e81a2',
    'neutral no RT': '#c4c4c4',
    'negative no RT': '#fa8b02'
}

all_departments = data.copy()
# if not include_retweets:
#     all_departments = all_departments.drop_duplicates(subset=['text'], keep=False)
    
all_departments['date'] = pd.to_datetime(all_departments['date'])
all_departments = all_departments[(all_departments['date'] >= start_date) & (all_departments['date'] <= end_date)]
all_departments['month'] = all_departments['date'].dt.to_period('M')
all_departments['year'] = all_departments['date'].dt.to_period('Y')

if not proportion:
    fig, axs = plt.subplots(2, 3, figsize=(20, 10))
    for i, department in enumerate(departments):
        df_with_tone_sample = all_departments[all_departments['department'] == department]
        df_with_tone_sample = df_with_tone_sample.groupby(['year', 'month', 'tone']).size().reset_index(name='count')
        df_with_tone_sample = df_with_tone_sample.pivot_table(index=['year', 'month'], columns='tone', values='count').reset_index()
        df_with_tone_sample = df_with_tone_sample.fillna(0)

        df_with_tone_sample['total'] = df_with_tone_sample['negative'] + df_with_tone_sample['neutral'] + df_with_tone_sample['positive']
        # Standardize the data (1 is the maximum value)
        max_value = df_with_tone_sample['negative'].max()
        df_with_tone_sample['total'] = df_with_tone_sample['total']/max_value
        df_with_tone_sample['negative'] = df_with_tone_sample['negative']/max_value
        df_with_tone_sample['neutral'] = df_with_tone_sample['neutral']/max_value
        df_with_tone_sample['positive'] = df_with_tone_sample['positive']/max_value

        df_with_tone_sample = df_with_tone_sample.drop(columns=['total'])
        df_with_tone_sample = df_with_tone_sample.melt(id_vars=['year', 'month'], var_name='tone', value_name='count')
        df_with_tone_sample['month'] = df_with_tone_sample['month'].astype(str)

        plt.subplot(2, 3, i+1)
        for tone in ['positive', 'neutral', 'negative']:
            df_tone = df_with_tone_sample[df_with_tone_sample['tone'] == tone]
            plt.plot(df_tone['month'], df_tone['count'], label=tone, color=color_mapping[tone], alpha=0.7)
        plt.title(f'{department}')
        plt.legend()
        plt.xticks(rotation=90)
        
        
all_departments = all_departments.drop_duplicates(subset=['text'], keep=False)
    
all_departments['date'] = pd.to_datetime(all_departments['date'])
all_departments = all_departments[(all_departments['date'] >= start_date) & (all_departments['date'] <= end_date)]
all_departments['month'] = all_departments['date'].dt.to_period('M')
all_departments['year'] = all_departments['date'].dt.to_period('Y')

if not proportion:
    for i, department in enumerate(departments):
        df_with_tone_sample = all_departments[all_departments['department'] == department]
        df_with_tone_sample = df_with_tone_sample.groupby(['year', 'month', 'tone']).size().reset_index(name='count')
        df_with_tone_sample = df_with_tone_sample.pivot_table(index=['year', 'month'], columns='tone', values='count').reset_index()
        df_with_tone_sample = df_with_tone_sample.fillna(0)

        df_with_tone_sample['negative no RT'] = df_with_tone_sample['negative']
        df_with_tone_sample['neutral no RT'] = df_with_tone_sample['neutral']
        df_with_tone_sample['positive no RT'] = df_with_tone_sample['positive']
        
        df_with_tone_sample['total no RT'] = df_with_tone_sample['negative no RT'] + df_with_tone_sample['neutral no RT'] + df_with_tone_sample['positive no RT']
        # Standardize the data (1 is the maximum value)
        max_value = df_with_tone_sample['negative no RT'].max()
        df_with_tone_sample['total no RT'] = df_with_tone_sample['total no RT']/max_value
        df_with_tone_sample['negative no RT'] = df_with_tone_sample['negative no RT']/max_value
        df_with_tone_sample['neutral no RT'] = df_with_tone_sample['neutral no RT']/max_value
        df_with_tone_sample['positive no RT'] = df_with_tone_sample['positive no RT']/max_value

        df_with_tone_sample = df_with_tone_sample.drop(columns=['total no RT','negative', 'neutral', 'positive'])
        df_with_tone_sample = df_with_tone_sample.melt(id_vars=['year', 'month'], var_name='tone', value_name='count')
        df_with_tone_sample['month'] = df_with_tone_sample['month'].astype(str)

        plt.subplot(2, 3, i+1)
        for tone in ['positive no RT', 'neutral no RT', 'negative no RT']:
            df_tone = df_with_tone_sample[df_with_tone_sample['tone'] == tone]
            plt.plot(df_tone['month'], df_tone['count'], label=tone, color=color_mapping[tone], alpha=0.5, linestyle='dotted')
        plt.title(f'{department}')
        plt.legend()
        plt.xticks(rotation=90)

# Save the plot to svg
plt.tight_layout()
plt.savefig('notebooks/2_spatiotemporal/7_line_plot_6main_deps.svg')