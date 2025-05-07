import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/geolocation/geo_tweets_with_depts_and_tone.csv')

export_data = pd.DataFrame()
# Create 6 line plots (using plt) of the frequency (count) of positive, neutral and negative tweets over time for 6 departments defined by the user, in a 2x3 grid/ Including a start date and end date for the time period
departments = ['Bogotá Distrito Capital', 'Antioquia', 'Valle del Cauca', 'Cundinamarca', 'Santander', 'Atlántico']
proportion = False
# include_retweets = False
start_date = '2018-01-01'
end_date = '2020-04-01'


color_mapping = {
    'Positive': '#1e81a2',
    'Neutral': '#c4c4c4',
    'Negative': '#fa8b02',
    'Positive without reposts': '#1e81a2',
    'Neutral without reposts': '#c4c4c4',
    'Negative without reposts': '#fa8b02'
}

name_mapping = {
    'negative': 'Negative',
    'neutral': 'Neutral',
    'positive': 'Positive',

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

        df_with_tone_sample = df_with_tone_sample.rename(columns=name_mapping)
        
        df_with_tone_sample['Total'] = df_with_tone_sample['Negative'] + df_with_tone_sample['Neutral'] + df_with_tone_sample['Positive']
        # Standardize the data (1 is the maximum value)
        max_value = df_with_tone_sample['Negative'].max()
        df_with_tone_sample['Total'] = df_with_tone_sample['Total']/max_value
        df_with_tone_sample['Negative'] = df_with_tone_sample['Negative']/max_value
        df_with_tone_sample['Neutral'] = df_with_tone_sample['Neutral']/max_value
        df_with_tone_sample['Positive'] = df_with_tone_sample['Positive']/max_value

        df_with_tone_sample = df_with_tone_sample.drop(columns=['Total'])
        df_with_tone_sample = df_with_tone_sample.melt(id_vars=['year', 'month'], var_name='tone', value_name='count')
        df_with_tone_sample['month'] = df_with_tone_sample['month'].astype(str)

        df_with_tone_sample['department'] = department
        export_data = pd.concat([export_data, df_with_tone_sample], ignore_index=True)
        
        plt.subplot(2, 3, i+1)
        for tone in ['Positive', 'Neutral', 'Negative']:
            df_tone = df_with_tone_sample[df_with_tone_sample['tone'] == tone]
            plt.plot(df_tone['month'], df_tone['count'], label=tone, color=color_mapping[tone], alpha=0.7)
        plt.title(f'{department}')
        plt.legend(loc='upper left')
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

        df_with_tone_sample = df_with_tone_sample.rename(columns=name_mapping)

        df_with_tone_sample['Negative without reposts'] = df_with_tone_sample['Negative']
        df_with_tone_sample['Neutral without reposts'] = df_with_tone_sample['Neutral']
        df_with_tone_sample['Positive without reposts'] = df_with_tone_sample['Positive']
        
        df_with_tone_sample['Total without reposts'] = df_with_tone_sample['Negative without reposts'] + df_with_tone_sample['Neutral without reposts'] + df_with_tone_sample['Positive without reposts']
        # Standardize the data (1 is the maximum value)
        max_value = df_with_tone_sample['Negative without reposts'].max()
        df_with_tone_sample['Total without reposts'] = df_with_tone_sample['Total without reposts']/max_value
        df_with_tone_sample['Negative without reposts'] = df_with_tone_sample['Negative without reposts']/max_value
        df_with_tone_sample['Neutral without reposts'] = df_with_tone_sample['Neutral without reposts']/max_value
        df_with_tone_sample['Positive without reposts'] = df_with_tone_sample['Positive without reposts']/max_value

        df_with_tone_sample = df_with_tone_sample.drop(columns=['Total without reposts','Negative', 'Neutral', 'Positive'])
        df_with_tone_sample = df_with_tone_sample.melt(id_vars=['year', 'month'], var_name='tone', value_name='count')
        df_with_tone_sample['month'] = df_with_tone_sample['month'].astype(str)

        df_with_tone_sample['department'] = department
        export_data = pd.concat([export_data, df_with_tone_sample], ignore_index=True)
        
        plt.subplot(2, 3, i+1)
        for tone in ['Negative without reposts', 'Neutral without reposts', 'Positive without reposts']:
            df_tone = df_with_tone_sample[df_with_tone_sample['tone'] == tone]
            plt.plot(df_tone['month'], df_tone['count'], label=tone, color=color_mapping[tone], alpha=0.5, linestyle='dotted')
        plt.title(f'{department}')
        plt.legend(loc='upper left')
        plt.xticks(rotation=90)

# Save the plot to svg
# plt.tight_layout()
# plt.savefig('notebooks/2_spatiotemporal/7_line_plot_6main_deps.svg')

# Save the plot to tiff
plt.tight_layout()
plt.savefig('./docs/figures/Fig8.tiff')

# # Save the data into one csv
# export_data = export_data.sort_values(by=['department', 'year', 'month'])
# export_data = export_data.drop(columns=['year'])
# export_data = export_data.rename(columns={'count': 'frequency'})
# export_data.to_csv('notebooks/2_spatiotemporal/7_line_plot_6main_deps_data.csv', index=False)