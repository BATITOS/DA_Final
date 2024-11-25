from sklearn.svm import SVC


def svm(X, y, X_all):
    model = SVC()
    model.fit(X, y)
    y_pred = model.predict(X_all)

    return y_pred
