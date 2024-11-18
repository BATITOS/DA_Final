from sklearn import linear_model
from sklearn.model_selection import train_test_split


def linear_reg(X, y, x_all):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # print('Coefficients:' , model.coef_)
    # print('Intercept:', model.intercept_)
    # print('Mean squared error (MSE): %.2f' % mean_squared_error(Y_test, Y_pred))
    # print('Coefficient of determination (R^2): %.2f' % r2_score(Y_test ,Y_pred))

    return y_pred
