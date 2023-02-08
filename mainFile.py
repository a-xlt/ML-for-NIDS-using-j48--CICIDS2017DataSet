import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import plot_tree
df = pd.read_csv('CICIDS2017_sample.csv')
X = df.drop('Label', axis=1).to_numpy()
y = df['Label'].to_numpy()
z = df.columns
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.67, test_size=0.33, shuffle=True)
clf = tree.DecisionTreeClassifier(max_features=60, max_depth=10, criterion="entropy")
clf.fit(X_train, y_train)
accuracy2Test = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, accuracy2Test)
print('accuracy :', (accuracy * 100), '%')
scores = cross_val_score(clf, X, y, cv=10)
print("Cross Validation(10): ", scores.mean())
scores = cross_val_score(clf, X, y, cv=5)
print("Cross Validation(5): ", scores.mean())
scores = cross_val_score(clf, X, y, cv=3)
print("Cross Validation(3): ", scores.mean())
plt.figure(figsize=(100, 100), facecolor='gray')
plot_tree(clf, filled=True, feature_names=z, rounded=True)
plt.savefig('result.pdf')
