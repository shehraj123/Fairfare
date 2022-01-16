import pandas as pd
import numpy as np

def createModel(csv):

    df = pd.read_csv(csv)
    df = clean(df)
    (X_train, X_test, y_train, y_test) = trainTestSplit(df, 0.2, 1)

    model = train(X_train, y_train)
    pred = model.predict(X_test)
    evaluate(y_test, pred)

    return model

def clean(df):
    
    df = df.dropna()
    df = df.drop('pickup_datetime', axis = 1)
    df = df.drop('key', axis = 1)
    
    return df

def trainTestSplit(df, size, state):

    x = df.drop('fare_amount', axis = 1)
    y = df['fare_amount']

    from sklearn.model_selection import train_test_split
    return train_test_split(x, y, test_size = size, random_state=state)

def train(X_train, y_train):
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    return lr

def scale(df):
    from sklearn.preprocessing import MinMaxScaler
    mn = MinMaxScaler()
    df_mn = mn.fit_transform(df)
    df = pd.DataFrame(df_mn, columns=df.columns, index = df.index)

    return df

def evaluate(pred, y_test):
    from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
    print("r2 score", r2_score(y_test, pred))
    print("mean absolute error", mean_absolute_error(y_test, pred))
    print("mean squared", mean_squared_error(y_test, pred))


