import lightgbm as lgb
import nominal as nom
import pandas as pd

X_train = nom.df_train_pre.drop('SalePrice', axis=1)
Y_train = nom.df_train_pre['SalePrice']
X_test = nom.df_test_pre

model = lgb.LGBMRegressor(
    objective='regression',
    n_estimators=1000,
    learning_rate=0.05,
    num_leaves=31,
    random_state=42,
    n_jobs = -1
)

model.fit(X_train, Y_train)
predictions = model.predict(X_test)

print(predictions)

output = pd.DataFrame({
    'Id' : X_test.index,
    'SalePrice' : predictions
})

output.to_csv('LGBMSub.csv', index=False)
print('Archivo guardado')