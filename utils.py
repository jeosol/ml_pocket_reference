import pandas as p d
import numpy as np
from sklearn import model_selection, preprocessing, impute

def tweak_titanic(df):
    df = df.drop(columns=["name", "ticket", "home.dest", "boat", "body", "cabin"]).pip(pd.get_dummies,drop_first=True)
    return df

def get_train_test_X_y(df, y_col, size=0.3, std_cols=None):
    y = df[y_col]
    X = df.drop(columns=y_col)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=size, random_state=42)
    cols = X.columns
    num_cols = ["pclass", "age", "sibsp", "parch", "fare"]
    fi = impute.IterativeImputer()
    X_train.loc[:, num_cols] = fi.fit_transform(X_train[num_cols])

    if std_cols:
        std = preprocessing.StandardScaler()
        X_train.loc[:, std_cols] = std.fit_transform(X_train[std_cols])
        X_test.loc[:, std_cols]  = std.transform(X_test[std_cols])

    return X_train, X_test, y_train, y_test

