import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import nominal as nom


X_train = nom.df_train_pre.drop('SalePrice', axis=1)
Y_train = nom.df_train_pre['SalePrice']
X_test = nom.df_test_pre

print('\nEntrenando modelo\n')
model = RandomForestRegressor(n_estimators=1000, max_depth=10, random_state=42)
model.fit(X_train, Y_train)
print('\nEntrenamiento completado')

print('Realizando Predicciones con el test.csv')
predictions = model.predict(X_test)
print(predictions)

output = pd.DataFrame({
    'Id' : X_test.index,
    'SalePrice' : predictions
})

output.to_csv('submission.csv', index=False)
print('Archivo guardado')