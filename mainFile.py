import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import plot_tree


def main_function(path='CICIDS2017_sample.csv', criteriontype="entropy", trainSize=0.67, testSize=0.33):
    df = pd.read_csv(path)
    X = df.drop('Label', axis=1).to_numpy()
    y = df['Label'].to_numpy()
    z = df.columns
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=trainSize, test_size=testSize, shuffle=True)
    clf = tree.DecisionTreeClassifier(max_features=60, max_depth=10, criterion=criteriontype)
    clf.fit(X_train, y_train)
    accuracy2Test = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, accuracy2Test)
    scores10 = cross_val_score(clf, X, y, cv=10)
    scores5 = cross_val_score(clf, X, y, cv=5)
    scores3 = cross_val_score(clf, X, y, cv=3)
    plt.figure(figsize=(100, 100), facecolor='gray')
    plot_tree(clf, filled=True, feature_names=z, rounded=True)
    plt.savefig('result.pdf')
    return (accuracy * 100), scores10.mean(), scores5.mean(), scores3.mean()
