from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model


def linear_reg(X, y, X_all):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X_all)

    return y_pred


def random_forest(X, y, X_all):
    rf = RandomForestClassifier()
    rf.fit(X, y)
    y_pred = rf.predict(X_all)

    return y_pred


def svm(X, y, X_all):
    model = SVC()
    model.fit(X, y)
    y_pred = model.predict(X_all)

    return y_pred
