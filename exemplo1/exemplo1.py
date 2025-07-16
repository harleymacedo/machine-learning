print('Exemplo 1 - Python')

import matplotlib as plt
import numpy as np
import pandas as pd
import sklearn.linear_model 

# Carrega os dados
oecd_bli = pd.read_csv('oecd_bli_2015.csv', thousands=',')
gdp_per_capita = pd.read_csv('gdp_per_capita.csv', thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')

# Prepara os dados 
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
x = np.c_[country_stats['GDP per capita']]
y = np.c_[country_stats['Life satisfaction']]

# Visualiza os dados
country_stats.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.show()

# Seleciona um modelo linear
model = sklearn.linear_model.LinearRegression()

# Treina o modelo
model.fit(x, y)

# Efetua uma predição para o Chipre
X_new = [[22587]]  # GDP per capita do Chipre
print(model.predict(X_new))  # Entradas [[5.96242338]]