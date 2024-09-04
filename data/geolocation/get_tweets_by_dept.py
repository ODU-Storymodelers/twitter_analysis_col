### This script reads the tweets with tone and the geolocation data of the Colombian cities and assigns a department to each tweet based on the city where it was posted. The output is a csv file with the tweets, their tone and the department where they were posted.
import pandas as pd

TWEETS_PATH = '../texts/colombian_valid_tweets_tone_preds_wwm.csv'
LAT_LONGS_PATH = './lats_longs_cities_colombia.csv'
OUTPUT_PATH = '../geolocation/geo_tweets_with_depts_and_tone.csv'
include_text = True


# read tweets with tone
print("Reading tweets with locations...")
df = pd.read_csv(LAT_LONGS_PATH)

df_with_depts = df.copy()

departments = ['Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas', 'Caquetá', 'Casanare', 'Valle del Cauca',
               'Cauca', 'Cesar', 'Chocó', 'Córdoba', 'Cundinamarca', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta',
               'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda', 'San Andrés y Providencia', 'Santander', 'Sucre', 
               'Tolima', 'Vaupés', 'Vichada', 'Bogotá Distrito Capital']

for index, row in df_with_depts.iterrows():
    if "Valledupar" in row['address']:
        df_with_depts.loc[index, 'department'] = 'Cesar'
    else:
        for department in departments:
            if department in row['address']:
                df_with_depts.loc[index, 'department'] = department
                break
            
# Add text
if include_text:
    print("Reading tweets with tone...")
    df_tweets = pd.read_csv(TWEETS_PATH)
    df_tweets = df_tweets[['Id', 'text', 'tone']]
    df_with_depts = pd.merge(df_with_depts, df_tweets, left_on='Id', right_on='Id', how='inner')


df_with_depts.to_csv(OUTPUT_PATH, index=False)
print("Done! File saved at: ", OUTPUT_PATH)