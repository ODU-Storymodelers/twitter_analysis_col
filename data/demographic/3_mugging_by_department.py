import pandas as pd
import json
# Load mugging data
file_paths = json.load(open('./data/demographic/file_paths.json')) # Path to datasets
df_mugging = pd.read_excel(file_paths['mugging_data'])

#Print departments
print(df_mugging['DEPARTAMENTO'].unique())
"""['AMAZONAS' 'ANTIOQUIA' 'ARAUCA' 'ATLÁNTICO' 'BOLÍVAR' 'BOYACÁ' 'CALDAS'
 'CAQUETÁ' 'CASANARE' 'CAUCA' 'CESAR' 'CHOCÓ' 'CÓRDOBA' 'CUNDINAMARCA'
 'GUAJIRA' 'GUAVIARE' 'HUILA' 'MAGDALENA' 'META' 'NARIÑO'
 'NORTE DE SANTANDER' 'PUTUMAYO' 'QUINDÍO' 'RISARALDA' 'SAN ANDRÉS'
 'SANTANDER' 'SUCRE' 'TOLIMA' 'VALLE' 'VICHADA' 'GUAINÍA' 'VAUPÉS']"""

# If MUNICIPIO is BOGOTÁ D.C. (CT), then DEPARTAMENTO is BOGOTÁ D.C. (DC)
df_mugging.loc[df_mugging['MUNICIPIO'] == 'BOGOTÁ D.C. (CT)', 'DEPARTAMENTO'] = 'BOGOTÁ D.C. (DC)'


# Fix based on list
departments = ['Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas', 'Caquetá', 'Casanare', 'Valle del Cauca', 'Cauca', 'Cesar', 'Chocó', 'Córdoba', 'Cundinamarca', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda', 'San Andrés y Providencia', 'Santander', 'Sucre', 'Tolima', 'Vaupés', 'Vichada', 'Bogotá Distrito Capital']

replace_dict = {
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
    'GUAJIRA': 'La Guajira',
    'MAGDALENA': 'Magdalena',
    'META': 'Meta',
    'NARIÑO': 'Nariño',
    'NORTE DE SANTANDER': 'Norte de Santander',
    'PUTUMAYO': 'Putumayo',
    'QUINDÍO': 'Quindío',
    'RISARALDA': 'Risaralda',
    'SAN ANDRÉS': 'San Andrés y Providencia',
    'SANTANDER': 'Santander',
    'SUCRE': 'Sucre',
    'TOLIMA': 'Tolima',
    'VALLE': 'Valle del Cauca',
    'VICHADA': 'Vichada',
    'GUAINÍA': 'Guainía',
    'VAUPÉS': 'Vaupés',
    'BOGOTÁ D.C. (DC)': 'Bogotá Distrito Capital',
}


# Replace departments
df_mugging['DEPARTAMENTO'] = df_mugging['DEPARTAMENTO'].replace(replace_dict)

# Rename DEPARTAMENTO to department
df_mugging = df_mugging.rename(columns={'DEPARTAMENTO': 'department'})

# Get number of mugging by department (aggregate the column CANTIDAD)
df_mugging_by_department = df_mugging.groupby('department')['CANTIDAD'].sum().reset_index(name='mugging')

# Load population data
df_population = pd.read_csv('./data/demographic/1_population_by_department_2018_DANE.csv')

# Merge mugging data with population data
df_mugging_by_department = df_mugging_by_department.merge(df_population, on='department', how='left')

# get Number of mugging per department (per 100,000 inhabitants)
df_mugging_by_department['proportion_per_100000'] = [100000*df_mugging_by_department['mugging'][i] / df_mugging_by_department['population_2018'][i] for i in range(len(df_mugging_by_department))]

# Sort by proportion in descending order
df_mugging_by_department = df_mugging_by_department.sort_values(by='proportion_per_100000', ascending=False)

print(df_mugging_by_department[['department', 'proportion_per_100000']])

# Save to csv
df_mugging_by_department.to_csv('./data/demographic/3_mugging_by_department.csv', index=False)

