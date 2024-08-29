import pandas as pd

PATH = './data/texts/colombian_valid_tweets_tone_preds_wwm.csv'
OUTPUT_PATH = './data/texts/months/2020-10-noRT.xlsx'
DATE = '2020-10-01'
include_retweets = False


print('Extracting tweets from', DATE)

df = pd.read_csv(PATH)
df = df[df['date'] == DATE]

if not include_retweets: #remove duplicated texts or Ids
    df = df.drop_duplicates(subset=['Id'])
    df = df.drop_duplicates(subset=['text'])

df.reset_index(drop=True, inplace=True)

print('Number of tweets:', df.shape[0])

# Add a column with the number of times the tweet is repeated
for index, row in df.iterrows():
    df.at[index, 'count'] = df[df['text'] == row['text']].shape[0]
     
    if index % 5000 == 0:
        print(index,'/', df.shape[0], 'tweets processed:', round(index/df.shape[0]*100, 1), '%')
    

df.to_excel(OUTPUT_PATH, index=False)

print('Done!')