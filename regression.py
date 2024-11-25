from sklearn import linear_model


def linear_reg(X, y, X_all):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X_all)

    return y_pred
