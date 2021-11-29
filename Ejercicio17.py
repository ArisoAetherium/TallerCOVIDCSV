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

# Ejercicio 17 - Agrupando por departamento y en orden de Mayor a menor las ciudades con más casos de contagios

agrupado = datosCovid.groupby(['Nombre departamento', 'Nombre municipio'])
ordenado = agrupado.size().sort_values(ascending=False)
print("-------------------")
print("las ciudades con mas casos de contagiados: {}".format(ordenado))
print("-------------------")