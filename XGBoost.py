from xgboost import XGBRegressor
import nominal as nom
import pandas as pd
import numpy as np

X_train = nom.df_train_pre.drop('SalePrice', axis=1)
Y_train = nom.df_train_pre['SalePrice']
X_test = nom.df_test_pre
model = XGBRegressor(objective='reg:squarederror',
                     n_estimators=1000, 
                     learning_rate=0.05,
                     max_depth=5,
                     subsample=0.8,
                     random_state=42,
                     n_jobs=1
)
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
print(predictions[:10])

output = pd.DataFrame({
    'Id' : X_test.index,
    'SalePrice' : predictions
})

output.to_csv('XGBsub.csv', index=False)
print('Archivo guardado')

