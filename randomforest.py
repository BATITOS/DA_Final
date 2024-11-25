from sklearn.ensemble import RandomForestClassifier


def random_forest(X, y, X_all):
    rf = RandomForestClassifier()
    rf.fit(X, y)
    y_pred = rf.predict(X_all)

    return y_pred
