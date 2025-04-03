# 6_map_tone_population_per_departments.py
# This script maps the tone of tweets per department and the population per department. This code will create 2 separate maps:
# 1. Tone map: Maps the tone of tweets per department. Saved to svg `./notebooks/3_spatiotemporal/6_tone_map_per_department.svg`
# 2. Population map: Maps the population per department. Saved to svg `./notebooks/3_spatiotemporal/6_population_map_per_department.svg`

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Define the standard department names
standard_departments = ['Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas', 
                      'Caquetá', 'Casanare', 'Valle del Cauca', 'Cauca', 'Cesar', 'Chocó', 'Córdoba', 
                      'Cundinamarca', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta', 
                      'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda', 
                      'San Andrés y Providencia', 'Santander', 'Sucre', 'Tolima', 'Vaupés', 'Vichada', 
                      'Bogotá Distrito Capital']

# Load the shapefile
shp = gpd.read_file('./notebooks/3_spatiotemporal/6_departments_gis/departamentos.shp')

# Print unique department names from shapefile
print("Shapefile department names:")
print(sorted(shp['NOMBRE_DPT'].unique()))

# Create department name mapping dictionary
dept_name_mapping = {
    'AMAZONAS': 'Amazonas',
    'ANTIOQUIA': 'Antioquia',
    'ARAUCA': 'Arauca',
    'ATLÁNTICO': 'Atlántico',
    'BOLÍVAR': 'Bolívar',
    'BOYACÁ': 'Boyacá',
    'CALDAS': 'Caldas',
    'CAQUETÁ': 'Caquetá',
    'CASANARE': 'Casanare',
    'CAUCA': 'Cauca',
    'CESAR': 'Cesar',
    'CHOCÓ': 'Chocó',
    'CÓRDOBA': 'Córdoba',
    'CUNDINAMARCA': 'Cundinamarca',
    'GUAINÍA': 'Guainía',
    'GUAVIARE': 'Guaviare',
    'HUILA': 'Huila',
    'LA GUAJIRA': 'La Guajira',
    'MAGDALENA': 'Magdalena',
    'META': 'Meta',
    'NARIÑO': 'Nariño',
    'NORTE DE SANTANDER': 'Norte de Santander',
    'PUTUMAYO': 'Putumayo',
    'QUINDÍO': 'Quindío',
    'RISARALDA': 'Risaralda',
    'SAN ANDRÉS Y PROVIDENCIA': 'San Andrés y Providencia',
    'SANTANDER': 'Santander',
    'SUCRE': 'Sucre',
    'TOLIMA': 'Tolima',
    'VALLE DEL CAUCA': 'Valle del Cauca',
    'VAUPÉS': 'Vaupés',
    'VICHADA': 'Vichada',
    'BOGOTÁ, D.C.': 'Bogotá Distrito Capital'
}

# Apply the mapping to the shapefile
shp['department'] = shp['NOMBRE_DPT'].map(dept_name_mapping)

# Load the tweets data
df_tone = pd.read_csv('./notebooks/3_spatiotemporal/1_tweets_per_department_standardized_100000.csv')

# Merge the data using the new standardized department names
merged = shp.merge(df_tone, on='department', how='left')

# Create the map
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Plot with a sequential colormap
merged.plot(column='proportion_per_100000_negative', 
           cmap='Reds',
           legend=True,
           legend_kwds={'label': 'Proportion of Negative Tweets per 100,000 Population',
                       'orientation': 'horizontal'},
           missing_kwds={'color': 'lightgrey'},
           ax=ax)

# Add title and remove axes
ax.set_title('Proportion of Negative Tweets per 100,000 Population by Department', pad=20, fontsize=14)
ax.axis('off')

# Add department labels using the standardized names
merged.apply(lambda x: ax.annotate(text=x.department, 
                                 xy=(x.geometry.centroid.x, x.geometry.centroid.y),
                                 ha='center',
                                 fontsize=8), 
            axis=1)

plt.tight_layout()
plt.show()

# 2) Map the population per department
# # Load the data
# df_population = pd.read_csv('./data/demographic/3_population_by_department.csv')

