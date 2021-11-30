# Hecho por Luis Mendoza


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargado de CSV

# Profe, modifique el filepath para evitar el error que impide cargar el documento correctamente.
# Debe colocar la dirección en carpeta COMPLETA del archivo para que cargue

filePathCSV = "D:/Shared/Mis Cosas de la Universidad/9 - Semestre/Inteligencia Computacional/Tercer Corte/30-11-2021/Archivos/covid_22_noviembre.csv"
datosCovid = pd.read_csv(filePathCSV)

# Normalización de los datos datos


datosCovid[datosCovid['Sexo']=='F'].shape[0]
datosCovid[datosCovid['Sexo']=='M'].shape[0]
datosCovid[datosCovid['Sexo']=='f'].shape[0]
datosCovid[datosCovid['Sexo']=='m'].shape[0]

datosCovid.groupby('Sexo').size()
datosCovid.groupby('Estado').size()

datosCovid['Estado'].replace('LEVE','leve', inplace=True)
datosCovid['Estado'].replace('moderado','Moderado', inplace=True)
datosCovid['Estado'].replace('leve','Leve', inplace=True)

datosCovid['Tipo de contagio'].replace('En ESTUDIO','En Estudio', inplace=True)

datosCovid['Tipo de contagio'].replace('relacionado','Relacionado', inplace=True)

datosCovid['Ubicación del caso'].replace('CASA','Casa', inplace=True)

datosCovid['Tipo de contagio'].replace('En estudio','En Estudio', inplace=True)

datosCovid['Tipo de contagio'].replace('RELACIONADO','relacionado', inplace=True)


datosCovid['Sexo'].replace('m','M', inplace=True)
datosCovid['Sexo'].replace('f','F', inplace=True)

# Ejercicio 35 - Gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia

agr = 'Fecha de diagnóstico'
fig = plt.figure(figsize=(12, 5))
datosCovid.groupby(agr).size().plot(kind='bar')
org_rec = datosCovid[datosCovid['Recuperado'] == 'Recuperado'].groupby(agr).size()
org_fal = datosCovid[datosCovid['Estado'] == 'Fallecido'].groupby(agr).size()
org_rec.plot(kind='bar', color="C2")
org_fal.plot(kind='bar', color="C3")
plt.legend(('Contagio', 'Recuperado', 'Muerte'), prop={'size': 15}, loc='upper right')

print("-------------------")
print("El gráfico de barras por tipo de toda Colombia")
plt.show()
print("-------------------")
