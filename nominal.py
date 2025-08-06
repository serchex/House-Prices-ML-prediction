import pandas as pd
import numpy as np

def preprocess_data(df):
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data>=0]
    missing_percentage = (missing_data/len(df)) * 100
    missing_df = pd.DataFrame({
        'Total missing' : missing_data,
        'Percentage' : missing_percentage
    }).sort_values(by='Percentage', ascending=False)

    print('Columns with missing values\n')
    print(missing_df)

    categorical_missing_cols = df[missing_df.index].select_dtypes(include='object').columns.tolist()[:-1]
    numerical_missing_cols = df[missing_data.index].select_dtypes(include=['float64', 'int64']).columns.tolist()[:-1]
    print('Categorical columns\n')
    print(categorical_missing_cols)
    print('\nNumerical columns\n')
    print(numerical_missing_cols)
    print('\nNo NAN to ceros\n')
    for col in numerical_missing_cols:
        df[col] = df[col].fillna(0)
    print(df[col])

    # Paso 2: Imputacion de columnas categoricos donde NaN signfica 'No tiene' / 'None'
    # Step 2: Imputation of categorical columns where NaN is 'None'
    categorical_cols_none = [
        'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'MasVnrType',
        'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
        'GarageCond', 'BsmtExposure', 'BsmtFinType2', 'BsmtQual',
        'BsmtCond', 'BsmtFinType1'
    ]

    for col in categorical_cols_none:
        if col in df.columns:
            df[col] = df[col].fillna(f'No {col}')
        else:
            df[col] = df[col].fillna('None')
        print(df[col])

    # Paso 3: Imputar cualquier NaN restante en columnas categoricas con la moda
    # Step 3: Impute any NaN remaining in categorical columns with mode
    remaining_categorical_with_nan = df.select_dtypes(include='object').columns[df.select_dtypes(include='object').isnull().any()].tolist()
    print('\n--- Categorial Columns remaining with NAN (before imput with mode) ---')
    print(df[remaining_categorical_with_nan].isnull().sum())

    for col in remaining_categorical_with_nan:
        most_frequent_value = df[col].mode()[0]
        df[col] = df[col].fillna(most_frequent_value)
        print(f'Imputed {col} with mode: {most_frequent_value}')

    # Paso 4: Imputar cualquier NaN restante en columnas numericas con la mediana
    # Step 4: Impute any NaN remaining in numerical columns with median
    remaining_categorical_with_nan = df.select_dtypes(include=np.number).columns[df.select_dtypes(include=np.number).isnull().any()].tolist()

    print('\n--- Numerical Columns remaining NaN (before imput with median) ---')
    print(df[remaining_categorical_with_nan].isnull().sum())

    for col in remaining_categorical_with_nan:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
        print(f'Imputed {col} with median : {median_value}')

    # Verificar que no queden valores nulos
    # Check that no remaining null values
    print('\n --- Final Check of null values ---')
    final_missing = df.isnull().sum()
    final_missing = final_missing[final_missing > 0]

    if final_missing.empty:
        print('All null values has been hadled successfully!')
    else:
        print('Warning! there are null values into DataFrame yet')
        print(final_missing)

    print(df)

    # Paso 5: Separacion y codificacion de columnas
    print('--- Starting Variables codification ---')

    # Ordinal variables
    qualityMap = {
        'Ex' : 5, 'Gd' : 4, 'TA' : 3, 'Fa' : 2, 'Po' : 1, 'None' : 0, 'No ExterQual' : 0,
        'No ExterCond' : 0, 'No BsmtQual' : 0, 'No BsmtCond' : 0,
        'FireplaceQu' : 0, 'No GarageQual' : 0, 'No GarageCond' : 0, 'PoolQC' : 0
    }

    bsmtExposure_map = {
        'Gd' : 4, 'Av': 3, 'Mn' : 2, 'No' : 1, 'No BsmtExposure' : 0
    }

    bsmtFinType_map = {
        'GLQ' : 6, 'ALQ' : 5, 'BLQ' : 4, 'Rec' : 3, 'LwQ' : 2, 'Unf' : 1, 'No BsmtFinType1' : 0,
        'No BsmtFinType2' : 0
    }
    fence_map = {
        'GdPrv': 4, 'MnPrv': 3, 'GdWo': 2, 'MnWw': 1, 'No Fence': 0
    }
    garage_finish_map = {
        'Fin' : 3, 'RFn' : 2, 'Unf' : 1, 'No GarageFinish' : 0
    }

    ordinal_colums_to_map = [
        ('ExterQual', qualityMap), ('ExterCond', qualityMap),
        ('BsmtQual', qualityMap), ('BsmtCond', qualityMap),
        ('HeatingQC', qualityMap), ('KitchenQual', qualityMap),
        ('FireplaceQu', qualityMap), ('GarageQual', qualityMap),
        ('GarageCond', qualityMap), ('PoolQC', qualityMap),
        ('BsmtExposure', bsmtExposure_map), ('BmstFinType1', bsmtFinType_map),
        ('BsmtFinType2', bsmtFinType_map), ('Fence', fence_map),
        ('GarageFinish', garage_finish_map)
    ]

    for col, mapping in ordinal_colums_to_map:
        if col in df.columns:
            df[col] = df[col].map(mapping).fillna(0).astype(int)
            print(f'Column {col} mapped to oridinal values')

    # Codificacion de variables nominales
    nominal_cols = df.select_dtypes(include='object').columns.tolist()
    print(f'Columns to map with One hot encoding: {nominal_cols}')

    # Aplica one hot encoding
    #df = pd.get_dummies(df, columns=nominal_cols, drop_first=True)

    print('Final dataframe shape', df.shape)
    print('Data Type after codification:\n')
    print(df.dtypes.value_counts())
    print('First rows from final DataFrame (check structure):')
    print(df.head())

    return df

df = pd.read_csv('train.csv').set_index('Id')
df_train_pre = preprocess_data(df)
test = pd.read_csv('test.csv').set_index('Id')
df_test_pre = preprocess_data(test)
df_test_pre = df_test_pre.reindex(columns=df_train_pre.columns.drop('SalePrice'), fill_value=0)


