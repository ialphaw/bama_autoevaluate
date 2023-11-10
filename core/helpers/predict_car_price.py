from core.helpers.fetch_car_data_as_dataframe import fetch_car_data_as_dataframe

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def predict_car_price(brand, model, user_car):
    # Fetch data
    df = fetch_car_data_as_dataframe(brand, model)
    df = df[df["price"] != 0]
    print(df)

    # Preprocess and train model (as shown in the previous example)
    X = df[["color_body", "year", "mileage"]]
    y = df["price"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), ["year", "mileage"]),
            ("cat", OneHotEncoder(), ["color_body"]),
        ]
    )

    model = Pipeline(
        [("preprocessor", preprocessor), ("regressor", LinearRegression())]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)

    # Predict price for user's car
    predicted_price = model.predict(pd.DataFrame([user_car]))
    return predicted_price[0]
