corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending=False)

from pandas.plotting import scartter_matrix

attributes = ['median_house_value', 'median_income', 'total_rooms', 'housing_median_age']

scartter_matrix(housing[attributes], figsize=(12, 8))