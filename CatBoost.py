from catboost import CatBoostRegressor
import numpy as np
import nominal as nom
import pandas as pd
import joblib

x_train = nom.df_train_pre.drop('SalePrice', axis=1)
y_train = nom.df_train_pre['SalePrice']
x_test = nom.df_test_pre
categorical_features_indices = list(np.where(x_train.dtypes == 'object')[0])

model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    cat_features=categorical_features_indices,
    random_seed=42,
    verbose=0
)

model.fit(x_train, y_train)
predictions = model.predict(x_test)

print(predictions)

output = pd.DataFrame({
    'Id' : x_test.index,
    'SalePrice' : predictions
})

output.to_csv('CatBoostSub.csv', index=False)
print('Archivo guardado')

catmodel_save = joblib.dump(model, 'models\catboost_model.pkl')
print('Model saved as catboost_model.pkl')
joblib.dump(list(nom.test.columns), 'feature_order.pkl')