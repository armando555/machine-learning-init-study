from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X,y = load_wine(return_X_y=True)

lr = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = lr.fit(X_train, y_train)

predictions = model.predict(X_test)




rf = RandomForestClassifier()
rf_model = rf.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)