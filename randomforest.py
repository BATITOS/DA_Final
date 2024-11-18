from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def random_forest(X,y):
    X_train , X_test , y_train , y_test = train_test_split(X, y, test_size=0.2)
    rf = RandomForestClassifier()
    rf.fit(X_train,y_train)
    y_pred = rf.predict(X_test)
    
    return y_pred