import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import plot_tree


def main_function(path, criteriontype, trainSize, testSize, printOption=False):
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
    if printOption:
        plt.figure(figsize=(30, 30), facecolor='white')
        plot_tree(clf, filled=True, feature_names=z, rounded=True)
        plt.savefig('Result.pdf')

    return (accuracy * 100), scores10.mean(), scores5.mean(), scores3.mean()


def indvisual_scan(pathToTarin, criteriontype, patToTest):
    df = pd.read_csv(pathToTarin)
    X = df.drop('Label', axis=1).to_numpy()
    y = df['Label'].to_numpy()
    z = df.columns
    clf = tree.DecisionTreeClassifier(max_features=60, max_depth=10, criterion=criteriontype)
    clf.fit(X, y)
    df2 = pd.read_csv(patToTest)
    X2 = df2.to_numpy()
    return clf.predict(X2)



