corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending=False)